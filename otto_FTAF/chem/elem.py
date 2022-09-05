# This Python file uses the following encoding: utf-8

# -------------------- #
#    Documentation     #
# -------------------- #

"""
NOME:
    otto_FTAF.chem.elem - Propriedades químicas dos elementos

IMPORT:
    import otto_FTAF.chem.elem

DESCRIÇÃO:
    Neste módulo são definidos as propriedades dos elementos na foram de um dicionário global denominado "isot".
    Estas constantes foram obtidas de [2].
    O dicionário tem o seguinte formato:

        - As chaves são o número atômico de cada elemento;
        - Os valores são sub-dicionários com as chaves 'sym' e 'iso';
        - O valor de 'sym' é o símbolo do elemento químico, como, por exemplo, "He" para Hélio;
        - O valor de 'iso' é um dicionário que representa os isótopos dos elementos e tem chaves iguais ao número de
        tal isótopo;
        - O sub-sub-dicionário dos isótopos tem as chaves 'm' e 'a';
        - O valor de 'm' é a massa atômica do elemento, por exemplo: C possui massa atômica igual a 12;
        - O valor de 'a' é a abundância, em %, de tal isótopo na Terra, sendo None para os produzidos artificalmente.

    A seguir está um exemplo de como são apresentados estes dados para o Hélio:
    2: {
        'sym': 'He',
        'iso': {
            3: {
                'm': 3.01602930979,
                'a': 0.0001373,
            },
            4: {
                'm': 4.002603249710,
                'a': 99.9998633,
            },
        },
    },

    Portanto:
        elem.isot[i]['sym'] retornará o símbolo do elemento na i-ésima posição;
        elem.isot[i]['iso'] retornará o dicionário de isótopos do elemento na i-ésima posição.

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
    'isot',         # Dicionário de isótopos dos elementos
]

# --------------- #
#   Módulo Elem   #
# --------------- #

# Dicionário de Isótopos dos elementos:
isot: dict = {
    1: {
        'sym': 'H',
        'iso': {
            1: {
                'm': 1.0078250320710,
                'a': 99.988570,
            },
            2: {
                'm': 2.01410177784,
                'a': 0.011570,
            },
            3: {
                'm': 3.016049277725,
                'a': None,
            },
        },
    },
    2: {
        'sym': 'He',
        'iso': {
            3: {
                'm': 3.01602930979,
                'a': 0.0001373,
            },
            4: {
                'm': 4.002603249710,
                'a': 99.9998633,
            },
        },
    },
    3: {
        'sym': 'Li',
        'iso': {
            6: {
                'm': 6.01512235,
                'a': 7.594,
            },
            7: {
                'm': 7.01600405,
                'a': 92.414,
            },
        },
    },
    4: {
        'sym': 'Be',
        'iso': {
            9: {
                'm': 9.01218214,
                'a': 100.0,
            },
        },
    },
    5: {
        'sym': 'B',
        'iso': {
            10: {
                'm': 10.01293704,
                'a': 19.97,
            },
            11: {
                'm': 11.00930555,
                'a': 80.17,
            },
        },
    },
    6: {
        'sym': 'C',
        'iso': {
            12: {
                'm': 12.0,
                'a': 98.938,
            },
            13: {
                'm': 13.003354837810,
                'a': 1.078,
            },
        },
    },
    7: {
        'sym': 'N',
        'iso': {
            14: {
                'm': 14.00307400529,
                'a': 99.6327,
            },
            15: {
                'm': 15.00010889849,
                'a': 0.3687,
            },
        },
    },
    8: {
        'sym': 'O',
        'iso': {
            16: {
                'm': 15.994914622115,
                'a': 99.75716,
            },
            17: {
                'm': 16.9991315022,
                'a': 0.0381,
            },
            18: {
                'm': 17.99916049,
                'a': 0.20514,
            },
        },
    },
    9: {
        'sym': 'F',
        'iso': {
            19: {
                'm': 18.998403207,
                'a': 100.0,
            },
        },
    },
    10: {
        'sym': 'Ne',
        'iso': {
            20: {
                'm': 19.992440175920,
                'a': 90.483,
            },
            21: {
                'm': 20.993846744,
                'a': 0.271,
            },
            22: {
                'm': 21.9913855123,
                'a': 9.253,
            },
        },
    },
    14: {
        'sym': 'Si',
        'iso': {
            28: {
                'm': 27.976926532519,
                'a': 92.22319,
            },
            29: {
                'm': 28.97649470022,
                'a': 4.6858,
            },
            30: {
                'm': 29.973770173,
                'a': 3.09211,
            },
        },
    },
    15: {
        'sym': 'P',
        'iso': {
            31: {
                'm': 30.9737616320,
                'a': 100.0,
            },
            32: {
                'm': 31.9739072720,
                'a': None,
            },
         },
    },
    16: {
        'sym': 'S',
        'iso': {
            32: {
                'm': 31.9720710015,
                'a': 94.9926,
            },
            33: {
                'm': 32.9714587615,
                'a': 0.752,
            },
            34: {
                'm': 33.9678669012,
                'a': 4.2524,
            },
            35: {
                'm': 34.9690321611,
                'a': None,
            },
            36: {
                'm': 35.9670807620,
                'a': 0.011,
            },
        },
    },
    17: {
        'sym': 'Cl',
        'iso': {
            35: {
                'm': 34.968852684,
                'a': 75.7610,
            },
            37: {
                'm': 36.965902595,
                'a': 24.2410,
            },
        },
    },
    18: {
        'sym': 'Ar',
        'iso': {
            36: {
                'm': 35.96754510629,
                'a': 0.336530,
            },
            38: {
                'm': 37.96273244,
                'a': 0.06325,
            },
            40: {
                'm': 39.962383122529,
                'a': 99.600330,
            },
        },
    },
    33: {
        'sym': 'As',
        'iso': {
            75: {
                'm': 74.921596520,
                'a': 100.0,
            },
        },
    },
    34: {
        'sym': 'Se',
        'iso': {
            74: {
                'm': 73.922476418,
                'a': 0.894,
            },
            75: {
                'm': 74.922523418,
                'a': None,
            },
            76: {
                'm': 75.919213618,
                'a': 9.3729,
            },
            77: {
                'm': 76.919914018,
                'a': 7.6316,
            },
            78: {
                'm': 77.917309118,
                'a': 23.7728,
            },
            79: {
                'm': 78.918499118,
                'a': None,
            },
            80: {
                'm': 79.916521321,
                'a': 49.6141,
            },
            82: {
                'm': 81.916699422,
                'a': 8.7322,
            },
        },
    },
    35: {
        'sym': 'Br',
        'iso': {
            79: {
                'm': 78.918337122,
                'a': 50.697,
            },
            81: {
                'm': 80.916290621,
                'a': 49.317,
            },
        },
    },
    36: {
        'sym': 'Kr',
        'iso': {
            78: {
                'm': 77.920364812,
                'a': 0.3353,
            },
            80: {
                'm': 79.916379016,
                'a': 2.28610,
            },
            82: {
                'm': 81.913483619,
                'a': 11.59331
            },
            83: {
                'm': 82.9141363,
                'a': 11.50019,
            },
            84: {
                'm': 83.9115073,
                'a': 56.98715,
            },
            86: {
                'm': 85.9106107311,
                'a': 17.27941,
            },
        },
    },
    52: {
        'sym': 'Te',
        'iso': {
            120: {
                'm': 119.90402010,
                'a': 0.091,
            },
            122: {
                'm': 121.903043916,
                'a': 2.5512,
            },
            123: {
                'm': 122.904270016,
                'a': 0.893,
            },
            124: {
                'm': 123.902817916,
                'a': 4.7414,
            },
            125: {
                'm': 124.904430716,
                'a': 7.0715,
            },
            126: {
                'm': 125.903311716,
                'a': 18.8425,
            },
            128: {
                'm': 127.904463119,
                'a': 31.748,
            },
            130: {
                'm': 129.9062224421,
                'a': 34.0862,
            },
        },
    },
    53: {
        'sym': 'I',
        'iso': {
            123: {
                'm': 122.9055894,
                'a': None,
            },
            125: {
                'm': 124.904630216,
                'a': None,
            },
            127: {
                'm': 126.9044734,
                'a': 100.0,
            },
            129: {
                'm': 128.9049883,
                'a': None,
            },
            131: {
                'm': 130.906124612,
                'a': None,
            },
        },
    },
    54: {
        'sym': 'Xe',
        'iso': {
            124: {
                'm': 123.905893020,
                'a': 0.09523,
            },
            126: {
                'm': 125.9042747,
                'a': 0.08902,
            },
            128: {
                'm': 127.903531315,
                'a': 1.91028,
            },
            129: {
                'm': 128.90477948,
                'a': 26.400682,
            },
            130: {
                'm': 129.90350808,
                'a': 4.071013,
            },
            131: {
                'm': 130.905082410,
                'a': 21.232430,
            },
            132: {
                'm': 131.904153510,
                'a': 26.908633,
            },
            134: {
                'm': 133.90539459,
                'a': 10.435721,
            },
            136: {
                'm': 135.9072198,
                'a': 8.857344,
            },
        },
    },
    85: {
        'sym': 'At',
        'iso': {
            210: {
                'm': 209.9871488,
                'a': None,
            },
            211: {
                'm': 210.987496330,
                'a': None,
            },
        },
    },
    86: {
        'sym': 'Rn',
        'iso': {
            211: {
                'm': 210.9906017,
                'a': None,
            },
            220: {
                'm': 220.011394024,
                'a': None,
            },
            222: {
                'm': 222.017577725,
                'a': None,
            },
        },
    },
}
