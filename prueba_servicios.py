
"""
Pruebas del modulo de servicios de Software FJ.
"""

from servicios import (
    Servicio,
    AlquilerEquipo,
    AsesoriaEspecializada
)


# PRUEBA 1: Verificar que Servicio sea abstracta.
print("\nPRUEBA 1: Clase abstracta")

try:
    servicio = Servicio()
except TypeError:
    print("Correcto: Servicio es una clase abstracta.")


# PRUEBA 2: Verificar herencia.
print("\nPRUEBA 2: Herencia")

equipo = AlquilerEquipo("Camara profesional", 25000)
asesoria = AsesoriaEspecializada("Diseño multimedia", 50000)

print("¿AlquilerEquipo hereda de Servicio?")
print(isinstance(equipo, Servicio))

print("¿AsesoriaEspecializada hereda de Servicio?")
print(isinstance(asesoria, Servicio))


# PRUEBA 3: Describir servicios.
print("\nPRUEBA 3: Descripcion de servicios")

print(equipo.describir())
print("Costo de 2 horas:", equipo.calcular_costo(2))

print("-" * 40)

print(asesoria.describir())
print("Costo de 2 horas:", asesoria.calcular_costo(2))


print("\nPRUEBAS FINALIZADAS")
