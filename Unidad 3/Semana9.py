class Producto:
    """
    Modelo de un producto en el inventario.
    """
    def __init__(self, codigo, descripcion, stock, valor):
        self.codigo = codigo
        self.descripcion = descripcion
        self.stock = stock
        self.valor = valor

    def modificar_stock(self, nuevo_stock):
        """Modifica la cantidad en existencia del producto."""
        self.stock = nuevo_stock

    def modificar_valor(self, nuevo_valor):
        """Cambia el precio del producto."""
        self.valor = nuevo_valor

    def __str__(self):
        return f"Código: {self.codigo} | Descripción: {self.descripcion} | Stock: {self.stock} | Valor: ${self.valor:.2f}"


class Inventario:
    """
    Administra la colección de productos.
    """
    def __init__(self):
        self.catalogo = {}

    def incluir_producto(self, producto):
        """Añade un producto si no está repetido."""
        if producto.codigo in self.catalogo:
            print("Error: Código ya existente en el inventario.")
        else:
            self.catalogo[producto.codigo] = producto
            print("Producto añadido exitosamente.")

    def retirar_producto(self, codigo):
        """Elimina un producto por su código."""
        if codigo in self.catalogo:
            del self.catalogo[codigo]
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, codigo, stock=None, valor=None):
        """Permite actualizar el stock y/o el valor de un producto existente."""
        if codigo in self.catalogo:
            if stock is not None:
                self.catalogo[codigo].modificar_stock(stock)
            if valor is not None:
                self.catalogo[codigo].modificar_valor(valor)
            print("Producto actualizado con éxito.")
        else:
            print("Error: Producto no registrado.")

    def localizar_producto(self, descripcion):
        """Busca productos que coincidan con la descripción dada."""
        coincidencias = [p for p in self.catalogo.values() if descripcion.lower() in p.descripcion.lower()]
        if coincidencias:
            for p in coincidencias:
                print(p)
        else:
            print("No se encontraron productos con esa descripción.")

    def listar_productos(self):
        """Muestra todos los productos disponibles."""
        if self.catalogo:
            for producto in self.catalogo.values():
                print(producto)
        else:
            print("El inventario está vacío.")


def pedir_entero(mensaje):
    """Solicita un número entero al usuario con validación."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingrese un número entero válido.")


def pedir_flotante(mensaje):
    """Solicita un número decimal al usuario con validación."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Ingrese un número decimal válido.")


def interfaz():
    """Menú interactivo para la gestión del inventario."""
    inventario = Inventario()

    while True:
        print("\n--- Panel de Control del Inventario ---")
        print("1. Agregar un nuevo producto")
        print("2. Eliminar un producto")
        print("3. Modificar un producto")
        print("4. Buscar producto por descripción")
        print("5. Ver todos los productos")
        print("0. Salir")

        seleccion = input("Seleccione una opción: ")

        if seleccion == '1':
            codigo = input("Código del producto: ")
            descripcion = input("Descripción del producto: ")
            stock = pedir_entero("Cantidad disponible: ")
            valor = pedir_flotante("Precio unitario: ")
            inventario.incluir_producto(Producto(codigo, descripcion, stock, valor))

        elif seleccion == '2':
            codigo = input("Código del producto a eliminar: ")
            inventario.retirar_producto(codigo)

        elif seleccion == '3':
            codigo = input("Código del producto a modificar: ")
            stock = input("Nuevo stock (Enter para omitir): ")
            valor = input("Nuevo valor (Enter para omitir): ")
            inventario.actualizar_producto(codigo,
                                           int(stock) if stock else None,
                                           float(valor) if valor else None)

        elif seleccion == '4':
            descripcion = input("Ingrese la descripción del producto: ")
            inventario.localizar_producto(descripcion)

        elif seleccion == '5':
            inventario.listar_productos()

        elif seleccion == '0':
            print("Saliendo del sistema de inventario...")
            break
        else:
            print("Opción inválida, intente nuevamente.")


if __name__ == "__main__":
    interfaz()
