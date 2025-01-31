mark_list = {"Pedro": 9, "Juan": 7, "Ana": 10}
def nota():
    promedio = 0
    max_student  = ""
    max_mark = 0
    for name, mark in mark_list.items():
        if mark > max_mark:
            max_mark = mark
            max_student = name
        promedio += mark/len(mark_list)
        
    return "Promedio: ",promedio," Nota máxima: ",max_mark,"Mejor estudiante: ",max_student
print (nota())