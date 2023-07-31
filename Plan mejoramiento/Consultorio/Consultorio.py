from datetime import datetime, date, time
from typing import List

class Paciente:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.citas = []

    def registrar_cita(self, medico, fecha, hora, motivo):
        if fecha.month != date.today().month:
            print("Solo se pueden registrar citas en el mes vigente.")
            return

        if not medico.validar_horario(hora):
            print("El médico no tiene disponibilidad en esa hora.")
            return

        if not self.validar_cita(fecha, hora):
            print("Ya tienes una cita registrada en esa fecha y hora.")
            return

        cita = Horario(fecha, hora, self, medico, motivo)
        medico.agregar_cita(cita)
        self.citas.append(cita)
        print(f"Cita registrada para el {fecha} a las {hora} con el Dr. {medico.nombre}.")

    def consultar_citas(self):
        if not self.citas:
            print("No tienes citas registradas.")
            return

        print("Citas registradas:")
        for cita in self.citas:
            print(f"Fecha: {cita.fecha}, Hora: {cita.hora}, Médico: {cita.medico.nombre}, Motivo: {cita.motivo}")

    def eliminar_cita(self, cita):
        if cita.fecha < date.today():
            print("No se puede eliminar una cita pasada.")
            return

        hora_actual = datetime.now().time()
        hora_limite = (datetime.combine(date.today(), cita.hora) - datetime.timedelta(hours=2)).time()

        if cita.fecha == date.today() and hora_actual > hora_limite:
            print("No se puede eliminar la cita con menos de 2 horas de anticipación.")
            return

        cita.medico.eliminar_cita(cita)
        self.citas.remove(cita)
        print("Cita eliminada con éxito.")

    def validar_cita(self, fecha, hora):
        for cita in self.citas:
            if cita.fecha == fecha and cita.hora == hora:
                return False
        return True

class Médico:
    def __init__(self, nombre: str, especialidad: str):
        self.nombre = nombre
        self.especialidad = especialidad
        self.citas = []
        self.horarios = []

    def validar_horario(self, hora):
        return hora in self.horarios

    def agregar_cita(self, cita):
        self.citas.append(cita)

    def eliminar_cita(self, cita):
        self.citas.remove(cita)

    def agregar_horario(self, horarios):
        self.horarios = horarios

    def consultar_horario_disponible(self):
        print("Horarios disponibles:")
        for horario in self.horarios:
            print(horario)

class Horario:
    def __init__(self, fecha: date, hora: time, paciente, medico, motivo: str):
        self.fecha = fecha
        self.hora = hora
        self.paciente = paciente
        self.medico = medico
        self.motivo = motivo

def mostrar_menu():
    print("===== Sistema de Gestión de Citas =====")
    print("1. Ingresar como Paciente")
    print("2. Ingresar como Médico")
    print("3. Salir")
    print("=======================================")

