import re

class Validar:
    
    @staticmethod
    def email(email):
        # Expresión regular para validar email estándar
        patron = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(patron, email):
            return True
        return False

    @staticmethod
    def solo_letras(texto):
        # Valida que solo contenga letras y espacios
        return all(x.isalpha() or x.isspace() for x in texto) and len(texto.strip()) > 0

    @staticmethod
    def no_vacio(texto):
        # Valida que el texto no esté vacío o solo contenga espacios
        return len(texto.strip()) > 0

    @staticmethod
    def titulo_nota(titulo):
        # Valida longitud mínima de 3 caracteres alfanuméricos
        return len(titulo.strip()) >= 3
