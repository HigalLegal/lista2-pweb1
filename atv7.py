def fibonnaci(numero):
    if numero < 2:
        return numero
    return fibonnaci(numero - 1) + fibonnaci(numero - 2)


resultado = fibonnaci(int(input("Bote um número: ")))

print(f'Sequência de fibonnaci dele: {resultado}')
