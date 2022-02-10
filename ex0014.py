"""Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit."""

c: float = float(input('Escreva a temperatura em ºC: '))
f = (c * 1.8) + 32
print(f'{c}ºC  é igual a {f:.2f}ºF')
