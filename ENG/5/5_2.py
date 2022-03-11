largest = None
smallest = None
count = 0

while True:
    num = input("Enter a number: ")
    if num == "hecho":
        break
  
    try:
        num = int(num)
        
        if count == 0:
            largest = num
            smallest = num
            count = count + 1
        
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
        
    except:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)