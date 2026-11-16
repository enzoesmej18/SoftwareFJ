
"""
Modulo que define la clase abstracta Entidad
del Software FJ.
"""

from abc import ABC, abstractmethod
from datetime import datetime


class Entidad(ABC):
    """Clase abstracta que representa una entidad general en el sistema."""

    contador = 0

    def __init__(self):
        Entidad.contador += 1

        self.__id = Entidad.contador
        self.__fecha_creacion = datetime.now()

    @property
    def id(self):
        """Devuelve el identificador de la entidad."""
        return self.__id

    @property
    def fecha_creacion(self):
        """Devuelve la fecha de creación."""
        return self.__fecha_creacion

    @abstractmethod
    def obtener_informacion(self):
        """Método que deben implementar las clases hijas."""
        pass
