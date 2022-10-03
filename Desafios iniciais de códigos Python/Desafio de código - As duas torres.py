# Desafios iniciais de Python, código 1: As duas torres

# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;
# Dar espaço entre os valores digitados para que que o método split() separe as strings em cada 
# posição da variável entrada;
# OBs: Adicionei texto no  input e print do código para teste no Visual código Editor, porém no compilador 
# do site estes textos devem ser retirados para não dar erro.

entrada = input(" Digite a distância entre as torres e os diâmetros dos Palatír: ").split() 
# No Site deve ficar  -> entrada = input().split()

distancia = int(entrada[0])
diametro_1 = int(entrada[1])
diametro_2 = int(entrada[2])
if (distancia > 0 and distancia < 10000):
    if (diametro_1 > 0) and (diametro_2 < 100):
        icm = distancia / (diametro_1 + diametro_2)
        print (f" O valor do ICM é: {icm:.2f}") 
        
# No site deve ficar  -> print(f' {icm:.2f}')
# Para arredondamento das casas decimais poderia ter sido utilizada a função round(),
# ficaria print (f" O valor do ICM é: {round(icm, 2)}") 