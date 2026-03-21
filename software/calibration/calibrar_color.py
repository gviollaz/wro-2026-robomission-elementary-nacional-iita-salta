# ============================================================================
# Calibracion de sensor de color - WRO Elementary 2026
# ============================================================================
#
# Autor:       Gustavo Viollaz
# Herramienta: Claude Opus 4.6
# Fecha:       2026-03-21 20:00
# Rev:         v1
# Hardware:    Spike Prime, sensor de color
#
# DESCRIPCION:
#   Script para calibrar el sensor de color sobre el mat WRO.
#   Muestra en pantalla el color detectado y valores HSV.
#   Usar para verificar deteccion de las 6 notas.
#
# ============================================================================

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub()
sensor = ColorSensor(Port.D)

print("=== CALIBRACION SENSOR DE COLOR ===")
print("Colocar el sensor sobre cada nota y presionar boton central.")
print("")

colores_notas = ["ROJA", "AZUL", "VERDE", "AMARILLA", "BLANCA", "NEGRA"]

for nombre in colores_notas:
    print("--- Posicionar sensor sobre nota " + nombre + " ---")
    print("Presionar boton central del hub cuando este listo...")

    while not hub.buttons.pressed():
        wait(50)
    while hub.buttons.pressed():
        wait(50)

    color = sensor.color()
    hsv = sensor.hsv()
    reflection = sensor.reflection()

    print("  Color detectado: " + str(color))
    print("  HSV: H=" + str(hsv.h) + ", S=" + str(hsv.s) + ", V=" + str(hsv.v))
    print("  Reflexion: " + str(reflection) + "%")
    print("")

print("=== CALIBRACION COMPLETA ===")
print("Anotar los valores HSV para ajustar la deteccion en el programa.")
