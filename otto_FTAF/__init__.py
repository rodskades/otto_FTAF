# This Python file uses the following encoding: utf-8

# -------------------- #
#    Documentation     #
# -------------------- #

"""
NOME:
    otto_FTAF - Finite Time Air-Fuel Otto Cycles in Python

IMPORTS:
    import otto_FTAF
    import otto_FTAF as FTAF

DESCRIÇÃO:
    Modelo Ar-Combustível de Tempo Finito de Adição de Calor de Motores Otto elaborado em [1].

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

from . import chem
from . import cycle
from . import therm

# ---------------- #
# Versão do Pacote #
# ---------------- #
__version__: tuple[str] = "0.0.2",  # (Major Release).(Bug fix).(Development)

# ---------------------------- #
# Declaração __all__ do Módulo #
# ---------------------------- #

__all__ = [
    '__version__',  # Versão do pacote
    'chem',         # Módulo de química
    'cycle',        # Módulo do ciclo Otto
    'therm',        # Módulo de termodinâmica
]

