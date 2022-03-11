def calcula_calificacion(nota):
    if nota <=0.0 or nota>=1.0:
        cadena = "Puntuación incorrecta"
    elif nota >= 0.9:
        cadena = "Sobresaliente"
    elif nota >= 0.8:
        cadena = "Notable"
    elif nota >= 0.7:
        cadena = "Bien"
    elif nota >= 0.6:
        cadena = "Suficiente"
    else:
        cadena = "Insuficiente"
    return cadena

nota = input("Introduce una puntuación: ")

try:
    nota = float(nota)
    puntuacion = calcula_calificacion(nota)
    print(puntuacion)

except:
    print("Puntuación incorrecta")