class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.detalles = (titulo, autor)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn
    
    def __str__(self):
        return f"{self.detalles[0]} por {self.detalles[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados
    
    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"

class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = {}  # Diccionario con ID de usuario como clave y objeto Usuario como valor
    
    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print("El libro ya está en la biblioteca.")
    
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("El libro no se encuentra en la biblioteca.")
    
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print("El usuario ya está registrado.")
    
    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print("El usuario no está registrado.")
    
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            usuario.libros_prestados.append(libro)
            del self.libros[isbn]  # Remover el libro de la biblioteca
            print(f"Libro prestado: {libro} a {usuario.nombre}")
        else:
            print("Usuario o libro no encontrado.")
    
    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro  # Reintegrar el libro a la biblioteca
                    print(f"Libro devuelto: {libro}")
                    return
            print("El usuario no tiene prestado este libro.")
        else:
            print("Usuario no encontrado.")
    
    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        resultados = [libro for libro in self.libros.values()
                      if (titulo is None or libro.detalles[0] == titulo)
                      and (autor is None or libro.detalles[1] == autor)
                      and (categoria is None or libro.categoria == categoria)]
        return resultados
    
    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            return [str(libro) for libro in usuario.libros_prestados]  # Convertir objetos a string
        return []

# Pruebas del sistema
biblio = Biblioteca()
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "1234567890")
libro2 = Libro("1984", "George Orwell", "Distopía", "0987654321")
usuario1 = Usuario("Pedro", "001")

biblio.registrar_usuario(usuario1)
biblio.agregar_libro(libro1)
biblio.agregar_libro(libro2)
biblio.prestar_libro("001", "1234567890")
print("Libros prestados:", biblio.listar_libros_prestados("001"))
biblio.devolver_libro("001", "1234567890")

