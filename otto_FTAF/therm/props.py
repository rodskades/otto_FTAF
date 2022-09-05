# This Python file uses the following encoding: utf-8

# -------------------- #
#    Documentation     #
# -------------------- #

"""
NOME:
    otto_FTAF.therm.props - Propriedades termodinâmicas básicas

IMPORT:
    import otto_FTAF.therm.props

DESCRIÇÃO:
    Este módulo define propriedades termodinâmicas de algumas substâncias escolhidas, de modo que estas possam ser
    modeladas como gases ideais em uma mistura. Estas propriedades foram coletadas de [2].
    As substâncias escolhidas incluem alguns combustíveis mais comuns e alguns produtos de combustões.
    O dicionário stdProps possui a seguinte forma:

        - As chaves são os símbolos/fórmulas químicas das substâncias;
        - Os valores são sub-dicionários com chaves 'n', 's', 'l' e 'g';
        - As chaves 'n' possuem como valor uma string contendo o nome da substância
        - As chaves 's' possuem como valor sub-sub-dicionários contendo as propriedades da substância em estado sólido;
        - As chaves 'l' possuem como valor sub-sub-dicionários contendo as propriedades da substância em estado líquido;
        - As chaves 'g' possuem como valor sub-sub-dicionários contendo as propriedades da substância em estado gasoso.

    A seguir está um exemplo de chave/valor para o dicionário stdProps para a substância dióxido de carbono 'CO2':

    'CO2': {
        'n': 'Carbon dioxide',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'g': {
            'hf0': -393.5,  # kJ/mol
            'gf0': -394.4,  # kJ/mol
            's_0': 213.8,   # J/mol·K
            'c_p': 37.1,    # J/mol·K
        },
    },

REFERÊNCIAS:
    [2]: David R. Lide, ed., CRC  Handbook  of  Chemistry  and  Physics,
         Internet Version 2005, <http://www.hbcpnetbase.com>, CRC Press,
         Boca Raton, FL, 2005.

AUTORES:
    R. K. O. Silva, <rodolpho_kades@hotmail.com>
    C. Naaktgeboren, <NaaktgeborenC@utfpr.edu.br> (Orientador)

"""

# ------- #
# Imports #
# ------- #

# ---------------------------- #
# Declaração __all__ do Módulo #
# ---------------------------- #

__all__ = [
    'stdProps',     # Dicionário de propriedades comuns (standard)
]

# ---------- #
#   Módulo   #
# ---------- #

