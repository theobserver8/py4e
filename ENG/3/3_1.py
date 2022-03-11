hours = input("Introduce las horas: ")
rate = input("Introduce la tasa: ")

hours = float(hours)
rate = float(rate)

if hours > 40:
    hours = hours - 40
    pay = 40*rate
    rate = rate * 1.5
    pay = pay + hours*rate
else:
    pay = hours*rate

print(pay)