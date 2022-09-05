# This Python file uses the following encoding: utf-8

# -------------------- #
#    Documentation     #
# -------------------- #

"""
NOME:
    otto_FTAF.cycle.otto - Soluciona o Ciclo Otto do modelo FTAF.

IMPORT:
    import otto_FTAF.cycle.otto

DESCRIÇÃO:
    Neste módulo está implementado de fato o ciclo Otto a ar-combustível com tempo finito de adição de calor,
    conforme definido por [1].

REFERÊNCIAS:
    [1]: R. K. O. Silva,  "Modelo  Ar-Combustivel  de  Tempo  Finito  de
         Adição de Calor de Motores Otto", Trabalho de conclusão de curso. UTFPR.
         Guarapuava, Paraná, Brasil, 2017.

AUTORES:
    R. K. O. Silva, <rodolpho_kades@hotmail.com>
    C. Naaktgeboren, <NaaktgeborenC@utfpr.edu.br> (Orientador)

"""

# ------- #
# Imports #
# ------- #

import numpy
import math
import matplotlib.pyplot as plt
import matplotlib.pylab as plb
from otto_FTAF.cycle import crank_rod
from otto_FTAF.therm import ideal_mix

# ---------------------------- #
# Declaração __all__ do Módulo #
# ---------------------------- #

__all__ = [
    'Solve',
]


# ---------- #
#   Módulo   #
# ---------- #

