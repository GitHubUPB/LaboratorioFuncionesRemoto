def is_prime(n):
    cont=0
    prim=0
    while cont<=n:
        cont+=1
        if n % cont == 0:
            prim += 1

    return prim
contP=0
try:
    n=int(input("Valor evaluado: "))
    is_prim(n)
    r=is_prim(n)

    if r>2:
        print("0")
    else:
     print("1")
     contP+=1
except Exception:
    print("-1")

c=input(" voler a intentarlo? y/n: ")
if c=="y":
       try:
        while c!="n":

            d = int(input("Base Nueva a: "))
            if d<=0:
                raise Exception("-1")

            if d <=0:

                break
            is_prim(d)
            s=is_prim(d)
            if s > 2:
                print("0")
            else:
                print("1")
                contP+=1


       except Exception:
           print("-1")

else:
    if c=="n":

        print("Gacias")

print("Cantidad De Primos: ",contP)
