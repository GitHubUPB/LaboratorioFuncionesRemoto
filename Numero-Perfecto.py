def perfect_number(n):
    a=0
    for i in range(1,n):
        if(n%i==0):
            a+=i
    if (a==n):
        print("numero perfecto")
    else:
        print("numero perfecto")
    if (a<=(n-3)):
        print("no es numero perfecto")
    else:
        print("numero casi perfecto")
n=int(input("Numero evaluado_: "))
perfect_number(n)
