print('Bem vindo a CalculadoraIsaac')

def adicao(a, b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a,b):
    return a / b

calc = int(input('Qual tipo você quer usar?\n1. Adição \n2. Subtração \n3. Multiplicação \n4. Divisão \n5. Sair \nDigite aqui: '))
if calc == 1:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print(adicao(a, b))

if calc == 2:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print(subtracao(a,b))

if calc == 3:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print(multiplicacao(a,b))

if calc == 4:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print(divisao(a,b))

if calc == 5:
    print('Saindo da calculadora...')