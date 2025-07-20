# 🐾 VetCare — Sistema de Gestión de Citas

Aplicación de consola en Python para la gestión de citas veterinarias. Permite ver horarios disponibles, agendar nuevas citas y consultar el listado de atenciones programadas.

## ✅ Funcionalidades

- Ver horarios disponibles por día
- Agendar nuevas citas ingresando datos de mascota, dueño y motivo
- Consultar citas agendadas por día
- Menú interactivo para navegación sencilla

## 📅 Estructura del Menú


--- Sistema VetCare ---
- Ver horarios disponibles
- Agendar nueva cita
- Ver citas agendadas
- Salir

## 🧰 Tecnologías utilizadas

- Python 3.x
- Entrada/salida en consola (`input()`, `print()`)
- Estructuras de datos: diccionarios y listas
- Control de flujo con condicionales y bucles

## 🛠️ Lógica de funcionamiento

- Los días disponibles son de lunes a viernes.
- Cada día contiene un conjunto de horarios (09:00 a 18:00).
- Una vez que un horario es ocupado, se elimina de la disponibilidad.
- Cada cita contiene:
  - 🕒 `hora`
  - 🐶 `mascota`
  - 👤 `dueño`
  - 📋 `motivo`

## 📦 Ejecución

1. Descarga el script como `vetcare.py`.
2. Ejecuta en consola:

```bash
python vetcare.py


- Utiliza el menú para interactuar con el sistema.
💡 Ejemplo de uso
Elija un día (Lunes-Viernes): Martes
Elija una hora (formato HH:MM): 10:00
Nombre de la mascota: Toby
Nombre del dueño: María
Motivo de la consulta: Vacunación

Cita agendada para Toby el Martes a las 10:00


👨‍💻 Autor
Luis Enrique Díaz Huenulef
Especialista en atención al cliente, programación estructurada y metodologías educativas aplicadas al desarrollo técnico.
