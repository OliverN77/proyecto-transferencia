# 🧩 Ejercicio 1: Calcular promedio de números
# OBJETIVO: Leer números, calcular promedio y manejar errores de conversión

def calcular_promedio():
    """Calcula el promedio de números ingresados separados por comas."""
    try:
        numeros_str = input("Ingrese números enteros separados por comas: ")
        numeros = [int(num.strip()) for num in numeros_str.split(",")]
        
        if len(numeros) == 0:
            raise ValueError("No se ingresaron números.")
        
        suma = sum(numeros)
        cantidad = len(numeros)
        promedio = suma / cantidad
        
        print(f"\nNúmeros ingresados: {numeros}")
        print(f"Suma: {suma}")
        print(f"Cantidad: {cantidad}")
        print(f"✓ Promedio: {promedio:.2f}\n")
    
    except ValueError as e:
        print(f"❌ Error de valor: {e}\n")
    except Exception as e:
        print(f"❌ Error inesperado: {e}\n")


def menu_promedio():
    """Punto de entrada del menú para ejercicio 1."""
    calcular_promedio()


if __name__ == "__main__":
    menu_promedio()
    
