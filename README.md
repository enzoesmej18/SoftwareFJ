# Software FJ

## Sistema Integral de Gestión de Clientes, Servicios y Reservas

Software FJ es una aplicación desarrollada en Python que permite gestionar clientes, servicios y reservas mediante programación orientada a objetos (POO).

El proyecto utiliza almacenamiento en memoria y un sistema de registro de eventos y errores mediante archivos de log. No requiere conexión a una base de datos.

## 1. Objetivo

Desarrollar un sistema que permita registrar clientes, administrar diferentes tipos de servicios, crear y gestionar reservas, calcular costos y controlar las operaciones mediante excepciones personalizadas.

## 2. Funcionalidades principales

- Registro y validación de clientes.
- Protección de datos mediante encapsulación.
- Prevención de documentos duplicados durante la ejecución.
- Gestión de servicios especializados.
- Creación, confirmación, cancelación y procesamiento de reservas.
- Cálculo de costos con impuestos y descuentos.
- Validación de disponibilidad y parámetros.
- Manejo de excepciones personalizadas.
- Registro de eventos y errores en archivos de log.
- Simulación de operaciones exitosas y fallidas.

## 3. Tipos de servicios

El sistema implementa tres servicios especializados:

- **AlquilerEquipo:** permite gestionar el alquiler de equipos.
- **AsesoriaEspecializada:** representa servicios de asesoría profesional.
- **ReservaSala:** permite gestionar la reserva de espacios según su capacidad.

Los servicios heredan de la clase abstracta `Servicio` e implementan sus propios métodos de validación, cálculo de costos y descripción.

## 4. Programación orientada a objetos

El proyecto aplica los siguientes conceptos:

- **Abstracción:** mediante las clases abstractas `Entidad` y `Servicio`.
- **Herencia:** mediante `Cliente` y los servicios especializados.
- **Encapsulación:** mediante atributos privados y propiedades.
- **Polimorfismo:** mediante la implementación especializada de métodos en los diferentes servicios.
- **Excepciones:** mediante clases personalizadas para controlar errores y operaciones no permitidas.

## 5. Estructura del proyecto

| Archivo | Descripción |
|---|---|
| `entidad.py` | Define la clase abstracta Entidad. |
| `cliente.py` | Gestiona los clientes y sus validaciones. |
| `servicios.py` | Define la clase Servicio y sus tres especializaciones. |
| `reservas.py` | Gestiona el ciclo de vida de las reservas. |
| `excepciones.py` | Contiene las excepciones personalizadas. |
| `logs.py` | Configura el registro de eventos y errores. |
| `main.py` | Ejecuta la simulación general del sistema. |
| `prueba_cliente.py` | Prueba las funcionalidades de clientes. |
| `prueba_servicios.py` | Prueba los servicios básicos. |
| `prueba_servicios_completa.py` | Prueba abstracción, herencia, polimorfismo y validaciones. |
| `prueba_integracion.py` | Comprueba la integración de los módulos. |
| `prueba_robustez.py` | Comprueba el manejo de errores. |
| `registros/` | Almacena el archivo de registro `software_fj.log`. |

## 6. Requisitos

- Python 3.10 o superior.
- Consola o terminal compatible.
- No requiere instalar paquetes externos para ejecutar las funcionalidades implementadas.

## 7. Ejecución

Ubicarse en la carpeta raíz del proyecto y ejecutar:

```bash
python main.py
```

El programa ejecuta una simulación general de 13 operaciones, incluyendo casos exitosos y situaciones de error controlado.

## 8. Ejecución de pruebas

Las pruebas pueden ejecutarse individualmente:

```bash
python prueba_cliente.py
python prueba_servicios.py
python prueba_servicios_completa.py
python prueba_integracion.py
python prueba_robustez.py
```

Para ejecutar la simulación general:

```bash
python main.py
```

## 9. Registro de eventos y errores

El sistema utiliza el módulo `logging` de Python para registrar las operaciones realizadas y los errores encontrados.

Los registros se almacenan en:

`registros/software_fj.log`

Se utilizan los niveles de registro `INFO` y `ERROR`, además del registro de excepciones con sus detalles técnicos.

## 10. Almacenamiento de información

Los datos de clientes, servicios y reservas se administran en memoria durante la ejecución del programa.

Por tanto, la información no se conserva automáticamente cuando se cierra la aplicación. Los registros de eventos y errores sí permanecen almacenados en el archivo de log.

## 11. Simulación general

La simulación de `main.py` contempla 13 operaciones que incluyen:

- Registro de clientes.
- Validación de información.
- Creación de servicios.
- Creación y confirmación de reservas.
- Cálculo y procesamiento de costos.
- Intentos de operaciones no permitidas.
- Gestión de servicios no disponibles.
- Cancelación de reservas.

El programa captura los errores esperados y continúa con las siguientes operaciones.

## 12. Autores

Proyecto académico desarrollado colaborativamente por el equipo de Software FJ.
