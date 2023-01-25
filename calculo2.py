
#Programa para exibir o maior valor

valor_a = int(input('Digite o valor A: \n'))
valor_b = int(input('Digite o valor B: \n'))

if valor_a > valor_b:
    print('O valor A eh maior', valor_a)
elif valor_a < valor_b:
    print('O valor B eh maior', valor_b)
else:
    print('Os valores sao iguais')

