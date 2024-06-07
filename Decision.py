def calcular_descuento(precio, es_cliente_frecuente):
    if es_cliente_frecuente:
        return precio * 0.9  # 10% de descuento
    else:
        return precio

# Prueba de decisión
def test_calcular_descuento():
    # Caso 1: Cliente frecuente
    assert calcular_descuento(100, True) == 90, "Error en descuento para cliente frecuente"
    
    # Caso 2: Cliente no frecuente
    assert calcular_descuento(100, False) == 100, "Error en descuento para cliente no frecuente"

# Ejecutar las pruebas
test_calcular_descuento()
print("Todas las pruebas de decisión pasaron.")