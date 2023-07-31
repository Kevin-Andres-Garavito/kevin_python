import random

def generar_arreglo_sin_repetir(n):
    arreglo = []
    numeros_generados = set()

    while len(arreglo) < n:
        numero = random.randint(1, 100)  # Puedes ajustar el rango según tus necesidades.
        if numero not in numeros_generados:
            numeros_generados.add(numero)
            arreglo.append(numero)
        else:
            print(f"El número {numero} ya está en el arreglo. No se permite duplicados.")

    return arreglo

if __name__ == "__main__":
    n = int(input("Ingrese el tamaño del arreglo (n): "))
    arreglo = generar_arreglo_sin_repetir(n)
    print("Arreglo generado:", arreglo)
