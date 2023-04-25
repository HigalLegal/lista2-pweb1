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

lista.sort()


print(f'Menor valor: {lista[0]}')
print(f'Maior valor: {lista[len(lista) - 1]}')
