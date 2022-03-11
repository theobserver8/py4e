horas = input("Introduce las horas: ")
rate = input("Introduce el rate: ")
pay = int(horas)*float(rate) #Hay que convertir los strings que damos, a números.
pay = str(pay) #Ese resultado numérico hay que convertirlo a cadena
print("Pay: " + pay) #Se convierte a cadena ya que la concatenación solo funciona con strings.