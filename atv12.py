lista = []

loop = True

while (loop):
    valor = input("Coloque um valor numérico. Para parar, digite 'CANCELAR': ")

    if (valor == "CANCELAR"):
        loop = False
    else:
        valorNumerico = int(valor)
        lista.append(valorNumerico)

print(f'Soma dos números: {sum(lista)}')
