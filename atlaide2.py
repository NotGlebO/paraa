a = float(input("Ievadīt spirkumu summa: "))

if 500 > a >= 200:
    b = a * 10 / 100
    c = a - b
    print("Jums atlaide 10%, summa ar atlaide: " + str(c) + " eiro")
if a >= 500:
    b = a * 20 / 100
    c = a - b
    print("Jums atlaide 20%, summa ar atlaide: " + str(c) + " eiro")
else:
    print("pirkumu summa " + str(a))
