# ecommerce_m3.py
# Sistema de E-commerce básico por consola cumpliendo requisitos del M3

def mostrar_menu():
    """Muestra las opciones disponibles en el sistema."""
    print("\n==============================")
    print("  Bienvenido/a a tu Ecommerce")
    print("==============================")
    print("1) Ver catálogo completo de productos")
    print("2) Buscar productos por Grupo / Categoría")
    print("3) Agregar producto al carrito por ID")
    print("4) Ver carrito y total")
    print("5) Vaciar carrito")
    print("0) Salir")

def listar_productos(catalogo):
    """Recorre y muestra de forma ordenada cualquier lista de productos."""
    print("\n--- Listado de productos ---")
    for producto in catalogo:
        print(f"ID: {producto['id']} | Nombre: {producto['nombre']:<15} | Categoría: {producto['categoria']:<12} | Precio: ${producto['precio']}")

def buscar_productos(catalogo):
    """Muestra las categorías, filtra y RETORNA los productos que coinciden."""
    # Estructura compuesta para agrupar categorías únicas
    categorias = list(set(p['categoria'] for p in catalogo))
    
    print("\n--- Grupos de Productos Disponibles ---")
    for i, cat in enumerate(categorias, 1):
        print(f"{i}) {cat.capitalize()}")
    print("0) Volver al menú principal")
    
    try:
        seleccion = int(input("Seleccione el número del grupo que desea ver: "))
        if seleccion == 0:
            return [] # Retorna lista vacía si decide volver
        
        if 1 <= seleccion <= len(categorias):
            categoria_elegida = categorias[seleccion - 1]
            # Filtrado usando ciclos/comprensión
            resultados = [p for p in catalogo if p['categoria'] == categoria_elegida]
            return resultados # FUNCIÓN QUE RETORNA UN VALOR (Lista filtrada)
        else:
            print("Opción inválida.")
            return []
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return []

def agregar_al_carrito(catalogo, carrito):
    """Añade productos al carrito validando que la cantidad sea mayor a 0."""
    try:
        id_producto = int(input("Ingrese el ID del producto que desea agregar: "))
        # Busca si el ID existe en el catálogo
        producto_encontrado = next((p for p in catalogo if p['id'] == id_producto), None)
        
        if producto_encontrado:
            # Validación de cantidad > 0 (Requisito Técnico)
            cantidad = int(input(f"¿Cuántas unidades de '{producto_encontrado['nombre']}' desea agregar?: "))
            
            if cantidad > 0:
                # Agregamos el producto la cantidad de veces solicitada
                for _ in range(cantidad):
                    carrito.append(producto_encontrado)
                print(f"¡Éxito! Se han agregado {cantidad} unidad(es) de '{producto_encontrado['nombre']}' al carrito.")
            else:
                print("Error: La cantidad debe ser mayor a 0.")
        else:
            print("ID de producto no encontrado.")
    except ValueError:
        print("Entrada inválida. Debe ingresar números enteros.")

def mostrar_carrito_y_total(carrito):
    """Muestra el contenido del carrito y calcula el total."""
    # Condicional para mostrar mensajes distintos según si está vacío o no (Requisito)
    if not carrito:
        print("\nEl carrito está actualmente vacío. ¡Anímate a comprar!")
    else:
        print("\n--- Tu Carrito de Compras ---")
        # Reutiliza la función de listado para recorrer el carrito
        listar_productos(carrito)
        total = sum(p['precio'] for p in carrito)
        print(f"Total a pagar: ${total}")

def vaciar_carrito(carrito):
    """Limpia todos los elementos almacenados en el carrito."""
    carrito.clear()
    print("Carrito vaciado correctamente.")

def main():
    # Estructura compuesta para el catálogo (Lista de diccionarios)
    catalogo = [
        {'id': 1, 'nombre': 'Camiseta', 'categoria': 'ropa', 'precio': 25},
        {'id': 2, 'nombre': 'Zapatillas', 'categoria': 'ropa', 'precio': 60},
        {'id': 3, 'nombre': 'Jeans Ovalados', 'categoria': 'ropa', 'precio': 45},
        {'id': 4, 'nombre': 'Chaqueta Denim', 'categoria': 'ropa', 'precio': 85},
        {'id': 5, 'nombre': 'Polerón Hoodie', 'categoria': 'ropa', 'precio': 40},
        {'id': 6, 'nombre': 'Calcetines Pack', 'categoria': 'ropa', 'precio': 12},
        
        {'id': 7, 'nombre': 'Laptop Core i7', 'categoria': 'tecnología', 'precio': 800},
        {'id': 8, 'nombre': 'Smartphone 5G', 'categoria': 'tecnología', 'precio': 500},
        {'id': 9, 'nombre': 'Audífonos BT', 'categoria': 'tecnología', 'precio': 75},
        {'id': 10, 'nombre': 'Mouse Gamer', 'categoria': 'tecnología', 'precio': 35},
        {'id': 11, 'nombre': 'Teclado Mecánico', 'categoria': 'tecnología', 'precio': 90},
        {'id': 12, 'nombre': 'Monitor 24 IPS', 'categoria': 'tecnología', 'precio': 180},
        
        {'id': 13, 'nombre': 'Sartén Teflón', 'categoria': 'hogar', 'precio': 45},
        {'id': 14, 'nombre': 'Cafetera Goteo', 'categoria': 'hogar', 'precio': 55},
        {'id': 15, 'nombre': 'Lámpara Escritorio', 'categoria': 'hogar', 'precio': 20},
        {'id': 16, 'nombre': 'Juego de Sábanas', 'categoria': 'hogar', 'precio': 30},
        {'id': 17, 'nombre': 'Licuadora Pro', 'categoria': 'hogar', 'precio': 65},
        {'id': 18, 'nombre': 'Organizador Mueble', 'categoria': 'hogar', 'precio': 25}
    ]
    
    # Estructura compuesta para el carrito (Lista vacía inicialmente)
    carrito = []
    opcion = -1
    
    # Ciclo while para el menú principal (Requisito Técnico)
    while opcion != 0:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            
            # Condicionales para validar las opciones del menú
            if opcion == 1:
                listar_productos(catalogo)
            elif opcion == 2:
                # Al buscar, guardamos la lista que RETORNA la función
                productos_filtrados = buscar_productos(catalogo)
                if productos_filtrados:
                    print(f"\nResultados encontrados:")
                    listar_productos(productos_filtrados)
                    
                    # Interacción rápida manteniendo los IDs a la vista
                    print("\n--------------------------------------------------")
                    opcion_rapida = input("¿Deseas agregar un producto de esta lista al carrito? (s/n): ").lower()
                    if opcion_rapida == 's':
                        agregar_al_carrito(productos_filtrados, carrito)
            elif opcion == 3:
                agregar_al_carrito(catalogo, carrito)
            elif opcion == 4:
                mostrar_carrito_y_total(carrito)
            elif opcion == 5:
                vaciar_carrito(carrito)
            elif opcion == 0:
                print("Gracias por usar nuestro Ecommerce. ¡Hasta luego!")
            else:
                print("Opción fuera de rango. Intente nuevamente.")
        except ValueError:
            print("Error: Por favor, elija una opción numérica válida.")
            opcion = -1

if __name__ == "__main__":
    main()