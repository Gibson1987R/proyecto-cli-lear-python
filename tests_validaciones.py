import pytest
from usuarios.validaciones import Validar

def test_email_valido():
    assert Validar.email("test@gmail.com") == True
    assert Validar.email("usuario.nombre@empresa.es") == True

def test_email_invalido():
    assert Validar.email("test@") == False
    assert Validar.email("test@gmail") == False
    assert Validar.email("testgmail.com") == False

def test_solo_letras_valido():
    assert Validar.solo_letras("Victor") == True
    assert Validar.solo_letras("Juan Perez") == True

def test_solo_letras_invalido():
    assert Validar.solo_letras("Victor123") == False
    assert Validar.solo_letras("Juan_Perez") == False
    assert Validar.solo_letras("") == False

def test_no_vacio():
    assert Validar.no_vacio("Algo") == True
    assert Validar.no_vacio("  ") == False
    assert Validar.no_vacio("") == False

def test_titulo_nota_valido():
    assert Validar.titulo_nota("Mi nota") == True
    assert Validar.titulo_nota("Abc") == True

def test_titulo_nota_invalido():
    assert Validar.titulo_nota("Ab") == False
    assert Validar.titulo_nota(" ") == False
