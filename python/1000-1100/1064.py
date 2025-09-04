valores=[]
for _ in range(6):
    n=float(input())
    if n>=0:
        valores.append(n)
media=sum(valores)/len(valores)
print(f'{len(valores)} valores positivos')
print(f"{media:.1f}")