
from time import time

def numerosPrimos(inicio = 0, fin = 1000):
    tiempo_inicial = time()
    primos = []
    for i in range(inicio,fin + 1):
        if i == 0 or i == 1:
            pass
        else:
            casos_incorrectos = 0
            for j in range(1,i):
                n = i%j
                if n == 0:
                    casos_incorrectos += 1
            if casos_incorrectos == 1:
                primos.append(i)
    tiempo_final = time()
    print(primos, "\n\nLa ejecucion tardo {} segundos".format(tiempo_final-tiempo_inicial))
    

if "__main__" == __name__:
    numerosPrimos(0,1000)
