total = 0
count = 0

while True:
    line = input("> ")
    if line == "done":
        break
        
    try:
        number = int(line)
        total = total + number
        count = count + 1
    except:
        print("Invalid input")


print(total, count, total/count)