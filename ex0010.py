'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quntos dólares ela pode comprar considere US 1,00 = R$5.50'''

n = float(input('Quantos reais você tem? '))
r = n / 5.50
print('R${} é igual a US{:.2f} dólares!'.format(n, r))

