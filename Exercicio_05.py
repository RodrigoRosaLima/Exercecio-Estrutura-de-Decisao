'''5 - Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.'''

print('########## APROVADO ou REPROVADO ##########')

nota_1 = input('Digite sua primeira nota: --> ')
nota_2 = input('Digite sua outra nota: --> ')
nota_1 = float(nota_1)
nota_2 = float(nota_2)
media = (nota_1 + nota_2) / 2

if media == 10:
    print(f'Sua média foi {media} e você está APROVADO COM DISTRINÇÃO.')
elif media >= 7:
    print(f'Sua média foi {media} e você está APROVADO.')
elif media < 7:
    print(f'Sua média foi {media} e você está REPROVADO.')





