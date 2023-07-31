#Pedir 3 numeros e indicar cual de ellos es el valor del medio. Ej 11, 2 1000, el
#valor del medio es 11. No use operadores lógicos
def pedir_numeros():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    num3 = float(input("Introduce el tercer número: "))
    return num1, num2, num3

def encontrar_medio(num1, num2, num3):
    if num1 <= num2 and num2 <= num3:
        return num2
    elif num3 <= num2 and num2 <= num1:
        return num2
    elif num2 <= num1 and num1 <= num3:
        return num1
    else:
        return num3

def main():
    num1, num2, num3 = pedir_numeros()
    valor_medio = encontrar_medio(num1, num2, num3)
    print("El valor del medio es:", valor_medio)

if __name__ == "__main__":
    main()
    
