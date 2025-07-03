# Unidad 3: Colecciones y librerías en Python.
# Ejercicio 1: Registro de Estudiantes
# Descripcion: Crea un sistema sencillo para registrar estudidantes y sus calificaciones, permitiendo actualizar la informacion.
# Instrucciones: 
# 1. Crear una lista vacia llamada registro_estudiantes.
# 2. Define una funcion mostrar_registro(registro) que imprima todos los estudiantes y sus datos de forma legible.
# 3. Agrega los siguientes estudiantes (diccionarios) a la lista registro_estudiantes en este orden:
#    
#  {"nombre": "Ana", "edad": 20, "calificaciones": {"Matematicas": 85, "Historia": 90}}
#
#  {"nombre": "Pedro", "edad": 22, "calificaciones": {"Matematicas": 78, "Historia": 88}}
#
#  {"nombre": "Luisa", "edad": 21, "calificaciones": {"Matematicas": 92, "Historia": 75}}
#
# 4. Imprime el registro completo de estudiantes despues de cada adiccion.
# 5. Crea una funcion actualizar_calificacion(registro, nombre_estudiantes, materia, nueva_nota) que actualice la calificacion de un estudiante. La funcion debe utilizar deepcopy() para crear una copia del registro antes de la modificacion y retornar True si el cambio se realizo correctamente (comparando la copia original con la modificada), False en caso contriario.
# 6. Actualiza la calificacion de "Ana" en "Matematicas" a 95 usando la funcion actualizar_calificacion. Muestra si el cambio fue exitoso.
# 7. Imprime el registro final de estudiantes.
#   
#   Salida Esperada:
#
#   --- Registro de Estudiantes ---
#
#   No hay estudiantes registrados.
#
#   --- Registro de Estudiantes ---
#
#   Nombre: Ana, Edad: 20, Calificaciones: {'Matematicas': 85, 'Historia': 90}
#
#   --- Registro de Estudiantes ---
#
#   Nombre: Ana, Edad: 20, Calificaciones: {'Matematicas': 85, 'Historia': 90}
#   Nombre: Pedro, Edad: 22, Calificaciones: {'Matematicas': 78, 'Historia': 88}
#
#   --- Registro de Estudiantes ---
#
#   Nombre: Ana, Edad: 20, Calificaciones: {'Matematicas': 85, 'Historia': 90}
#   Nombre: Pedro, Edad: 22, Calificaciones: {'Matematicas': 78, 'Historia': 88}
#   Nombre: Luisa, Edad: 21, Calificaciones: {'Matematicas': 92, 'Historia': 75}
#
#   Se actualizó la calificación de Ana en Matematicas?: True
#
#   --- Registro de Estudiantes ---
#
#   Nombre: Ana, Edad: 20, Calificaciones: {'Matematicas': 95, 'Historia': 90}
#   Nombre: Pedro, Edad: 22, Calificaciones: {'Matematicas': 78, 'Historia': 88}
#   Nombre: Luisa, Edad: 21, Calificaciones: {'Matematicas': 92, 'Historia': 75}

import copy

# Crear la lista vacía para el registro de estudiantes
registro_estudiantes = []

# Función para mostrar el registro de estudiantes
def mostrar_registro(registro):
    print("--- Registro de Estudiantes ---")
    if not registro:
        print()
        print("No hay estudiantes registrados.")
    else:
        for estudiante in registro:
            print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Calificaciones: {estudiante['calificaciones']}")
    print()

# Mostrar el registro inicial vacío
mostrar_registro(registro_estudiantes)

# Agregar estudiantes uno por uno y mostrar el registro después de cada adición
registro_estudiantes.append({
    "nombre": "Ana", 
    "edad": 20, 
    "calificaciones": {"Matematicas": 85, "Historia": 90}
})
mostrar_registro(registro_estudiantes)

registro_estudiantes.append({
    "nombre": "Pedro", 
    "edad": 22, 
    "calificaciones": {"Matematicas": 78, "Historia": 88}
})
mostrar_registro(registro_estudiantes)

registro_estudiantes.append({
    "nombre": "Luisa", 
    "edad": 21, 
    "calificaciones": {"Matematicas": 92, "Historia": 75}
})
mostrar_registro(registro_estudiantes)

# Función para actualizar la calificación de un estudiante
def actualizar_calificacion(registro, nombre_estudiante, materia, nueva_nota):
    copia_original = copy.deepcopy(registro)
    for estudiante in registro:
        if estudiante['nombre'] == nombre_estudiante:
            if materia in estudiante['calificaciones']:
                estudiante['calificaciones'][materia] = nueva_nota
            break
    return registro != copia_original

# Actualizar la calificación de Ana en Matemáticas y mostrar si fue exitoso
resultado = actualizar_calificacion(registro_estudiantes, "Ana", "Matematicas", 95)
print(f"Se actualizó la calificación de Ana en Matematicas?: {resultado}\n")

# Mostrar el registro final de estudiantes
mostrar_registro(registro_estudiantes)