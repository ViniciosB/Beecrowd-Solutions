par=0; impar=0; pos=0; neg=0
for _ in range(5):
    n=int(input())
    if (n%2)==0:
        par+=1
    if (n%2)!=0:
        impar+=1
    if n>0:
        pos+=1
    if n<0:
        neg+=1

print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{pos} valor(es) positivo(s)")
print(f"{neg} valor(es) negativo(s)")
