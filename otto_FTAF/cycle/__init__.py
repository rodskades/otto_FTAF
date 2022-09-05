# This Python file uses the following encoding: utf-8

# -------------------- #
#    Documentation     #
# -------------------- #

"""
NOME:
    otto_FTAF.cycle - Módulos para resolução do ciclo

IMPORT:
    import otto_FTAF.cycle

DESCRIÇÃO:
    Módulos para solução do ciclo Otto definido em [1].

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

from . import alt_eng
from . import crank_rod
from . import otto

# ---------------------------- #
# Declaração __all__ do Módulo #
# ---------------------------- #

__all__ = [
    'alt_eng',      # Módulo para lidar com relações entre os parâmetros do motor
    'crank_rod',    # Módulo para lidar com alguns parâmetros específicos do motor
    'otto',         # Módulo para a solução do ciclo Otto
]