stdProps: dict = {
    'C': {
        'n': 'Carbon',
        's': {  # solid
            'hf0': 0.0,     # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': 5.7,     # J/mol·K
            'c_p': 8.5,     # J/mol·K
        },
        'l': {  # liquid
            'hf0': None,    # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': None,    # J/mol·K
        },
        'g': {  # gas
            'hf0': 716.7,   # kJ/mol
            'gf0': 671.3,   # kJ/mol
            's_0': 158.1,   # J/mol·K
            'c_p': 20.8,    # J/mol·K
        },
    },
    'CO': {
        'n': 'Carbon monoxide',
        's': {  # solid
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {  # liquid
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'g': {  # gas
            'hf0': -110.5,  # kJ/mol
            'gf0': -137.2,  # kJ/mol
            's_0': 197.7,   # J/mol·K
            'c_p': 29.1,    # J/mol·K
        },
    },
    'CO2': {
        'n': 'Carbon dioxide',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'g': {
            'hf0': -393.5,  # kJ/mol
            'gf0': -394.4,  # kJ/mol
            's_0': 213.8,   # J/mol·K
            'c_p': 37.1,    # J/mol·K
        },
    },
    'N': {
        'n': 'Nitrogen (atomic)',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'g': {
            'hf0': 472.7,  # kJ/mol
            'gf0': 455.5,  # kJ/mol
            's_0': 153.3,  # J/mol·K
            'c_p': 20.8,   # J/mol·K
        },
    },
    'NO': {
        'n': 'Nitric oxide',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'g': {
            'hf0': 91.3,   # kJ/mol
            'gf0': 87.6,   # kJ/mol
            's_0': 210.8,  # J/mol·K
            'c_p': 29.9,   # J/mol·K
        },
    },
    'NO2': {
        'n': 'Nitrogen dioxide',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'g': {
            'hf0': 33.2,   # kJ/mol
            'gf0': 51.3,   # kJ/mol
            's_0': 240.1,  # J/mol·K
            'c_p': 37.2,   # J/mol·K
        },
    },
    'N2': {
        'n': 'Nitrogen',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'g': {
            'hf0': 0.0,    # kJ/mol
            'gf0': None,   # kJ/mol
            's_0': 191.6,  # J/mol·K
            'c_p': 29.1,   # J/mol·K
        },
    },
    'O2': {
        'n': 'Oxygen',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'g': {
            'hf0': 0.0,    # kJ/mol
            'gf0': None,   # kJ/mol
            's_0': 205.2,  # J/mol·K
            'c_p': 29.4,   # J/mol·K
        },
    },
    'H2': {
        'n': 'Hydrogen',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'g': {
            'hf0': 0.0,    # kJ/mol
            'gf0': None,   # kJ/mol
            's_0': 130.7,  # J/mol·K
            'c_p': 28.8,   # J/mol·K
        },
    },
    'HO': {
        'n': 'Hydroxyl',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'g': {
            'hf0': 39.0,   # kJ/mol
            'gf0': 34.2,   # kJ/mol
            's_0': 183.7,  # J/mol·K
            'c_p': 29.9,   # J/mol·K
        },
    },
    'H2O': {
        'n': 'Water',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': -285.8,  # kJ/mol
            'gf0': -237.1,  # kJ/mol
            's_0': 70.0,    # J/mol·K
            'c_p': 75.3,    # J/mol·K
        },
        'g': {
            'hf0': -241.8,  # kJ/mol
            'gf0': -228.6,  # kJ/mol
            's_0': 188.8,   # J/mol·K
            'c_p': 33.6,    # J/mol·K
        },
    },
    'H4N2': {
        'n': 'Hydrazine',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': 50.6,   # kJ/mol
            'gf0': 149.3,  # kJ/mol
            's_0': 121.2,  # J/mol·K
            'c_p': 98.9,   # J/mol·K
        },
        'g': {
            'hf0': 95.4,   # kJ/mol
            'gf0': 159.4,  # kJ/mol
            's_0': 238.5,  # J/mol·K
            'c_p': 48.4,   # J/mol·K
        },
    },
    # Hydrocarbons ( C_{n}H_{2n+2} )
    'CH4': {
        'n': 'Methane',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'g': {
            'hf0': -74.6,  # kJ/mol
            'gf0': -50.5,  # kJ/mol
            's_0': 186.3,  # J/mol·K
            'c_p': 35.7,  # J/mol·K
        },
    },
    'C2H6': {
        'n': 'Ethane',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'g': {
            'hf0': -84.0,  # kJ/mol
            'gf0': -32.0,  # kJ/mol
            's_0': 229.2,  # J/mol·K
            'c_p': 52.5,   # J/mol·K
        },
    },
    'C3H8': {
        'n': 'Propane',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': -120.9,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': None,    # J/mol·K
        },
        'g': {
            'hf0': -103.8,  # kJ/mol
            'gf0': -23.4,   # kJ/mol
            's_0': 270.3,   # J/mol·K
            'c_p': 73.6,    # J/mol·K
        },
    },
    'C4H10': {
        'n': 'Butane',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': -147.3,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': 140.9,   # J/mol·K
        },
        'g': {
            'hf0': -125.7,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': 99.7,    # J/mol·K [Wylen]
        },
    },
    'C5H12': {
        'n': 'Pentane',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': -173.5,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': 167.2,   # J/mol·K
        },
        'g': {
            'hf0': -146.9,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': None,    # J/mol·K
        },
    },
    'C6H14': {
        'n': 'Hexane',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': -198.7,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': 195.6,   # J/mol·K
        },
        'g': {
            'hf0': -166.9,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': None,    # J/mol·K
        },
    },
    'C7H16': {
        'n': 'Heptane',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': -224.2,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': 224.7,   # J/mol·K
        },
        'g': {
            'hf0': -187.6,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': None,    # J/mol·K
        },
    },
    'C8H18': {
        'n': 'Octane',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': -250.1,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': 254.6,   # J/mol·K
        },
        'g': {
            'hf0': -208.5,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': 195.5,   # J/mol·K [Wylen]
        },
    },
    'C9H20': {
        'n': 'Nonane',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': -274.7,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': 284.4,   # J/mol·K
        },
        'g': {
            'hf0': -228.2,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': None,    # J/mol·K
        },
    },
    'C10H22': {
        'n': 'Decane',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': -300.9,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': 314.4,   # J/mol·K
        },
        'g': {
            'hf0': -249.5,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': None,    # J/mol·K
        },
    },
    'C11H24': {
        'n': 'Undecane',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': -327.2,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': 344.9,   # J/mol·K
        },
        'g': {
            'hf0': -270.8,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': None,    # J/mol·K
        },
    },
    'C12H26': {
        'n': 'Dodecane',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': -350.9,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': 375.8,   # J/mol·K
        },
        'g': {
            'hf0': -289.4,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': None,    # J/mol·K
        },
    },
    'C13H28': {
        'n': 'Tridecane',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': None,   # kJ/mol
            'gf0': None,   # kJ/mol
            's_0': None,   # J/mol·K
            'c_p': 406.7,  # J/mol·K
        },
        'g': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
    },
    # Alcools ( C_{n}H_{2n+2}O )
    'CH4O': {
        'n': 'Methanol',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': -239.2,  # kJ/mol
            'gf0': -166.6,  # kJ/mol
            's_0': 126.8,   # J/mol·K
            'c_p': 81.1,    # J/mol·K
        },
        'g': {
            'hf0': -201.0,  # kJ/mol
            'gf0': -162.3,  # kJ/mol
            's_0': 239.9,   # J/mol·K
            'c_p': 44.1,    # J/mol·K
        },
    },
    'C2H6O': {
        'n': 'Ethanol',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': -277.6,  # kJ/mol
            'gf0': -174.8,  # kJ/mol
            's_0': 160.7,   # J/mol·K
            'c_p': 112.3,   # J/mol·K
        },
        'g': {
            'hf0': -234.8,  # kJ/mol
            'gf0': -167.9,  # kJ/mol
            's_0': 281.6,   # J/mol·K
            'c_p': 65.6,    # J/mol·K
        },
    },
    'C3H8O': {
        'n': '1-Propanol',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': -302.6,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': 193.6,   # J/mol·K
            'c_p': 143.9,   # J/mol·K
        },
        'g': {
            'hf0': -255.1,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': 322.6,   # J/mol·K
            'c_p': 85.6,    # J/mol·K
        },
    },
    'C4H10O': {
        'n': '2-Butanol',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': -342.6,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': 214.9,   # J/mol·K
            'c_p': 196.9,   # J/mol·K
        },
        'g': {
            'hf0': -292.8,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': 359.5,   # J/mol·K
            'c_p': 112.7,   # J/mol·K
        },
    },
    'C5H12O': {
        'n': '1-Pentanol',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': -351.6,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': 208.1,   # J/mol·K
        },
        'g': {
            'hf0': -294.6,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': None,    # J/mol·K
        },
    },
    'C6H14O': {
        'n': '1-Hexanol',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': -377.5,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': 287.4,   # J/mol·K
            'c_p': 240.4,   # J/mol·K
        },
        'g': {
            'hf0': -315.9,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': None,    # J/mol·K
        },
    },
    'C7H16O': {
        'n': '1-Heptanol',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': -403.3,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': 272.1,   # J/mol·K
        },
        'g': {
            'hf0': -336.5,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': None,    # J/mol·K
        },
    },
    'C8H18O': {
        'n': '1-Octanol',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': -426.5,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': 305.2,   # J/mol·K
        },
        'g': {
            'hf0': -355.6,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': None,    # J/mol·K
        },
    },
    'C9H20O': {
        'n': '1-Nonanol',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': -453.4,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': None,    # J/mol·K
        },
        'g': {
            'hf0': -376.5,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': None,    # J/mol·K
        },
    },
    'C10H22O': {
        'n': '1-Decanol',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': -478.1,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': 370.6,   # J/mol·K
        },
        'g': {
            'hf0': -396.6,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': None,    # J/mol·K
        },
    },
    'C11H24O': {
        'n': '1-Undecanol',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': -504.8,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': None,    # J/mol·K
        },
        'g': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
    },
    'C12H26O': {
        'n': '1-Dodecanol',
        's': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'l': {
            'hf0': -528.5,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': 438.1,   # J/mol·K
        },
        'g': {
            'hf0': -436.6,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': None,    # J/mol·K
        },
    },
    'C13H28O': {
        'n': '1-Tridecanol',
        's': {
            'hf0': -599.4,  # kJ/mol
            'gf0': None,    # kJ/mol
            's_0': None,    # J/mol·K
            'c_p': None,    # J/mol·K
        },
        'l': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
        'g': {
            'hf0': None,  # kJ/mol
            'gf0': None,  # kJ/mol
            's_0': None,  # J/mol·K
            'c_p': None,  # J/mol·K
        },
    },
}
