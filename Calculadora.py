n1 = 0
n2 = 0
operacao = ''
resultado = 0

n1 = int(input("digite o primeiro numero "))
operacao = input("digite a operação desejada ")
n2 = int(input("digite o segundo numero "))

if operacao == '+':
    resultado = n1 + n2
    print(resultado)
elif operacao == '-':
    resultado = n1 - n2
    print(resultado)
elif operacao == '/':
    resultado = n1/n2
    print(resultado)
elif operacao == '*':
    resultado = n1 * n2
    print(resultado)
else:
    resultado = 'vai dar não patrão'

