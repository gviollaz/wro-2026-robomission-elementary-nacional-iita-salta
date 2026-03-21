# ============================================================================
# Configuracion base del robot - WRO Elementary 2026 "Robot Rockstars"
# ============================================================================
#
# Autor:       Gustavo Viollaz
# Herramienta: Claude Opus 4.6
# Fecha:       2026-03-21 20:00
# Rev:         v1
# Hardware:    Spike Prime, 2 motores grandes, 1 motor mediano, sensor color
#
# DESCRIPCION:
#   Configuracion base del robot: hub, motores, sensores y DriveBase.
#   Importar este archivo desde los programas de mision.
#
# ============================================================================

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Stop, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# --- HUB ---
hub = PrimeHub()

# --- MOTORES ---
motor_izq = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_der = Motor(Port.B)
motor_garra = Motor(Port.C)

# --- SENSORES ---
sensor_color = ColorSensor(Port.D)

# --- DRIVEBASE ---
# MEDIR CON REGLA Y AJUSTAR ESTOS VALORES
WHEEL_DIAMETER = 56    # mm - diametro de la rueda
AXLE_TRACK = 112       # mm - distancia entre centros de ruedas

robot = DriveBase(motor_izq, motor_der,
    wheel_diameter=WHEEL_DIAMETER,
    axle_track=AXLE_TRACK)

# --- VELOCIDADES ---
def velocidad_normal():
    robot.settings(
        straight_speed=200,
        straight_acceleration=100,
        turn_rate=100,
        turn_acceleration=50
    )

def velocidad_lenta():
    robot.settings(
        straight_speed=100,
        straight_acceleration=50,
        turn_rate=50,
        turn_acceleration=30
    )

# --- GARRA ---
def garra_abrir():
    motor_garra.run_angle(300, 90, then=Stop.HOLD)

def garra_cerrar():
    motor_garra.run_angle(300, -90, then=Stop.HOLD)

# Inicializar
velocidad_normal()
