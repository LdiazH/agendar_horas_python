
citas = {
    "Lunes": [],
    "Martes": [],
    "Miercoles": [],
    "Jueves": [],
    "Viernes": [],
}

horarios_disponibles = {
    "Lunes": ["09:00", "10:00", "11:00", "12:00", "15:00", "16:00", "17:00", "18:00"],
    "Martes": ["09:00", "10:00", "11:00", "12:00", "15:00", "16:00", "17:00", "18:00"],
    "Miercoles": ["09:00", "10:00", "11:00", "12:00", "15:00", "16:00", "17:00", "18:00"],
    "Jueves": ["09:00", "10:00", "11:00", "12:00", "15:00", "16:00", "17:00", "18:00"],
    "Viernes": ["09:00", "10:00", "11:00", "12:00", "15:00", "16:00", "17:00", "18:00"],
}

#funcion mostrar horarios disponibles
def mostrar_horarios_disponibles():
    """Muestra los horarios disponibles por día"""
    print("\n--- Horarios Disponibles ---")
    for dia, horas in horarios_disponibles.items():
        if horas:  # Solo mostrar días con horas disponibles
            print(f"{dia}: {', '.join(horas)}")

#Funcion agregar cita
def agendar_cita():
    """Permite al usuario ver una cita y agendarla"""
    mostrar_horarios_disponibles()
    
    # Selección del día
    while True:
        dia = input("\nElija un día (Lunes-Viernes): ").capitalize()
        if dia in horarios_disponibles and horarios_disponibles[dia]:
            break
        print("Día no válido o sin horarios disponibles. Intente nuevamente.")
    
    # Selección de la hora
    while True:
        print(f"\nHoras disponibles para {dia}: {', '.join(horarios_disponibles[dia])}")
        hora = input("Elija una hora (formato HH:MM): ")
        if hora in horarios_disponibles[dia]:
            break
        print("Hora no válida o no disponible. Intente nuevamente.")
    
    # Registro de información de la cita
    mascota = input("Nombre de la mascota: ")
    dueño = input("Nombre del dueño: ")
    motivo = input("Motivo de la consulta: ")
    
    # Crear registro de la cita en arreglo citas
    nueva_cita = {
        'hora': hora,
        'mascota': mascota,
        'dueño': dueño,
        'motivo': motivo
    }
    
    # Agregar a las citas y quitar de disponibilidad 
    citas[dia].append(nueva_cita)
    horarios_disponibles[dia].remove(hora)
    
    print(f"\n Cita agendada para {mascota} el {dia} a las {hora}")

#funcion para mostrar citas agendadas
def mostrar_citas_agendadas():
    """Muestra todas las citas agendadas"""
    print("\n--- Citas Agendadas ---")
    for dia, citas_dia in citas.items():
        if citas_dia:
            print(f"\n{dia}:")
            for cita in citas_dia:
                print(f"  {cita['hora']} - {cita['mascota']} ({cita['dueño']}): {cita['motivo']}")

#funcione menu principal
def menu_principal():
    """Muestra el menú principal del sistema"""
    while True:
        print("\n--- Sistema VetCare ---")
        print("1. Ver horarios disponibles")
        print("2. Agendar nueva cita")
        print("3. Ver citas agendadas")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_horarios_disponibles()
        elif opcion == "2":
            agendar_cita()
        elif opcion == "3":
            mostrar_citas_agendadas()
        elif opcion == "4":
            print("Gracias por usar VetCare. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()

