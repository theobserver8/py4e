nota = input("Introduce una puntuación: ")

try:
    nota = float(nota)
    if nota <=0.0 or nota>=1.0:
        print("Puntuación incorrecta")
    elif nota >= 0.9:
        print("Sobresaliente")
    elif nota >= 0.8:
        print("Notable")
    elif nota >= 0.7:
        print("Bien")
    elif nota >= 0.6:
        print("Suficiente")
    else:
        print("Insuficiente")

except:
    print("Puntuación incorrecta")