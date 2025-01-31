notalist = {"Jose": 9, "Marcos": 7, "Manuel": 10}
def notas():
    promedio = 0
    max_estudiante  = ""
    max_nota = 0
    for name, nota in notalist.items():
        if nota > max_nota:
            max_nota = nota
            max_estudiante = name
        promedio += nota/len(notalist)
        
    return "Promedio: ",promedio," Nota máxima: ",max_nota,"Mejor estudiante: ",max_estudiante
print (notas())