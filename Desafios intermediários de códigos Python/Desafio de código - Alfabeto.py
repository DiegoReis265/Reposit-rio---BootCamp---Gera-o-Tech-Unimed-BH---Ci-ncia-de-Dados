# Desafios intermediários de Python, código 1: Alfabeto

# Desafio
# Dada a letra N do alfabeto, nos diga qual a sua posição.

# Entrada
# Um único caracter N, uma letra maiúscula ('A'-'Z') do alfabeto (que contém 26 letras).


# Saída
# Um único inteiro, que representa a posição da letra no alfabeto.

# Exemplo de Entrada  |  Exemplo de Saída
#         C           |         3
#         J	          |         10
#         Z           |         26                         
#         A           |         1  
                                              
# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO ord(): Retorna o valor  ASCII de cada letra ou símbolo do teclado;
# OBS: Adicionei texto no  input e print do código para teste no Visual código Editor, porém no compilador
# do site estes textos devem ser retirados para não dar erro.

NUM = 64 # Variável imutável
letra = input(" Digite a letra desejada: ") 
# No Site deve ficar  -> letra = input();
letra = letra.upper() # Garante que a letra de entrada será lida em maiúscula;
print(f' A posição correspondente da letra digitada é:  {ord(letra) - NUM}') # Retorna o valor correspondente ASCII 
# da letra digitada e subtrai da variável NUM;
# Os valores em decimal de A até Z conforme a tabela ASCII estão compreendidos dentro de um intervalo sequencial de 
# 65 até 90, sendo 65 para letra A e 90 para a letra Z;
# No Site deve ficar  -> print(ord(letra) - NUM).





