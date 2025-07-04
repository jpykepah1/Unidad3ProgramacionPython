# main.py (Punto de entrada principal)
from autenticacion import verificar_credenciales
from menu_principal import mostrar_menu
import gestion_tareas
import productos_inmutables
import registro_estudiantes

def main():
    # Sistema de autenticación
    print("\n=== SISTEMA DE EVALUACIÓN SEGURA ===")
    print("Por favor ingrese sus credenciales\n")
    
    if not verificar_credenciales():
        return
    
    # Menú principal
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            gestion_tareas.ejecutar_gestion_tareas()
        elif opcion == '2':
            productos_inmutables.ejecutar_demo_productos()
        elif opcion == '3':
            registro_estudiantes.ejecutar_registro_estudiantes()
        elif opcion == '4':
            print("\nSesión finalizada. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Por favor seleccione 1-4.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
