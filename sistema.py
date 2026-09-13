def registrar_producto(nombre, precio, cantidad):
    """Registra un producto y devuelve sus datos."""
    if not nombre:
        raise ValueError("El nombre del producto es obligatorio.")

    if precio <= 0:
        raise ValueError("El precio debe ser mayor que cero.")

    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que cero.")

    return {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }


def calcular_total(precio, cantidad):
    """Calcula el valor total de un producto."""
    if precio < 0 or cantidad < 0:
        raise ValueError("Los valores no pueden ser negativos.")

    return precio * cantidad


def validar_producto(nombre, precio, cantidad):
    """Verifica si los datos de un producto son válidos."""
    return (
        bool(nombre)
        and precio > 0
        and cantidad > 0
    )


if __name__ == "__main__":
    producto = registrar_producto("Cuaderno", 8000, 2)
    total = calcular_total(producto["precio"], producto["cantidad"])

    print("=== SISTEMA DE GESTIÓN DE PRODUCTOS ===")
    print(f"Producto: {producto['nombre']}")
    print(f"Precio: ${producto['precio']}")
    print(f"Cantidad: {producto['cantidad']}")
    print(f"Total: ${total}")
    print(f"Producto válido: {validar_producto('Cuaderno', 8000, 2)}")