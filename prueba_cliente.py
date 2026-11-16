
"""
Pruebas de la clase Cliente y su relación con Entidad.
"""

from cliente import Cliente
from entidad import Entidad
from excepciones import DatosInvalidosError


# PRUEBA 1: Comprobar que Entidad es abstracta.
print("\nPRUEBA 1: Clase abstracta")

try:
    entidad = Entidad()
except TypeError:
    print("Correcto: no se puede instanciar Entidad.")


# PRUEBA 2: Crear un cliente válido.
print("\nPRUEBA 2: Crear cliente")

try:
    cliente = Cliente(
        "María Fernanda",
        "123456789",
        "maria@gmail.com",
        "3001234567",
        "Calle 10 # 20-30"
    )

    print(cliente)
    print(cliente.obtener_informacion())

except DatosInvalidosError as error:
    print(f"Error: {error}")


# PRUEBA 3: Correo incorrecto.
print("\nPRUEBA 3: Validar correo")

try:
    cliente_invalido = Cliente(
        "Carlos Pérez",
        "987654321",
        "correo_incorrecto",
        "3001234567",
        "Calle 15"
    )

except DatosInvalidosError as error:
    print(f"Correcto: {error}")


# PRUEBA 4: Documento duplicado.
print("\nPRUEBA 4: Evitar documentos duplicados")

try:
    cliente_duplicado = Cliente(
        "Otra Persona",
        "123456789",
        "otra@gmail.com",
        "3101234567",
        "Carrera 20"
    )

except DatosInvalidosError as error:
    print(f"Correcto: {error}")


print("\nPRUEBAS FINALIZADAS")
