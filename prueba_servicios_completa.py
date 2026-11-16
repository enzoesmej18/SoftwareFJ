
"""
Prueba completa de los servicios de Software FJ.
"""

from servicios import (
    Servicio,
    AlquilerEquipo,
    AsesoriaEspecializada,
    ReservaSala
)

from excepciones import (
    DatosInvalidosError,
    ServicioNoDisponibleError
)


print("\n===== PRUEBAS COMPLETAS DE SERVICIOS =====")


# PRUEBA 1: Clase abstracta.
print("\nPRUEBA 1: Clase abstracta")

try:
    Servicio()
except TypeError:
    print("Correcto: Servicio no se puede instanciar.")


# PRUEBA 2: Crear los tres servicios.
print("\nPRUEBA 2: Creacion de servicios")

equipo = AlquilerEquipo("Camara profesional", 25000)
asesoria = AsesoriaEspecializada("Diseno multimedia", 50000)
sala = ReservaSala("Sala multimedia", 80000, 20)

servicios = [equipo, asesoria, sala]

for servicio in servicios:
    print(servicio.describir())
    print("¿Hereda de Servicio?", isinstance(servicio, Servicio))


# PRUEBA 3: Polimorfismo.
print("\nPRUEBA 3: Polimorfismo")

for servicio in servicios:
    print(
        f"{servicio}: costo de 2 horas = "
        f"${servicio.calcular_costo(2):,.2f}"
    )


# PRUEBA 4: Validacion de capacidad.
print("\nPRUEBA 4: Capacidad invalida")

try:
    ReservaSala("Sala pequena", 50000, 0)
except DatosInvalidosError as error:
    print("Correcto:", error)


# PRUEBA 5: Duracion invalida.
print("\nPRUEBA 5: Duracion invalida")

try:
    sala.calcular_costo(-2)
except DatosInvalidosError as error:
    print("Correcto:", error)


# PRUEBA 6: Servicio no disponible.
print("\nPRUEBA 6: Sala no disponible")

sala_cerrada = ReservaSala(
    "Sala de reuniones",
    60000,
    10,
    disponible=False
)

try:
    sala_cerrada.calcular_costo(2)
except ServicioNoDisponibleError as error:
    print("Correcto:", error)


print("\n===== PRUEBAS COMPLETADAS =====")
