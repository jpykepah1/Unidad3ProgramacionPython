# registro_estudiantes.py

def validar_nota(nota_str):
    """Valida que la nota sea un número decimal entre 1.0 y 7.0"""
    try:
        nota = float(nota_str)
        if 1.0 <= nota <= 7.0:
            return True, nota
        return False, "La nota debe estar entre 1.0 y 7.0"
    except ValueError:
        return False, "Debe ingresar un valor numérico válido"

def mostrar_registro(registro):
    """Muestra el registro completo de estudiantes"""
    if not registro:
        print("\nNo hay estudiantes registrados.")
        return
    
    print("\n--- REGISTRO DE ESTUDIANTES ---")
    for nombre, nota in registro.items():
        print(f"{nombre}: {nota}")

def ejecutar_registro_estudiantes():
    """Sistema principal de registro de estudiantes"""
    registro = {}
    
    print("\n" + "="*50)
    print("REGISTRO DE ESTUDIANTES CON VALIDACIÓN".center(50))
    print("="*50)
    
    while True:
        print("\nOpciones:")
        print("1. Agregar nuevo estudiante")
        print("2. Actualizar calificación")
        print("3. Mostrar registro completo")
        print("4. Volver al menú principal")
        
        opcion = input("\nSeleccione una operación: ")
        
        if opcion == '1' or opcion == '2':
            nombre = input("\nNombre del estudiante: ").strip().title()
            calificacion = input("Calificación (1.0-7.0): ").strip()
            
            valido, resultado = validar_nota(calificacion)
            
            if not valido:
                print(f"\nError: {resultado}")
                continue
            
            if opcion == '1':
                if nombre in registro:
                    print(f"\nEl estudiante {nombre} ya está registrado. Se actualizará su calificación.")
                registro[nombre] = resultado
                print(f"\nRegistro actualizado: {nombre} = {resultado}")
            else:
                if nombre not in registro:
                    print(f"\nError: {nombre} no está registrado")
                else:
                    registro[nombre] = resultado
                    print(f"\nCalificación actualizada: {nombre} = {resultado}")
        
        elif opcion == '3':
            mostrar_registro(registro)
        
        elif opcion == '4':
            print("\nRegresando al menú principal...")
            break
        
        else:
            print("Opción inválida. Intente nuevamente.")
