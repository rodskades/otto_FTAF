# This Python file uses the following encoding: utf-8

# -------------------- #
#    Documentation     #
# -------------------- #

"""
NOME:
    otto_FTAF.therm.fuels - Propriedades de combustíveis para os ciclos Otto

IMPORT:
    import otto_FTAF.therm.fuels

DESCRIÇÃO:
    Este módulo implementa o modelo de combustíveis como gases ideais com calores específicos constantes, conforme
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

from otto_FTAF.chem import molec
from otto_FTAF.therm.props import stdProps

# ---------------------------- #
# Declaração __all__ do Módulo #
# ---------------------------- #

__all__ = [
    'Fuel'
]

# ---------- #
#   Módulo   #
# ---------- #


class Fuel(molec.Molecula):
    """
    class Fuel(molec.Molecula):
    Esta classe calcula as propriedades do combustível fornecido.
    """

    def __init__(self, _fuel: str) -> None:
        """
        def __init__(self, _fuels):
        Este construtor requer uma string para iniciar a classe. Ex.: 'C8H18'.
        :param _fuel: str.
        """
        if isinstance(_fuel, str):
            super().__init__(_fuel)
            self.__Fuel: dict = {_fuel: {'atomos': molec.atomize(_fuel), 'M': molec.massa_molar(_fuel)}}
        else:
            raise TypeError('Parâmetro _fuel deve ser uma string.')
        self.__hf0: float = self.h_form()
        self.__n_is: dict = self.find_n_is()
        self.__eps: float = self.epsilon()

    @property
    def eps(self) -> float:
        """
        Propriedade para acessar o epsilon do combustível.
        :return: float
        """
        return self.__eps

    @property
    def hf0(self) -> float:
        """
        Propriedade para acessar a entalpia de formação do combustível.
        :return: float
        """
        return self.__hf0

    @property
    def n_is(self) -> dict:
        """
        Propriedade para acessar o dicionário de quantidade de átomos do combustível.
        :return: dict
        """
        return self.__n_is

    def epsilon(self) -> float:
        """
        def epsilon(self):
        Esta função calcula o epsilon de certo combustível.
        O epsilon é o inverso da quantia estequiométrica de ar para a combustão.
        :return: float
        """
        n_c: float = 0.0                            # Número de mols de Carbono
        n_h: float = 0.0                            # Número de mols de Hidrogênio
        n_o: float = 0.0                            # Número de mols de Oxigênio
        if 'C' in self.atomos.keys():
            n_c = self.atomos['C']
        if 'H' in self.atomos.keys():
            n_h = self.atomos['H']
        if 'O' in self.atomos.keys():
            n_o = self.atomos['O']

        epsilon = 1/(n_c + n_h/4 - n_o/2)
        self.__Fuel[self.formula]['eps'] = epsilon  # Adiciona o epsilon no dicionário do combustível.
        return epsilon

    def h_form(self) -> float:
        """
        def h_form(self):
        Esta função calcula a entalpia de formação do combustível fornecido.
        Retorna o valor em kJ/mol.
        :return: float
        """
        tmp_hf: float = 0.0
        if self.formula in stdProps.keys():
            tmp_hf = stdProps[self.formula]['g']['hf0']
        else:
            print(f'A substância {self.formula} não está implementada no módulo props.py.')

        self.__Fuel[self.formula]['hf0'] = tmp_hf  # Adiciona a entalpia de formação no dicionário do combustível.
        return tmp_hf

    def find_n_is(self) -> dict:
        """
        def n_is(self):
        Esta função separa a quantia de atomos de C, H, O e N no combustível e armazena em um dicionário.
        Encontra o n_i para C, para H, para O e para N.
        :return: dict
        """
        nis: dict = dict()
        if 'C' in self.atomos.keys():
            nis['C'] = self.atomos['C']
        else:
            nis['C'] = 0

        if 'H' in self.atomos.keys():
            nis['H'] = self.atomos['H']
        else:
            nis['H'] = 0

        if 'O' in self.atomos.keys():
            nis['O'] = self.atomos['O']
        else:
            nis['O'] = 0

        if 'N' in self.atomos.keys():
            nis['N'] = self.atomos['N']
        else:
            nis['N'] = 0

        self.__Fuel[self.formula]['nis'] = nis  # Adiciona este dicionário no dicionário do combustível.
        return nis
