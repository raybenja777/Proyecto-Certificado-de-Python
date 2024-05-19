import pickle
from typing import Dict, List

class Libro:
    def __init__(self, titulo: str, autor: str, cantidad: int = 1, disponible: bool = True):
        # Clase para representar un libro en la biblioteca.

        # Parámetros:
        #   titulo (str): El título del libro.
        #   autor (str): El autor del libro.
        #   cantidad (int, opcional): La cantidad de copias disponibles del libro. Por defecto es 1.
        #   disponible (bool, opcional): Indica si el libro está disponible para ser prestado. Por defecto es True.
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad
        self.disponible = disponible
       

class Usuario:
    def __init__(self, nombre: str):
        # Clase para representar un usuario de la biblioteca.

        # Parámetros:
        #   nombre (str): El nombre del usuario.
        self.nombre = nombre
        self.libros_prestados = [] # Lista para almacenar los libros prestados por el usuario
        
class Biblioteca:
    def __init__(self):
        # Clase para representar la biblioteca y sus operaciones.

        # Atributos:
        #   libros (Dict[str, Libro]): Un diccionario que mapea títulos de libros a objetos Libro.
        #   usuarios (Dict[str, Usuario]): Un diccionario que mapea nombres de usuarios a objetos Usuario.
        self.libros: Dict[str, Libro] = {} # Diccionario para almacenar los libros en la biblioteca
        self.usuarios: Dict[str, Usuario] = {} # Diccionario para almacenar los usuarios en la biblioteca
        
    def agregar_libro(self, titulo: str, autor: str):
        # Agrega un libro a la biblioteca.

        # Parámetros:
        #   titulo (str): El título del libro a agregar.
        #   autor (str): El autor del libro a agregar.
        if titulo in self.libros:
            self.libros[titulo].cantidad += 1
        else:
            self.libros[titulo] = Libro(titulo, autor)
            
    def mostrar_libros(self):
        # Muestra la lista de libros disponibles en la biblioteca.
        print("Libros disponibles:")
        for titulo, libro in self.libros.items():
            print(f"Título: {libro.titulo}, Autor: {libro.autor}, Cantidad: {libro.cantidad}, Disponible: {'Si' if libro.disponible else 'No'}")
            
    def prestar_libro(self, titulo: str, nombre_usuario: str):
        # Presta un libro a un usuario dado su título y nombre de usuario.

        # Parámetros:
        #   titulo (str): El título del libro a prestar.
        #   nombre_usuario (str): El nombre del usuario al que se prestará el libro.
        if titulo not in self.libros:
            print(f"El libro '{titulo}' no se encuentra en la biblioteca.")
            return

        if not self.libros[titulo].disponible:
            print(f"El libro '{titulo}' no está disponible para prestar.")
            return

        if nombre_usuario not in self.usuarios:
            print(f"El usuario '{nombre_usuario}' no está registrado.")
            return

        # Realiza el préstamo del libro
        self.libros[titulo].disponible = False
        self.libros[titulo].cantidad -= 1
        self.usuarios[nombre_usuario].libros_prestados.append(titulo)
        print(f"El libro '{titulo}' ha sido prestado a {nombre_usuario}.")
    
        
    def registrar_usuario(self, nombre: str):
        # Registra un nuevo usuario en la biblioteca.

        # Parámetros:
        #   nombre (str): El nombre del usuario a registrar.
        if nombre not in self.usuarios:
            self.usuarios[nombre] = Usuario(nombre)
            print(f"Usuario '{nombre}' registrado exitosamente.")
        else:
            print(f"El usuario {nombre} ya existe.")
            
    def guardar_datos(self):
        # Guarda los datos actuales de la biblioteca en un archivo pickle.
        with open('datos_biblioteca.pkl', 'wb') as archivo:
            pickle.dump((self.libros, self.usuarios), archivo)
            
    def cargar_datos(self):
        # Intenta cargar los datos previos de la biblioteca desde el archivo 'datos_biblioteca.pkl' utilizando pickle.
        try:
            with open('datos_biblioteca.pkl', 'rb') as archivo:
                self.libros, self.usuarios = pickle.load(archivo)
        except FileNotFoundError:
            print('No se encontraron datos guardados.')
            
    def listar_usuarios(self):
        # Muestra una lista de los usuarios registrados en la biblioteca.
        if not self.usuarios:
            print("No hay usuarios registrados.")
        else:
            print("Usuarios registrados:")
            for nombre in self.usuarios:
                print(nombre)
            
    def listar_libros_usuario(self, nombre_usuario: str):
        # Muestra una lista de libros prestados a un usuario específico.

        # Parámetros:
        #   nombre_usuario (str): El nombre del usuario del que se desea mostrar los libros prestados.
        if nombre_usuario in self.usuarios:
            libros_prestados = self.usuarios[nombre_usuario].libros_prestados
            print(f"Libros prestados a {nombre_usuario}:")
            for titulo in libros_prestados:
                libro = self.libros[titulo]
                print(f"Título: {libro.titulo}, Autor: {libro.autor}")
        else:
            print("Usuario no encontrado.")
        
    def devolver_libro(self, titulo: str, nombre_usuario: str):
        # Permite a un usuario devolver un libro prestado.

        # Parámetros:
        #   titulo (str): El título del libro que se va a devolver.
        #   nombre_usuario (str): El nombre del usuario que devuelve el libro.
        if nombre_usuario in self.usuarios and titulo in self.usuarios[nombre_usuario].libros_prestados:
            self.usuarios[nombre_usuario].libros_prestados.remove(titulo)
            self.libros[titulo].disponible = True
            self.libros[titulo].cantidad += 1
            print(f'El libro {titulo} ha sido devuelto correctamente.')
        else: 
            print('El usuario no tiene prestado este libro')