n=int(input())

for _ in range(n):
    impar=[]
    x,y=map(int, input().split())
    for i in range(min(x,y)+1,max(x,y),1):
        if i%2!=0:
            impar.append(i)
    print(sum(impar))