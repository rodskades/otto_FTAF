# This Python file uses the following encoding: utf-8

# -------------------- #
#    Documentation     #
# -------------------- #

"""
NOME:
    otto_FTAF.therm.ideal_mix - Módulo para conduzir a mistura de gases ideais

IMPORT:
    import otto_FTAF.therm.ideal_mix

DESCRIÇÃO:
    Este módulo implementa o modelo de misturas de gases ideais com calores específicos constantes, conforme
    discutido em [1].

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

import math
import numpy
from typing import List
from scipy import constants
from otto_FTAF.chem import molec
from otto_FTAF.chem import air
from otto_FTAF.therm import fuels
from otto_FTAF.therm.props import stdProps

# ---------------------------- #
# Declaração __all__ do Módulo #
# ---------------------------- #

__all__ = [
    'ChemMix',
    'FuelMix',
    'IdealMix',
    'OttoMix',
]

# ---------- #
#   Módulo   #
# ---------- #


# Classe ChemMix para lidar com misturas de substâncias químicas.
class ChemMix:
    """
    class ChemMix:
    Classe para a mistura química de substâncias.
    """
    __subs_atoms: dict = dict()   # Dicionário que irá armazenar os átomos das substâncias informadas no construtor.
    __Mms: dict = dict()          # Dicionário que irá armazenar as massas molares das substâncias informadas.
    __total_mols: float = 0.0     # Quantidade total de mols na mistura - kmol.
    __Xis: dict = dict()          # Dicionário de frações molares das substâncias informadas.
    __massa_molar: float = 0.0    # Massa molar total da mistura - kg/kmol.
    __massa: float = 0.0          # Massa total da mistura - kg.
    __massas_frac: dict = dict()  # Dicionário de frações de massa de cada substância na mistura.

    def __init__(self, species: List[str], n: List[float]) -> None:
        """
        def __init__(self, species, n):
        Este objeto irá lidar com a composição química de certa substância ou mistura de substâncias.
        Neste é possível calcular massa molar, fração molar, entre outros.
        Para iniciar é necessária uma lista com as substâncias (species) e uma lista com o número de mols de cada
        substância (n).
        :param species: List[str]
        :param n: List[float]
        """
        if isinstance(species, str) or isinstance(n, str):
            raise TypeError("Informe as substâncias na forma de uma lista. Exemplo: ['C8H18', 'H2']")
        if len(species) != len(n):
            raise IndexError("A lista de substâncias e a lista de número de mols devem ter mesmo tamanho.")
        else:
            self.__mix: dict = {species[i]: n[i] for i in range(len(species))}  # Dicionário da mistura de substâncias
            self.__N: numpy.ndarray = numpy.array(n)                            # Array com os números de mols

    @property
    def mix(self) -> dict:
        """
        def mix(self):
        Propriedade para acessar o dicionário da mistura de substâncias.
        :return: dict
        """
        return self.__mix

    @mix.setter
    def mix(self, new: dict) -> None:
        """
        Setter para substituir o dicionário da mistura de substâncias se necessário.
        :param new: dict
        """
        self.__mix = new

    @property
    def n_s(self) -> numpy.ndarray:
        """
        def n_s(self):
        Propriedade para acessar o array contendo os números de mols de cada substância.
        :return: array
        """
        return self.__N

    @n_s.setter
    def n_s(self, new: numpy.ndarray) -> None:
        """
        Setter para substituir o array de números de mols se necessário.
        :param new: array
        """
        self.__N = new

    def atomize(self) -> dict:
        """
        def atomize(self):
        Separa os átomos das substâncias da lista de substâncias e retorna um dicionário.
        :return: dict
        """
        tmp: list = list(self.__mix.keys())
        for i in range(len(tmp)):
            self.__subs_atoms[tmp[i]] = molec.atomize(tmp[i])
        return self.__subs_atoms

    @property
    def subs_atoms(self) -> dict:
        """
        def subs_atoms(self):
        Propriedade para acessar o dicionário de átomos das substâncias informadas.
        :return: dict
        """
        return self.__subs_atoms

    def massas_molares(self) -> dict:
        """
        def massas_molares(self):
        Retorna um dicionário contendo todas as massas molares das substâncias fornecidas.
        Valores em kg/kmol.
        :return: dict
        """
        tmp: list = list(self.__mix.keys())
        for i in range(len(tmp)):
            self.__Mms[tmp[i]] = molec.massa_molar(tmp[i]) / 1000.0
        return self.__Mms

    @property
    def mms(self) -> dict:
        """
        def mms(self):
        Propriedade para acessar o dicionário de massas molares da lista de substâncias.
        :return: dict
        """
        return self.__Mms

    def mols_total(self) -> float:
        """
        def mols_total(self):
        Retorna a soma de todos os mols da lista 'n' fornecida.
        :return: float
        """
        self.__total_mols = self.__N.sum()
        return self.__total_mols

    @property
    def total_mols(self) -> float:
        """
        def total_mols(self):
        Propriedade para acessar o total de mols na mistura.
        :return: float
        """
        return self.__total_mols

    def frac_molar(self) -> dict:
        """
        def frac_molar(self):
        Retorna um dicionário contendo a fração molar de cada substância na mistura.
        :return: dict
        """
        self.mols_total()
        tmp: list = list(self.__mix.keys())
        for i in range(len(tmp)):
            self.__Xis[tmp[i]] = self.__N[i] / self.__total_mols
        return self.__Xis

    @property
    def xi(self) -> dict:
        """
        def xi(self):
        Propriedade para retornar o dicionário de frações molares das substãncias.
        :return: dict
        """
        return self.__Xis

    def massa_molar_total(self) -> float:
        """
        def massa_molar_total(self):
        Calcula a massa molar da mistura a partir das massas molares das substâncias e das frações molares.
        :return: float
        """
        tmp: list = list(self.__mix.keys())
        self.frac_molar()
        mm = 0.0
        for i in range(len(tmp)):
            mm += molec.massa_molar(tmp[i]) * self.__Xis[tmp[i]] / 1000.0
        self.__massa_molar = mm
        return self.__massa_molar

    @property
    def massa_molar(self) -> float:
        """
        def massa_molar(self):
        Propriedade para acessar a massa molar da mistura.
        :return: float
        """
        return self.__massa_molar

    def massa_total(self) -> float:
        """
        def massa_total(self):
        Esta função calcula a massa da mistura utilizando a massa molar e o número de mols.
        Retorna massa em kg.
        :return: float
        """
        self.mols_total()
        self.massa_molar_total()
        self.__massa = self.__total_mols * self.__massa_molar
        return self.__massa

    @property
    def massa(self) -> float:
        """
        def massa(self):
        Propriedade para acessar a massa da mistura.
        :return: float
        """
        return self.__massa

    def massa_frac(self) -> dict:
        """
        def mass_frac(self):
        Esta função calcula a fração de massa de cada substância na mistura.
        :return: dict
        """
        self.frac_molar()
        self.massa_molar_total()
        self.massas_molares()
        tmp: list = list(self.__mix.keys())
        for i in range(len(tmp)):
            self.__massas_frac[tmp[i]] = self.__Xis[tmp[i]] * self.__Mms[tmp[i]] / self.__massa_molar
        return self.__massas_frac

    @property
    def massas_frac(self) -> dict:
        """
        def massas_frac(self):
        Propriedade para acessar o dicionário de frações de massa de cada substância.
        :return: dict
        """
        return self.__massas_frac

    def massa_de(self, substancia: str) -> float:
        """
        def massa_de(self, substancia):
        Retorna a massa parcial de uma substancia específica fornecida.
        :param substancia: str
        :return: float
        """
        self.massa_total()
        self.massa_frac()
        try:
            return self.__massas_frac[substancia] * self.__massa
        except KeyError:
            print(f'Não foi encontrada a substância {substancia} na mistura.')


# Classe FuelMix para lidar com misturas de combustíveis.
class FuelMix(ChemMix):
    """
    class FuelMix(ChemMix):
    Misturas de combustíveis, pode ser apenas um, deve permitir o cáclulo de epsilon e da entalpia de formação.
    Herda a classe 'ChemMix'.
    """
    __h_form: float = 0.0  # Entalpia de formação da mistura - kJ/mol.
    __Eps: float = 0.0     # Epsilon da mistura de combustíveis.
    __nC: float = 0.0      # Número de átomos de 'C' nos combustíveis
    __nH: float = 0.0      # Número de átomos de 'C' nos combustíveis
    __nO: float = 0.0      # Número de átomos de 'C' nos combustíveis
    __nN: float = 0.0      # Número de átomos de 'C' nos combustíveis

    def __init__(self, species: List[str], n: List[float]) -> None:
        """
        def __init__(self, species, n):
        Este objeto irá lidar com a composição química de certos combustíveis.
        Neste é possível calcular massa molar, fração molar, entre outros.
        Para iniciar é necessária uma lista com os combustíveis (species) e uma lista com o número de mols de cada
        substância (n).
        :param species: List[str]
        :param n: List[float]
        """
        super().__init__(species, n)
        self.frac_molar()
        self.__prop: list = list(self.xi.values())                         # Lista de proporções dos combustíveis.
        self.__hi_formacao: numpy.ndarray = numpy.zeros(len(self.__prop))  # Array das entalpias de formação.

    @property
    def prop(self) -> list:
        """
        def prop(self):
        Propriedade para acessar a lista de proporções dos combustíveis.
        :return: list
        """
        return self.__prop

    def h_formacao(self) -> float:
        """
        def h_formacao(self):
        Esta função retorna a entalpia de formação da mistura de combustíveis fornecidos.
        Retorna em kJ/mol.
        :return: float
        """
        tmp1: list = list(self.mix.keys())
        tmp2: float = 0.0
        for i in range(len(self.__hi_formacao)):
            tmp3 = fuels.Fuel(tmp1[i])
            self.__hi_formacao[i] = tmp3.hf0
            tmp2 += self.__prop[i] * tmp3.hf0
        self.__h_form = tmp2
        return self.__h_form

    @property
    def hi_formacao(self) -> numpy.ndarray:
        """
        def hi_formacao(self):
        Propriedade para acessar a array com as entalpias de formação dos combustíveis.
        :return: array
        """
        return self.__hi_formacao

    @property
    def h_form(self) -> float:
        """
        def h_form(self):
        Propriedade para acessar a entalpia de formação da mistura.
        :return: float
        """
        return self.__h_form

    def n_is(self) -> tuple:
        """
        def n_is(self):
        Retorna a quantidade de átomos de C, H, O e N nos combustíveis.
        :return: float, float, float, float
        """
        tmp1 = list(self.mix.keys())
        nc = nh = no = nn = 0.0
        for i in range(len(tmp1)):
            tmp2 = fuels.Fuel(tmp1[i])
            nc += tmp2.n_is['C']
            nh += tmp2.n_is['H']
            no += tmp2.n_is['O']
            nn += tmp2.n_is['N']

        self.__nC = nc
        self.__nH = nh
        self.__nO = no
        self.__nN = nn
        return self.__nC, self.__nH, self.__nO, self.__nN

    def mix_epsilon(self) -> float:
        """
        def mix_epsilon(self):
        Retorna o epsilon da mistura de combustíveis.
        :return: float
        """
        self.n_is()
        self.__Eps = 1.0 / (self.__nC + self.__nH / 4.0 - self.__nO / 2.0)
        return self.__Eps

    @property
    def nc(self) -> float:
        """
        def nc(self):
        Propriedade para acessar a quantidade de átomos de C na mistura.
        :return: float
        """
        return self.__nC

    @property
    def nh(self) -> float:
        """
        def nh(self):
        Propriedade para acessar a quantidade de átomos de H na mistura.
        :return: float
        """
        return self.__nH

    @property
    def no(self) -> float:
        """
        def no(self):
        Propriedade para acessar a quantidade de átomos de O na mistura.
        :return: float
        """
        return self.__nO

    @property
    def nn(self) -> float:
        """
        def nn(self):
        Propriedade para acessar a quantidade de átomos de N na mistura.
        :return: float
        """
        return self.__nN

    @property
    def epsilon(self) -> float:
        """
        def epsilon(self):
        Propriedade para acessar o epsilon da mistura fornecida.
        :return: float
        """
        return self.__Eps


# Classe para lidar com a termodinâmica de mistura de gases ideais.
class IdealMix(FuelMix):
    """
    class IdealMix(FuelMix):
    Esta classe lida com a parte termodinâmica da mistura de substâncias fornecidas em determinado estado de
    (Pressão, Temperatura).
    Herda a classe 'FuelMix(ChemMix)'.
    """
    __Ru: float = constants.R / 1000.0  # Constante universal dos gases: R = 8.3144598e-3 kJ/K.mol
    __R_mix: float = 0.0                # Constante dos gases da mistura fornecida
    __P_i: dict = dict()                # Dicionário de pressões parciais para cada substância da mistura
    __V_i: dict = dict()                # Dicionário de volumes parciais para cada substância da mistura
    __cp_i: dict = dict()               # Dicionário de calores específicos a pressão constante
    __cp: float = 0.0                   # Calor específico a pressão constante da mistura
    __cv_i: dict = dict()               # Dicionário de calores específicos a volume constante
    __cv: float = 0.0                   # Calor específico a volume constante da mistura
    __upper_cp = 0.0                    # Capacidade térmica a pressão constante da mistura
    __upper_cv = 0.0                    # Capacidade térmica a volume constante da mistura
    __cp_massa = 0.0                    # Calor específico a pressão constante da mistura em kJ/kg.K
    __cv_massa = 0.0                    # Calor específico a volume constante da mistura em kJ/kg.K

    def __init__(self, species: List[str], n: List[float], pressao: float, temperatura: float) -> None:
        """
        def __init__(self, species, n, p, t):
        Este objeto deve lidar com a parte termodinâmica da mistura.
        Para iniciar é necessário uma lista de substâncias ('species'), uma lista com o número de mols de cada
        substância (n), a pressão ('p') em kPa e a temperatura ('t') em K da mistura.
        :param species: List[str]
        :param n: List[float]
        :param pressao: float
        :param temperatura: float
        """
        super().__init__(species, n)
        self.__P: float = pressao
        self.__T: float = temperatura
        self.__V: float = self.mols_total() * self.__Ru * self.__T / self.__P  # Solução para eq. dos gases (PV = nRT)

    @property
    def ru(self) -> float:
        """
        def ru(self):
        Propriedade para acessar a constante universal dos gases.
        :return: float
        """
        return self.__Ru

    def r_mix(self) -> float:
        """
        def r_mix(self):
        Esta função calcula a constante de gás da mistura.
        :return: float
        """
        self.massa_molar_total()
        self.__R_mix = self.__Ru / self.massa_molar
        return self.__R_mix

    @property
    def mix_r(self) -> float:
        """
        def mix_r(self):
        Propriedade para acessar a constante de gás da mistura.
        :return: float
        """
        return self.__R_mix

    def p_parcial(self) -> dict:
        """
        def p_parcial(self):
        Esta função é uma implementação da lei de Dalton para misturas ideais, ou seja, P_mix = sum(P_parciais).
        Com a pressão da mistura fornecida no construtor __init__, calcula-se as pressões parciais para cada substância
        da mistura.
        :return: dict
        """
        self.frac_molar()
        tmp: list = list(self.mix.keys())
        for i in range(len(tmp)):
            self.__P_i[tmp[i]] = self.xi[tmp[i]] * self.__P
        return self.__P_i

    @property
    def p_i(self) -> dict:
        """
        def p_i(self):
        Propriedade para acessar o dicionário de pressões parciais das substâncias na mistura.
        :return: dict
        """
        return self.__P_i

    def v_parcial(self) -> dict:
        """
        def v_parcial(self):
        Esta função é uma implementação da lei de Amagat para misturas ideais, ou seja, V_mix = sum(V_parciais).
        Como o volume da mistura é calculado no construtor __init__, calcula-se os volumes parciais para cada
        substância.
        :return: dict
        """
        self.frac_molar()
        tmp: list = list(self.mix.keys())
        for i in range(len(tmp)):
            self.__V_i[tmp[i]] = self.xi[tmp[i]] * self.__V
        return self.__V_i

    @property
    def v_i(self) -> dict:
        """
        def v_i(self):
        Propriedade para retornar o dicionário de volumes parciais das substâncias na mistura.
        :return: dict
        """
        return self.__V_i

    def cp_is(self) -> dict:
        """
        def cp_i(self):
        Esta função calcula os calores específicos a pressão constante de todas as substâncias na mistura.
        Os valores do dicionário são em kJ/mol.K.
        Primeiro a função tenta utilizar o valor do calor específico da substância em estado gasoso. Caso não exista o
        valor implementado no dicionário stdProps, ela tentará utilizar o estado líquido para prosseguir com a
        simulação.
        :return: dict
        """
        tmp: list = list(self.mix.keys())
        for i in range(len(tmp)):
            cp = stdProps[tmp[i]]['g']['c_p']
            if cp is None:
                cp = stdProps[tmp[i]]['l']['c_p']
                if cp is None:
                    raise ValueError("Esta substância ainda não foi implementada. Verificar o módulo props.py.")
                else:
                    self.__cp_i[tmp[i]] = cp/1000.0
            else:
                self.__cp_i[tmp[i]] = cp/1000.0
        return self.__cp_i

    @property
    def cp_i(self) -> dict:
        """
        Propriedade para acessar o dicionário de calores específicos a pressão constante.
        :return: dict
        """
        return self.__cp_i

    def cp_mix(self) -> float:
        """
        def cp_mix(self):
        Esta função calcula o calor específico em pressão constante da mistura fornecida.
        Retorna valor em kJ/mol.K
        :return: float
        """
        tmp: list = list(self.mix.keys())
        self.cp_is()
        self.frac_molar()
        cp: float = 0.0
        for i in range(len(tmp)):
            cp += self.xi[tmp[i]] * self.__cp_i[tmp[i]]
        self.__cp = cp
        return self.__cp

    @property
    def cp(self) -> float:
        """
        Propriedade para acessar o calor específico a pressão constante da mistura.
        :return: float
        """
        return self.__cp

    def cv_is(self) -> dict:
        """
        def cv_is(self):
        Esta função calcula os calores específicos a volume constante de todas as substâncias na mistura.
        Os valores do dicionário são em kJ/mol.K.
        :return: dict
        """
        tmp: list = list(self.mix.keys())
        self.cp_is()
        for i in range(len(tmp)):
            self.__cv_i[tmp[i]] = self.__cp_i[tmp[i]] - self.__Ru  # cv = cp - Ru
        return self.__cv_i

    @property
    def cv_i(self) -> dict:
        """
        def cv_i(self):
        Propriedade para acessar o dicionário de calores específicos a volume constante.
        :return: dict
        """
        return self.__cv_i

    def cv_mix(self) -> float:
        """
        def cv_mix(self):
        Esta função calcula o calor específico em volume constante da mistura fornecida.
        Retorna valor em kJ/mol.K.
        :return: float
        """
        self.cv_is()
        self.frac_molar()
        tmp: list = list(self.mix.keys())
        cv: float = 0.0
        for i in range(len(tmp)):
            cv += self.xi[tmp[i]] * self.__cv_i[tmp[i]]
        self.__cv = cv
        return self.__cv

    @property
    def cv(self) -> float:
        """
        def cv(self):
        Propriedade para acessar o calor específico a volume constante da mistura.
        :return: float
        """
        return self.__cv

    def capacidade_termica_p(self) -> float:
        """
        def capacidade_termica(self):
        Esta função calcula a capacidade térmica a pressão constante (CP) da mistura.
        :return: float
        """
        tmp: list = list(self.mix.keys())
        up_cp: float = 0.0
        self.cp_is()
        for i in range(len(tmp)):
            up_cp += self.__cp_i[tmp[i]] * self.n_s[i]
        self.__upper_cp = up_cp
        return self.__upper_cp

    @property
    def upper_cp(self) -> float:
        """
        def upper_cp(self):
        Propriedade para acessar a capacidade térmica a pressão constante (CP) da mistura.
        :return: float
        """
        return self.__upper_cp

    def capacidade_termica_v(self) -> float:
        """
        def capacidade_termica_v(self):
        Esta função calcula a capacidade térmica a volume constante (CV) da mistura.
        :return: float
        """
        tmp: list = list(self.mix.keys())
        up_cv: float = 0.0
        self.cv_is()
        for i in range(len(tmp)):
            up_cv += self.__cv_i[tmp[i]] * self.n_s[i]
        self.__upper_cv = up_cv
        return self.__upper_cv

    @property
    def upper_cv(self) -> float:
        """
        def upper_cv(self):
        Propriedade para acessar a capacidade térmica a volume constante (CV) da mistura.
        :return: float
        """
        return self.__upper_cv

    def cp_mass(self) -> float:
        """
        def cp_mass(self):
        Esta função calcula o calor específico a pressão constante em kJ/kg.K (a partir da massa).
        :return: float
        """
        self.capacidade_termica_p()
        self.massa_total()
        self.__cp_massa = self.__upper_cp / self.massa
        return self.__cp_massa

    @property
    def cp_massa(self) -> float:
        """
        def cp_massa(self):
        Propriedade para acessar o calor específico a pressão constante em kJ/kg.K.
        :return: float
        """
        return self.__cp_massa

    def cv_mass(self) -> float:
        """
        def cv_mass(self):
        Esta função calcula o calor especifico a volume constante em kJ/kg.K (a partir da massa)
        :return: float
        """
        self.capacidade_termica_v()
        self.massa_total()
        self.__cv_massa = self.__upper_cv * self.massa
        return self.__cv_massa

    @property
    def cv_massa(self) -> float:
        """
        def cv_massa(self):
        Propriedade para acessar o calor específico a volume constante em kJ/kg.K
        :return: float
        """
        return self.__cv_massa

    # Funções para lidar com a parte termodinâmica das leis de misturas de gases ideais.
    # Utiliza-se a equação dos estados para encontrar novos valores de pressão, volume e temperatura.
    @staticmethod
    def u_mix(cv: float, t_mix: float) -> float:
        """
        def u_mix(self, cv, t_m):
        Esta função retorna a energia interna da mistura de substâncias, dados o calor específico a volume constante e
        a temperatura da mistura.
        Retorna valor em kJ.
        :param cv: float
        :param t_mix: float
        :return: float
        """
        u_m: float = cv * t_mix
        return u_m

    @staticmethod
    def t_mix(cv: float, u_mix: float) -> float:
        """
        def t_mix(cv, u):
        Esta função retorna a temperatura da mistura de substâncias, dados o calor específico a volume constante e
        a energia interna da mistura.
        :param cv: float
        :param u_mix: float
        :return: float
        """
        t_m: float = u_mix / cv
        return t_m

    def novo_p(self, n_mix: float, v_mix: float, t_mix: float) -> float:
        """
        def novo_p(self, n_mix: float, v_mix: float, t_mix: float):
        Esta função retorna a pressão da mistura dados o número de mols na mistura, o volume e a temperatura da
        mistura.
        :param n_mix: float
        :param v_mix: float
        :param t_mix: float
        :return: float
        """
        p_mix: float = n_mix * self.__Ru * t_mix / v_mix
        return p_mix

    def novo_t(self, n_mix: float, v_mix: float, p_mix: float) -> float:
        """
        def novo_t(self, n_mix: float, v_mix: float, p_mix: float):
        Esta função retorna a temperatura da mistura dados o número de mols na mistura, o volume e a pressão da
        mistura.
        :param n_mix: float
        :param v_mix: float
        :param p_mix: float
        :return: float
        """
        t_mix: float = p_mix * v_mix / (n_mix * self.__Ru)
        return t_mix

    def novo_v(self, n_mix: float, t_mix: float, p_mix: float) -> float:
        """
        def novo_v(self, n_mix, t_mix, p_mix):
        Esta função retorna o volume da mistura dados o número de mols na mistura, a temperatura e a pressão da
        mistura.
        :param n_mix: float
        :param t_mix: float
        :param p_mix: float
        :return: float
        """
        v_mix: float = n_mix * self.__Ru * t_mix / p_mix
        return v_mix


# Classe para lidar com a mistura de combustível e ar:
class OttoMix(IdealMix):
    """
    class OttoMix(IdealMix):
    Esta classe lida com a mistura de um combustível ou mistura de combustíveis com ar.
    Ela retorna as propriedades químicas e termodinâmicas considerando todas as substâncias envolvidas como
    gases ideais.
    Herda a classe IdealMix(FuelMix).
    """
    __nCO2: float = 0.0              # Número de mols de CO2
    __nH2O: float = 0.0              # Número de mols de H2O
    __nCO: float = 0.0               # Número de mols de CO
    __nH2: float = 0.0               # Número de mols de H2
    __nO2: float = 0.0               # Número de mols de O2
    __nN2: float = 0.0               # Número de mols de N2
    __burnt_nTotal: float = 0.0       # Número total de mols nos gases queimados
    __burnt_N: list = list()          # Lista de gases queimados
    __burnt_xi: dict = dict()         # Dicionário de gases e números de mols nos produtos da combustão
    __burnt_massa_molar: float = 0.0  # Massa molar dos gases queimados
    __burnt_massa: float = 0.0        # Massa dos gases queimados
    __burnt_cp_i: dict = dict()       # Dicionário de calores específicos a pressão constante dos gases queimados
    __burnt_cp: float = 0.0           # Calor específico a pressão constante da mistura de gases queimados
    __burnt_cv_i: dict = dict()       # Dicionário de calores específicos a volume constante dos gases queimados
    __burnt_cv: float = 0.0           # Calor específico a volume constante da mistura de gases queimados
    __burnt_upper_cp: float = 0.0     # Capacidade térmica a pressão constante dos gases queimados
    __burnt_upper_cv: float = 0.0     # Capacidade térmica a volume constante dos gases queimados
    __hfCO2 = stdProps['CO2']['g']['hf0']  # Entalpia de formação de CO2
    __hfH2O = stdProps['H2O']['g']['hf0']  # Entalpia de formação de H2O
    __hfCO = stdProps['CO']['g']['hf0']    # Entalpia de formação de CO
    __totalQ: float = 0.0                  # Calor total gerado na queima dos combustíveis

    def __init__(self, fuel: List[str], props: List[float], phi: float, pressao: float, temperatura: float,
                 volume: float, q_ext: float = 0.0):
        """
        Esta classe utiliza o ar definido no módulo otto_FTAF.chem.air.py.
        Para inicializar esta classe deve-se informar os parâmetros devidamente.
        :param fuel: list - Lista contendo um ou mais combustíveis para a queima.
        :param props: list - Lista de proporções dos combustíveis. [1.0] quando apenas um combustível é informado.
        :param phi: float - A proporção entre ar e combustível.
        :param pressao: float - A pressão da mistura em kPa.
        :param temperatura: float - A temperatura da mistura em K.
        :param volume: float - O volume da mistura em metro cúbico (m³)
        :param q_ext: float - A adição de calor de fonte externa. Necessário caso phi = 0.0.
        """
        super().__init__(fuel, props, pressao, temperatura)
        self.__phi: float = phi
        self.__Qext: float = q_ext
        # Encontrando os n's de combustível e de ar:
        self.mix_epsilon()
        ar = air.Ar()
        self.__psi: float = ar.psi
        self.__n_ar: float = (pressao * volume / (self.ru * temperatura)) / (1 + phi * self.epsilon / (1 + ar.psi))
        self.__n_F: float = self.__n_ar * phi * self.epsilon / (1 + ar.psi)
        # Os átomos de C, H, O e N:
        self.n_is()

        # Atualizando o dicionário da mistura 'mix' para incluir o ar:
        new_mix: dict = {fuel[i]: self.__n_F * self.prop[i] for i in range(len(fuel))}
        new_mix['O2'] = ar.mix_air['O2'] * self.__n_ar
        new_mix['N2'] = ar.mix_air['N2'] * self.__n_ar
        self.mix = new_mix
        new_n = numpy.array(list(new_mix.values()))
        self.n_s = new_n
        # P, T, V e U iniciais:
        self.__V = volume
        self.__P0 = pressao
        self.__T0 = temperatura
        self.__V0 = volume
        self.capacidade_termica_v()
        self.__U0 = self.u_mix(self.upper_cv, temperatura)

    @property
    def p0(self) -> float:
        return self.__P0

    @property
    def t0(self) -> float:
        return self.__T0

    @property
    def v0(self) -> float:
        return self.__V0

    @property
    def u0(self) -> float:
        """
        Propriedade para acessar o valor de U0.
        :return: float
        """
        return self.__U0

    def burnt_n_i(self, k: float = 3.5) -> list:
        """
        Esta função calcula os números de mols de cada componente dos gases queimados.
        Representa a Tabela 4 da referência [1].
        :param k: float
        :return: list
        """
        if self.__phi <= 1.0:
            self.__nCO2 = self.nc * self.__n_F
            self.__nH2O = self.nh * self.__n_F / 2.0
            self.__nO2 = (self.__n_ar / (1.0 + self.__psi)
                          + self.no * self.__n_F / 2.0 - self.nc * self.__n_F - self.nh * self.__n_F / 4.0)
            self.__nN2 = self.__n_ar * self.__psi / (1.0 + self.__psi) + self.nn * self.__n_F / 2.0
            self.__burnt_nTotal = self.__nCO2 + self.__nH2O + self.__nCO + self.__nH2 + self.__nO2 + self.__nN2
            self.__burnt_N = [self.__nCO2, self.__nH2O, self.__nCO, self.__nH2, self.__nO2, self.__nN2]

        elif self.__phi > 1.0:
            aa = k - 1.0
            bb = (2.0 * (self.nc * self.__n_F - self.__n_ar / (1 + self.__psi)) +
                  k * (2.0 * self.__n_ar / (self.__psi + 1.0) - (3.0 * self.nc + self.nh / 2.0 - self.no) * self.__n_F)
                  - self.no * self.__n_F)
            cc = k * self.nc * self.__n_F * (2.0 * self.nc * self.__n_F + self.nh * self.__n_F / 2.0 -
                                             self.no * self.__n_F - 2.0 * self.__n_ar / (self.__psi + 1.0))
            _c = (-bb - math.sqrt(bb ** 2 - 4.0 * aa * cc)) / (2.0 * aa)
            if _c < 0.0:
                _c = (-bb + math.sqrt(bb ** 2 - 4.0 * aa * cc)) / (2.0 * aa)
            self.__nCO2 = self.nc * self.__n_F - _c
            self.__nH2O = 2.0 * (self.__n_ar / (1.0 + self.__psi) + self.no * self.__n_F / 2.0 -
                                 self.nc * self.__n_F) + _c
            self.__nCO = _c
            self.__nH2 = (self.nh * self.__n_F - 2.0 * (self.__n_ar / (1.0 + self.__psi) + self.no * self.__n_F / 2.0
                                                        - self.nc * self.__n_F) - _c)
            self.__nN2 = self.__n_ar * self.__psi / (1.0 + self.__psi) + self.nn * self.__n_F / 2.0
            self.__burnt_nTotal = self.__nCO2 + self.__nH2O + self.__nCO + self.__nH2 + self.__nO2 + self.__nN2
            self.__burnt_N = [self.__nCO2, self.__nH2O, self.__nCO, self.__nH2, self.__nO2, self.__nN2]
        return self.__burnt_N

    @property
    def phi(self) -> float:
        """
        def phi(self):
        Propriedade para acessar o phi da mistura de ar e combustível.
        :return: float
        """
        return self.__phi

    @property
    def psi(self) -> float:
        """
        def psi(self):
        Propriedade para acessar o psi do ar utilizado na mistura.
        :return: float
        """
        return self.__psi

    @property
    def n_ar(self) -> float:
        """
        def n_ar(self):
        Propriedade para acessar o número de mols de ar na mistura.
        :return: float
        """
        return self.__n_ar

    @property
    def n_f(self) -> float:
        """
        def n_f(self):
        Propriedade para acessar o número de mols de combustível na mistura.
        :return: float
        """
        return self.__n_F

    def burnt_frac_molar(self) -> dict:
        """
        def burnt_frac_molar(self):
        Retorna um dicionário com as frações molares dos gases no produto da combustão.
        :return: dict
        """
        self.burnt_n_i()
        tmp: list = ['CO2', 'H2O', 'CO', 'H2', 'O2', 'N2']
        for i in range(len(tmp)):
            self.__burnt_xi[tmp[i]] = self.__burnt_N[i] / self.__burnt_nTotal
        return self.__burnt_xi

    @property
    def burnt_xi(self) -> dict:
        """
        Propriedade para acessar o dicionário de frações de gases queimados na combustão.
        :return: dict
        """
        return self.__burnt_xi

    def burnt_m_molar(self) -> float:
        """
        def burnt_massa_molar(self):
        Esta função calcula a massa molar da mistura de gases queimados.
        :return: float
        """
        tmp1: list = ['CO2', 'H2O', 'CO', 'H2', 'O2', 'N2']
        self.burnt_frac_molar()
        tmp2: float = 0.0
        for i in range(len(tmp1)):
            tmp2 += self.__burnt_xi[tmp1[i]] * molec.massa_molar(tmp1[i]) / 1000.0
        self.__burnt_massa_molar = tmp2
        return self.__burnt_massa_molar

    @property
    def burnt_massa_molar(self) -> float:
        """
        def burnt_m_molar(self):
        Propriedade para acessar a massa molar dos gases queimados.
        :return: float
        """
        return self.__burnt_massa_molar

    def burnt_mass(self) -> float:
        """
        def burnt_massa(self):
        Esta função calcula a massa da mistura de gases queimados.
        :return: float
        """
        # self.burnt_frac_molar()
        self.burnt_m_molar()
        self.__burnt_massa = self.__burnt_nTotal * self.__burnt_massa_molar
        return self.__burnt_massa

    @property
    def burnt_massa(self) -> float:
        """
        Propriedade para acessar a massa dos gases queimados.
        :return: float
        """
        return self.__burnt_massa

    # Calores específicos e capacidades térmicas em pressão e volume constantes dos gases queimados:
    def burnt_cp_is(self) -> dict:
        """
        def burnt_cp_is(self):
        Esta função retorna um dicionário contendo os calores específicos a pressão constante dos gases de combustão.
        :return: dict
        """
        tmp: list = ['CO2', 'H2O', 'CO', 'H2', 'O2', 'N2']
        for i in range(len(tmp)):
            cp = stdProps[tmp[i]]['g']['c_p']
            if cp is None:
                cp = stdProps[tmp[i]]['l']['c_p']
                if cp is None:
                    raise ValueError("Esta substância ainda não foi implementada. Verifique o módulo props.py.")
                else:
                    self.__burnt_cp_i[tmp[i]] = cp / 1000.0
            else:
                self.__burnt_cp_i[tmp[i]] = cp / 1000.0
        return self.__burnt_cp_i

    @property
    def burnt_cp_i(self) -> dict:
        """
        def burnt_cp_i(self):
        Propriedade para acessar o dicionário de calores específicos a pressão constante dos gases de combustão.
        :return: dict
        """
        return self.__burnt_cp_i

    def burnt_cp_mix(self) -> float:
        """
        def burnt_cp_mix(self):
        Esta função calcula o calor específico a pressão constante da mistura de gases queimados.
        Retorna o valor em kJ/mol.K
        :return: float
        """
        tmp: list = ['CO2', 'H2O', 'CO', 'H2', 'O2', 'N2']
        self.burnt_frac_molar()
        self.burnt_cp_is()
        cp_mix: float = 0.0
        for i in range(len(tmp)):
            cp_mix += self.__burnt_xi[tmp[i]] * self.__burnt_cp_i[tmp[i]]
        self.__burnt_cp = cp_mix
        return self.__burnt_cp

    @property
    def burnt_cp(self) -> float:
        """
        Propriedade para acessar o calor específico a pressão constante da mistura de gases queimados.
        :return: float
        """
        return self.__burnt_cp

    def burnt_cv_is(self) -> dict:
        """
        def burnt_cv_is(self):
        Esta função retorna um dicionário contendo os calores específicos a volume constante dos gases de combustão.
        :return: dict
        """
        tmp: list = ['CO2', 'H2O', 'CO', 'H2', 'O2', 'N2']
        self.burnt_cp_is()
        for i in range(len(tmp)):
            self.__burnt_cv_i[tmp[i]] = self.__burnt_cp_i[tmp[i]] - self.ru
        return self.__burnt_cv_i

    @property
    def burnt_cv_i(self) -> dict:
        """
        def burnt_cv_i(self):
        Propriedade para acessar o dicionário de calores específicos a volume constante dos gases de combustão.
        :return: dict
        """
        return self.__cv_i

    def burnt_cv_mix(self) -> float:
        """
        Esta função calcula o calor específico a volume constante da mistura de gases queimados.
        Retorna o valor em kJ/mol.K
        :return: float
        """
        self.burnt_cv_is()
        tmp: list = ['CO2', 'H2O', 'CO', 'H2', 'O2', 'N2']
        cv: float = 0.0
        for i in range(len(tmp)):
            cv += self.__burnt_xi[tmp[i]] * self.__burnt_cv_i[tmp[i]]
        self.__burnt_cv = cv
        return self.__burnt_cv

    @property
    def burnt_cv(self) -> float:
        """
        Propriedade para acessar o calor específico a volume constante da mistura de gases queimados.
        :return: float
        """
        return self.__burnt_cv

    def burnt_capacidade_termica_p(self) -> float:
        """
        def burnt_capacidade_termica_p(self):
        Esta função calcula a capacidade térmica a pressão constante dos gases queimados.
        :return: float
        """
        tmp: list = ['CO2', 'H2O', 'CO', 'H2', 'O2', 'N2']
        cp: float = 0.0
        self.burnt_n_i()
        self.burnt_cp_is()
        for i in range(len(tmp)):
            cp += self.__burnt_cp_i[tmp[i]] * self.__burnt_N[i]
        self.__burnt_upper_cp = cp
        return self.__burnt_upper_cp

    @property
    def burnt_upper_cp(self) -> float:
        """
        def burnt_upper_cp(self):
        Propriedade para acessar a capacidade térmica a pressão constante dos gases queimados.
        :return: float
        """
        return self.__burnt_upper_cp

    def burnt_capacidade_termica_v(self) -> float:
        """
        def burnt_capacidade_termica_v(self):
        Esta função calcula a capacidade térmica a volume constante dos gases queimados.
        :return: float
        """
        tmp: list = ['CO2', 'H2O', 'CO', 'H2', 'O2', 'N2']
        cv: float = 0.0
        self.burnt_n_i()
        self.burnt_cv_is()
        for i in range(len(tmp)):
            cv += self.__burnt_cv_i[tmp[i]] * self.__burnt_N[i]
        self.__burnt_upper_cv = cv
        return self.__burnt_upper_cv

    @property
    def burnt_upper_cv(self) -> float:
        """
        def burnt_upper_cv(self):
        Propriedade para acessar a capacidade térmica a volume constante dos gases queimados.
        :return: float
        """
        return self.__burnt_upper_cv

    # Entalpias de formação, calor gerado e outros:
    def h_fs(self) -> tuple:
        """
        def h_fs(self):
        Esta função retorna a entalpia de formação de CO2, H2O e CO em kJ/mol.
        :return: tuple
        """
        return self.__hfCO2, self.__hfH2O, self.__hfCO

    def q_total(self, zeta: float) -> float:
        """
        def q_total(self, zeta):
        Retorna a quantidade de calor gerada na queima do combustível.
        Retorna valor em kJ.
        :param zeta: float
        :return: float
        """
        self.h_formacao()
        self.burnt_n_i()
        self.massa_total()
        self.__totalQ = (self.__n_F * self.h_form - self.__hfCO * self.__nCO - self.__hfH2O * self.__nH2O -
                         self.__hfCO2 * self.__nCO2 + self.__Qext * self.massa) * (1 - zeta)
        return self.__totalQ

    @property
    def total_q(self) -> float:
        """
        def total_q(self):
        Propriedade para acessar o calor gerado na queima do combustível.
        :return: float
        """
        return self.__totalQ

    def qj(self, y1: float, y2: float, zeta: float) -> float:
        """
        def qj(self, y1, y2, zeta):
        Calcula a quantidade de calor gerada entre os estados y1 e y2 (y_j e y_j+1 em [1]).
        Retorna valor em kJ.
        :param y1: float
        :param y2: float
        :param zeta: float
        :return: float
        """
        self.h_formacao()
        self.burnt_n_i()
        self.massa_total()
        q_12 = ((zeta + (1 - zeta) * y1) * (self.__nCO2 * self.__hfCO2 + self.__nH2O * self.__hfH2O +
                                            self.__nCO * self.__hfCO) -
                ((zeta + (1-zeta) * y2) * (self.__nCO2 * self.__hfCO2 + self.__nH2O * self.__hfH2O +
                                           self.__nCO * self.__hfCO)) + self.__Qext * (y2 - y1) * self.massa)
        for i in range(len(self.prop)):
            q_12 += ((1 - y1) * (1 - zeta) * self.__n_F * self.prop[i] * self.hi_formacao[i] -
                     (1 - y2) * (1 - zeta) * self.__n_F * self.prop[i] * self.hi_formacao[i])
        return q_12

    # Outras funções importantes para o ciclo Otto a ser resolvido:
    def chi(self, y: float, zeta: float) -> tuple:
        """
        def chi(self, y: float, zeta: float):
        Esta função realiza uma reação parcial, retornando a composição instantânea da mistura baseada em y e zeta.
        :param y: float
        :param zeta: float
        :return: tuple
        """
        self.burnt_n_i()
        inst_f = (1.0 - y) * (1.0 - zeta) * self.__n_F
        inst_ar = (1.0 - y) * (1.0 - zeta) * self.__n_ar
        inst_co2 = (zeta + (1.0 - zeta) * y) * self.__nCO2
        inst_h2o = (zeta + (1.0 - zeta) * y) * self.__nH2O
        inst_co = (zeta + (1.0 - zeta) * y) * self.__nCO
        inst_h2 = (zeta + (1.0 - zeta) * y) * self.__nH2
        inst_o2 = (zeta + (1.0 - zeta) * y) * self.__nO2 + inst_ar / (1.0 + self.__psi)
        inst_n2 = (zeta + (1.0 - zeta) * y) * self.__nN2 + inst_ar * self.__psi / (1.0 + self.__psi)
        return inst_f, inst_co2, inst_h2o, inst_co, inst_h2, inst_o2, inst_n2

    def nm_j(self, y: float, zeta: float) -> float:
        """
        def nm_j(self, y: float, zeta: float):
        Esta função calcula o número total de mols na mistura no instante y.
        :param y: float
        :param zeta: float
        :return: float
        """
        tmp: tuple = self.chi(y, zeta)
        return sum(tmp)

    def xi_j(self, y: float, zeta: float) -> dict:
        """
        def xi_j(self, y: float, zeta: float):
        Esta função calcula a fração molar dos componentes da mistura no instante y.
        :param y: float
        :param zeta: float
        :return: dict
        """
        formulas_fuel: list = list(self.mix.keys())
        tmp1: tuple = self.chi(y, zeta)
        tmp2: float = self.nm_j(y, zeta)
        xi_j = {'CO2': tmp1[1] / tmp2,
                'H2O': tmp1[2] / tmp2,
                'CO': tmp1[3] / tmp2,
                'H2': tmp1[4] / tmp2,
                'O2': tmp1[5] / tmp2,
                'N2': tmp1[6] / tmp2}
        for i in range(len(self.prop)):
            xi_j[formulas_fuel[i]] = tmp1[0] * self.prop[i] / tmp2
        return xi_j

    def cv_m_j(self, y: float, zeta: float) -> float:
        """
        def cv_m_j(self, y, zeta):
        Esta função retorna o valor instantâneo do calor específico a volume constante da mistura no instante y.
        :param y: float
        :param zeta: float
        :return: float
        """
        self.cv_is()
        self.burnt_cv_is()
        tmp: dict = self.xi_j(y, zeta)
        formulas_fuel: list = list(self.mix.keys())
        cv_j = (self.__burnt_cv_i['CO2'] * tmp['CO2'] + self.__burnt_cv_i['H2O'] * tmp['H2O'] +
                self.__burnt_cv_i['CO'] * tmp['CO'] + self.__burnt_cv_i['H2'] * tmp['H2'] +
                self.__burnt_cv_i['O2'] * tmp['O2'] + self.__burnt_cv_i['N2'] * tmp['N2'])
        for i in range(len(self.prop)):
            cv_j += self.cv_i[formulas_fuel[i]] * tmp[formulas_fuel[i]]
        return cv_j

    def upper_cv_j(self, y: float, zeta: float) -> float:
        """
        def upper_cv_j(self, y, zeta):
        Esta função retorna o valor instantâneo da capacidade térmica a volume constante da mistura no instante y.
        :param y: float
        :param zeta: float
        :return: float
        """
        tmp1: tuple = self.chi(y, zeta)
        tmp2: list = list(self.mix.keys())
        self.cv_is()
        self.burnt_cv_is()
        cv_j = (tmp1[1] * self.__burnt_cv_i['CO2'] + tmp1[2] * self.__burnt_cv_i['H2O'] +
                tmp1[3] * self.__burnt_cv_i['CO'] + tmp1[4] * self.__burnt_cv_i['H2'] +
                tmp1[5] * self.__burnt_cv_i['O2'] + tmp1[6] * self.__burnt_cv_i['N2'])
        for i in range(len(self.prop)):
            cv_j += self.cv_i[tmp2[i]] * tmp1[0] * self.prop[i]
        return cv_j
