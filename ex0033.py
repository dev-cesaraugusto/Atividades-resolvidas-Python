'''Faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor '''
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a 
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O menor valor digitado foi {}'.format(menor))
#Verificando quem é o maior
maior = a 
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('-=-' * 20)
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
print('-=-' * 20)