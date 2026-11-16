
"""
Prueba de integracion de los modulos de Software FJ.
"""

from cliente import Cliente
from servicios import AlquilerEquipo
from reservas import Reserva


print("\n===== PRUEBA DE INTEGRACION =====")


# 1. Crear un cliente.
print("\n1. REGISTRO DE CLIENTE")

cliente = Cliente(
    "Laura Martínez",
    "456789123",
    "laura@gmail.com",
    "3104567890",
    "Calle 20 # 15-30"
)

print(cliente)


# 2. Crear un servicio.
print("\n2. CREACION DE SERVICIO")

servicio = AlquilerEquipo(
    "Camara profesional",
    25000
)

print(servicio.describir())


# 3. Crear una reserva.
print("\n3. CREACION DE RESERVA")

reserva = Reserva(
    cliente,
    servicio,
    3
)

print("Reserva creada:", reserva.id)
print("Estado:", reserva.estado)


# 4. Confirmar reserva.
print("\n4. CONFIRMACION")

reserva.confirmar()

print("Estado:", reserva.estado)


# 5. Calcular costo.
print("\n5. CALCULO DEL COSTO")

costo = reserva.calcular_costo(
    impuesto=0.19,
    descuento=0.10
)

print(f"Costo total: ${costo:,.2f}")


# 6. Procesar reserva.
print("\n6. PROCESAMIENTO")

resultado = reserva.procesar(
    impuesto=0.19,
    descuento=0.10
)

print(f"Costo procesado: ${resultado:,.2f}")
print("Estado final:", reserva.estado)


print("\n===== PRUEBA FINALIZADA =====")
