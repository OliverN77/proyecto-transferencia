# 🧩 Ejercicio 4: Calculadora refactorizada
# OBJETIVO: Función clara, manejo de errores, operaciones seguras

def realizar_operacion(a: float, b: float, op: str) -> float:
    """Realiza operaciones aritméticas básicas."""
    ops = {
        "suma": lambda x, y: x + y,
        "resta": lambda x, y: x - y,
        "multiplicacion": lambda x, y: x * y,
        "division": lambda x, y: x / y if y != 0 else (_ for _ in ()).throw(
            ZeroDivisionError("No se puede dividir entre cero.")
        )
    }
    
    if op not in ops:
        raise ValueError(f"Operación '{op}' no válida. Use: {', '.join(ops.keys())}")
    
    return ops[op](a, b)


def menu_calculadora():
    """Menú interactivo para la calculadora."""
    print("\n--- CALCULADORA ---")
    print("Operaciones disponibles: suma, resta, multiplicacion, division\n")
    
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        op = input("Ingrese la operación (suma, resta, multiplicacion, division): ").strip().lower()
        
        resultado = realizar_operacion(a, b, op)
        print(f"\n✓ El resultado de {a} {op} {b} = {resultado}\n")
    
    except ValueError as e:
        print(f"\n❌ Error: {e}\n")
    except ZeroDivisionError as e:
        print(f"\n❌ Error: {e}\n")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}\n")


if __name__ == "__main__":
    menu_calculadora()
