'''Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada'''

n = int(input('Escreva um número: '))
do = n * 2
tri = n * 3
rq = n ** (1/2)
print('O dobro de {} é {}, o triplo é {}\nA raiz quadrada é {:.3f}'.format(n,do,tri,rq))

#pw(n , (1/2)) calcula a raiz quadrada
