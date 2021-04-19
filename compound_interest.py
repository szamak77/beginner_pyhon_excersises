yrs = input("Enter how much years do you want to save:")
rate = input("Enter Yearly Rate:")
percent = input("Enter anual profit percentage:")
y = float(yrs)
r = float(rate)
p = float(percent)*0.01
pay = y*r
if y <= 40.0:
    pay = y*r
else:
    pay = 40*r+1.5*r*(y-40)
print(pay)
