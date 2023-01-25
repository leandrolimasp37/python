
#Programa para calcular o salario hora

boas_vindas = input('Qual o seu nome? \n')
print('Seja bem vindo', boas_vindas)

#coletando dados de entrada
salario_mes = int(input('Qual o salario mensal? \n'))
horas_mes = int(input('Qtas horas trabalhadas no mes? \n'))

#criando uma funcao para calcular os dados
def calcular():
    salario_hora = int(salario_mes / horas_mes)
    return print('Seu salario hora:', salario_hora, 'reais')

#iniciando a funcao
calcular()

