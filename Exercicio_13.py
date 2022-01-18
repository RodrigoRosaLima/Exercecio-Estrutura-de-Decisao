"""13 - Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido."""

print('########## DIA DA SEMANA ##########')

dia = input('Digite um número de 1 até 6 para saber o dia da semana: --> ')

if dia == '1':
    print('DOMINGO')
elif dia == '2':
    print('SEGUNDA')
elif dia == '3':
    print('TERÇA')
elif dia == '4':
    print('QUARTA')
elif dia == '5':
    print('QUINTA')
elif dia == '6':
    print('SEXTA')
else:
    print('VALOR INVÁLIDO')


