hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
pay = h*r
if h <= 40.0:
    pay = h*r
else:
    pay = 40*r+1.5*r*(h-40)
print(pay)
