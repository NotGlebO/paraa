a = float(input("Ievadīt spirkumu summa: "))

if a >= 200:
    b = a * 10 / 100
    c = a - b
    print("Jums atlaide 10%, summa ar atlaide: " + str(c) + " eiro")
    
else:
    print("pirkumu summa " + str(a))
