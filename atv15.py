lista = []

loop = True

valorX = int(input("Digite o valor que você quer encontrar: "))

while (loop):
    valor = input("Coloque um valor numérico. Para parar, digite 'CANCELAR': ")

    if (valor == "CANCELAR"):
        loop = False
    else:
        valorNumerico = int(valor)
        lista.append(valorNumerico)

print()

contador = 0

for n in range(0, len(lista)):
    if lista[n] == valorX:
        print(f'Valor X ({lista[n]}) encontrado na posição {n}')
    else:
        contador += 1

if contador > 0:
    print("Valor não encontrado.")
