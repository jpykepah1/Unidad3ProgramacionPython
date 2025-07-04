# productos_inmutables.py

def mostrar_info_producto(producto):
    """Muestra la información de un producto"""
    print(f"\n--- Producto ---")
    print(f"Nombre: {producto[0]}")
    print(f"Precio: ${producto[2]}")

def ejecutar_demo_productos():
    """Demuestra el uso de tuplas inmutables"""
    print("\n" + "="*50)
    print("INFORMACIÓN DE PRODUCTO INMUTABLE".center(50))
    print("="*50)
    
    # Crear productos como tuplas inmutables
    laptop = ("Laptop", "Electrónica", 1200000, "ABC123XYZ")
    mouse = ("Mouse", "Electrónica", 12000, "XYHA12812312")
    
    # Mostrar información del primer producto
    mostrar_info_producto(laptop)
    
    # Intentar modificación (debe fallar)
    try:
        # Esto generará un error porque las tuplas son inmutables
        laptop = (laptop[0], laptop[1], 1150000, laptop[3])
        print("¡Modificación exitosa! (esto no debería aparecer)")
    except TypeError as error:
        print(f"\nError al intentar modificar el precio: {error}")
    
    print("\nDemostración de inmutabilidad completada.")
