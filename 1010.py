total = 0.0

for _ in range(2):
    codigo, qtd, valor = input().split()
    qtd, valor = int(qtd), float(valor)
    total += (qtd * valor)

print(f"VALOR A PAGAR: R$ {total:.2f}")
