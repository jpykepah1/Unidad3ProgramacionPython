# autenticacion.py
import getpass

def verificar_credenciales():
    """Verifica las credenciales del usuario con protección contra fuerza bruta"""
    intentos = 3
    while intentos > 0:
        usuario = input("Usuario: ").strip()
        contrasena = getpass.getpass("Contraseña: ").strip()
        
        if usuario == "profe" and contrasena == "iammadman":
            return True
        
        intentos -= 1
        print(f"Credenciales incorrectas. Intentos restantes: {intentos}")
        if intentos == 0:
            print("Sistema bloqueado. Contacte al administrador.")
            return False
    
    return False
