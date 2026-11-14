
"""
Servicios desarrollados por el integrante 2.
"""

from excepciones import (
    DatosInvalidosError,
    ServicioNoDisponibleError
)


class AlquilerEquipo:
    """Representa el alquiler de equipos."""

    def __init__(self, nombre, tarifa_hora, disponible=True):
        self.nombre = nombre
        self.tarifa_hora = tarifa_hora
        self.disponible = disponible

        self.validar_parametros()

    def validar_parametros(self):
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise DatosInvalidosError(
                "El nombre del equipo es obligatorio."
            )

        if (
            not isinstance(self.tarifa_hora, (int, float))
            or isinstance(self.tarifa_hora, bool)
            or self.tarifa_hora <= 0
        ):
            raise DatosInvalidosError(
                "La tarifa por hora debe ser mayor que cero."
            )

    def calcular_costo(self, duracion):
        if not self.disponible:
            raise ServicioNoDisponibleError(
                f"El equipo {self.nombre} no está disponible."
            )

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidosError(
                "La duración debe ser mayor que cero."
            )

        return self.tarifa_hora * duracion

    def describir(self):
        return (
            f"Alquiler de equipo: {self.nombre}. "
            f"Tarifa por hora: ${self.tarifa_hora:,.2f}"
        )

    def __str__(self):
        return f"Alquiler de {self.nombre}"


class AsesoriaEspecializada:
    """Representa un servicio de asesoría especializada."""

    def __init__(self, especialidad, tarifa_hora, disponible=True):
        self.especialidad = especialidad
        self.tarifa_hora = tarifa_hora
        self.disponible = disponible

        self.validar_parametros()

    def validar_parametros(self):
        if (
            not isinstance(self.especialidad, str)
            or not self.especialidad.strip()
        ):
            raise DatosInvalidosError(
                "La especialidad es obligatoria."
            )

        if (
            not isinstance(self.tarifa_hora, (int, float))
            or isinstance(self.tarifa_hora, bool)
            or self.tarifa_hora <= 0
        ):
            raise DatosInvalidosError(
                "La tarifa por hora debe ser mayor que cero."
            )

    def calcular_costo(self, duracion):
        if not self.disponible:
            raise ServicioNoDisponibleError(
                "La asesoría no está disponible."
            )

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidosError(
                "La duración debe ser mayor que cero."
            )

        return self.tarifa_hora * duracion

    def describir(self):
        return (
            f"Asesoría especializada en {self.especialidad}. "
            f"Tarifa por hora: ${self.tarifa_hora:,.2f}"
        )

    def __str__(self):
        return f"Asesoría en {self.especialidad}"
