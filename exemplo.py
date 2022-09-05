# This Python file uses the following encoding: utf-8

# -------------------- #
#    Documentation     #
# -------------------- #

"""
NOME:
    exemplo.py - Exemplo de utilização do pacote.

DESCRIÇÃO:
    Este exemplo existe para iluminar o modo de utilização do pacote otto_FTAF [1].

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

import otto_FTAF as FTAF
import math

# ----------- #
#   EXEMPLO   #
# ----------- #

# ---------------------------------------------------------- #
#    Para começar um estudo de caso, deve-se ter um motor    #
# ---------------------------------------------------------- #
"""
Nosso dicionário para o motor deve ter as chaves: 
    -> 'r_v'; 
    -> 'V_du'; 
    -> 'r_s';
    -> 'V_2'; 
    -> 'S';
    -> 'V_1';
    -> 'D';
    -> 'r';
    -> 'L'.

O módulo alt_eng.py nos ajuda a calcular estes parâmetros[1], ou eles podem ser fornecidos diretamente caso saiba 
todos.
"""
# Caso haja dúvidas, a documentação fornece o necessário para iniciar FTAT.cycle.alt_eng.solver().
# Instancia-se um motor incompleto:
motor_incompleto = {'r_v': 12.0,     # Razão de compressão: 12:1
                    'V_du': 250e-6,  # Volume Deslocado Unitário: 1/4 de litro
                    'r_s': 1.0       # Motor do tipo quadrado: diâmetro = curso dos pistões
                    }
# Encontrando alguns parâmetros do motor apenas com o que temos:
E = FTAF.cycle.alt_eng.solver(motor_incompleto)[0]  # Apenas [0] pois esta função retorna uma tupla: (motor, bool)

# Aqui eu escolho definir uma razão L = 3r para o raio da manivela (r) e o comprimento da biela (L). Isto depende do
# motor.
E['L'] = 3 * E['r']

# Feito isto, utiliza-se o módulo alt_eng.py para encontrar os parâmetros restantes e definir o motor:
ENGINE = FTAF.cycle.alt_eng.solver(E)[0]

# Imprimindo todos os parâmetros do motor obtidos:
print('-------- Motor --------')
for chave in ENGINE.keys():
    print(f'{chave}: {ENGINE[chave]}')

# ------------------------------------------- #
#   Resolvendo o ciclo Otto para este motor   #
# ------------------------------------------- #

# Instancia-se um objeto para a solução do ciclo Otto:
solver = FTAF.cycle.otto.Solve(
    ENGINE,                   # Dicionário com os parâmetros do motor
    na=25,                    # Quantidade de processos para compressão e expansão
    nc=25,                    # Quantidade de processos para a combustão
    theta=math.radians(-30),  # Ângulo de ignição
    delta=math.radians(60),   # Duração angular de combustão
    fuel=['C8H18'],           # Lista de combustíveis para o ciclo
    prop=[1],                 # Lista de proporções entre combustíveis, [1] para apenas um combustível
    phi=1.0,                  # Razão de equivalência combustível-ar, 1.0 -> mistura estequiométrica
    p0=100,                   # Pressão inicial em kPa
    t0=300,                   # Temperatura inicial em K
    e_v=1.0e-8,               # Tolerância para a diferença de volumes
    e_w=1.0e-8                # Tolerância para o trabalho, para garantir um processo politrópico[1]
)

# Resolvendo e armazenando os resultados:
nt, W_liq, rbw = solver.results()

# --------------------------- #
#   Impressão de resultados   #
# --------------------------- #

# Tabela de principais resultados:
print('-' * 20)
print(f'nt = {nt*100:.3f}% \nW_liq = {W_liq:.5f} kJ \nrbw = {rbw:.3f}')
print('-' * 20)

# Diagrama P-V para observar comportamento do ciclo:
solver.pv_plot()

# Diagrama T-V:
# solver.tv_plot()
