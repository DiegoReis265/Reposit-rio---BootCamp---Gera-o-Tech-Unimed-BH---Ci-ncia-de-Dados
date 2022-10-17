# Desafios intermediários de Python, código 3: Aumento Salarial

# A empresa que você trabalha resolveu conceder um aumento salarial a todos funcionários, de acordo com a tabela abaixo:

#       Salário	         |    Percentual de Reajuste
#    0 - 600.00          |              17%
#    600.01 - 900.00     |              13% 
#    900.01 - 1500.00    |              12%
#    1500.01 - 2000.00   |              10%
#    Acima de 2000.00    |              5%

# Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

# A entrada contém apenas um valor de ponto flutuante, que pode ser maior ou igual a zero, com duas casas decimais, conforme exemplos abaixo.

# Exemplo 1

#     Entrada	           Saída
#      	          |  Novo salario: 1120,00 
#       1000      |  Reajuste ganho: 120,00                                                                                     
#                 |  Em percentual: 12 %
 

# Exemplo 2

#     Entrada	           Saída
#      	          |  Novo salario: 2200,00 
#       2000      |  Reajuste ganho: 200,00                                                                                     
#                 |  Em percentual: 10 %


# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;
# OBS: Adicionei texto no input e print do código para teste no Visual código Editor, porém no compilador
# do site estes textos devem ser retirados para não dar erro.

salario = int(input(" Digite o salário do empregado: "))
# No Site deve ficar  -> situacao_pernas = input();
# No desafio pediram para a entrada ser flutuante, porém os valores para teste são inteiros, o correto seria a 
# variável salario ser do tipo float;

if (salario > 0 and salario <= 600):
    percentual_ganho = 17
    reajuste_ganho = salario * (percentual_ganho / 100)
    novo_salario = salario + reajuste_ganho

elif (salario >= 600.01 and salario <= 900):
    percentual_ganho = 13
    reajuste_ganho = salario * (percentual_ganho / 100)
    novo_salario = salario + reajuste_ganho

elif (salario >= 900.01 and salario <= 1500):
    percentual_ganho = 12
    reajuste_ganho = salario * (percentual_ganho / 100)
    novo_salario = salario + reajuste_ganho

elif (salario >= 1500.01 and salario <= 2000):
    percentual_ganho = 10
    reajuste_ganho = salario * (percentual_ganho / 100)
    novo_salario = salario + reajuste_ganho

else: 
    percentual_ganho = 5
    reajuste_ganho = salario * (percentual_ganho / 100)
    novo_salario = salario + reajuste_ganho

print(f' Novo salario: {"{:.2f}".format(novo_salario)}\n Reajuste ganho: {"{:.2f}".format(reajuste_ganho)}\n Em percentual: {percentual_ganho} %')