import usuarios.usuario as modelo
import notas.notacciones 
from usuarios.validaciones import Validar

class Acciones:

    def registros(self):
            print('\nOk!! Vamos a resgistrarte en el sistema ...')

            nombre = input('Cual es tu nombre?: ')
            while not Validar.solo_letras(nombre):
                print("Error: El nombre solo debe contener letras.")
                nombre = input('Cual es tu nombre?: ')

            apellido = input('Cual es tu apellido?: ')
            while not Validar.solo_letras(apellido):
                print("Error: El apellido solo debe contener letras.")
                apellido = input('Cual es tu apellido?: ')

            email = input('Introducce tu email: ')
            while not Validar.email(email):
                print("Error: Introduce un email válido.")
                email = input('Introducce tu email: ')

            password = input('Introduce tu contraseña: ')
            while not Validar.no_vacio(password):
                print("Error: La contraseña no puede estar vacía.")
                password = input('Introduce tu contraseña: ')

            usuario = modelo.Usuario(nombre, apellido, email, password)
            registro = usuario.registrar()

            if registro[0] >= 1: #aca registro[0] apunta al indice
                print(f'\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}')
            else:
                print('\nNo te has registrado correctamente (es posible que el email ya exista)!!!')

    def login(self):
        print('Vale!! Identificate en el sistema...')

        try:
            email = input('Introducce tu email: ')
            while not Validar.email(email):
                print("Error: Formato de email incorrecto.")
                email = input('Introducce tu email: ')

            password = input('Introduce tu contraseña: ')
            while not Validar.no_vacio(password):
                print("Error: La contraseña es obligatoria.")
                password = input('Introduce tu contraseña: ')
            
            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if login:
                if email == login[3]:
                    print(f'Bienvenido {login[1]}, te has registrado en el sistema el {login[5]}')
                    self.proximasAcciones(login)
            else:
                print(f'Login incorrecto!!! Intentalo mas tarde')

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f'Error: {e}')
            print(f'Ocurrió un error inesperado.')
    
    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
            - Crear nota (crear)
            - Mostrar notas (mostrar)
            - Eliminar nota (eliminar)
            - Salir (salir)
        """)
        
        accion = input('Que quieres hacer?: ')
        
        hazEl = notas.notacciones.Notacciones()

        if accion == 'crear':
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == 'mostrar':
            # ¡Aquí está la conexión mágica!
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == 'eliminar': 
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == 'salir':
            print(f'Ok {usuario[1]}, hasta pronto!!!')
            exit()
