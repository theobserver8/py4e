txt = 'but soft what light in yonder window breaks'
words = txt.split()


t = list()
for word in words:
    t.append((len(word), word))

print(t)

t.sort()
print(t)