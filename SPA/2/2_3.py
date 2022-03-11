horas = input("Introduzca Horas: ")
tarifa = input("Introduzca tarifa: ")
salario = int(horas)*float(tarifa)
print("Salario:", salario) #Aquí no se puede concatenar con el + porque salario no es un string.