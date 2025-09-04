value=float(input())

centavos=round(value*100)

notes=[100*100, 50*100, 20*100, 10*100, 5*100, 2*100]

coins=[1*100, 50, 25, 10, 5, 1]

print("NOTAS:")
for note in notes:
    qtd = centavos // note
    centavos %= note
    print(f"{qtd} nota(s) de R$ {note/100:.2f}")

print("MOEDAS:")
for coin in coins:
    qtd = centavos // coin
    centavos %= coin
    print(f"{qtd} moeda(s) de R$ {coin/100:.2f}")
