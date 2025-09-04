values = list(map(float, input().split()))
values.sort(reverse=True)  # Ordena decrescente
A, B, C = values

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if abs(A**2 - (B**2 + C**2)) < 1e-9:  # tolerância para ponto flutuante
        print("TRIANGULO RETANGULO")
    elif A**2 > (B**2 + C**2):
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    if abs(A - B) < 1e-9 and abs(B - C) < 1e-9:
        print("TRIANGULO EQUILATERO")
    elif abs(A - B) < 1e-9 or abs(B - C) < 1e-9 or abs(A - C) < 1e-9:
        print("TRIANGULO ISOSCELES")
