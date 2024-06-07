# test_mi_modulo.py
from mi_modulo import calcular_descuento, procesar_pedido

def test_calcular_descuento():
    assert calcular_descuento(100, True) == 90, "Error en descuento para cliente frecuente"
    assert calcular_descuento(100, False) == 100, "Error en descuento para cliente no frecuente"

def test_procesar_pedido():
    assert procesar_pedido([]) == "Error: No hay productos", "Error en validación de productos vacíos"
    assert procesar_pedido([10, 20, 30]) == "Pedido confirmado. Total: 60", "Error en cálculo de total sin descuento"
    assert procesar_pedido([50, 60, 20]) == "Pedido confirmado. Total: 121.5", "Error en cálculo de total con descuento"

# Ejecutar las pruebas
if __name__ == "__main__":
    test_calcular_descuento()
    test_procesar_pedido()
    print("Todas las pruebas pasaron.")
