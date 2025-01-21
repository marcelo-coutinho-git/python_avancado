'''
Crie um programa que receba seu saldo bancario e o quanto voce deve
Em seguida o programa vai dizer se voce tem o saldo positivo ou negativo
'''

saldo_bancario = int(input("Digite seu Saldo: "))
divida = int(input("Digite sua Divida: "))

print(f'Seu saldo é R${saldo_bancario}')
print(f'Sua divida é de R${divida}')

saldo = saldo_bancario-divida

if saldo_bancario > divida:
    print(f'Seu saldo é de R${saldo}, portanto ele é positivo')
elif saldo_bancario == divida:
    print("Voce nao possui saldo")
else:
    print(f'Seu saldo é de R${saldo}, portanto ele é Negativo')