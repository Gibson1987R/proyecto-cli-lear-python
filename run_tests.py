from usuarios.validaciones import Validar

def run_manual_tests():
    print("Iniciando Pruebas de Validación...")
    
    # Pruebas Email
    assert Validar.email("test@gmail.com") == True
    assert Validar.email("invalido") == False
    print("✅ Emails validados")

    # Pruebas Solo Letras
    assert Validar.solo_letras("Gibson") == True
    assert Validar.solo_letras("Gibson 123") == False
    print("✅ Nombres validados")

    # Pruebas Notas
    assert Validar.titulo_nota("Mi nota") == True
    assert Validar.titulo_nota("No") == False
    print("✅ Notas validadas")

    print("\n--- ¡TODAS LAS PRUEBAS PASARON CORRECTAMENTE! ---")

if __name__ == "__main__":
    run_manual_tests()
