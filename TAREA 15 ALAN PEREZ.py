# RETO 3

def leer_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Error: el valor debe ser mayor o igual a {minimo}.")
            else:
                return valor
        except ValueError:
            print("Error: ingrese un número entero válido")

def leer_decimal(mensaje, minimo=None):
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Error: el valor debe ser mayor o igual a {minimo}.")
            else:
                return valor
        except ValueError:
            print("Error: ingrese un número válido")

# LISTA ENLAZADA (INVENTARIO)
class NodoProducto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.siguiente = None

inventario = None  # ahora ya no es lista, es nodo

def buscar_producto(nombre):
    actual = inventario
    while actual:
        if actual.nombre.lower() == nombre.lower():
            return actual
        actual = actual.siguiente
    return None

def registrar_producto():
    global inventario
    print("\n=== REGISTRAR PRODUCTO ===")
    nombre = input("Nombre: ").strip()
    if nombre == "":
        print("Nombre inválido")
        return
    existente = buscar_producto(nombre)
    if existente:
        print("El producto ya existe")
        cantidad = leer_entero("Cantidad a agregar: ", 1)
        existente.cantidad += cantidad
        # guardar en pila
        historial.append(("agregar_stock", nombre, cantidad))
        return
    cantidad = leer_entero("Cantidad: ", 0)
    precio = leer_decimal("Precio: ", 0)
    nuevo = NodoProducto(nombre, cantidad, precio)
    if inventario is None:
        inventario = nuevo
    else:
        actual = inventario
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo
    historial.append(("nuevo_producto", nombre, cantidad))
    print("Producto registrado")

def mostrar_productos():
    print("\n=== INVENTARIO ===")
    if inventario is None:
        print("Vacío")
        return
    actual = inventario
    i = 1
    while actual:
        print(f"{i}. {actual.nombre} | {actual.cantidad} | ${actual.precio}")
        actual = actual.siguiente
        i += 1

# COLA (PEDIDOS)
class NodoPedido:
    def __init__(self, cliente, producto, cantidad, total):
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad
        self.total = total
        self.siguiente = None

frente = None
final = None

def obtener_producto_por_numero(numero):
    actual = inventario
    contador = 1
    while actual:
        if contador == numero:
            return actual
        actual = actual.siguiente
        contador += 1
    return None

def registrar_pedido():
    global frente, final
    print("\n=== REGISTRAR PEDIDO ===")
    if inventario is None:
        print("No hay productos")
        return
    cliente = input("Cliente: ").strip()
    if cliente == "":
        print("Nombre de cliente inválido")
        return
    mostrar_productos()
    opcion_producto = leer_entero("Seleccione el número del producto: ", 1)
    producto = obtener_producto_por_numero(opcion_producto)
    if producto is None:
        print("Opción de producto no válida")
        return
    cantidad = leer_entero("Cantidad: ", 1)
    if cantidad > producto.cantidad:
        print("Stock insuficiente")
        return
    total = cantidad * producto.precio
    nuevo = NodoPedido(cliente, producto.nombre, cantidad, total)
    # Agregar a la cola FIFO
    if final is None:
        frente = nuevo
        final = nuevo
    else:
        final.siguiente = nuevo
        final = nuevo
    producto.cantidad -= cantidad
    historial.append(("pedido", producto.nombre, cantidad))
    print("Pedido agregado a la cola")
    print(f"Producto: {producto.nombre}")
    print(f"Total: ${total}")

def mostrar_pedidos():
    print("\n=== PEDIDOS (COLA) ===")
    if frente is None:
        print("No hay pedidos")
        return
    actual = frente
    i = 1
    while actual:
        print(f"{i}. {actual.cliente} | {actual.producto} | {actual.cantidad}")
        actual = actual.siguiente
        i += 1

def atender_pedido():
    global frente, final
    print("\n=== ATENDER PEDIDO ===")
    if frente is None:
        print("No hay pedidos")
        return
    print("Siguiente pedido en la cola:")
    print(f"Cliente: {frente.cliente}")
    print(f"Producto: {frente.producto}")
    print(f"Cantidad: {frente.cantidad}")
    print(f"Total: ${frente.total}")
    pedido = frente
    frente = frente.siguiente
    if frente is None:
        final = None
    print("Pedido atendido correctamente")

# PILA (DESHACER)
historial = []  # pila

def deshacer():
    print("\n=== DESHACER ===")
    if len(historial) == 0:
        print("Nada que deshacer")
        return
    accion = historial.pop()
    if accion[0] == "nuevo_producto":
        nombre = accion[1]
        global inventario
        if inventario and inventario.nombre == nombre:
            inventario = inventario.siguiente
        else:
            actual = inventario
            while actual and actual.siguiente:
                if actual.siguiente.nombre == nombre:
                    actual.siguiente = actual.siguiente.siguiente
                    break
                actual = actual.siguiente
        print("Producto eliminado (deshacer)")
    elif accion[0] == "agregar_stock":
        producto = buscar_producto(accion[1])
        if producto:
            producto.cantidad -= accion[2]
        print("Stock revertido")
    elif accion[0] == "pedido":
        producto = buscar_producto(accion[1])
        if producto:
            producto.cantidad += accion[2]
        print("Pedido revertido (stock devuelto)")

# MENÚ PRINCIPAL
while True:
    print("\n=== SISTEMA ===")
    print("1. Registrar producto")
    print("2. Ver inventario")
    print("3. Registrar pedido")
    print("4. Ver pedidos")
    print("5. Atender pedido")
    print("6. Deshacer")
    print("7. Salir")

    op = input("Opción: ")

    if op == "1":
        registrar_producto()
    elif op == "2":
        mostrar_productos()
    elif op == "3":
        registrar_pedido()
    elif op == "4":
        mostrar_pedidos()
    elif op == "5":
        atender_pedido()
    elif op == "6":
        deshacer()
    elif op == "7":
        break
    else:
        print("Opción inválida")