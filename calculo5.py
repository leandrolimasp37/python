
#Programa para acertar numero aleatório
import random

#utiliza-se a biblioteca random e a função randrange
num = random.randrange(1,11)
print(num)

#enquanto o chute for diferente de num...
while True:
    chute = int(input('chute um numero: '))
    if chute < num:
        print('Chute foi abaixo')
    elif chute > num:
        print('Chute foi acima')
    else:
        print('ACERTOU', num)
        break
    
print('Saindo...')
