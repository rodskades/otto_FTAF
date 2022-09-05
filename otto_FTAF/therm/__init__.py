# This Python file uses the following encoding: utf-8

# -------------------- #
#    Documentation     #
# -------------------- #

"""
NOME:
    otto_FTAF.therm - Módulos de propriedades termodinâmicas do modelo

IMPORT:
    import otto_FTAF.therm

DESCRIÇÃO:
    Módulos para solução da parte termodinâmica do modelo definido em [1].

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

from . import fuels
from . import ideal_mix
from . import props

# ---------------------------- #
# Declaração __all__ do Módulo #
# ---------------------------- #

__all__ = [
    'fuels',        # Módulo para lidar com combustíveis
    'ideal_mix',    # Módulo para lidar com misturas de substâncias
    'props',        # Propriedades termodinâmicas
]
