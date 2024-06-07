# mi_modulo.py
def calcular_descuento(precio, es_cliente_frecuente):
    if es_cliente_frecuente:
        return precio * 0.9  # 10% de descuento
    else:
        return precio

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