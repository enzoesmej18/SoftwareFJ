
"""
Punto de entrada principal de Software FJ.

Sistema integral de gestion de clientes,
servicios y reservas.
"""

from cliente import Cliente
from servicios import (
    AlquilerEquipo,
    AsesoriaEspecializada,
    ReservaSala
)
from reservas import Reserva

from excepciones import (
    DatosInvalidosError,
    OperacionNoPermitidaError,
    ServicioNoDisponibleError
)

from logs import registrar_evento, registrar_error


def mostrar_titulo():
    """Muestra la informacion inicial del sistema."""

    print("=" * 60)
    print("       SOFTWARE FJ")
    print("Sistema de gestion de clientes, servicios y reservas")
    print("=" * 60)


def ejecutar_operacion(numero, descripcion, funcion):
    """
    Ejecuta una operacion y captura los errores
    para evitar que se interrumpa la simulacion.
    """

    print(f"\nOPERACION {numero}: {descripcion}")

    try:
        resultado = funcion()

        if resultado is not None:
            print(resultado)

        print("Resultado: EXITOSO")
        registrar_evento(
            f"Operacion {numero} exitosa: {descripcion}"
        )

    except Exception as error:
        print(f"Resultado: ERROR CONTROLADO")
        print(f"Detalle: {error}")

        registrar_error(
            f"Operacion {numero} fallida: {descripcion}. "
            f"Detalle: {error}"
        )


def ejecutar_simulacion():
    """Ejecuta las operaciones generales del sistema."""

    mostrar_titulo()

    clientes = {}
    servicios = {}
    reservas = {}

    # Operacion 1: Registrar un cliente.
    def registrar_cliente():
        cliente = Cliente(
            "Laura Martinez",
            "1001001001",
            "laura@gmail.com",
            "3104567890",
            "Calle 20 # 15-30"
        )

        clientes["laura"] = cliente
        return f"Cliente registrado: {cliente}"

    ejecutar_operacion(
        1,
        "Registrar cliente",
        registrar_cliente
    )

    # Operacion 2: Registrar un segundo cliente.
    def registrar_segundo_cliente():
        cliente = Cliente(
            "Carlos Rodriguez",
            "1001001002",
            "carlos@gmail.com",
            "3004567890",
            "Carrera 15 # 20-10"
        )

        clientes["carlos"] = cliente
        return f"Cliente registrado: {cliente}"

    ejecutar_operacion(
        2,
        "Registrar segundo cliente",
        registrar_segundo_cliente
    )

    # Operacion 3: Intentar registrar un cliente invalido.
    def registrar_cliente_invalido():
        Cliente(
            "",
            "1001001003",
            "correo_invalido",
            "123",
            "Calle 10"
        )

    ejecutar_operacion(
        3,
        "Registrar cliente con datos invalidos",
        registrar_cliente_invalido
    )

    # Operacion 4: Crear alquiler de equipo.
    def crear_alquiler():
        servicio = AlquilerEquipo(
            "Camara profesional",
            25000
        )

        servicios["equipo"] = servicio
        return servicio.describir()

    ejecutar_operacion(
        4,
        "Crear servicio de alquiler de equipo",
        crear_alquiler
    )

    # Operacion 5: Crear asesoria especializada.
    def crear_asesoria():
        servicio = AsesoriaEspecializada(
            "Diseno multimedia",
            50000
        )

        servicios["asesoria"] = servicio
        return servicio.describir()

    ejecutar_operacion(
        5,
        "Crear servicio de asesoria",
        crear_asesoria
    )

    # Operacion 6: Crear reserva de sala.
    def crear_sala():
        servicio = ReservaSala(
            "Sala multimedia",
            80000,
            20
        )

        servicios["sala"] = servicio
        return servicio.describir()

    ejecutar_operacion(
        6,
        "Crear servicio de reserva de sala",
        crear_sala
    )

    # Operacion 7: Crear una reserva de alquiler.
    def crear_reserva():
        reserva = Reserva(
            clientes["laura"],
            servicios["equipo"],
            3
        )

        reservas["reserva1"] = reserva

        return (
            f"Reserva creada: {reserva.id}. "
            f"Estado: {reserva.estado}"
        )

    ejecutar_operacion(
        7,
        "Crear reserva de alquiler de equipo",
        crear_reserva
    )

    # Operacion 8: Confirmar la reserva.
    def confirmar_reserva():
        reserva = reservas["reserva1"]
        reserva.confirmar()

        return f"Estado actual: {reserva.estado}"

    ejecutar_operacion(
        8,
        "Confirmar reserva",
        confirmar_reserva
    )

    # Operacion 9: Calcular costo con impuesto y descuento.
    def calcular_costo():
        reserva = reservas["reserva1"]

        costo = reserva.calcular_costo(
            impuesto=0.19,
            descuento=0.10
        )

        return f"Costo total: ${costo:,.2f}"

    ejecutar_operacion(
        9,
        "Calcular costo con impuesto y descuento",
        calcular_costo
    )

    # Operacion 10: Procesar la reserva.
    def procesar_reserva():
        reserva = reservas["reserva1"]

        costo = reserva.procesar(
            impuesto=0.19,
            descuento=0.10
        )

        return (
            f"Costo procesado: ${costo:,.2f}. "
            f"Estado: {reserva.estado}"
        )

    ejecutar_operacion(
        10,
        "Procesar reserva confirmada",
        procesar_reserva
    )

    # Operacion 11: Intentar cancelar una reserva procesada.
    def cancelar_reserva_procesada():
        reservas["reserva1"].cancelar()

    ejecutar_operacion(
        11,
        "Intentar cancelar una reserva procesada",
        cancelar_reserva_procesada
    )

    # Operacion 12: Crear una reserva con un servicio no disponible.
    def crear_reserva_no_disponible():
        equipo = AlquilerEquipo(
            "Proyector",
            30000,
            disponible=False
        )

        reserva = Reserva(
            clientes["carlos"],
            equipo,
            2
        )

        reservas["reserva2"] = reserva

        reserva.confirmar()

        return reserva.procesar()

    ejecutar_operacion(
        12,
        "Intentar procesar un servicio no disponible",
        crear_reserva_no_disponible
    )

    # Operacion 13: Crear y cancelar una reserva pendiente.
    def cancelar_reserva_pendiente():
        reserva = Reserva(
            clientes["carlos"],
            servicios["sala"],
            2
        )

        reservas["reserva3"] = reserva

        reserva.cancelar()

        return f"Reserva {reserva.id}: {reserva.estado}"

    ejecutar_operacion(
        13,
        "Cancelar una reserva pendiente",
        cancelar_reserva_pendiente
    )

    # Resumen final.
    print("\n" + "=" * 60)
    print("RESUMEN DE LA SIMULACION")
    print("=" * 60)

    print(f"Clientes registrados: {len(clientes)}")
    print(f"Servicios creados: {len(servicios)}")
    print(f"Reservas creadas: {len(reservas)}")
    print("Operaciones ejecutadas: 13")

    print("\nLa simulacion ha finalizado.")
    print("El sistema continua funcionando ante errores.")

    registrar_evento(
        "Simulacion general de Software FJ finalizada."
    )


if __name__ == "__main__":
    ejecutar_simulacion()
