"""15 - Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar
se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo,
se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;"""

print('########## TIPO DE TRIANGULO ##########')

lado_1 = input('Digite o valor de um dos lados de um triângulo: --> ')
lado_2 = input('Digite o valor do outro lado do triângulo: --> ')
lado_3 = input('Digite o valor do ultimo lado do triângulo: --> ')
lado_1 = int(lado_1)
lado_2 = int(lado_2)
lado_3 = int(lado_3)

print()
if lado_1 == lado_2 == lado_3:
    print('Esse é um Triângulo Equilátero.')
elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    print('Esse é um Triângulo Isósceles.')
elif lado_1 != lado_2 != lado_3:
    print('Esse é um Triângulo Escaleno.')

