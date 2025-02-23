import json
import os

class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde un archivo JSON o crea uno nuevo si no existe."""
        if not os.path.isfile(self.archivo):
            return {}
        try:
            with open(self.archivo, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            print("Error al leer el archivo de inventario. Se inicializará un inventario vacío.")
            return {}
        except PermissionError:
            print("Error: No tienes permisos para acceder al archivo.")
            return {}

    def guardar_inventario(self):
        """Guarda los productos en el archivo JSON."""
        try:
            with open(self.archivo, "w", encoding="utf-8") as file:
                json.dump(self.productos, file, indent=4)
        except PermissionError:
            print("Error: No se pudo guardar el inventario debido a permisos insuficientes.")

    def agregar_producto(self, nombre, cantidad, precio):
        """Añade un nuevo producto al inventario."""
        if nombre in self.productos:
            print("El producto ya existe. Usa la opción de actualizar.")
            return
        self.productos[nombre] = {"cantidad": cantidad, "precio": precio}
        self.guardar_inventario()
        print(f"Producto '{nombre}' agregado exitosamente.")

    def actualizar_producto(self, nombre, cantidad=None, precio=None):
        """Modifica la cantidad o precio de un producto."""
        if nombre not in self.productos:
            print("El producto no existe en el inventario.")
            return
        if cantidad is not None:
            self.productos[nombre]["cantidad"] = cantidad
        if precio is not None:
            self.productos[nombre]["precio"] = precio
        self.guardar_inventario()
        print(f"Producto '{nombre}' actualizado correctamente.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_inventario()
            print(f"Producto '{nombre}' eliminado.")
        else:
            print("El producto no existe en el inventario.")

    def mostrar_inventario(self):
        """Muestra el contenido del inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario Actual:")
            for nombre, datos in self.productos.items():
                print(f"{nombre}: Cantidad: {datos['cantidad']}, Precio: {datos['precio']}")

if __name__ == "__main__":
    inventario = Inventario()
    while True:
        print("\nMenú de Inventario:")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(nombre, cantidad, precio)
        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            cantidad = input("Nueva cantidad (presiona Enter para no modificar): ")
            precio = input("Nuevo precio (presiona Enter para no modificar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(nombre, cantidad, precio)
        elif opcion == "3":
            nombre = input("Nombre del producto: ")
            inventario.eliminar_producto(nombre)
        elif opcion == "4":
            inventario.mostrar_inventario()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
