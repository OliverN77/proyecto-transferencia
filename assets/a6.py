#🧩 Ejercicio 6: Procesamiento de ventas con descuentos
# OBJETIVO: Refactorizar procesamiento, validar datos, calcular totales

def calculate_sale_total(venta: dict) -> float:
    """Calcula total de una venta con descuentos aplicados."""
    if venta.get("status") != "ok":
        raise ValueError(f"Venta inválida: {venta}")
    
    precio, cantidad = venta["price"], venta["quantity"]
    cliente = venta.get("customer", "regular")
    
    # Descuento: 10% si cantidad >= 10, +5% extra si es VIP
    descuento = (0.1 if cantidad >= 10 else 0.0) + (0.05 if cliente == "vip" else 0.0)
    
    return precio * cantidad * (1 - descuento)


def calculate_total(ventas: list) -> float:
    """Suma totales de ventas válidas (ignora inválidas)."""
    total = 0
    for venta in ventas:
        try:
            total += calculate_sale_total(venta)
        except ValueError:
            continue
    return total


def report_invalid_sales(ventas: list) -> None:
    """Reporta ventas inválidas."""
    invalidas = [v for v in ventas if v.get("status") != "ok"]
    if invalidas:
        print("VENTAS INVÁLIDAS:")
        for venta in invalidas:
            print(f"  - {venta}")
    else:
        print("No hay ventas inválidas.")


def menu_procesamiento_ventas():
    """Menú de pruebas para el procesamiento de ventas."""
    print("\n--- PROCESAMIENTO DE VENTAS ---\n")
    
    # Test cases
    test_cases = [
        {
            "nombre": "Suma correcta",
            "ventas": [
                {"status": "ok", "price": 100, "quantity": 1, "customer": "regular"},
                {"status": "ok", "price": 50, "quantity": 1, "customer": "regular"}
            ],
            "esperado": 150.0
        },
        {
            "nombre": "Descuento por cantidad (10%)",
            "ventas": [{"status": "ok", "price": 100, "quantity": 10, "customer": "regular"}],
            "esperado": 900.0
        },
        {
            "nombre": "Descuento VIP (15% total)",
            "ventas": [{"status": "ok", "price": 100, "quantity": 10, "customer": "vip"}],
            "esperado": 850.0
        },
        {
            "nombre": "Ignora ventas inválidas",
            "ventas": [
                {"status": "ok", "price": 100, "quantity": 1, "customer": "regular"},
                {"status": "cancelled", "price": 50, "quantity": 1, "customer": "regular"},
                {"status": "ok", "price": 25, "quantity": 1, "customer": "regular"}
            ],
            "esperado": 125.0
        }
    ]
    
    print("Ejecutando tests...\n")
    passed = 0
    
    for i, test in enumerate(test_cases, 1):
        resultado = calculate_total(test["ventas"])
        es_correcto = resultado == test["esperado"]
        status = "✓" if es_correcto else "❌"
        
        print(f"{status} Test {i}: {test['nombre']}")
        print(f"   Resultado: {resultado}, Esperado: {test['esperado']}")
        
        if es_correcto:
            passed += 1
    
    print(f"\n_________________________________")
    print(f"Resultado: {passed}/{len(test_cases)} pruebas pasadas\n")
    
    # Reporte de ventas
    print("Reporte de ventas del último test:")
    report_invalid_sales(test_cases[-1]["ventas"])
    print()


if __name__ == "__main__":
    menu_procesamiento_ventas()