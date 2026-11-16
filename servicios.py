
"""
Modulo que define los servicios disponibles
en el sistema Software FJ.
"""

from abc import ABC, abstractmethod
from math import isfinite

from excepciones import (
    DatosInvalidosError,
    ServicioNoDisponibleError
)


class Servicio(ABC):
    """Clase abstracta que define el comportamiento de los servicios."""

    @abstractmethod
    def validar_parametros(self):
        """Valida los datos especificos del servicio."""
        pass

    @abstractmethod
    def calcular_costo(self, duracion):
        """Calcula el costo del servicio segun su duracion."""
        pass

    @abstractmethod
    def describir(self):
        """Devuelve una descripcion del servicio."""
        pass

    @staticmethod
    def validar_duracion(duracion):
        """Comprueba que la duracion sea un numero positivo."""

        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or not isfinite(duracion)
            or duracion <= 0
        ):
            raise DatosInvalidosError(
                "La duracion debe ser un numero mayor que cero."
            )

    @staticmethod
    def validar_tarifa(tarifa):
        """Comprueba que la tarifa sea un numero positivo."""

        if (
            not isinstance(tarifa, (int, float))
            or isinstance(tarifa, bool)
            or not isfinite(tarifa)
            or tarifa <= 0
        ):
            raise DatosInvalidosError(
                "La tarifa debe ser un numero mayor que cero."
            )


class AlquilerEquipo(Servicio):
    """Representa el alquiler de equipos."""

    def __init__(self, nombre, tarifa_hora, disponible=True):
        self.nombre = nombre.strip() if isinstance(nombre, str) else nombre
        self.tarifa_hora = tarifa_hora
        self.disponible = disponible

        self.validar_parametros()

    def validar_parametros(self):
        if not isinstance(self.nombre, str) or not self.nombre:
            raise DatosInvalidosError(
                "El nombre del equipo es obligatorio."
            )

        self.validar_tarifa(self.tarifa_hora)

        if not isinstance(self.disponible, bool):
            raise DatosInvalidosError(
                "La disponibilidad debe ser verdadera o falsa."
            )

    def calcular_costo(self, duracion):
        self.validar_duracion(duracion)

        if not self.disponible:
            raise ServicioNoDisponibleError(
                f"El equipo {self.nombre} no esta disponible."
            )

        return self.tarifa_hora * duracion

    def describir(self):
        return (
            f"Alquiler de equipo: {self.nombre}. "
            f"Tarifa por hora: ${self.tarifa_hora:,.2f}"
        )

    def __str__(self):
        return f"Alquiler de {self.nombre}"


class AsesoriaEspecializada(Servicio):
    """Representa un servicio de asesoria especializada."""

    def __init__(self, especialidad, tarifa_hora, disponible=True):
        self.especialidad = (
            especialidad.strip()
            if isinstance(especialidad, str)
            else especialidad
        )
        self.tarifa_hora = tarifa_hora
        self.disponible = disponible

        self.validar_parametros()

    def validar_parametros(self):
        if (
            not isinstance(self.especialidad, str)
            or not self.especialidad
        ):
            raise DatosInvalidosError(
                "La especialidad es obligatoria."
            )

        self.validar_tarifa(self.tarifa_hora)

        if not isinstance(self.disponible, bool):
            raise DatosInvalidosError(
                "La disponibilidad debe ser verdadera o falsa."
            )

    def calcular_costo(self, duracion):
        self.validar_duracion(duracion)

        if not self.disponible:
            raise ServicioNoDisponibleError(
                "La asesoria no esta disponible."
            )

        return self.tarifa_hora * duracion

    def describir(self):
        return (
            f"Asesoria especializada en {self.especialidad}. "
            f"Tarifa por hora: ${self.tarifa_hora:,.2f}"
        )

    def __str__(self):
        return f"Asesoria en {self.especialidad}"


class ReservaSala(Servicio):
    """Representa la reserva de una sala."""

    def __init__(
        self,
        nombre,
        tarifa_hora,
        capacidad,
        disponible=True
    ):
        self.nombre = nombre.strip() if isinstance(nombre, str) else nombre
        self.tarifa_hora = tarifa_hora
        self.capacidad = capacidad
        self.disponible = disponible

        self.validar_parametros()

    def validar_parametros(self):
        if not isinstance(self.nombre, str) or not self.nombre:
            raise DatosInvalidosError(
                "El nombre de la sala es obligatorio."
            )

        self.validar_tarifa(self.tarifa_hora)

        if (
            not isinstance(self.capacidad, int)
            or isinstance(self.capacidad, bool)
            or self.capacidad <= 0
        ):
            raise DatosInvalidosError(
                "La capacidad debe ser un entero mayor que cero."
            )

        if not isinstance(self.disponible, bool):
            raise DatosInvalidosError(
                "La disponibilidad debe ser verdadera o falsa."
            )

    def calcular_costo(self, duracion):
        self.validar_duracion(duracion)

        if not self.disponible:
            raise ServicioNoDisponibleError(
                f"La sala {self.nombre} no esta disponible."
            )

        return self.tarifa_hora * duracion

    def describir(self):
        return (
            f"Reserva de sala: {self.nombre}. "
            f"Capacidad: {self.capacidad} personas. "
            f"Tarifa por hora: ${self.tarifa_hora:,.2f}"
        )

    def __str__(self):
        return f"Sala {self.nombre}"
