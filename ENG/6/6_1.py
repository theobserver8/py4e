fruit = "banana"

index = 1
while index <= len(fruit):
    letter = fruit[index*(-1)]
    print(letter)
    index = index + 1

for char in fruit:
    print(char)