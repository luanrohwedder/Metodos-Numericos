import numpy as np

def funcao(x):
  return np.cos(x) - x

def proximo_X(x_atual, x_ant):
    return x_atual - funcao(x_atual) * (x_atual - x_ant)/(funcao(x_atual) - funcao(x_ant))

def secante(x0, x1, tolerancia, virgula):
    x0_alg = x0
    x1_alg = x1

    while True:
        #Calcula o x² e o f(x²)
        x2_alg = proximo_X(x1_alg, x0_alg)
        fx1 = funcao(x1_alg)
        fx2 = funcao(x2_alg)        
        erro = abs(x2_alg - x1_alg)

        #Adcionando na lista
        xAtual.append(round(x1_alg, virgula))
        xProx.append(round(x2_alg, virgula))
        funcao_xAtual.append(round(fx1, virgula))
        funcao_xProx.append(round(fx2, virgula))
        erros.append(round(erro, virgula))

        #Verificação de raíz
        if(erro <= tolerancia):
            return round(x2_alg, virgula)
        
        x0_alg = x1_alg
        x1_alg = x2_alg

#Listas
xAtual = []
xProx = []
funcao_xAtual = []
funcao_xProx = []
erros = []

#Inserção das aproximações inicias de X e a tolerância
print("Insira as aproximações iniciais:")
print("X0: ", end='')
x0 = float(input())
print("X1: ", end='')
x1 = float(input())

print("\nInsira a aproximacao:")
tol = float(input())

print("\nInsira quantas após a vírgula:")
dot = int(input());

res = secante(x0, x1, tol, dot)

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
