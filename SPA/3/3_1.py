horas = input("Introduzca las Horas: ")
horas = int(horas)
tarifa = input("Introduzca la tarifa: ")
tarifa = float(tarifa)

salario = int(horas)*float(tarifa)
if horas > 40:
    extra = (horas-40)*0.5*tarifa
    salario = salario + extra

print("Salario:", salario) #Aquí no se puede concatenar con el + porque salario no es un string.