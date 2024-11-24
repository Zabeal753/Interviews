# Python

def comparar_y_filtrar(n, lista):
    # Comprobamos si el tamaño de la lista es correcto
    if len(lista) != n:
        raise ValueError("El tamaño de la lista no coincide con el entero proporcionado.")
    
    # Convertimos la lista a una lista mutable
    lista = list(lista)
    
    while True:
        cambios = False  # Variable para rastrear si hubo cambios en la lista
        
        # Creamos una copia de la lista para evitar modificarla mientras iteramos
        nueva_lista = lista.copy()
        
        for i in range(len(lista)):
            if lista[i] > 0:  # Si es positivo
                # Comparamos con el siguiente elemento si existe y es negativo
                if i + 1 < len(lista) and lista[i + 1] < 0:
                    if abs(lista[i]) > abs(lista[i + 1]):  # El positivo gana
                        nueva_lista[i + 1] = None  # Marcamos el negativo para eliminar
                        cambios = True
                    else:
                        nueva_lista[i] = None # Marcamos el positivo para eliminar
                        cambios = True 

            if lista[-1] > 0 and lista[0] < 0:
                if abs(lista[-1]) > abs(lista[0]):  # El positivo gana
                    nueva_lista[0] = None  # Marcamos el negativo para eliminar
                    cambios = True
                else:
                    nueva_lista[-1] = None  # Marcamos el positivo para eliminar
                    cambios = True

        # Filtramos los elementos marcados como None
        nueva_lista = [x for x in nueva_lista if x is not None]
        
        # Si no hubo cambios, salimos del bucle
        if not cambios:
            break
        
        # Actualizamos la lista original con los nuevos valores
        lista = nueva_lista
    
    return lista

# Ejemplo de uso
n = 6
lista = [3, -2, -5, 4, -1, 2]
resultado = comparar_y_filtrar(n, lista)
print("Valores restantes en la lista:", resultado)