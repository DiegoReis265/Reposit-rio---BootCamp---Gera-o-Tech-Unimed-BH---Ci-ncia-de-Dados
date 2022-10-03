# Desafios iniciais de Python, código 3: Cálculo de viagem

# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;
# Dar espaço entre os valores digitados para que que o método split() separe as strings em cada 
# posição da variável valores;
# OBS: Adicionei texto no  input e print do código para teste no Visual código Editor, porém no compilador 
# do site estes textos devem ser retirados para não dar erro.
# Abaixo segue um exemplo de código que você pode ou não utilizar

valores = input(" Digite a quantidade de horas gastas na viagem e a velocidade media em Km/h: ").split()

tempo_gasto = int(valores[0])
velocidade_media = int(valores[1])

distancia_percorrida = tempo_gasto * velocidade_media
litros_necessarios = distancia_percorrida / 12
print(f' O total de litros necessários para percorrer {distancia_percorrida} Km é: {litros_necessarios:.3f}') 
# TODO:  Calcule quantidade de litros necessária para realizar a viagem e imprima com TRÊS dígitos após o ponto decimal