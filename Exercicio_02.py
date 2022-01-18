'''2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.'''

print('########## POSITIVO OU NEGATIVO ##########')

numero = input('Digite um número positivo ou negativo: --> ')
numero = float(numero)

if numero > 0:
    print('Este número é POSITIVO')
elif numero == 0:
    print('Esse número é ZERO')
else:
    print('Esse número é NEGATIVO')
