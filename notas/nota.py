import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota:

    def __init__(self, usuario_id, email, titulo, descripcion):
        self.usuario_id = usuario_id
        self.email = email
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):


        
        sql = 'INSERT INTO notas VALUES(null, %s, %s, %s, %s, CURDATE())'
        nota = (self.usuario_id, self.email, self.titulo, self.descripcion)

        cursor.execute(sql, nota)
        database.commit()

        return [cursor.rowcount, self]

    def listar(self):
        # Buscamos todas las notas que pertenezcan a este usuario
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"
        cursor.execute(sql)
        resultado = cursor.fetchall()

        return resultado
    
    def eliminar(self):
        sql = f'DELETE FROM notas WHERE usuario_id ={self.usuario_id} AND titulo LIKE "%{self.titulo}%" '

        cursor.execute(sql)
        database.commit()

        return [cursor.rowcount, self]