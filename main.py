'''
Proyecto Python y Mysql:
- Abrir asistente
- Login o Registro
- Si elegimos registro, crera un usuario en la bbdd
- Si elegiomos login, identifica al usuario y nos preguntara
- Crear nota, mostrar notas, borrarlas.
'''

from usuarios import acciones

print('''
Acciones disponibles:
    - registro
    - login
''')

hazEl = acciones.Acciones()
accion = input(' Que quieres hacer?: ')

if accion == 'registro' :
    hazEl.registros()

elif accion == 'login':
    hazEl.login()