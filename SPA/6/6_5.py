cadena = 'X-DSPAM-Confidence:0.8475'

posicion = cadena.find(':')
registro = cadena[posicion+1:]

numero = float(registro)
print(numero)