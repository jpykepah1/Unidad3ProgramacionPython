# Unidad 3: Colecciones y librerías en Python
# Ejercicio 3: Registro de estudiantes con validación
# Descripción: Sistema para registrar estudiantes y calificaciones con manejo de errores
# Instrucciones:
# 1. Crear diccionario vacío para registro
# 2. Solicitar nombre y calificación (entero)
# 3. Manejar excepciones:
#    a. Validar que calificación sea entero
#    b. Actualizar calificación si estudiante existe
# 4. Mostrar registro después de cada operación
# 5. Probar con diferentes casos

def mostrar_registro(registro):
    """Muestra el registro completo de estudiantes"""
    if not registro:
        print("Registro vacío.")
    else:
        print("\n--- Registro de Estudiantes ---")
        for nombre, calif in registro.items():
            print(f"{nombre}: {calif}")
    print()  # Línea en blanco

def agregar_o_actualizar_estudiante(registro):
    """Agrega o actualiza estudiante con validación de datos"""
    nombre = input("Nombre del estudiante: ").strip()
    
    try:
        # Validar que la calificación sea entero
        calificacion = int(input("Calificación (entero): "))
    except ValueError:
        print("Error: ¡La calificación debe ser un número entero!")
    else:
        # Verificar si estudiante existe para actualizar
        if nombre in registro:
            print(f"[Actualizado] {nombre}: {registro[nombre]} → {calificacion}")
        else:
            print(f"[Agregado] {nombre}: {calificacion}")
        registro[nombre] = calificacion
    
    # Mostrar registro actualizado después de cada operación
    mostrar_registro(registro)

def menu_principal():
    """Menú interactivo para gestionar el registro"""
    registro = {}  # Diccionario para almacenar estudiantes
    
    while True:
        print("\n1. Agregar/Actualizar estudiante")
        print("2. Mostrar registro completo")
        print("3. Salir")
        opcion = input("Seleccione opción: ").strip()
        
        if opcion == "1":
            agregar_o_actualizar_estudiante(registro)
        elif opcion == "2":
            mostrar_registro(registro)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar programa principal
if __name__ == "__main__":
    menu_principal()