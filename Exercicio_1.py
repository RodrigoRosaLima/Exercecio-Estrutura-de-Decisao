'''1 - Faça um Programa que peça dois números e imprima o maior deles.'''

print('########## MAIOR NÚMERO ##########')

numero_1 = input('Passe um número qualquer: --> ')
numero_2 = input('Passe outro número qualquer: --> ')
numero_1 = int(numero_1)
numero_2 = int(numero_2)

print(max(numero_1, numero_2))
