productos = []

def cargar_datos():
    """Cargar productos desde un archivo."""
    try:
        with open("productos.txt", "r") as file:
            for line in file:
                nombre, precio, cantidad = line.strip().split(",")
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })
    except FileNotFoundError:
        print("No se encontró el archivo de productos. Se iniciará con una lista vacía.")
    except Exception as e:
        print(f"Ocurrió un error al cargar los datos: {e}")

def guardar_datos():
    """Guardar productos en un archivo."""
    with open("productos.txt", "w") as file:
        for producto in productos:
            file.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados correctamente.")

def añadir_producto():
    """Añadir un nuevo producto a la lista."""
    nombre = input("Ingrese el nombre del producto: ")
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad disponible: "))
            break
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos para precio y cantidad.")
    
    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print(f"Producto '{nombre}' añadido correctamente.")

def ver_productos():
    """Mostrar la lista de productos."""
    if not productos:
        print("No hay productos en la lista.")
        return
    print("Lista de productos:")
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def actualizar_producto():
    """Actualizar los detalles de un producto existente."""
    nombre_actual = input("Ingrese el nombre del producto a actualizar: ")
    for producto in productos:
        if producto['nombre'] == nombre_actual:
            nuevo_nombre = input("Ingrese el nuevo nombre del producto (deje vacío para no cambiar): ")
            nuevo_precio = input("Ingrese el nuevo precio (deje vacío para no cambiar): ")
            nueva_cantidad = input("Ingrese la nueva cantidad (deje vacío para no cambiar): ")

            # Actualiza el nombre si se proporciona uno nuevo
            if nuevo_nombre:
                producto['nombre'] = nuevo_nombre
            
            # Actualiza el precio si se proporciona uno nuevo
            if nuevo_precio:
                try:
                    producto['precio'] = float(nuevo_precio)
                except ValueError:
                    print("Valor de precio inválido. No se realizó ningún cambio.")

            # Actualiza la cantidad si se proporciona una nueva
            if nueva_cantidad:
                try:
                    producto['cantidad'] = int(nueva_cantidad)
                except ValueError:
                    print("Valor de cantidad inválido. No se realizó ningún cambio.")

            print(f"Producto '{nombre_actual}' actualizado correctamente.")
            return
    print(f"No se encontró el producto '{nombre_actual}'.")

def eliminar_producto():
    """Eliminar un producto de la lista."""
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado correctamente.")
            return
    print(f"No se encontró el producto '{nombre}'.")

def menu():
    """Mostrar el menú y manejar la selección del usuario."""
    while True:
        print("\nSistema de Gestión de Productos")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    cargar_datos()
    try:
        menu()
    finally:
        guardar_datos()  # Asegura que los datos se guardan al salir

