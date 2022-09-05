# This Python file uses the following encoding: utf-8

# -------------------- #
#    Documentation     #
# -------------------- #

"""
NOME:
    otto_FTAF.cycle.alt_eng - Ferramentas para cálculos em motores de combustão interna.

IMPORT:
    import otto_FTAF.cycle.alt_eng

DESCRIÇÃO:
    Neste módulo define-se algumas ferramentas úteis para a solução do modelo de ciclo Otto elaborado em [1].

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

import sympy
from sympy.abc import alpha
from sympy.abc import omega
from sympy.abc import theta
from sympy.abc import delta

# ---------------------------- #
# Declaração __all__ do Módulo #
# ---------------------------- #

__all__ = [
    'rel',
    'solver',
]

# ---------- #
#   Módulo   #
# ---------- #

# Definindo alguns símbolos para constantes inteiras (apenas as necessárias):
_zero = sympy.Integer(0)
_one = sympy.Integer(1)
_two = sympy.Integer(2)
_four = sympy.Integer(4)
_six = sympy.Integer(6)
_30 = sympy.Integer(30)
_60 = sympy.Integer(60)
_90 = sympy.Integer(90)
_180 = sympy.Integer(180)

# Definindo símbolo para razões (apenas as necessárias):
_half = sympy.Rational(_one, _two)

# Parâmetros globais:
# Geométricos:
_S, _V1, _V2, _Vdu, _z, _D, _Vd, _rv = sympy.symbols('S V_1 V_2 V_du z D V_d r_v')

# Cinemáticos:
_alpha = alpha  # Posição angular da manivela
_omega = omega  # Velocidade angular do virabrequim
_r, _L, _x, _c, _a, _t = sympy.symbols('r L x c a t')

# Termodinâmicos:
_theta = theta                             # Ângulo de ignição
_delta = delta                             # Duração angular da combustão
_V, _Va, _tb = sympy.symbols('V V_a t_b')  # Volume e tempo de combustão

# Fração acumulada de reação química
_y, _ya = sympy.symbols('y y_a')

# Dicionário de relações do motor:
rel = dict()

# Volume Deslocado Unitário:
rel['V_du'] = (sympy.Eq(_Vdu, _V1 - _V2),
               sympy.Eq(_Vdu, sympy.pi * _D ** _two * _S / _four))

# Volume Deslocado do Motor (Cilindrada do motor):
rel['V_d'] = (sympy.Eq(_Vd, _z * _Vdu),)

# Razão Volumétrica (Taxa de compressão):
tmpA = sympy.Eq(_rv, _V1 / _V2)
tmpB = tmpA.subs({'V_1': sympy.solve(rel['V_du'][0], _V1)[0]}).expand()
rel['r_v'] = (tmpA,
              tmpB)

# Curso do Pistão:
rel['S'] = (sympy.Eq(_S, _two * _r),
            sympy.Eq(_S, sympy.solve(rel['V_du'][1], _S)[0]))

# Posição Angular da Manivela com referência a um eixo vertical:
rel['alpha'] = (sympy.Eq(_alpha, _omega * _t),)

# Posição Instantânea do Pistão:
tmpA = sympy.Eq(_x, _r * (_one - sympy.cos(_alpha)) + _L * (_one - sympy.sqrt(_one - (sympy.sin(_alpha)*_r/_L) ** _two))
                )
tmpB = tmpA.subs({'alpha': rel['alpha'][0].rhs})
rel['x'] = (tmpA,
            tmpB)

# Velocidade do pistão, obtido pela derivação no tempo:
tmpB = sympy.Eq(_c, sympy.diff(rel['x'][1].rhs, _t))
tmpA = tmpB.subs({'t': sympy.solve(rel['alpha'][0], _t)[0]})
rel['c'] = (tmpA,
            tmpB)

# Aceleração do pistão, obtido pela derivação no tempo:
tmpB = sympy.Eq(_a, sympy.diff(rel['c'][1].rhs, _t))
tmpA = tmpB.subs({'t': sympy.solve(rel['alpha'][0], _t)[0]})
rel['a'] = (tmpA,
            tmpB)

# Volume Instantâneo Total no cilindro:
tmpA = sympy.Eq(_V, _V2 + _x * sympy.pi * _D ** _two / _four)
tmpB = tmpA.subs({'x': rel['x'][0].rhs})
tmpC = tmpA.subs({'x': rel['x'][1].rhs})
rel['V'] = (tmpA,
            tmpB,
            tmpC)

# Alteração angular do volume:
tmpA = sympy.Eq(_Va, sympy.diff(rel['V'][1].rhs, _alpha))
rel['V_a'] = (tmpA,)

# Fração de calor gerado a cada passo angular:
tmpA = sympy.Eq(
    _y,
    sympy.Piecewise(
        (_zero, _alpha < _theta),
        (_half * (_one - sympy.cos(sympy.pi * (_alpha - _theta) / _delta)),
            _alpha <= _theta + _delta),
        (_one, _alpha > _theta + _delta)
    )
)
rel['y'] = (tmpA,)

# Razão angular de liberação de calor
tmpB = sympy.Eq(_ya, sympy.diff(rel['y'][0].rhs, _alpha))
tmpA = tmpB.subs({'t': sympy.solve(rel['alpha'][0], _t)[0]})
rel['y_a'] = (tmpA,
              tmpB)

# Duração Angular de Combustão:
rel['delta'] = (sympy.Eq(_delta, _omega * _tb),)

# Tempo de combustão:
rel['t_b'] = (
    sympy.Eq(_tb, _delta / _omega),
)

# Formato da câmara de combustão do motor - quadrado, superquadrado ou subquadrado:
_rs = sympy.symbols('r_s')
# A definição a seguir assume que r_s < 1.0 para motores subquadrados:
tmpA = sympy.Eq(_rs, _D / _S)
# Resolvendo a equação cúbica de _S:
tmpC = sympy.solve(rel['S'][1].subs({'D': sympy.solve(tmpA, _D)[0]}), _S)
# Removendo raízes complexas:
tmpD = [j for j in tmpC if j.subs({i: 1.0 for i in j.free_symbols}).evalf(6).is_real]
# Usando a raiz real da equação cúbica:
tmpB = sympy.Eq(_S, tmpD[0])
rel['r_s'] = (tmpA,
              tmpB)


# Função solver:
def solver(eng: dict, eps: float = 1.0e-6) -> tuple:
    """
    def solver(eng, eps):
    Iniciando a partir de um dicionário de parâmetros conhecidos, esta função aplica as relações globais definidas no
    dicionário (rel) para solucionar o maior número possível de parâmetros desconhecidos, escrevendo os resultados no
    dicionário (eng) se os valores retornados forem consistentes com as relações globais dentro de uma tolerância
    fornecida, (eps), definida como 1.0e-6 por padrão.
    A função retorna uma tupla contendo as soluções e uma bool como um relatório.
    Este relatório pode ser:
         - True: Não houve testes falhos. Soluções podem conter novas informações.
         - False: Os dados inseridos foram inconsistentes com a tolerância (eps)
         - None: Parâmetro (eng) não é um dicionário ou então é um dicionário vazio.
    :param eng: dict
    :param eps: float
    :return: tuple
    """
    # Funções auxiliares de organização:
    def known() -> set:
        return {i for i in eng if eng[i] is not None}

    def mk_rel_d() -> dict:
        return {i: {j: {str(l) for l in k.free_symbols}
                    for j, k in enumerate(rel[i])} for i in rel}

    def redund(rel_dict) -> list:
        return [(i, j) for i in rel_dict for j in rel_dict[i]
                if len(rel_dict[i][j] - known()) == 0]

    def mk_u_rel(rel_dict) -> list:
        return [(i, j, list(rel_dict[i][j] - known())[0])
                for i in rel_dict for j in rel_dict[i]
                if len(rel_dict[i][j] - known()) == 1]

    def to_subs() -> dict:
        return {i: eng[i] for i in known()}

    def real_sol(s_list) -> list:
        tmp_a = [j for j in s_list
                 if j.subs({i: 1.0 for i in j.free_symbols}).evalf(6).is_real]
        return tmp_a

    def posi_sol(s_list) -> list:
        tmp_a = real_sol(s_list)
        tmp_b = [j for j in tmp_a
                 if j.subs({i: 1.0 for i in j.free_symbols}).evalf(6) >= 0.0]
        return tmp_b

    # Testes preliminares:
    if not isinstance(eng, dict):
        return eng, None

    if len(eng) == 0:
        return eng, None

    # Criando um dicionário com as relações disponíveis:
    reldict = mk_rel_d()
    # Teste de "redundâncias":
    for i in redund(reldict):
        lhs_ = rel[i[0]][i[1]].lhs  # Parte esquerda da equação
        rhs_ = rel[i[0]][i[1]].rhs  # Parte direita da equação
        if (lhs_.subs(to_subs()) - rhs_.subs(to_subs())).evalf(6) >= eps:
            return eng, False
    # Lista de relações úteis:
    u_rel = mk_u_rel(reldict)
    # Loop de solução:
    while len(u_rel):
        for i in u_rel:
            to_solve = i[2]
            if to_solve not in known():
                sols = sympy.solve(rel[i[0]][i[1]].subs(to_subs()))
                if len(sols) == 1:
                    eng[to_solve] = sols[0]
                else:
                    # Eliminando soluções complexas e recontando:
                    solr = real_sol(sols)
                    if len(solr) == 1:
                        eng[to_solve] = solr[0]
                    else:
                        # Retorna para primeira solução positiva
                        eng[to_solve] = posi_sol(solr)[0]
        u_rel = mk_u_rel(reldict)
    return eng, True
