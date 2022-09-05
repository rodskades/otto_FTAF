# This Python file uses the following encoding: utf-8

# -------------------- #
#    Documentation     #
# -------------------- #

"""
NOME:
    otto_FTAF.cycle.crank_rod - Classe CrankRod para lidar com a geometria do motor.

IMPORT:
    import otto_FTAF.cycle.crank_rod

DESCRIÇÃO:
    Neste módulo define-se a classe CrankRod para lidar com a geometria do motor e parte do ciclo Otto a ser resolvido,
    conforme discutido em [1].

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

# ---------------------------- #
# Declaração __all__ do Módulo #
# ---------------------------- #

__all__ = [
    'CrankRod',
]


# ---------- #
#   Módulo   #
# ---------- #

class CrankRod:
    """
    Classe para armazenar alguns dos parâmetros geométricos do motor, além de apresentar alguns métodos para lidar com
    o ciclo Otto.
    """

    def __init__(self, d: float, l_: float, r: float, v_min: float) -> None:
        """
        def __init__(self, d, l, r, v_min):
        Para inicializar a classe CrankRod, deve-se informar o Diâmetro do pistão (D), o Comprimento da biela (L), o
        raio da manivela (r) e o volume mínimo da câmara de combustão (v_min).
        :param d: float
        :param l_: float
        :param r: float
        :param v_min: float
        """
        self.__M: dict = {'D': d, 'L': l_, 'R': r, 'Vmin': v_min}

    @property
    def m(self):
        """
        Propriedade para acessar o dicionário de parâmetros geométricos.
        :return: dict
        """
        return self.__M

    def x(self, alpha: float) -> float:
        """
        def x(self, alpha):
        Esta função calcula a posição instântanea do pistão baseado-se na posição angular da manivela (alpha).
        :param alpha: float
        :return: float
        """
        ret = self.__M['R'] * (1.0 - numpy.cos(alpha))
        ret += self.__M['L'] * (1.0 - numpy.sqrt(
            numpy.float64(1.0 - (numpy.sin(alpha) * self.__M['R'] / self.__M['L']) ** 2)
        ))
        return ret

    def v(self, alpha: float) -> float:
        """
        def v(self, alpha):
        Esta função calcula o volume instântaneo total no cilindro a partir da posição angular da manivela (alpha).
        :param alpha: float
        :return: float
        """
        volume = self.x(alpha) * numpy.pi * self.__M['D'] ** 2 / 4.0 + self.__M['Vmin']
        return volume

    def v_du(self) -> float:
        """
        def v_du(self):
        Esta função calcula o volume deslocado, ou cilindrada unitária, que o pistão percorre.
        :return: float
        """
        volume = float(self.__M['R'] * numpy.pi * self.__M['D'] ** 2 / 2.0)
        return volume

    def r_v(self) -> float:
        """
        def r_v(self):
        Esta função calcula a taxa de compressão do motor.
        :return: float
        """
        r = float(1.0 + self.v_du() / self.__M['Vmin'])
        return r
