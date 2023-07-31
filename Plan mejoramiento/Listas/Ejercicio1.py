import random

def generar_arreglo(n):
    return [random.randint(1, 100) for _ in range(n)]

def imprimir_arreglo(arreglo):
    print("Arreglo original:", arreglo)

def suma(arreglo):
    return sum(arreglo)

def promedio(arreglo):
    return sum(arreglo) / len(arreglo)

def mayor(arreglo):
    return max(arreglo)

def menor(arreglo):
    return min(arreglo)

def ordenar_ascendente(arreglo):
    return sorted(arreglo)

def ordenar_descendente(arreglo):
    return sorted(arreglo, reverse=True)

def moda(arreglo):
    freq = {}
    for num in arreglo:
        freq[num] = freq.get(num, 0) + 1
    max_freq = max(freq.values())
    return [num for num, f in freq.items() if f == max_freq]

def mediana(arreglo):
    sorted_arreglo = sorted(arreglo)
    n = len(sorted_arreglo)
    if n % 2 == 0:
        return (sorted_arreglo[n//2 - 1] + sorted_arreglo[n//2]) / 2
    else:
        return sorted_arreglo[n//2]

def buscar_numero(arreglo, numero):
    indices = [i for i, num in enumerate(arreglo) if num == numero]
    return indices, len(indices)

def menu():
    print("\nMenú de operaciones:")
    print("a. Imprimir arreglo original")
    print("b. Suma")
    print("c. Promedio")
    print("d. Mayor")
    print("e. Menor")
    print("f. Ordenar ascendente")
    print("g. Ordenar descendente")
    print("h. Moda")
    print("i. Mediana")
    print("j. Buscar")
    print("q. Salir")
    return input("Seleccione una opción: ").lower()

if __name__ == "__main__":
    n = int(input("Ingrese el tamaño del arreglo (n): "))
    arreglo = generar_arreglo(n)
    print("Arreglo generado:", arreglo)

    while True:
        opcion = menu()

        if opcion == 'a':
            imprimir_arreglo(arreglo)
        elif opcion == 'b':
            print("Suma:", suma(arreglo))
        elif opcion == 'c':
            print("Promedio:", promedio(arreglo))
        elif opcion == 'd':
            print("Mayor:", mayor(arreglo))
        elif opcion == 'e':
            print("Menor:", menor(arreglo))
        elif opcion == 'f':
            print("Arreglo ascendente:", ordenar_ascendente(arreglo))
        elif opcion == 'g':
            print("Arreglo descendente:", ordenar_descendente(arreglo))
        elif opcion == 'h':
            print("Moda:", moda(arreglo))
        elif opcion == 'i':
            print("Mediana:", mediana(arreglo))
        elif opcion == 'j':
            numero_buscar = int(input("Ingrese el número a buscar: "))
            indices, cantidad = buscar_numero(arreglo, numero_buscar)
            if cantidad > 0:
                print(f"El número se encuentra en las posiciones: {indices}")
                print(f"Cantidad de veces que aparece: {cantidad}")
            else:
                print("El número no se encuentra en el arreglo.")
        elif opcion == 'q':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
