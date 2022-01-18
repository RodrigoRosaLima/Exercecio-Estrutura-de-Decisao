'''4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

print('########## VOGAL OU CONSOANTE ##########')
print()

letra = input('Digite uma letra: --> ').upper()
vogal = 'AEIOU'

print()
if letra in vogal:
    print(f'A letra "{letra}" é uma VOGAL.')
else:
    print(f'A letra "{letra}" é uma CONSOANTE.')