# Desafios iniciais de Python, código 2: Cachorros-Quentes

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
valores = input(" Digite a quantidade de cachorros quentes consumidos e o número de participantes: ").split() 

total_cachorros_quentes = int (valores[0])
participantes = int (valores[1])
if(total_cachorros_quentes >=1 and participantes <= 1000 ):
  media_cachorros_quentes = total_cachorros_quentes / participantes
  print (f' O valor médio de cachorros quentes consumidos por participante é: {media_cachorros_quentes:.2f}')

# TODO:  Calcule a média de cachorros quentes consumidas por participante e imprima o valor com DUAS casas decimais.
# No site deve ficar  -> print(f' {media_cachorros_quentes:.2f}')
# Para arredondamento das casas decimais poderia ter sido utilizada a função round(),
# ficaria print (f' O valor médio de cachorros quentes consumidos por participante é: {round(media_cachorros_quentes, 2)}') 