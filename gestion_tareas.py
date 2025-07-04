# gestion_tareas.py
import copy

def mostrar_lista_tareas(tareas):
    """Muestra la lista de tareas con formato legible"""
    if not tareas:
        print("--- Lista de Tareas ---\nNo hay elementos en la lista.")
        return
    
    print("\n--- Lista de Tareas ---")
    print("Estado    -   Tarea")
    for tarea in tareas:
        print(f"[{tarea['estado']}] - {tarea['nombre']}")

def cambiar_estado_tarea(tareas, nombre_tarea, nuevo_estado):
    """Cambia el estado de una tarea usando copia profunda"""
    copia_tareas = copy.deepcopy(tareas)
    for tarea in copia_tareas:
        if tarea['nombre'] == nombre_tarea:
            tarea['estado'] = nuevo_estado
            return copia_tareas, True
    return copia_tareas, False

def ejecutar_gestion_tareas():
    """Función principal para la gestión de tareas"""
    print("\n" + "="*50)
    print("GESTIÓN DE TAREAS PENDIENTES".center(50))
    print("="*50)
    
    # Inicializar lista de tareas
    lista_tareas = []
    mostrar_lista_tareas(lista_tareas)
    
    # Agregar tareas iniciales
    tareas_iniciales = [
        "Hacer la cama", 
        "Estudiar Python", 
        "Ir de compras"
    ]
    
    for tarea in tareas_iniciales:
        lista_tareas.append({
            'nombre': tarea, 
            'estado': 'pendiente'
        })
        mostrar_lista_tareas(lista_tareas)
        print("-"*40)
    
    # Cambiar estado de una tarea
    lista_modificada, exito = cambiar_estado_tarea(
        lista_tareas, 
        "Estudiar Python", 
        "completada"
    )
    
    print(f"Se logró completar la tarea?: {exito}")
    print("-"*40)
    mostrar_lista_tareas(lista_modificada)
    
    # Agregar nueva tarea
    lista_modificada.append({
        'nombre': 'Preparar cena', 
        'estado': 'pendiente'
    })
    print("\n" + "-"*40)
    mostrar_lista_tareas(lista_modificada)
    
    print("\nGestión de tareas completada.")
