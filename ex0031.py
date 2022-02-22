'''Desenvolva um programa que pergunte a distância de uma viagem em KM.
Calcule o preço da passagem, cobrando R$0,50 por KM para viagens até 200KM e R$0,45 para viagens mais longas.'''

distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a comecar uma viagem de {}KM.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
    print('E o preço da sua passagem será de R${:.2f}'.format(preco))
else: 
    preco = distancia * 0.45
    print('E o preço da sua passagem será de R${:.2f}'.format(preco))
