# Lista para almacenar productos
productos = []

# Clase para representar un Producto
class Producto:
    def __init__(self, id, nombre, cantidad_stock, precio, cantidad_minima):
        self.id = id
        self.nombre = nombre
        self.cantidad_stock = cantidad_stock
        self.precio = precio
        self.cantidad_minima = cantidad_minima

# Funciones de CRUD para productos
def registrar_producto(nombre, cantidad_stock, precio, cantidad_minima):
    id = len(productos) + 1  # Genera un nuevo ID
    nuevo_producto = Producto(id, nombre, cantidad_stock, precio, cantidad_minima)
    productos.append(nuevo_producto)

def vender_producto(producto_id, cantidad):
    for producto in productos:
        if producto.id == producto_id:
            if producto.cantidad_stock >= cantidad:
                producto.cantidad_stock -= cantidad
                print("Venta realizada con éxito.")
            else:
                print("No hay suficiente stock.")
            return
    print("Producto no encontrado.")

def consultar_productos():
    for producto in productos:
        print(f"ID: {producto.id}, Nombre: {producto.nombre}, Stock: {producto.cantidad_stock}, Precio: {producto.precio}, Cantidad mínima: {producto.cantidad_minima}")

def actualizar_stock(producto_id, nueva_cantidad):
    for producto in productos:
        if producto.id == producto_id:
            producto.cantidad_stock = nueva_cantidad
            return
    print("Producto no encontrado.")

def eliminar_producto(producto_id):
    global productos
    productos = [producto for producto in productos if producto.id != producto_id]

def reporte_bajo_stock():
    bajo_stock = [producto for producto in productos if producto.cantidad_stock < producto.cantidad_minima]
    if bajo_stock:
        print("Productos con bajo stock:")
        for producto in bajo_stock:
            print(f"ID: {producto.id}, Nombre: {producto.nombre}, Stock: {producto.cantidad_stock}")
    else:
        print("No hay productos con bajo stock.")

def buscar_producto_por_nombre(nombre_busqueda):
    resultados = [producto for producto in productos if nombre_busqueda.lower() in producto.nombre.lower()]
    if resultados:
        print(f"Resultados para '{nombre_busqueda}':")
        for producto in resultados:
            print(f"ID: {producto.id}, Nombre: {producto.nombre}, Stock: {producto.cantidad_stock}")
    else:
        print(f"No se encontraron productos con el nombre '{nombre_busqueda}'.")

# Menú para el vendedor
def menu_vendedor():
    while True:
        print("\n--- Menú Vendedor ---")
        print("1. Registrar Venta")
        print("2. Consultar Productos")
        print("3. Buscar Producto por Nombre")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            producto_id = int(input("Ingrese el ID del producto a vender: "))
            cantidad = int(input("Ingrese la cantidad a vender: "))
            vender_producto(producto_id, cantidad)
        elif opcion == '2':
            consultar_productos()
        elif opcion == '3':
            nombre_busqueda = input("Ingrese el nombre del producto a buscar: ")
            buscar_producto_por_nombre(nombre_busqueda)
        elif opcion == '4':
            break
        else:
            print("Opción no válida.")

# Menú para el supervisor
def menu_supervisor():
    while True:
        print("\n--- Menú Supervisor ---")
        print("1. Registrar Producto")
        print("2. Registrar Venta")
        print("3. Consultar Productos")
        print("4. Actualizar Stock")
        print("5. Eliminar Producto")
        print("6. Reporte de Bajo Stock")
        print("7. Buscar Producto por Nombre")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre del producto: ")
            cantidad_stock = int(input("Cantidad en stock: "))
            precio = float(input("Precio del producto: "))
            cantidad_minima = int(input("Cantidad mínima: "))
            registrar_producto(nombre, cantidad_stock, precio, cantidad_minima)
        elif opcion == '2':
            producto_id = int(input("Ingrese el ID del producto a vender: "))
            cantidad = int(input("Ingrese la cantidad a vender: "))
            vender_producto(producto_id, cantidad)
        elif opcion == '3':
            consultar_productos()
        elif opcion == '4':
            producto_id = int(input("Ingrese el ID del producto a actualizar: "))
            nueva_cantidad = int(input("Ingrese la nueva cantidad en stock: "))
            actualizar_stock(producto_id, nueva_cantidad)
        elif opcion == '5':
            producto_id = int(input("Ingrese el ID del producto a eliminar: "))
            eliminar_producto(producto_id)
        elif opcion == '6':
            reporte_bajo_stock()
        elif opcion == '7':
            nombre_busqueda = input("Ingrese el nombre del producto a buscar: ")
            buscar_producto_por_nombre(nombre_busqueda)
        elif opcion == '8':
            break
        else:
            print("Opción no válida.")

# Sistema de inicio de sesión para diferenciar entre vendedor y supervisor
def inicio_sesion():
    while True:
        print("\n--- Inicio de Sesión ---")
        print("1. Iniciar como Vendedor")
        print("2. Iniciar como Supervisor")
        print("3. Salir")
        opcion = input("Seleccione su rol: ")

        if opcion == '1':
            menu_vendedor()
        elif opcion == '2':
            menu_supervisor()
        elif opcion == '3':
            break
        else:
            print("Opción no válida.")

# Ejecución principal del sistema
if __name__ == "__main__":
    inicio_sesion()
