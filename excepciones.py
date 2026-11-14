
"""
Excepciones personalizadas del sistema Software FJ.
"""


class ErrorSoftwareFJ(Exception):
    """Excepción base del sistema."""
    pass


class DatosInvalidosError(ErrorSoftwareFJ):
    """Error cuando los datos ingresados no son válidos."""
    pass


class ClienteNoEncontradoError(ErrorSoftwareFJ):
    """Error cuando no se encuentra un cliente."""
    pass


class ServicioNoDisponibleError(ErrorSoftwareFJ):
    """Error cuando un servicio no está disponible."""
    pass


class ReservaInvalidaError(ErrorSoftwareFJ):
    """Error cuando una reserva no cumple los requisitos."""
    pass


class OperacionNoPermitidaError(ErrorSoftwareFJ):
    """Error cuando se intenta una operación no permitida."""
    pass


class ErrorCalculoError(ErrorSoftwareFJ):
    """Error durante el cálculo de costos."""
    pass
