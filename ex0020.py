'''O mesmo professor quer sortear a ordem da apresentação dos alunos, faça um programa que leia o nome dos quatro alunos e mostre
a ordem sorteada'''

import random
a1 = str(input('Digite o aluno 1:'))
a2 = str(input('Digite o aluno 2:'))
a3 = str(input('Digite o aluno 3:'))
a4 = str(input('Digite o aluno 4:'))
lista = [a1,a2,a3,a4]
random.shuffle(lista)
print('A ordem de apresentação será ')
print(lista)
