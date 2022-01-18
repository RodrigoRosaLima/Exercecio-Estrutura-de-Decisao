"""7 - Faça um Programa que leia três números e mostre o maior e o menor deles."""


print('########## MAIOR ou MENOR ##########')

num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite outro número: '))
num_3 = int(input('Digite outro número: '))

print()
print(f'O MAIOR número foi {max(num_1, num_2, num_3)}')
print(f'O MENOR número foi {min(num_1, num_2, num_3)}')

