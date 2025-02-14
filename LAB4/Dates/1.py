from datetime import date, timedelta 

a = date.today()
b = a - timedelta(days=5)

print("Current data: ", a)
print("Substract five days: ", b)