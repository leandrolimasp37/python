
#Programa para calcular a fatorial de um numero
num = int(input('Digite um numero: '))

if num < 0:
    print('soh numeros positivos')

resu=1
cont=1

while cont <= num:
    resu *= cont
    cont += 1
    print(resu)

print('fatorial:', resu)