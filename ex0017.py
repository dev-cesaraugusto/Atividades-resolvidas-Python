""" Faça um progrma que leia o oposto do cateto adjacente de um triangulo retangulo, calcue e mostre o comprimento da hipotenusa """

"""co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))      #metodo alternativo
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))"""

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai meidr {:.2f}'.format(hi))
