# 🧩 Ejercicio 2: Contar líneas de un archivo
# OBJETIVO: Abrir archivo, contar líneas, manejar errores y cerrar en finally

def contar_lineas_archivo():
    """Abre un archivo y cuenta el número de líneas."""
    try:
        nombre_archivo = input("Ingrese el nombre del archivo (ej: archivo.txt): ")
        archivo = open(nombre_archivo, "r", encoding="utf-8")
    except FileNotFoundError:
        print(f"❌ Error: El archivo '{nombre_archivo}' no se encontró.\n")
    except Exception as e:
        print(f"❌ Error: {e}\n")
    else:
        try:
            lineas = archivo.readlines()
            print(f"\n✓ El archivo '{nombre_archivo}' tiene {len(lineas)} línea(s).")
            if len(lineas) > 0:
                print(f"Primera línea: {lineas[0].strip()}")
        except Exception as e:
            print(f"❌ Error al leer el archivo: {e}")
    finally:
        try:
            archivo.close()
            print("Archivo cerrado correctamente.\n")
        except NameError:
            print("El archivo no se abrió, no se puede cerrar.\n")


def menu_contar_lineas():
    """Punto de entrada del menú para ejercicio 2."""
    contar_lineas_archivo()


if __name__ == "__main__":
    menu_contar_lineas()