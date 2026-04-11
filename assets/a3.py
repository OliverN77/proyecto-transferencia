# 🧩 Ejercicio 3: Menú con operaciones
# OBJETIVO: Menú que permite dividir números, abrir archivo, o salir

def menu_dividir_y_archivos():
    """Menú con opciones de división y apertura de archivo."""
    while True:
        print("\n--- SUBMENU EJERCICIO 3 ---")
        print("1. Dividir números")
        print("2. Abrir un archivo y mostrar la primera línea")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                resultado = num1 / num2
                print(f"✓ El resultado de la división es: {resultado}\n")
            except ValueError:
                print("❌ Error: Por favor, ingrese números válidos.\n")
            except ZeroDivisionError:
                print("❌ Error: No se puede dividir entre cero.\n")
        
        elif opcion == "2":
            try:
                archivo = open("archivo.txt", "r", encoding="utf-8")
            except FileNotFoundError:
                print("❌ Error: El archivo no se encontró.\n")
            except Exception as e:
                print(f"❌ Error: {e}\n")
            else:
                try:
                    primera_linea = archivo.readline()
                    print(f"✓ La primera línea del archivo es: {primera_linea}\n")
                except Exception as e:
                    print(f"❌ Error: {e}\n")
                finally:
                    try:
                        archivo.close()
                    except NameError:
                        print("El archivo no se abrió, no se puede cerrar.")
        
        elif opcion == "3":
            break
        
        else:
            print("❌ Opción no válida. Por favor, seleccione una opción válida.\n")


if __name__ == "__main__":
    menu_dividir_y_archivos()