import math

a, b, c = map(float, input().split())

if a == 0 or (math.pow(b,2) - 4*a*c) < 0:
    print("Impossivel calcular")

else:
    delta=math.pow(b,2)-4*a*c
    r1=(-b+math.sqrt(delta))/(2*a)
    r2=(-b+-math.sqrt(delta))/(2*a)
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')
