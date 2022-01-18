"""9 - Faça um Programa que leia três números e mostre-os em ordem decrescente."""

print('########## DECRESCENTE ##########')

num_1 = input('Digite um número: --> ')
num_2 = input('Digite outro número: --> ')
num_3 = input('Digite outro número: --> ')
num_1 = int(num_1)
num_2 = int(num_2)
num_3 = int(num_3)

lista = [num_1, num_2, num_3]
lista.sort(reverse=True)

print(lista)