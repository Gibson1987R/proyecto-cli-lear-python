import notas.nota as modelo
from usuarios.validaciones import Validar

class Notacciones:
    
    def crear(self, usuario):
        print(f'\nOk {usuario[1]}!!! Vamos a crear una nueva nota...')

        titulo = input('Introduce el titutlo de tu nota: ')
        while not Validar.titulo_nota(titulo):
            print("Error: El título debe tener al menos 3 caracteres.")
            titulo = input('Introduce el titutlo de tu nota: ')

        descripcion = input('Mete el contenido de tu nota: ')
        while not Validar.no_vacio(descripcion):
            print("Error: El contenido no puede estar vacío.")
            descripcion = input('Mete el contenido de tu nota: ')

        nota = modelo.Nota(usuario[0], usuario[3], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f'\nPerfecto has guardado la nota: {nota.titulo}')
        
        else:
            print(f'No se ha guardado la nota, lo siento {usuario[1]}')

    def mostrar(self, usuario):
        # Creamos un objeto Nota para llamar a listar()
        # Ponemos el email vacío porque para listar solo necesitamos el ID del usuario
        nota = modelo.Nota(usuario[0], "", "", "")
        notas = nota.listar()

        print(f"\nEstas son tus notas {usuario[1]}:")
        
        for n in notas:
            print("\n---------------------------------------")
            print(f"Título: {n[3]}") # n[3] es el título en la base de datos
            print(f"Contenido: {n[4]}") # n[4] es la descripción
            print(f"Fecha: {n[5]}") # n[5] es la fecha
            print("---------------------------------------")

    def borrar(self, usuario):
        print(f'\nOkey {usuario[1]} !!! Vamos a borrar notas')

        titulo = input('Introduce el titulo de la nota a borrar: ')
        while not Validar.no_vacio(titulo):
            print("Error: Debes introducir un título.")
            titulo = input('Introduce el titulo de la nota a borrar: ')

        nota = modelo.Nota(usuario[0], "", titulo, "")
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f'Hemos borrado la nota: {nota.titulo}')
        
        else:
            print('No se ha borrado la nota, prueba luego ...')