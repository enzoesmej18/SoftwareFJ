
"""
Modulo que define la clase Cliente
del sistema Software FJ.
"""

import re

from entidad import Entidad
from excepciones import DatosInvalidosError
from logs import registrar_evento


class Cliente(Entidad):
    """Representa un cliente registrado en Software FJ."""

    # Almacena los documentos registrados durante la ejecución.
    documentos_registrados = set()

    def __init__(self, nombre, documento, correo, telefono, direccion):

        # Validamos los datos antes de crear la entidad.
        self.__nombre = self._validar_nombre(nombre)
        self.__documento = self._validar_documento(documento)
        self.__correo = self._validar_correo(correo)
        self.__telefono = self._validar_telefono(telefono)
        self.__direccion = self._validar_direccion(direccion)

        # Evitamos documentos duplicados.
        if self.__documento in Cliente.documentos_registrados:
            raise DatosInvalidosError(
                "Ya existe un cliente con ese documento."
            )

        # Inicializamos los atributos heredados de Entidad.
        super().__init__()

        # Registramos el documento después de validar los datos.
        Cliente.documentos_registrados.add(self.__documento)

        registrar_evento(
            f"Cliente {self.id} registrado correctamente."
        )

    @staticmethod
    def _validar_nombre(nombre):
        """Valida que el nombre contenga caracteres permitidos."""

        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError(
                "El nombre del cliente es obligatorio."
            )

        nombre = nombre.strip()

        if not re.fullmatch(
            r"[^\W\d_]+(?:[ '\-][^\W\d_]+)*",
            nombre,
            flags=re.UNICODE
        ):
            raise DatosInvalidosError(
                "El nombre contiene caracteres no permitidos."
            )

        return nombre

    @staticmethod
    def _validar_documento(documento):
        """Valida el documento de identidad."""

        if not isinstance(documento, str):
            raise DatosInvalidosError(
                "El documento debe ingresarse como texto."
            )

        documento = documento.strip()

        if not re.fullmatch(r"[A-Za-z0-9-]{5,20}", documento):
            raise DatosInvalidosError(
                "El documento debe tener entre 5 y 20 caracteres "
                "alfanuméricos o guiones."
            )

        return documento.upper()

    @staticmethod
    def _validar_correo(correo):
        """Valida el formato del correo electrónico."""

        if not isinstance(correo, str) or not correo.strip():
            raise DatosInvalidosError(
                "El correo electrónico es obligatorio."
            )

        correo = correo.strip().lower()

        patron = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        if not re.fullmatch(patron, correo):
            raise DatosInvalidosError(
                "El formato del correo electrónico no es válido."
            )

        return correo

    @staticmethod
    def _validar_telefono(telefono):
        """Valida el número telefónico."""

        if not isinstance(telefono, str) or not telefono.strip():
            raise DatosInvalidosError(
                "El teléfono es obligatorio."
            )

        telefono = telefono.strip()

        if not re.fullmatch(r"\+?[\d\s()-]+", telefono):
            raise DatosInvalidosError(
                "El teléfono contiene caracteres no permitidos."
            )

        cantidad_digitos = sum(
            caracter.isdigit() for caracter in telefono
        )

        if not 7 <= cantidad_digitos <= 15:
            raise DatosInvalidosError(
                "El teléfono debe contener entre 7 y 15 dígitos."
            )

        return telefono

    @staticmethod
    def _validar_direccion(direccion):
        """Valida la dirección del cliente."""

        if not isinstance(direccion, str) or not direccion.strip():
            raise DatosInvalidosError(
                "La dirección del cliente es obligatoria."
            )

        return direccion.strip()

    @property
    def nombre(self):
        return self.__nombre

    @property
    def documento(self):
        return self.__documento

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    @property
    def direccion(self):
        return self.__direccion

    def obtener_informacion(self):
        """Devuelve la información general del cliente."""

        return (
            f"ID: {self.id}\n"
            f"Nombre: {self.nombre}\n"
            f"Documento: {self.documento}\n"
            f"Correo: {self.correo}\n"
            f"Teléfono: {self.telefono}\n"
            f"Dirección: {self.direccion}\n"
            f"Fecha de creación: {self.fecha_creacion}"
        )

    def __str__(self):
        return f"Cliente {self.id}: {self.nombre}"
