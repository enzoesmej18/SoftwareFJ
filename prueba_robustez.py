
"""
Pruebas de robustez del sistema Software FJ.
"""

from cliente import Cliente
from servicios import AlquilerEquipo
from reservas import Reserva
from excepciones import (
    DatosInvalidosError,
    OperacionNoPermitidaError,
    ServicioNoDisponibleError
)


print("\n===== PRUEBAS DE ROBUSTEZ =====")


# Crear los objetos necesarios para las pruebas.
cliente = Cliente(
    "Andrea Gómez",
    "789456123",
    "andrea@gmail.com",
    "3009876543",
    "Carrera 15"
)

servicio = AlquilerEquipo(
    "Camara profesional",
    25000
)


# PRUEBA 1: Confirmar dos veces la misma reserva.
print("\nPRUEBA 1: Confirmacion duplicada")

reserva1 = Reserva(cliente, servicio, 2)
reserva1.confirmar()

try:
    reserva1.confirmar()
except OperacionNoPermitidaError as error:
    print("Correcto:", error)


# PRUEBA 2: Procesar sin confirmar.
print("\nPRUEBA 2: Procesamiento sin confirmar")

reserva2 = Reserva(cliente, servicio, 2)

try:
    reserva2.procesar()
except OperacionNoPermitidaError as error:
    print("Correcto:", error)


# PRUEBA 3: Cancelar una reserva procesada.
print("\nPRUEBA 3: Cancelacion de reserva procesada")

reserva3 = Reserva(cliente, servicio, 2)
reserva3.confirmar()
reserva3.procesar()

try:
    reserva3.cancelar()
except OperacionNoPermitidaError as error:
    print("Correcto:", error)


# PRUEBA 4: Duracion invalida.
print("\nPRUEBA 4: Duracion invalida")

try:
    Reserva(cliente, servicio, 0)
except DatosInvalidosError as error:
    print("Correcto:", error)


# PRUEBA 5: Servicio no disponible.
print("\nPRUEBA 5: Servicio no disponible")

servicio_no_disponible = AlquilerEquipo(
    "Proyector",
    30000,
    disponible=False
)

try:
    reserva5 = Reserva(cliente, servicio_no_disponible, 2)
    reserva5.confirmar()
    reserva5.procesar()
except ServicioNoDisponibleError as error:
    print("Correcto:", error)


# PRUEBA 6: Impuesto fuera de los limites.
print("\nPRUEBA 6: Impuesto invalido")

reserva6 = Reserva(cliente, servicio, 2)

try:
    reserva6.calcular_costo(impuesto=1.5)
except DatosInvalidosError as error:
    print("Correcto:", error)


print("\n===== PRUEBAS FINALIZADAS =====")
