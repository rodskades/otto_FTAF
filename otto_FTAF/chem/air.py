# This Python file uses the following encoding: utf-8

# -------------------- #
#    Documentation     #
# -------------------- #

"""
NOME:
    otto_FTAF.chem.air - Propriedades químicas do ar necessárias para o modelo

IMPORT:
    import otto_FTAF.chem.air

DESCRIÇÃO:
    Modelagem do ar como sendo um gás ideal, conforme discutido em [1].

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

from typing import List

# ---------------------------- #
# Declaração __all__ do Módulo #
# ---------------------------- #

__all__ = [
    'Ar',           # Classe Ar()
]

# -------------- #
#   Módulo Air   #
# -------------- #


class Ar:
    """
    Para esta classe, assume-se o ar como sendo composto 79% de N2 e 21% de O2, de forma que a proporção de Nitrogênio
    por Oxigênio no ar é de 3,76 como default.
    Contudo, é possível o usuário alterar tal proporção caso deseje.
    """

    def __init__(self, psi: float = 3.76) -> None:
        """
        def __init__(self, psi):
        A proporção é de 3.76 de modo padrão, mas pode ser alterada conforme desejado.
        :param psi: Proporção de nitrogênio por oxigênio no ar.
        """
        self.__psi: float = psi
        self.__mix_air: dict = {'O2': 1 / (1 + psi), 'N2': psi / (1 + psi)}
        self.__comp: List[str] = list(self.__mix_air.keys())

    @property
    def psi(self) -> float:
        """
        Propriedade para acessar o psi do ar.
        :return: float
        """
        return self.__psi

    @psi.setter
    def psi(self, valor: float):
        """
        Esta função setter permite alterar o valor de psi para estudos de caso.
        """
        self.__psi = valor

    @property
    def mix_air(self) -> dict:
        """
        Propriedade para acessar o dicionário da composição do ar.
        :return: dict
        """
        return self.__mix_air

    @property
    def comp(self) -> List[str]:
        """
        Propriedade para acessar a lista de elementos no ar.
        :return: list
        """
        return self.__comp
