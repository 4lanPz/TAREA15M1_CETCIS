# TAREA15M1_CETCIS

# Sistema de Gestión de Inventario y Pedidos – Reto 3

En el reto 3 se implementó un sistema básico de inventario y gestión de pedidos utilizando listas, para este reto se utiliza de base el reto 1 y el reto 2.
El sistema fue optimizado mediante el uso de estructuras de datos avanzadas como listas enlazadas, colas y pilas, con el objetivo de mejorar la organización y manejo de la información.

---

## ¿Qué hace el sistema?

El sistema permite:
- Registrar productos en un inventario
- Visualizar los productos disponibles
- Registrar pedidos de clientes
- Visualizar pedidos pendientes
- Atender pedidos en orden
- Deshacer la última acción realizada

---

## Cambios respecto al Reto 2

En el Reto 2:
- El inventario y los pedidos se manejaba con una lista
- No existía historial de acciones

---

### Lista enlazada (Inventario)

Se reemplazó la lista tradicional por una lista enlazada para almacenar los productos lo que permite manejar una colección dinámica de productos sin depender de índices.

---

### Cola – FIFO (Pedidos)

Los pedidos ahora se manejan con una cola, respetando el principio lo que ayuda a que el primer pedido en registrarse es el primero en ser atendido, simulando un caso real.

---

### Pila (Historial)

Se implementó una pila para guardar las acciones realizadas y poder deshacer la última operación que permite revertir cambios fácilmente (ej: ingreso de producto o pedido).

---

## Mejoras comparando el reto 1 y 2

- Mejor organización de los datos
- Uso de estructuras más cercanas a aplicaciones reales
- Implementación de lógica FIFO para pedidos
- Posibilidad de deshacer acciones
- Código más alineado con estructuras de datos vistas en clase

---

## Capturas

![Imagen 1](https://github.com/4lanPz/TAREA15M1_CETCIS/blob/main/captura%201.jpg)

![Imagen 2](https://github.com/4lanPz/TAREA15M1_CETCIS/blob/main/captura%202.jpg)

![Imagen 3](https://github.com/4lanPz/TAREA15M1_CETCIS/blob/main/captura%203.jpg)
