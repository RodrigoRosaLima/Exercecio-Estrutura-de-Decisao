'''3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''

print('########## MASCULINO OU FEMININO ##########')

sexo = input('Digite F - Feminino ou M - Masculino: ').strip()[0]

if sexo in 'Ff':
    print(f'O sexo digitado foi FEMININO')
elif sexo in 'Mm':
    print(f'O sexo digitado foi MASCULINO')
else:
    print('SEXO INVÁLIDO')