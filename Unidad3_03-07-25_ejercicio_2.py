# Unidad 3: Colecciones y librerías en Python.
# Ejercicio 2: Catalogo de Libros
# Descrípcion: Gestiona un catalogo de libros cada libro es representado por un diccionario, y las operaciones se realizan sobre una lista de libros.
# Instrucciones: 
#   1. Inicializa una lista vacia llamada catalogo_libros.
#   2. Crea una funcion mostrar_catalogo(catalogo) que imprima cada libro con su titulo, autor y año.
#   3. Añade los siguientes libros a la lista en el orden indicado:
#       {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "año": 1967}
#       
#       {"titulo": "1984", "autor": "George Orwell", "año": 1949}
#
#   4. Imprime el catalogo despues de cada adicion. 
#   5. Define una funcion agregar_etiqueta(catalogo, titulo_libro, etiqueta) que añada una nueva etiqueta (string) a un libro especifico. La funcion debe utilizar deepcopy() para la lista de diccionarios, y retornar la lista modificada y un booleano indicando si la etiqueta fue agregada.
#   6. Agrega la etiqueta "Clasico" al libro "Cien años de soledad". Muestra si se agrego la etiqueta.
#   7. Imprime el catalogo final.
#  
#   Salida Esperada:
#
#   --- Catálogo de Libros ---
#
#   No hay libros en el catálogo.
#
#   --- Catálogo de Libros ---
#
#   Título: Cien años de soledad, Autor: Gabriel García Márquez, Año: 1967
#
#   --- Catálogo de Libros ---
#
#   Título: Cien años de soledad, Autor: Gabriel García Márquez, Año: 1967
#   Título: 1984, Autor: George Orwell, Año: 1949
#
#   Se agregó la etiqueta "Clásico" a "Cien años de soledad": True
#
#   --- Catálogo de Libros ---
#
#   Título: Cien años de soledad, Autor: Gabriel García Márquez, Año: 1967, Etiquetas: ['Clásico']
#   Título: 1984, Autor: George Orwell, Año: 1949

import copy

# Inicializar la lista vacía para el catálogo de libros
catalogo_libros = []

# Función para mostrar el catálogo de libros
def mostrar_catalogo(catalogo):
    print("--- Catálogo de Libros ---")
    print()
    if not catalogo:
        print("No hay libros en el catálogo.")
    else:
        for libro in catalogo:
            mensaje = f"Título: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['año']}"
            if 'etiquetas' in libro:
                mensaje += f", Etiquetas: {libro['etiquetas']}"
            print(mensaje)
    print()

# Mostrar el catálogo inicial vacío
mostrar_catalogo(catalogo_libros)

# Agregar libros uno por uno y mostrar el catálogo después de cada adición
catalogo_libros.append({
    "titulo": "Cien años de soledad", 
    "autor": "Gabriel García Márquez", 
    "año": 1967
})
mostrar_catalogo(catalogo_libros)

catalogo_libros.append({
    "titulo": "1984", 
    "autor": "George Orwell", 
    "año": 1949
})
mostrar_catalogo(catalogo_libros)

# Función para agregar una etiqueta a un libro específico
def agregar_etiqueta(catalogo, titulo_libro, etiqueta):
    copia_original = copy.deepcopy(catalogo)
    for libro in catalogo:
        if libro['titulo'] == titulo_libro:
            if 'etiquetas' not in libro:
                libro['etiquetas'] = []
            if etiqueta not in libro['etiquetas']:
                libro['etiquetas'].append(etiqueta)
            break
    return catalogo != copia_original

# Agregar la etiqueta "Clásico" al libro "Cien años de soledad" y mostrar el resultado
resultado = agregar_etiqueta(catalogo_libros, "Cien años de soledad", "Clásico")
print(f'Se agregó la etiqueta "Clásico" a "Cien años de soledad": {resultado}')
print()

# Mostrar el catálogo final de libros
mostrar_catalogo(catalogo_libros)