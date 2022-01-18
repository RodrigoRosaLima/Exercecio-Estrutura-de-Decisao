"""8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato."""

print('########## QUAL COMPRAR ##########')

produto_1 = input('Qual o valor do primeiro produto? --> ')
produto_2 = input('Qual o valor do segundo produto? --> ')
produto_3 = input('Qual o valor do terçeiro produto? --> ')
produto_1 = float(produto_1)
produto_2 = float(produto_2)
produto_3 = float(produto_3)

print()
if min(produto_1, produto_2, produto_3) == produto_1:
    print(f'O Primeiro produto no valor de R$ {produto_1} é o mais barato e deve ser comprado.')
if min(produto_1, produto_2, produto_3) == produto_2:
    print(f'O Segundo produto no valor de R$ {produto_2} é o mais barato e deve ser comprado.')
if min(produto_1, produto_2, produto_3) == produto_3:
    print(f'O terçeiro produto no valor de R$ {produto_3} é o mais barato e dever ser comprado.')
