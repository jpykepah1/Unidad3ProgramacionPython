# Unidad 3: Colecciones y librerías en Python
# Ejercicio 1: Gestión de tareas pendientes
# Descripción: Programa para gestionar una lista de tareas pendientes
# Instrucciones:
# 1. Crear lista vacía de tareas
# 2. Añadir tareas especificadas
# 3. Imprimir lista después de cada adición
# 4. Añadir nueva tarea al final
# 5. Imprimir lista final

from copy import deepcopy

# Lista vacía para almacenar tareas
tareas_pendientes = []

# Función para mostrar tareas en formato legible
def mostrar_tareas():
    if not tareas_pendientes:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for i, tarea in enumerate(tareas_pendientes, 1):
            print(f"{i}. {tarea['tarea']} - Estado: {tarea['estado']}")
    print()  # Línea en blanco para separación visual

# Paso 1: Mostrar lista inicial vacía
print("Lista inicial:")
mostrar_tareas()

# Paso 2: Agregar tareas iniciales como diccionarios
tareas_pendientes.append({"tarea": "Hacer la cama", "estado": "pendiente"})
print("Después de agregar 'Hacer la cama':")
mostrar_tareas()

tareas_pendientes.append({"tarea": "Estudiar Python", "estado": "pendiente"})
print("Después de agregar 'Estudiar Python':")
mostrar_tareas()

tareas_pendientes.append({"tarea": "Ir de compras", "estado": "pendiente"})
print("Después de agregar 'Ir de compras':")
mostrar_tareas()

# Paso 4: Agregar nueva tarea al final
tareas_pendientes.append({"tarea": "Preparar cena", "estado": "pendiente"})
print("Después de agregar 'Preparar cena':")
mostrar_tareas()

# Paso 5: Mostrar lista final completa
print("Lista final de tareas:")
mostrar_tareas()