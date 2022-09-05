# Motores Otto FTAF
Modelo termodinâmico de ciclo Otto a Ar-Combustível de Tempo Finito de Adição de Calor.

### FTAF: Finite-Time Air-Fuel

Este modelo foi desenvolvido inicialmente como um trabalho de conclusão de curso (TCC) de Engenharia Mecânica por 
Rodolpho Kades de Oliveira e Silva.

O presente pacote está em desenvolvimento para que seja possível utilizar das ferramentas para calcular a eficiência de
motores utilizando o modelo de Ciclos Otto a Ar-Combustível de Tempo Finito de Adição de Calor, de acordo com o 
que foi desenvolvido no trabalho original [1]. 
Diversas simplificações foram realizadas para simplificar os cálculos. 

Portanto, tenha em mente que o propósito inicial do trabalho é didático e este modelo _**não**_ deve ser utilizado 
comercialmente/industrialmente de forma alguma.

###### Este pacote ainda está sob testes e não foi publicado no repositório PyPI.

#### Estrutura do pacote:
    -> otto_FTAF:
        -> chem:
            - air.py
            - elem.py
            - molec.py
        -> cycle:
            - alt_eng.py
            - crank_rod.py
            - otto.py
        -> therm:
            - fuels.py
            - ideal_mix.py
            - props.py
    -> exemplo.py

Cada módulo apresenta documentação própria para compreensão de suas funcionalidades para o programa.

O arquivo exemplo.py apresenta, como o nome sugere, um exemplo de utilização do presente pacote para auxiliar futuros
usuários.

REFERÊNCIAS:
---------------------------------------
    [1]: R. K. O. Silva,  "Modelo  Ar-Combustivel  de  Tempo  Finito  de
         Adição de Calor de Motores Otto", Trabalho de conclusão de curso. UTFPR.
         Guarapuava, Paraná, Brasil, 2017.
    [2]: David R. Lide, ed., CRC  Handbook  of  Chemistry  and  Physics,
         Internet Version 2005, <http://www.hbcpnetbase.com>, CRC Press,
         Boca Raton, FL, 2005.

Contato:
-
[LinkedIn](https://www.linkedin.com/in/rodolpho-kades/)

[GitHub](https://github.com/rodskades)

<rodolpho_kades@hotmail.com>
