# Desafios intermediários de Python, código 2: Papagaio Poliglota

# Desafio
# Humberto tem um papagaio muito esperto. Quando está com as duas pernas no chão, o papagaio fala em português. Quando levanta 
# a perna esquerda, fala em inglês. Por fim, quando levanta a direita fala em francês. Nico, amigo de Humberto, ficou fascinado 
# com o animal. Em sua emoção perguntou: “E quando ele levanta as duas?”. Antes que Humberto pudesse responder, o papagaio gritou: 
# “Aí eu caio, idiota!”.

# Entrada
# A entrada consiste de diversos casos de teste. Cada caso de teste consiste uma string informando qual a situação de levantamento 
# de pernas do papagaio.

# Saída
# Para cada condição de levantamento de pernas do papagaio, imprima a linguagem que ele utilizará. Caso ele levante ambas as pernas, 
# imprima “caiu”. Quebre uma linha a cada caso de teste.

# Exemplo de Entrada	 |  Exemplo de Saída
#     esquerda           |       ingles
#     direita            |       frances
#     nenhuma            |       portugues
#     ambas              |       caiu


# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;
# while True significa que, enquanto houver entradas, o código após o try continuará sendo executado
# OBS: Adicionei texto no input e print do código para teste no Visual código Editor, porém no compilador
# do site estes textos devem ser retirados para não dar erro.

while True: 
    try: 
        situacao_pernas = input(" Digite a atual situação de levantamento de pernas do papagaio: ")
        # No Site deve ficar  -> situacao_pernas = input();
        situacao_pernas = situacao_pernas.lower().strip().replace(" ","") 
        # lower() para garantir que a string digitada fique toda em minúscula;
        # strip() para garantir que a string digitada não tenha espaçamentos no início e no fim, caso aja erro do usuário;
        # replace(" "."") para garantir que a string digitada não tenha espaçamentos entre os caracteres, caso aja erro do usuário;
        if (situacao_pernas == "esquerda"):
            print(" Falando em ingles \n")

        elif (situacao_pernas == "direita"):
            print("Falando em frances \n")

        elif (situacao_pernas == "nenhuma"):
            print("Falando em portugues \n")

        elif (situacao_pernas == "ambas"):
            print(" Ele caiu \n")

    except EOFError: 
        break