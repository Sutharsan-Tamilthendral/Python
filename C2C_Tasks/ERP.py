erp = int(input("Enter Employee's Rating Point: "))
if erp <= 100:
    if erp >= 81:
        print("A")
    elif 61 <= erp <= 80:
        print("B")
    elif 51 <= erp <= 60:
        print("C")
    elif 30 <= erp <= 50:
        print("D")
    else:
        print("ERP is lesser than 50")
else:
    print("ERP is greater than 100")