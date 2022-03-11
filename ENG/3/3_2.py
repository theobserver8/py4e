hours = input("Introduce las horas: ")
rate = input("Introduce la tasa: ")

try:
    hours = float(hours)
    rate = float(rate)

except:
    print("Error, please enter numeric input")
    quit()

    rate = input("Introduce la tasa: ")
    rate = float(rate)

    if hours > 40:
        hours = hours - 40
        pay = 40*rate
        rate = rate * 1.5
        pay = pay + hours*rate
    else:
        pay = hours*rate

    print(pay)



