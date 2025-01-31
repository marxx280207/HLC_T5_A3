def longitudes_palabras(palabras):
    return {palabra: len(palabra) for palabra in palabras}

print(longitudes_palabras(['gato', 'perro', 'elefante']))
