# menu_principal.py
def mostrar_menu():
    """Muestra el menú principal de la aplicación"""
    print("\n" + "="*50)
    print("SISTEMA DE EVALUACIÓN - PROGRAMACIÓN SEGURA".center(50))
    print("="*50)
    print("1. Gestión de Tareas Pendientes")
    print("2. Información de Producto Inmutable")
    print("3. Registro de Estudiantes con Validación")
    print("4. Salir")
    print("="*50)
    
    return input("\nSeleccione una opción (1-4): ")
