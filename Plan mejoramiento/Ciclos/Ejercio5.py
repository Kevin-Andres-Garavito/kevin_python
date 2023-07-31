def es_primo(numero):
    if numero <= 1:
        return False
    i = 2
    while i <= numero**0.5:
        if numero % i == 0:
            return False
        i += 1
    return True

def numeros_primos_entre_1_y_1000():
    numeros_primos = []
    numero = 1
    while numero <= 1000:
        if es_primo(numero):
            numeros_primos.append(numero)
        numero += 1
    return numeros_primos

def main():
    numeros_primos = numeros_primos_entre_1_y_1000()
    cantidad_numeros_primos = len(numeros_primos)

    print(f"Los números primos entre 1 y 1000 son:")
    for numero in numeros_primos:
        print(numero, end=" ")

    print(f"\nCantidad de números primos encontrados: {cantidad_numeros_primos}")

if __name__ == "__main__":
    main()
