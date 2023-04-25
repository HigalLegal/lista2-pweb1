lista = []

loop = True

while (loop):
    valor = input("Coloque um valor numérico. Para parar, digite 'CANCELAR': ")

    if (valor == "CANCELAR"):
        loop = False
    else:
        valorNumerico = int(valor)
        lista.append(valorNumerico)

for n in lista:
    if n % 2 == 0:
        print(f'PAR: {n}')
