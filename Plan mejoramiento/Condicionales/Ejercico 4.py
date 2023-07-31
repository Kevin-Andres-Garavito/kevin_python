def obtener_nota():
    while True:
        try:
            nota = float(input("Ingresa una nota entre 0 y 10: "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("La nota ingresada está fuera del rango permitido. Intenta nuevamente.")
        except ValueError:
            print("Debes ingresar un número válido.")

def obtener_calificacion(nota):
    if nota < 5:
        return "Insuficiente"
    elif nota < 7:
        return "Suficiente"
    elif nota < 9:
        return "Bien"
    elif nota < 10:
        return "Notable"
    else:
        return "Sobresaliente"

def main():
    nota = obtener_nota()
    calificacion = obtener_calificacion(nota)
    print(f"La nota {nota} corresponde a la calificación: {calificacion}.")

if __name__ == "__main__":
    main()