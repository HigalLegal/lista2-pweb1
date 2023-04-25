lista = []

loop = True

while (loop):
    valor = input("Coloque um valor numérico. Para parar, digite 'CANCELAR': ")

    if (valor == "CANCELAR"):
        loop = False
    else:
        valorNumerico = int(valor)
        lista.append(valorNumerico)

print()

lista = sorted(lista, key=int, reverse=True)

for n in lista:
    print(f'Numeros na ordem decrescente: {n}')
