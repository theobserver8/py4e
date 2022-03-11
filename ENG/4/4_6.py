def computepay(hours, rate):
    if hours > 40:
        hours = hours - 40
        pay = 40*rate
        rate = rate * 1.5
        pay = pay + hours*rate
    else:
        asdf
        pay = hours*rate

    return pay

hours = input("Introduce las horas: ")
rate = input("Introduce la tasa: ")

hours = float(hours)
rate = float(rate)

pay = computepay(hours, rate)
print(pay)