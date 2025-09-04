valores=[]
for _ in range(6):
    n=float(input())
    if n>=0:
        valores.append(n)

print(f'{len(valores)} valores positivos')