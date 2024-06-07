def procesar_pedido(productos):
    # Paso 1: Validar productos
    if not productos:
        return "Error: No hay productos"
    
    # Paso 2: Calcular total
    total = sum(productos)
    
    # Paso 3: Aplicar descuento si total > 100
    if total > 100:
        total *= 0.95  # 5% de descuento
    
    # Paso 4: Confirmar pedido
    return f"Pedido confirmado. Total: {total}"

# Prueba de secuencia
def test_procesar_pedido():
    # Caso 1: Pedido sin productos
    assert procesar_pedido([]) == "Error: No hay productos", "Error en validación de productos vacíos"
    
    # Caso 2: Pedido con productos total <= 100
    assert procesar_pedido([10, 20, 30]) == "Pedido confirmado. Total: 60", "Error en cálculo de total sin descuento"
    
    # Caso 3: Pedido con productos total > 100
    assert procesar_pedido([50, 60, 20]) == "Pedido confirmado. Total: 121.5", "Error en cálculo de total con descuento"

# Ejecutar las pruebas
test_procesar_pedido()
print("Todas las pruebas de secuencia pasaron.")