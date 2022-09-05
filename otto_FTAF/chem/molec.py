# This Python file uses the following encoding: utf-8

# -------------------- #
#    Documentation     #
# -------------------- #

"""
NOME:
    otto_FTAF.chem.molec - Funções para lidar com elementos e moléculas

IMPORT:
    import otto_FTAF.chem.molec

DESCRIÇÃO:
    Neste módulo são definidas algumas funções utilitárias para lidar com os elementos.

AUTORES:
    R. K. O. Silva, <rodolpho_kades@hotmail.com>
    C. Naaktgeboren, <NaaktgeborenC@utfpr.edu.br> (Orientador)

"""

# ------- #
# Imports #
# ------- #

from otto_FTAF.chem.elem import isot
import numpy
import re
from typing import List, Union

# ---------------------------- #
# Declaração __all__ do Módulo #
# ---------------------------- #

__all__ = [
    'isot',         # Dicionário de isótopos dos elementos
    'num_elem',
    'sym_elem',
    'elements',
    'isotopes',
    'isotopes_of',
    'mass_of',
    'm',
    'atomize',
    'massa_molar',
    'Molecula',
]

# ---------- #
#   Módulo   #
# ---------- #


# Funções genéricas quanto ao dicionário de isótopos

def num_elem() -> list:
    """
    def num_elem():
    Retorna uma lista dos números atômicos dos elementos em elem.isot
    :return: list
    """
    return list(sorted(isot.keys()))


def sym_elem() -> list:
    """
    def sym_elem():
    Retorna uma lista dos símbolos dos elementos em elem.isot
    :return: list
    """
    return [isot[k]['sym'] for k in sorted(isot.keys())]


def elements() -> List[tuple]:
    """
    def elements():
    Retorna uma lista de tuplas dos elementos da forma (número atômico, símbolo do elemento)
    :return: List[tuple]
    """
    return [(k, isot[k]['sym']) for k in sorted(isot.keys())]


def isotopes() -> List[tuple]:
    """
    def isotopes():
    Retorna uma lista de tuplas da forma (número atômico, símbolo do elemento, isótopos do elemento)
    :return: List[tuple]
    """
    return [(k, isot[k]['sym'], list(isot[k]['iso'].keys()))
            for k in sorted(isot.keys())]


def isotopes_of(x: Union[int, str]) -> list:
    """
    def isotopes_of(x):
    Retorna uma lista dos isótopos do elemento "x" fornecido, podendo ser um inteiro ou uma string (símbolo)
    :param x: int or string
    :return: list
    """
    if isinstance(x, int):
        # No caso de x ser o número atômico do elemento
        try:
            isos = list(isot[x]['iso'].keys())
        except KeyError:
            raise LookupError(f'Elemento de número {x} não encontrado no dicionário. Verifique o módulo elem.py.')
    elif isinstance(x, str):
        # No caso de x ser o símbolo do elemento
        try:
            z = [k for k in isot.keys() if isot[k]['sym'] is x][0]
        except IndexError:
            raise LookupError(f'Elemento {x} não encontrado no dicionário. Verifique o módulo elem.py.')
        isos = list(isot[z]['iso'].keys())
    else:
        raise TypeError('isotopes_of(x): x deve ser um int ou uma string')
    return isos


# Função básica para Cálculos específicos de elementos

def mass_of(dic: dict) -> float:
    """
    def mass_of(dic):
    Retorna a média mássica das massas "m"s baseando-se nas abundancias "a"s do dicionário dic inserido.
    :param dic: dict
    :return: float
    """
    if isinstance(dic, dict):
        k = dic.keys()
        upper_m = [dic[j]['m'] for j in k]
        upper_a = [dic[j]['a'] for j in k]
        a_test = [j is None for j in upper_a]
        if True in a_test:
            if False in a_test:
                a = numpy.array([0.0 if i is None else i for i in upper_a])
            else:
                a = numpy.array([1.0 if i is None else i for i in upper_a])
        else:
            a = numpy.array(upper_a)
        upper_w = a / a.sum()
        _m = numpy.array(upper_m)
        mass = (_m * upper_w).sum()
    else:
        raise TypeError('mass_of(dic): dic deve ser um dicionário.')
    return mass


# Funções utilitárias

