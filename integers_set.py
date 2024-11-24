# Python

from collections import deque

def multiplicar_hasta_n(A, N):
    # Ordenamos A para asegurar que las soluciones sean lexicográficamente menores
    A = sorted(A)
    
    # Cola para BFS: cada elemento es una tupla (valor_actual, secuencia)
    cola = deque([(1, [1])])
    visitado = set()  # Para evitar ciclos y valores repetidos
    
    while cola:
        valor_actual, camino = cola.popleft()
        
        # Si alcanzamos o superamos N, retornamos el camino
        if valor_actual == N:
            return camino
        
        for mult in A:
            proximo = valor_actual * mult
            # Solo consideramos valores que no hemos visitado
            if proximo not in visitado:
                visitado.add(proximo)
                # Agregamos el nuevo valor y su camino a la cola
                cola.append((proximo, camino + [mult] ))

# Ejemplo de uso
A = [2, 3, 5]
N = 12
resultado = multiplicar_hasta_n(A, N)
print("Secuencia lexicográficamente menor para alcanzar", N, ":", resultado)