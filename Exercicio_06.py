"""6 - Faça um Programa que leia três números e mostre o maior deles."""

print('########## MAIOR NÚMERO ##########')

num_1 = input('Digite um número qualquer: --> ')
num_2 = input('Digite outro número qualquer: --> ')
num_3 = input('Digite um ultimo número qualquer: --> ')
num_1 = int(num_1)
num_2 = int(num_2)
num_3 = int(num_3)

print()
print(f'O maior número digitado foi {max(num_1, num_2, num_3)}.')



