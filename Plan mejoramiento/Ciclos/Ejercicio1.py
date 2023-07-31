#Determinar los divisores de un número introducido por 
#teclado 
def obtener_numero():
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo: "))
            if numero > 0:
                return numero
            else:
                print("Por favor, ingrese un número entero positivo.")
        except ValueError:
            print("Debes ingresar un número válido.")

def calcular_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def main():
    numero = obtener_numero()
    divisores = calcular_divisores(numero)
    
    print(f"Los divisores de {numero} son:", end=" ")
    for divisor in divisores:
        print(divisor, end=" ")

if __name__ == "__main__":
    main()
   