
"""
Modulo para gestionar las reservas de Software FJ.
"""

import math

from excepciones import (
    DatosInvalidosError,
    ReservaInvalidaError,
    OperacionNoPermitidaError,
    ErrorCalculoError,
    ServicioNoDisponibleError
)

from logs import (
    registrar_evento,
    registrar_error,
    registrar_excepcion
)


class Reserva:
    """Representa una reserva de un cliente para un servicio."""

    contador = 0

    def __init__(self, cliente, servicio, duracion):
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = "Pendiente"
        self._costo_total = 0.0

        self._validar_datos()

        Reserva.contador += 1
        self._id = Reserva.contador

        registrar_evento(
            f"Reserva {self._id} creada correctamente."
    )

    def _validar_datos(self):
        """Comprueba que los datos de la reserva sean correctos."""

        if self._cliente is None:
            raise DatosInvalidosError(
            "La reserva debe tener un cliente."
        )

        if self._servicio is None:
            raise DatosInvalidosError(
            "La reserva debe tener un servicio."
        )

        if (
            not isinstance(self._duracion, (int, float))
            or isinstance(self._duracion, bool)
            or not math.isfinite(self._duracion)
            or self._duracion <= 0
    ):
            raise DatosInvalidosError(
                "La duración debe ser un número mayor que cero."
        )

        if not callable(
        getattr(self._servicio, "calcular_costo", None)
    ):
            raise DatosInvalidosError(
                "El servicio no tiene un método calcular_costo válido."
        )

    @property
    def id(self):
        return self._id

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def duracion(self):
        return self._duracion

    @property
    def estado(self):
        return self._estado

    @property
    def costo_total(self):
        return self._costo_total

    def confirmar(self):
        """Confirma una reserva pendiente."""

        if self._estado != "Pendiente":
            raise OperacionNoPermitidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self._estado = "Confirmada"

        registrar_evento(
            f"Reserva {self._id} confirmada."
        )

    def cancelar(self):
        """Cancela una reserva pendiente o confirmada."""

        if self._estado not in ("Pendiente", "Confirmada"):
            raise OperacionNoPermitidaError(
                "No se puede cancelar una reserva procesada o cancelada."
            )

        self._estado = "Cancelada"

        registrar_evento(
            f"Reserva {self._id} cancelada."
        )

    def calcular_costo(self, impuesto=0.0, descuento=0.0):
        """Calcula el costo final con impuestos y descuentos."""

        if (
            not isinstance(impuesto, (int, float))
            or isinstance(impuesto, bool)
            or not math.isfinite(impuesto)
            or not 0 <= impuesto <= 1
        ):
            raise DatosInvalidosError(
                "El impuesto debe ser un número entre 0 y 1."
        )

        if (
            not isinstance(descuento, (int, float))
            or isinstance(descuento, bool)
            or not math.isfinite(descuento)
            or not 0 <= descuento <= 1
        ):
            raise DatosInvalidosError(
                "El descuento debe ser un número entre 0 y 1."
            )

        try:
            costo_base = self._servicio.calcular_costo(
                self._duracion
            )

            if (
                not isinstance(costo_base, (int, float))
                or isinstance(costo_base, bool)
                or not math.isfinite(costo_base)
                or costo_base < 0
            ):
                raise ValueError(
                    "El servicio devolvió un costo inválido."
                )

            total = costo_base * (1 + impuesto)
            total = total * (1 - descuento)

            if not math.isfinite(total):
                raise ValueError(
                    "El costo final no es válido."
                )

            return round(total, 2)

        except ServicioNoDisponibleError:
            raise

        except Exception as error:
            registrar_excepcion(
                f"Error calculando el costo de la reserva {self._id}."
            )

            raise ErrorCalculoError(
                "No fue posible calcular el costo de la reserva."
            ) from error

    def procesar(self, impuesto=0.0, descuento=0.0):
        """Procesa una reserva confirmada."""

        if self._estado != "Confirmada":
            raise OperacionNoPermitidaError(
                "La reserva debe estar confirmada para procesarse."
            )

        try:
            self._costo_total = self.calcular_costo(
                impuesto,
                descuento
            )

            self._estado = "Procesada"

            registrar_evento(
                f"Reserva {self._id} procesada. "
                f"Costo total: {self._costo_total}"
            )

            return self._costo_total

        except Exception as error:
            registrar_error(
                f"No se pudo procesar la reserva "
                f"{self._id}: {error}"
            )

            raise