class Solve:
    """
    class Solve:
    Esta classe lida com o ciclo Otto do modelo FTAF.
    Ela utiliza os estados e propriedades químicas definidas pelo módulo therm.ideal_mix.py assim como o módulo para
    lidar com parâmetros do motor cycle.crank_rod.py.
    """
    __W_ent: float = 0.0  # Trabalho que entra no sistema
    __W_sai: float = 0.0  # Trabalho que é executado pelo sistema
    __Q_ent: float = 0.0  # Calor que entra no sistema
    __Q_sai: float = 0.0  # Calor que sai do sistema
    __W_liq: float = 0.0  # Trabalho líquido
    __eta: float = 0.0    # Eficiência térmica
    __rbw: float = 0.0    # Razão de volta de trabalho

    def __init__(self, engine: dict, na: int, nc: int, theta: float, delta: float, fuel: list, prop: list, phi: float,
                 p0: float, t0: float, e_v: float, e_w: float, q_ext: float = 0.0) -> None:
        """
        Este construtor inicializa a solução do ciclo Otto a partir dos parâmetros necessários, sendo estes:
        :param engine: dict - Dicionário contendo todos os parâmetros do motor necessários. Pode-se utilizar o módulo
        cycle.alt_eng.py para gerar este dicionário, veja o exemplo.py para entender melhor como utilizar.
        :param na: int - Quantidade de processos para a compressão e a expansão.
        :param nc: int - Quantidade de processos para a combustão.
        :param theta: float - Ângulo de ignição, onde a fagulha inicia a combustão (unidade: rad).
        :param delta: float - Duração angular da combustão (unidade: rad).
        :param fuel: list - Lista contendo um ou mais combustíveis para a queima.
        :param prop: list - Lista de proporções entre os combustíveis. Ex.: fuel=['CH4', 'C8H18'] -> prop=[0.4, 0.6].
        :param phi: float - Razão de equivalência combustível-ar.
        :param p0: float - Pressão da mistura (unidade: kPa).
        :param t0: float - Temperatura da mistura (unidade: K).
        :param e_v: float - A tolerância para o volume, para definir se o processo é isocórico ou não (unidade: m³).
        :param e_w: float - A tolerância para o trabalho, "loop k" em [1] (unidade: kJ).
        :param q_ext: float - Calor adicionado de fonte externa, necessário se phi = 0.0 (unidade: kJ).
        """
        self.__E = engine
        self.__CR = crank_rod.CrankRod(self.__E['D'], self.__E['L'], self.__E['r'], self.__E['V_2'])
        self.__Na = na
        self.__Nc = nc
        self.__theta = theta
        self.__delta = delta
        self.__alpha = numpy.zeros(2 * na + nc + 1)
        for j in range(len(self.__alpha) + 1):
            if 0 <= j < na:
                self.__alpha[j] = -numpy.pi + j * (theta + numpy.pi) / na
            elif na <= j <= na + nc:
                self.__alpha[j] = theta + (j - na) * delta / nc
            elif na + nc < j <= 2 * na + nc:
                self.__alpha[j] = theta + delta + (j - na - nc) * (numpy.pi - theta - delta) / na

        self.__Y = numpy.zeros(len(self.__alpha))
        for j in range(len(self.__Y)):
            if self.__alpha[j] < theta:
                self.__Y[j] = 0.0
            elif theta <= self.__alpha[j] <= theta + delta:
                self.__Y[j] = 0.5 - 0.5 * numpy.cos(numpy.pi * (self.__alpha[j] - theta) / delta)
            elif self.__alpha[j] > theta + delta:
                self.__Y[j] = 1.0

        self.__state = ideal_mix.OttoMix(fuel, prop, phi, p0, t0, self.__E['V_1'], q_ext=q_ext)
        self.__allFuel = fuel
        self.__P0 = self.__state.p0
        self.__T0 = self.__state.t0
        self.__V0 = self.__state.v0
        self.__U0 = self.__state.u0
        self.__vol = numpy.ones(len(self.__alpha))
        for j in range(len(self.__vol)):
            self.__vol[j] = self.__CR.v(self.__alpha[j])
        self.__allU = numpy.zeros(len(self.__vol))
        self.__allT = numpy.zeros(len(self.__vol))
        self.__allP = numpy.zeros(len(self.__vol))
        self.__allCv = numpy.zeros(len(self.__vol))
        self.__allQ = numpy.zeros(len(self.__Y) - 1)
        self.__eta = 0.0    # Eficiência térmica (W_liq / Q_ent)
        self.__rbw = 0.0    # Razão de volta de trabalho (W_ent / W_out)
        self.__W_liq = 0.0  # Trabalho líquido
        self.__e_V = e_v
        self.__e_W = e_w
        self.__trab = numpy.zeros(len(self.__allQ))

    @property
    def e_w(self) -> float:
        """
        Propriedade para acessar e_W:
        :return: float
        """
        return self.__e_W

    def zeta(self, p: float = 101.325) -> float:
        """
        def zeta(self, p=101.325):
        Esta função calcula a fração de gases residuais da combustão na câmara depois de cada ciclo.
        :param p: float
        :return: float
        """
        g_r = ((5.25 - 0.5 * self.__E['r_v']) * numpy.exp(8.5 - self.__E['r_v']))
        ret = 17.80689929
        ret += 6.42331483 * g_r
        ret += -(0.21709256 + 0.09426031 * g_r) * p
        ret += (1.02837062 + 0.44882466 * g_r) * 1e-3 * (p ** 2)
        return ret / 100.0

    def prim(self, zeta: float) -> tuple:
        """
        def prim(self, zeta):
        Esta função calcula todos os parâmetros "primários" (ver [1]) possíveis de se calcular.
        :param zeta: float
        :return: tuple
        """
        self.__allT[0] = self.__T0
        self.__allP[0] = self.__P0
        self.__allU[0] = self.__U0
        for j in range(len(self.__allCv)):
            self.__allCv[j] = self.__state.upper_cv_j(self.__Y[j], zeta)
        for j in range(len(self.__allQ)):
            self.__allQ[j] = self.__state.qj(self.__Y[j], self.__Y[j+1], zeta)
        return self.__allCv, self.__allQ

    @staticmethod
    def work(p: float, v0: float, v1: float, n0: float) -> float:
        """
        def work(p, v0, v1, n0):
        Esta função calcula a quantidade necessária de trabalho para ir do volume v0 para o volume v1 fornecidos (m³),
        sob a pressão p fornecida e para o coeficiente politrópico n0 fornecido.
        :param p: float
        :param v0: float
        :param v1: float
        :param n0: float
        :return: float
        """
        ret = (p / (1 - n0)) * (v0 - (v0 ** n0) / (v1 ** (n0 - 1)))
        return ret

    def iterate(self, zeta: float = None) -> numpy.ndarray:
        """
        def iterate(self, zeta):
        Esta função resolve de fato o ciclo Otto. Também retorna o array de pressões do ciclo.
        :param zeta: float
        :return: array
        """
        if zeta is None:
            zeta = self.zeta()
        self.prim(zeta)
        n_j = [[0.0] * (2 * self.__Na + self.__Nc)]                                           # n_j[k][j]
        upper_w = [[1.0] * (2 * self.__Na + self.__Nc), [1.0] * (2 * self.__Na + self.__Nc)]  # W[k][j]
        for j in range(len(self.__allQ)):
            k: int = 0
            if abs(self.__vol[j+1] - self.__vol[j]) < self.__e_V:
                self.__allU[j+1] = self.__allU[j] + self.__allQ[j]
                self.__allT[j+1] = self.__allQ[j] / self.__allCv[j] + self.__allT[j]
                self.__allP[j+1] = (self.__state.nm_j(self.__Y[j+1], zeta) * self.__state.ru *
                                    self.__allT[j+1] / self.__vol[j+1])
                self.__trab[j] = 0.0
            else:
                n_j[0][j] = 1 + self.__state.ru / self.__state.cv_m_j(self.__Y[j], zeta)
                upper_w[0][j] = self.work(self.__allP[j], self.__vol[j], self.__vol[j+1], n_j[0][j])
                while abs(upper_w[k-1][j] - upper_w[k][j]) > self.__e_W or (k == 0):
                    if k + 1 > len(n_j) - 1:                              # Possível correção na matriz n_j
                        n_j.append([0.0] * (2 * self.__Na + self.__Nc))
                    self.__allU[j+1] = self.__allU[j] + self.__allQ[j] + upper_w[k][j]
                    self.__allT[j+1] = self.__state.t_mix(self.__allCv[j+1], self.__allU[j+1])
                    self.__allP[j+1] = (self.__state.nm_j(self.__Y[j+1], zeta) * self.__state.ru *
                                        self.__allT[j+1] / self.__vol[j+1])
                    n_j[k+1][j] = (math.log(self.__allP[j+1] / self.__allP[j])) / (
                        math.log(self.__vol[j] / self.__vol[j+1]))
                    k = k + 1
                    upper_w[k][j] = self.work(self.__allP[j], self.__vol[j], self.__vol[j+1], n_j[k][j])
                    if k + 1 > len(upper_w) - 1:                             # Possível correção na matriz upper_w
                        upper_w.append([0.0] * (2 * self.__Na + self.__Nc))

                self.__allU[j+1] = self.__allU[j] + self.__allQ[j] + upper_w[k][j]
                self.__allT[j+1] = self.__state.t_mix(self.__allCv[j+1], self.__allU[j+1])
                self.__allP[j+1] = (self.__state.nm_j(self.__Y[j], zeta) * self.__state.ru *
                                    self.__allT[j+1] / self.__vol[j+1])
                self.__trab[j] = upper_w[k][j]
        return self.__allP

    def results(self, zeta: float = None) -> tuple:
        """
        def results(self, zeta):
        Esta função calcula alguns aspectos finais do ciclo Otto e retorna as principais características do ciclo:
            - eta = Eficiência térmica do ciclo (W_liq / Q_ent);
            - W_liq = Trabalho líquido (W_sai - W_ent);
            - rbw = Razão de volta de trabalho (W_ent / W_sai).
        :param zeta: float
        :return: tuple
        """
        if zeta is None:
            zeta = self.zeta()
        self.iterate(zeta)
        w_ent = 0.0
        w_sai = 0.0
        q_ent = 0.0
        q_sai = 0.0
        for j in range(len(self.__trab)):
            if self.__trab[j] >= 0.0:
                w_ent += self.__trab[j]
            elif self.__trab[j] < 0.0:
                w_sai += -self.__trab[j]

            if self.__allQ[j] >= 0.0:
                q_ent += self.__allQ[j]
            elif self.__allQ[j] < 0.0:
                q_sai += -self.__allQ[j]

        self.__W_ent = w_ent
        self.__W_sai = w_sai
        self.__Q_ent = q_ent
        self.__Q_sai = q_sai
        self.__W_liq = self.__W_sai - self.__W_ent
        self.__eta = self.__W_liq / self.__Q_ent
        self.__rbw = self.__W_ent / self.__W_sai
        return self.__eta, self.__W_liq, self.__rbw

    @property
    def eta(self) -> float:
        """
        def eta(self):
        Propriedade para acessar a eficiência térmica.
        :return: float
        """
        return self.__eta

    @property
    def w_liq(self) -> float:
        """
        def w_liq(self):
        Propriedade para acessar o trabalho líquido.
        :return: float
        """
        return self.__W_liq

    @property
    def rbw(self) -> float:
        """
        def rbw(self):
        Propriedade para acessar a razão de volta de trabalho.
        :return: float
        """
        return self.__rbw

    # Algumas funções para apresentação dos resultados:
    def pv_plot(self):
        """
        def pv_plot(self):
        Esta função utiliza os arrays de pressão e volume para retornar um diagrama P-V para o ciclo Otto.
        :return: graph
        """
        plb.rcParams['figure.figsize'] = (14, 5)
        plt.plot(self.__vol, self.__allP, 'r-', label=u'Ciclo Otto para %s: $\eta_t=$%.3f%%' %
                                                      (self.__allFuel, self.__eta * 100.0))
        plt.title('Diagrama $P-V$ para a razão de equivalência combustível-ar de $\u03C6=$%.1f e razão de compressão de'
                  ' $r_v =$%.1f.' % (self.__state.phi, self.__E['r_v']))
        plt.xlabel('Volume, m³')
        plt.ylabel('Pressão, $kPa$')
        plt.legend(loc='upper right')
        plt.grid()
        return plt.show()

    def pv_loglog(self):
        """
        def pv_loglog(self):
        Esta função utiliza os arrays de pressão e volume para retornar um diagrama P-V para o ciclo Otto em uma escala
        log-log.
        :return: graph
        """
        plb.rcParams['figure.figsize'] = (14, 5)
        plt.loglog(self.__vol, self.__allP, 'r-', label=u'Ciclo Otto para %s: $\eta_t=$%.3f%%' %
                                                        (self.__allFuel, self.__eta * 100.0))
        plt.title('Diagrama $P-V$ para a razão de equivalência combustível-ar de $\u03C6=$%.1f e razão de compressão de'
                  ' $r_v =$%.1f.' % (self.__state.phi, self.__E['r_v']))
        plt.xlabel('Volume, m³')
        plt.ylabel('Pressão, $kPa$')
        plt.legend(loc='upper right')
        plt.grid()
        return plt.show()

    def tv_plot(self):
        """
        def tv_plot(self):
        Esta função utiliza os arrays de temperatura e volume para retornar um diagrama T-V para o ciclo Otto.
        :return: graph
        """
        plb.rcParams['figure.figsize'] = (14, 5)
        plt.plot(self.__vol, self.__allT, 'r-', label=u'Ciclo Otto para %s: $\eta_t=$%.3f%%' %
                                                      (self.__allFuel, self.__eta * 100.0))
        plt.title('Diagrama $T-V$ para a razão de equivalência combustível-ar de $\u03C6=$%.1f e razão de compressão de'
                  ' $r_v =$%.1f.' % (self.__state.phi, self.__E['r_v']))
        plt.xlabel('Volume, m³')
        plt.ylabel('Temperatura, $K$')
        plt.legend(loc='upper right')
        plt.grid()
        return plt.show()

    def tv_loglog(self):
        """
        def tv_loglog(self):
        Esta função utilizar os arrays de temperatura e volume para retornar um diagrama T-V para o ciclo Otto em uma
        escala log-log.
        :return: graph
        """
        plb.rcParams['figure.figsize'] = (14, 5)
        plt.loglog(self.__vol, self.__allT, 'r-', label=u'Ciclo Otto para %s: $\eta_t=$%.3f%%' %
                                                        (self.__allFuel, self.__eta * 100.0))
        plt.title('Diagrama $T-V$ para a razão de equivalência combustível-ar de $\u03C6=$%.1f e razão de compressão de'
                  ' $r_v =$%.1f.' % (self.__state.phi, self.__E['r_v']))
        plt.xlabel('Volume, m³')
        plt.ylabel('Temperatura, $K$')
        plt.legend(loc='upper right')
        plt.grid()
        return plt.show()
