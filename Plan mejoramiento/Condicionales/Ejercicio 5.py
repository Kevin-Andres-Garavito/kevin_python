def pregunta1():
    respuesta = input("¿Colón descubrió América? (Responde 'Si' o 'No'): ")
    if respuesta.lower() == "si":
        print("Respuesta correcta.")
        return True
    else:
        print("Respuesta incorrecta.")
        return False

def pregunta2():
    respuesta = input("¿La independencia de Colombia fue en el año 1810? (Responde 'Si' o 'No'): ")
    if respuesta.lower() == "si":
        print("Respuesta correcta.")
        return True
    else:
        print("Respuesta incorrecta.")
        return False

def pregunta3():
    respuesta = input("¿The Doors fue un grupo de rock Americano? (Responde 'Si' o 'No'): ")
    if respuesta.lower() == "si":
        print("Respuesta correcta.")
        return True
    else:
        print("Respuesta incorrecta.")
        return False

def juego_preguntas():
    print("Bienvenido al juego de preguntas. Responde 'Si' o 'No' a las siguientes preguntas.")
    
    if pregunta1():
        if pregunta2():
            pregunta3()

    print("Fin del juego.")

if __name__ == "__main__":
    juego_preguntas()
