'''Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor'''

'''
n = int(input('Escreva um número: '))
su = n + 1
an = n - 1
print ('O sucessor do número {} é {} e seu antecessor é {} '.format(n,su,an))
'''
# (Dessa forma também está correto)

n = int(input('Escreva um número: '))
print('O sucessor do número {} é {} e seu antecessor é {} '.format(n, (n + 1), (n - 1)))
