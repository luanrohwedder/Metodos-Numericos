
def funcao(x):
    return x**2-3

def derivada(x):
    return 2*x

def proximo_X(x):
    return x - funcao(x)/derivada(x)

def Newton(x, tol):
    x0 = x

    while True:
        #Cálculo da função de x e a derivada
        fx0 = funcao(x0)
        fdx0 = derivada(x0)
        
        #Cálculo do pŕoximo x
        x1 = proximo_X(x0)
        fx1 = funcao(x1)

        erro = abs(x1 - x0)

        #Adcionando na lista
        xAtual.append(round(x0, 5))
        xProx.append(round(x1, 5))
        funcao_xAtual.append(round(fx0, 5))
        funcao_xProx.append(round(fx1, 5))
        erros.append(round(erro, 5))

        if(erro <= tol):
            return round(x1, 5)

        x0 = x1

#Listas
xAtual = []
xProx = []
funcao_xAtual = []
funcao_xProx = []
erros = []

#Inserção das aproximação inicial de X e a tolerância
print("Insira a aproximação inicial de x:")
print("X0: ", end='')
x = float(input())

print("\nInsira a aproximacao:")
tol = float(input())

res = Newton(x, tol)

print()

print('{:11}'.format(' n'), end='')
print('{:10}'.format('Xn'), end='')
print('{:12}'.format('Xn+1'), end='')
print('{:10}'.format('f(Xn)'), end='')
print('{:11}'.format('f(Xn+1)'), end='')
print('{:13}'.format('|Xn+1 - Xn|'))

for i in range(len(xProx)):    
    print('{:2}'.format(i+1), end='  |')
    print('{:9}'.format(xAtual[i]), end='  |')
    print('{:9}'.format(xProx[i]), end='  |')
    print('{:9}'.format(funcao_xAtual[i]), end='  |')
    print('{:9}'.format(funcao_xProx[i]), end='  |')
    print('{:9}'.format(erros[i]))

print(f"\n A raíz é: {res}")
