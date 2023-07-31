def generar_fibonacci(num_digitos):
    fibonacci = [0, 1]
    while True:
        next_num = fibonacci[-1] + fibonacci[-2]
        if len(str(next_num)) > num_digitos:
            break
        fibonacci.append(next_num)
    return fibonacci

if __name__ == "__main__":
    num_digitos = int(input("Ingrese la cantidad de dígitos para generar la serie de Fibonacci: "))
    fibonacci = generar_fibonacci(num_digitos)
    print("Serie de Fibonacci:")
    print(fibonacci)
