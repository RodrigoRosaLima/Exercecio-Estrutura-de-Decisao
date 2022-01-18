"""12 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e
que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme
o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00"""

print('########## FOLHA DE PAGAMENTO ###########')

hora = input('Digite quantas horas você trabalhou neste mês: --> ')
valor_hora = input('Quanto você ganha por hora? --> ')
hora = float(hora)
valor_hora = float(valor_hora)
salario = hora * valor_hora


if salario <= 900:
      desconto_ir = 0
      desconto = '(ISENTO)'
elif salario <= 1500:
      desconto_ir = salario * 0.05
      desconto = '(5%)'
elif salario <= 2500:
      desconto_ir = salario * 0.10
      desconto = '(10%)'
elif salario > 2500:
      desconto_ir = salario * 0.20
      desconto = '(20%)'

desconto_inss = salario * 0.10
desconto_fgts = salario * 0.11
desconto_sindicato = salario * 0.03

print()
print(f'Salário Bruto:              : R$ {salario:.2f}''\n'
      f'(-) IR                      : R$ {desconto_ir:.2f} - {desconto}''\n'
      f'(-) INSS (10%)              : R$ {desconto_inss:.2f}''\n'
      f'(-) Sindicato (3%)          : R$ {desconto_sindicato:.2f}''\n'
      f'FGTS (11%)                  : R$ {desconto_fgts:.2f}''\n'
      f'Total de descontos          : R$ {desconto_ir + desconto_inss + desconto_sindicato:.2f}''\n'
      f'Salário Liquido             : R$ {salario - (desconto_ir + desconto_inss + desconto_sindicato):.2f}')
