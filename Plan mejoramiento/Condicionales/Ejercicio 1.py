
# Escribe un programa que pida tres números y que escriba si son los tres
#iguales, si hay dos iguales o si son los tres distintos
def pedir_numeros():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    num3 = float(input("Introduce el tercer número: "))
    return num1, num2, num3

def verificar_numeros(num1, num2, num3):
    if num1 == num2 and num2 == num3:
        return "Los tres números son iguales."
    elif num1 == num2 or num1 == num3 or num2 == num3:
        return "Hay dos números iguales."
    else:
        return "Los tres números son distintos."

def main():
    num1, num2, num3 = pedir_numeros()
    resultado = verificar_numeros(num1, num2, num3)
    print(resultado)

if __name__ == "__main__":
    main()
    

    