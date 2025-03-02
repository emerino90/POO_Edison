import json

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, id_producto, nombre, cantidad, precio):
        if id_producto in self.productos:
            print("Error: El ID ya existe en el inventario.")
        else:
            self.productos[id_producto] = Producto(id_producto, nombre, cantidad, precio)
            print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            print("Producto actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_en_archivo(self, archivo="inventario.json"):
        with open(archivo, "w") as f:
            json.dump({id: vars(p) for id, p in self.productos.items()}, f)
        print("Inventario guardado en archivo.")

    def cargar_desde_archivo(self, archivo="inventario.json"):
        try:
            with open(archivo, "r") as f:
                datos = json.load(f)
                self.productos = {id: Producto(**p) for id, p in datos.items()}
            print("Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("No se encontró un archivo de inventario. Se creará uno nuevo.")


def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo()
    
    while True:
        print("\n=== Menú de Inventario ===")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar productos")
        print("6. Guardar y salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.añadir_producto(id_producto, nombre, cantidad, precio)
        
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        
        elif opcion == "5":
            inventario.mostrar_productos()
        
        elif opcion == "6":
            inventario.guardar_en_archivo()
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()

