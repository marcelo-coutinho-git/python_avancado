'''
Crie um programa que diga “se você precisar ir ao mercado”. Você precisa ir ao mercado se “faltar comida” 
ou “se for sábado”. Mostre na saída do programa o valor lógico, indicando sim ou não
'''

dia_da_semana = input('Digite o dia da Semana: ')
falta_comida = input('Falta comida? (sim ou nao): ')

if dia_da_semana == 'sabado' or falta_comida == 'sim':
    print('Voce deve ir ao mercado')

else:
    print('Voce nao precisa ir ao mercado')