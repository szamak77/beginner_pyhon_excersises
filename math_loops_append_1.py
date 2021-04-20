a = 9
b = 2
c = 8
sequence = [a, b]
for i in range(4):
    a, b = b, a + b + c
    sequence.append(b)
print(a + b + c)
