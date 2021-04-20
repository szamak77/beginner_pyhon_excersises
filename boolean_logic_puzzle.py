a, b = True, False
out = (a and b) or (a and b and not a) or a
print(out)
