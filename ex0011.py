"""Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m² """

h = int(input('Escreva a altura em metros: '))
l = int(input('Escreva a largura em metros: '))
a = h * l
t = a / 2
print('Será necessário {} litros de tinta para {} m². '.format(t, a))
