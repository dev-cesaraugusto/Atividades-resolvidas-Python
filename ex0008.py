'''Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros'''
n1 = float(input('Escreva a medida: '))
c = n1 * 100
mi = n1 * 1000
print('{} metros é igual a {} centímetros e {} milímetros.'.format(n1,c,mi))
