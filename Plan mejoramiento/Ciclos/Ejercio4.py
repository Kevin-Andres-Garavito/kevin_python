def es_perfecto(numero):
    suma_divisores = 0
    i = 1
    while i < numero:
        if numero % i == 0:
            suma_divisores += i
        i += 1
    return suma_divisores == numero

def numeros_perfectos_entre_1_y_1000():
    numeros_perfectos = []
    numero = 1
    while numero <= 1000:
        if es_perfecto(numero):
            numeros_perfectos.append(numero)
        numero += 1
    return numeros_perfectos

def main():
    numeros_perfectos = numeros_perfectos_entre_1_y_1000()
    cantidad_numeros_perfectos = len(numeros_perfectos)

    print(f"Los números perfectos entre 1 y 1000 son:")
    for numero in numeros_perfectos:
        print(numero, end=" ")

    print(f"\nCantidad de números perfectos encontrados: {cantidad_numeros_perfectos}")

if __name__ == "__main__":
    main()