def m(x: Union[int, str]) -> float:
    """
    def m(x):
    Retorna a massa atômica do elemento "x" calculada pela média das massas atômicas dos isótopos ponderada por suas
    abundancias.
    :param x: int ou string
    :return: float
    """
    if isinstance(x, int):
        # x sendo o número atômico do elemento:
        try:
            upper_m: float = mass_of(isot[x]['iso'])
        except KeyError:
            raise LookupError(f'Elemento de número atômico {x} não encontrado. Verifique o módulo elem.py.')
    elif isinstance(x, str):
        # x sendo o símbolo do elemento:
        try:
            z = [k for k in isot.keys() if isot[k]['sym'] is x][0]
        except IndexError:
            raise LookupError(f'Elemento {x} não encontrado. Verifique o módulo elem.py.')
        upper_m: float = mass_of(isot[z]['iso'])
    else:
        raise TypeError('m(x): x deve ser um int ou uma string.')
    return upper_m


def atomize(formula: str) -> dict:
    """
    Separa a fórmula química fornecida por seus átomos. Retorna um dicionário.
    :param formula: str
    :return: dict
    """
    char_pattern: str = '[A-Z][a-z]{0,1}'                       # Padrão de caracteres necessários para o pacote re
    all_pattern: str = char_pattern + '[0-9]{0,}'               # Padrão incluindo os números de 0 a 9
    elementos_formula: list = re.findall(all_pattern, formula)  # Separando os elementos da fórmula em uma lista
    atomos: dict = dict()                                       # Inicializando o dict (vazio ainda) que será retornado
    for tmp_elem in elementos_formula:
        s = re.search(char_pattern, tmp_elem)                   # Instancia-se objeto re (contem os elementos atômicos)
        elem: str = tmp_elem[s.start():s.end()]                 # Separando e armazenando cada elemento
        if len(tmp_elem[s.end():]) > 0:                         # Definindo a quantidade de átomos
            quant: int = int(tmp_elem[s.end():])
        else:
            quant: int = 1
        if elem in atomos:                                      # Inserindo "elemento": "quantidade" no dicionário
            atomos[elem] += quant
        else:
            atomos[elem] = quant
    return atomos


def massa_molar(formula: str) -> float:
    """
    def massa_molar(formula):
    Retorna o valor da massa molar da fórmula fornecida.
    Valor em kg/kmol.
    :param formula: str
    :return: float
    """
    form: dict = atomize(formula)
    simbolos: list = sym_elem()
    mass: float = 0.0
    for j in range(len(simbolos)):
        try:
            qnt = form[simbolos[j]]
            mass += qnt * m(simbolos[j])
        except KeyError:
            pass
    return mass


class Molecula:
    """
    class Molecula:
    Esta é uma classe que permite estanciar um objeto para certa fórmula química que contenha toda suas propriedades.
    """
    def __init__(self, formula: str) -> None:
        """
        Inicializa o objeto a partir de uma fórmula (string) e armazena as informações definidas pelas funções
        definidas no presente módulo.
        :param formula: str
        """
        self.__form: str = formula
        self.__atomos: dict = atomize(formula)
        self.__Mmolar: float = massa_molar(formula)

    @property
    def formula(self) -> str:
        """
        Propriedade para acessar a fórmula química da molécula.
        :return: str
        """
        return self.__form

    @property
    def atomos(self) -> dict:
        """
        Propriedade para acessar o dicionário de átomos da molécula.
        :return: dict
        """
        return self.__atomos

    @property
    def massa_molar(self) -> float:
        """
        Propriedade para acessar a massa molar da molécula
        :return: float
        """
        return self.__Mmolar

    def mass(self, n: float) -> float:
        """
        def mass(self, n):
        Calcula a quantidade de massa da substância a partir do número de mols fornecido (n).
        :param n: float
        :return: float
        """
        if isinstance(self.__Mmolar, float):
            if isinstance(n, float):
                mm: float = n * self.__Mmolar
            else:
                raise TypeError('O número de mols fornecido não é um float. Verifique a documentação.')
        else:
            raise TypeError('A massa molar não é um float. Verifique a documentação.')
        return mm


if __name__ == "__main__":
    massa = massa_molar('C8H18')
    print(f"Resultado de massa_molar('C8H18'): {massa}")
