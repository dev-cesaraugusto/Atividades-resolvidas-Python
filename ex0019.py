'''Um professor quer sortear um dos seus 4 alunos para apagar o quadro.
faça um progrma que ajude ele, lendo o nome deles e escrevendo o nome do escolhido'''

'''import random
lista = str(input('Digite o nome do aluno 1: ')), str(input('Digite o nome do aluno 2: ')),\
        str(input('Digite o nome do aluno 3: ')), str(input('Digite o nome do aluno 4: '))
print('O aluno sorteado foi o {}'.format(random.choice(lista))) #choice = uma escolha dentro da lista'''

'''import random
lista = ['Lucas', 'mateus', 'joao', 'marcos']
print('O aluno sorteado foi o {}'.format(random.choice(lista)))'''

import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1,n2,n3,n4]
print('O aluno escolhido foi {}'.format(random.choice(lista)))

