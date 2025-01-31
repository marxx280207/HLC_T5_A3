def suma_promedio():
    numeros = [1,2,3,4,5]
    suma = 0
    
    for i in numeros:
        suma = suma + i
        
    print ("la suma es", suma)
    print ("El promedii es", suma/len(numeros))

suma_promedio()