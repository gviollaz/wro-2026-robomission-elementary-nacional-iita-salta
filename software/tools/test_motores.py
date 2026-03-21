# ============================================================================
# Test basico de motores - WRO Elementary 2026
# ============================================================================
#
# Autor:       Gustavo Viollaz
# Herramienta: Claude Opus 4.6
# Fecha:       2026-03-21 20:00
# Rev:         v1
# Hardware:    Spike Prime, 2 motores grandes, 1 motor mediano
#
# DESCRIPCION:
#   Test rapido para verificar que todos los motores funcionan.
#   El robot avanza, retrocede, gira, y mueve la garra.
#
# ============================================================================

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()

print("=== TEST DE MOTORES ===")

motor_izq = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_der = Motor(Port.B)
robot = DriveBase(motor_izq, motor_der, wheel_diameter=56, axle_track=112)

print("1. Avanzar 200mm...")
robot.straight(200)
wait(500)

print("2. Retroceder 200mm...")
robot.straight(-200)
wait(500)

print("3. Girar 90 derecha...")
robot.turn(90)
wait(500)

print("4. Girar 90 izquierda...")
robot.turn(-90)
wait(500)

print("5. Motor garra (Puerto C)...")
try:
    motor_garra = Motor(Port.C)
    motor_garra.run_angle(300, 90, then=Stop.HOLD)
    wait(500)
    motor_garra.run_angle(300, -90, then=Stop.HOLD)
    print("   OK")
except:
    print("   No detectado en Puerto C")

print("=== TEST COMPLETO ===")
hub.speaker.beep(frequency=1000, duration=500)
