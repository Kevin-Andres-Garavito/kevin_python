#Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene. Cuando el número
#exceda los límites emita un mensaje y finalice el programa
def obtener_numero():
    while True:
        try:
            numero = int(input("Ingresa un número entre 0 y 9999: "))
            if 0 <= numero <= 9999:
                return numero
            else:
                print("El número ingresado está fuera del rango permitido. Intenta nuevamente.")
        except ValueError:
            print("Debes ingresar un número válido.")

def contar_cifras(numero):
    if numero == 0:
        return 1
    else:
        return len(str(numero))

def main():
    numero = obtener_numero()
    cifras = contar_cifras(numero)
    print(f"El número {numero} tiene {cifras} cifras.")

if __name__ == "__main__":
    main()
    


