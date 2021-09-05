import numpy as np

def funcao(x):
  return np.exp(-x) - np.log(x)

def bissecao(a, b, tolerancia):
    if(funcao(a)*funcao(b) > 0):
        print("Intervalo nao e valido!")
    else:        
        n = np.ceil(np.log((b-a)/tolerancia)/np.log(2))
        print()
        print('Iterações: ' , end='')
        print(n)
        iteracoes.append(n)
        a_alg = a
        b_alg = b

        intervalo_a.append(a_alg)
        intervalo_b.append(b_alg)
      
        for i in range(int(n)):
            p = (a_alg + b_alg) / 2
            fp = funcao(p)            
            e = (b_alg - a_alg) / 2

            raizes.append(round(p, 5))
            funcao_raizes.append(round(fp, 5))
            funcao_a.append(round(funcao(a_alg), 5))
            funcao_b.append(round(funcao(b_alg), 5))
            erro.append(round(e, 5))
            
            if funcao(a_alg) * fp < 0: 
                b_alg = p                
            else: 
                a_alg = p
                
            intervalo_b.append(round(b_alg, 5))   
            intervalo_a.append(round(a_alg, 5))
            
        return round(p, 5)

#Listas
iteracoes = []
raizes = []
funcao_raizes = []
funcao_a = []
funcao_b = []
intervalo_a = []
intervalo_b = []
erro = []

#Insercao do intervalo
print("Insira o intervalo:")
print("a: ", end='')
a = float(input())
print("b: ", end='')
b = float(input())

#Insercao da aproximacao
print("\nInsira a aproximacao:")
tol = float(input())

res = bissecao(a, b, tol)

print()

print('{:12}'.format(' n'), end='')
print('{:12}'.format('a'), end='')
print('{:12}'.format('b'), end='')
print('{:10}'.format('x'), end='')
print('{:12}'.format('f(a)'), end='')
print('{:13}'.format('f(x)'), end='')
print('{:12}'.format('f(b)'), end='')
print('f(e)')

for i in range(len(raizes)):
    print('{:2}'.format(i+1), end='  |')    
    print('{0:9}'.format(intervalo_a[i]), end='  |')    
    print('{0:9}'.format(intervalo_b[i]), end='  |')
    print('{:9}'.format(raizes[i]), end='  |')
    print('{:9}'.format(funcao_a[i]), end='  |')
    print('{:9}'.format(funcao_raizes[i]), end='  |')
    print('{:9}'.format(funcao_b[i]), end='  |')
    print('{:10}'.format(erro[i])) 

print(f"\n A raíz é: {res}") 
