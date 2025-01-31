def frecuencia_palabras(): 
    frase = "soy un funcionario publico"
    palabras = frase.split()
    frecuencia = {}

    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
            
    return frecuencia

print(frecuencia_palabras())
