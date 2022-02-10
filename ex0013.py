"""Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento"""

salario = float(input('Qual é o seu salário? R$'))
aumento: float = salario + (salario * 15 / 100)
print('O seu salário de R${:.2f} com o aumento de 15% fica R${:.2f}'.format(salario, aumento))
