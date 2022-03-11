def calculo_salario(horas, tarifa):
    salario = int(horas)*float(tarifa)
    if horas > 40:
        extra = (horas-40)*0.5*tarifa
        salario = salario + extra
    print("Salario:", salario)

horas = input("Introduzca las Horas: ")
try:
    horas = int(horas)
    tarifa = input("Introduzca la tarifa: ")
    tarifa = float(tarifa)

    salario = calculo_salario(horas, tarifa)

except:
    print("Error, por favor introduzca un número")