def main():
    pacientes = []
    medicos = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":  # Ingresar como Paciente
            nombre_paciente = input("Ingrese su nombre como paciente: ")
            paciente = Paciente(nombre_paciente)
            pacientes.append(paciente)

            while True:
                print("\n===== Menú de Paciente =====")
                print("1. Registrar cita")
                print("2. Consultar citas")
                print("3. Eliminar cita")
                print("4. Volver al menú principal")
                print("=============================")

                opcion_paciente = input("Seleccione una opción: ")

                if opcion_paciente == "1":  # Registrar cita
                    print("Médicos disponibles:")
                    for i, medico in enumerate(medicos, start=1):
                        print(f"{i}. {medico.nombre} - {medico.especialidad}")

                    medico_seleccionado = int(input("Seleccione el número del médico: "))
                    medico_seleccionado -= 1  # Ajustar el índice para acceder a la lista de médicos

                    while True:
                        fecha_str = input("Ingrese la fecha de la cita (YYYY-MM-DD): ")
                        try:
                            fecha_cita = datetime.strptime(fecha_str, "%Y-%m-%d").date()
                            if fecha_cita < date.today():
                                print("La fecha ingresada no puede ser anterior a la fecha actual.")
                            else:
                                break
                        except ValueError:
                            print("Formato de fecha inválido. Intente nuevamente.")

                    while True:
                        hora_str = input("Ingrese la hora de la cita (HH:MM): ")
                        try:
                            hora_cita = datetime.strptime(hora_str, "%H:%M").time()
                            break
                        except ValueError:
                            print("Formato de hora inválido. Intente nuevamente.")

                    motivo = input("Ingrese el motivo de la cita: ")

                    if not pacientes[0].validar_cita(fecha_cita, hora_cita):
                        print("Ya tienes una cita registrada en esa fecha y hora.")
                    else:
                        pacientes[0].registrar_cita(medicos[medico_seleccionado], fecha_cita, hora_cita, motivo)

                elif opcion_paciente == "2":  # Consultar citas
                    pacientes[0].consultar_citas()

                elif opcion_paciente == "3":  # Eliminar cita
                    if not pacientes[0].citas:
                        print("No tienes citas registradas.")
                        continue

                    print("Citas registradas:")
                    for i, cita in enumerate(pacientes[0].citas, start=1):
                        print(f"{i}. Fecha: {cita.fecha}, Hora: {cita.hora}, Médico: {cita.medico.nombre}, Motivo: {cita.motivo}")

                    cita_seleccionada = int(input("Seleccione el número de la cita que desea eliminar: "))
                    cita_seleccionada -= 1  # Ajustar el índice para acceder a la lista de citas

                    if 0 <= cita_seleccionada < len(pacientes[0].citas):
                        pacientes[0].eliminar_cita(pacientes[0].citas[cita_seleccionada])
                    else:
                        print("Opción inválida. Intente nuevamente.")

                elif opcion_paciente == "4":  # Volver al menú principal
                    break

                else:
                    print("Opción inválida. Intente nuevamente.")

        elif opcion == "2":  # Ingresar como Médico
            nombre_medico = input("Ingrese su nombre como médico: ")
            especialidad_medico = input("Ingrese su especialidad como médico: ")

            medico = Médico(nombre_medico, especialidad_medico)
            medicos.append(medico)

            while True:
                print("\n===== Menú de Médico =====")
                print("1. Consultar horario disponible")
                print("2. Agregar citas")
                print("3. Volver al menú principal")
                print("===========================")

                opcion_medico = input("Seleccione una opción: ")

                if opcion_medico == "1":  # Consultar horario disponible
                    medico.consultar_horario_disponible()

                elif opcion_medico == "2":  # Agregar citas
                    if not medico.horarios:
                        print("No has definido un horario de atención.")
                    else:
                        while True:
                            fecha_str = input("Ingrese la fecha de la cita (YYYY-MM-DD): ")
                            try:
                                fecha_cita = datetime.strptime(fecha_str, "%Y-%m-%d").date()
                                if fecha_cita < date.today():
                                    print("La fecha ingresada no puede ser anterior a la fecha actual.")
                                else:
                                    break
                            except ValueError:
                                print("Formato de fecha inválido. Intente nuevamente.")

                        while True:
                            hora_str = input("Ingrese la hora de la cita (HH:MM): ")
                            try:
                                hora_cita = datetime.strptime(hora_str, "%H:%M").time()
                                break
                            except ValueError:
                                print("Formato de hora inválido. Intente nuevamente.")

                        motivo = input("Ingrese el motivo de la cita: ")

                        pacientes_disponibles = [p for p in pacientes if p.validar_cita(fecha_cita, hora_cita)]
                        if not pacientes_disponibles:
                            print("No hay pacientes disponibles para esa fecha y hora.")
                        else:
                            print("Pacientes disponibles:")
                            for i, p in enumerate(pacientes_disponibles, start=1):
                                print(f"{i}. {p.nombre}")

                            paciente_seleccionado = int(input("Seleccione el número del paciente: "))
                            paciente_seleccionado -= 1  # Ajustar el índice para acceder a la lista de pacientes

                            pacientes_disponibles[paciente_seleccionado].registrar_cita(medico, fecha_cita, hora_cita, motivo)

                elif opcion_medico == "3":  # Volver al menú principal
                    break

                else:
                    print("Opción inválida. Intente nuevamente.")

        elif opcion == "3":  # Salir
            print("Gracias por usar el Sistema de Gestión de Citas. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()

