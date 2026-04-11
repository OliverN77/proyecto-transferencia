# 🧩 Ejercicio 5: Validador de contraseñas refactorizado
# OBJETIVO: Función clara, nombres explícitos, retornos tempranos

# Validadores modulares (reglas simples y reutilizables)
has_min_length = lambda pwd: len(pwd) >= 8
has_no_spaces = lambda pwd: " " not in pwd
has_uppercase = lambda pwd: pwd != pwd.lower()
has_digits = lambda pwd: any(c.isdigit() for c in pwd)


def is_valid_password(password: str) -> bool:
    """
    Valida una contraseña según reglas de seguridad.
    
    Reglas:
    - Longitud mínima: 8 caracteres
    - Al menos 1 dígito
    - Al menos 1 mayúscula
    - Sin espacios
    """
    try:
        if not isinstance(password, str):
            return False
        
        if not has_min_length(password):
            return False
        if not has_no_spaces(password):
            return False
        if not has_uppercase(password):
            return False
        if not has_digits(password):
            return False
        
        return True
    except Exception:
        return False


def menu_validador_contrasena():
    """Menú interactivo para validar contraseñas."""
    print("\n--- VALIDADOR DE CONTRASEÑAS ---")
    print("Requisitos:")
    print("  • Mínimo 8 caracteres")
    print("  • Al menos 1 dígito")
    print("  • Al menos 1 mayúscula")
    print("  • Sin espacios\n")
    
    try:
        pwd = input("Ingresa una contraseña para validar: ")
        resultado = is_valid_password(pwd)
        
        if resultado:
            print("✓ La contraseña es VÁLIDA\n")
        else:
            print("❌ La contraseña es INVÁLIDA\n")
            print("Verifica que cumpla todos los requisitos.\n")
    
    except KeyboardInterrupt:
        print("\n\nOperación cancelada")
    except Exception as e:
        print(f"❌ Error: {e}\n")


if __name__ == "__main__":
    menu_validador_contrasena()