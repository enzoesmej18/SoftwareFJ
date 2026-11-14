
"""
Modulo de registro de eventos y errores de Software FJ.
"""

import logging
import os

# Crear la carpeta de registros si no existe
os.makedirs("registros", exist_ok=True)

# Configurar el sistema de registros
logging.basicConfig(
    filename="registros/software_fj.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger("SoftwareFJ")


def registrar_evento(mensaje):
    """Registra una operación realizada correctamente."""
    logger.info(mensaje)


def registrar_error(mensaje):
    """Registra un error ocurrido en el sistema."""
    logger.error(mensaje)


def registrar_excepcion(mensaje):
    """Registra un error junto con sus detalles técnicos."""
    logger.exception(mensaje)
