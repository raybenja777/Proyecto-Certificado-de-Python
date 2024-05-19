from gestion_biblioteca import Biblioteca

def main():
    # Crear una instancia de la Biblioteca
    biblioteca = Biblioteca()
    
    # Cargar datos previos de la biblioteca (si existen)
    biblioteca.cargar_datos()
    
    while True:
        # Menú de opciones para el usuario
        print('\nBienvenido a la Biblioteca')
        print('1. Agregar un libro')
        print('2. Mostrar libros')
        print('3. Prestar libro')
        print('4. Registrar usuario')
        print('5. Listar Usuarios')
        print('6. Listar libros del usuario')
        print('7. Devolver libro')
        print('0. Salir')
        
        # Solicitar al usuario que ingrese una opción
        opcion = input('Ingrese el número de la acción que desea realizar: ')
        
        # Procesar la opción seleccionada por el usuario
        if opcion == '1':
            # Agregar un libro a la biblioteca
            titulo = input('Ingrese el título del libro: ')
            autor = input('Ingrese el autor del libro: ')
            biblioteca.agregar_libro(titulo, autor)
        elif opcion == '2':
            # Mostrar la lista de libros disponibles en la biblioteca
            biblioteca.mostrar_libros()
        elif opcion == '3':
            # Prestar un libro
            titulo = input('Ingrese el título del libro: ')
            nombre_usuario = input('Ingrese el nombre del usuario: ')
            biblioteca.prestar_libro(titulo, nombre_usuario)
        elif opcion == '4':
            # Registrar un usuario
            nombre_usuario = input('Ingrese el nombre del usuario a registrar: ')
            biblioteca.registrar_usuario(nombre_usuario)
        elif opcion == '5':
            # Listar los usuarios
            biblioteca.listar_usuarios()
        elif opcion == '6':
            # Listar los libros de un usuario
            nombre_usuario = input('Ingrese el nombre del usuario: ')
            biblioteca.listar_libros_usuario(nombre_usuario)
        elif opcion == '7':
            # Devolver un libro
            titulo = input('Ingrese el título del libro: ')
            nombre_usuario = input('Ingrese el nombre del usuario: ')
            biblioteca.devolver_libro(titulo, nombre_usuario)
        elif opcion == '0':
            # Guardar los datos al salir
            biblioteca.guardar_datos()
            print("Los datos se han guardado correctamente.")
            print("Gracias por usar la Biblioteca. ¡Hasta luego!")
            break
            
if __name__ == '__main__':
    main()
            