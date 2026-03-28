# ============================================================================
# robot_lib.py — Biblioteca de funciones para WRO Elementary 2026
# ============================================================================
#
# Equipo:      Robot Rockstars — IITA Salta
# Categoría:   WRO RoboMission Elementary 2026
# Uso:         Importar desde programas de bloques vía "External Task"
# Generado:    Claude Opus 4.6 — 2026-03-28
#
# VALORES DE REFERENCIA: ver hardware/robot-definition.md
#
# CÓMO USAR DESDE BLOQUES:
#   1. En Pybricks, crear este archivo como proyecto Python "robot_lib"
#   2. En tu proyecto de bloques, usar bloque "Import from: robot_lib"
#   3. Seleccionar las funciones que necesitás
#   4. Llamarlas con el bloque "Run Task"
#
# ============================================================================

from pybricks.parameters import Stop, Color
from pybricks.tools import wait

# ============================================================================
# CONSTANTES (actualizar desde hardware/robot-definition.md)
# ============================================================================

NEGRO = 10          # Reflexión sobre línea negra (CALIBRAR)
BLANCO = 90         # Reflexión sobre fondo blanco (CALIBRAR)
UMBRAL = 50         # (NEGRO + BLANCO) / 2
UMBRAL_CRUCE = 25   # Para detectar intersecciones

Kp = 1.5            # Ganancia proporcional (CALIBRAR)
Ki = 0.0            # Ganancia integral (empezar en 0)
Kd = 5.0            # Ganancia derivativa (CALIBRAR)
INTEGRAL_MAX = 100  # Límite anti-windup

# Variables internas del PID
_err_ant = 0
_integral = 0


# ============================================================================
# FUNCIONES DE CONTROL
# ============================================================================

def reset_pid():
    """Resetear estado del PID. Llamar al cambiar de tramo."""
    global _err_ant, _integral
    _err_ant = 0
    _integral = 0


# ============================================================================
# PERFILES DE VELOCIDAD
# ============================================================================

def perfil_preciso(robot):
    """Velocidad baja para posicionamiento exacto."""
    robot.settings(120, 80, 80, 60)

def perfil_normal(robot):
    """Velocidad estándar para navegación."""
    robot.settings(200, 150, 120, 80)

def perfil_rapido(robot):
    """Velocidad alta para tramos largos rectos."""
    robot.settings(350, 200, 150, 100)


# ============================================================================
# SEGUIMIENTO DE LÍNEA
# ============================================================================

def seguir_linea(sensor, robot, borde="izquierdo", vel=150, kp=None, kd=None):
    """
    Un ciclo de seguimiento PD. Llamar dentro de un while loop.
    
    sensor: ColorSensor configurado en el Setup de bloques
    robot:  DriveBase configurado en el Setup de bloques
    borde:  "izquierdo" o "derecho"
    vel:    velocidad en mm/s
    kp/kd:  si None usa los valores globales calibrados
    """
    global _err_ant
    _kp = kp if kp is not None else Kp
    _kd = kd if kd is not None else Kd

    if borde == "izquierdo":
        err = sensor.reflection() - UMBRAL
    else:
        err = UMBRAL - sensor.reflection()

    cor = _kp * err + _kd * (err - _err_ant)
    _err_ant = err
    robot.drive(vel, cor)


def ir_a_cruce(sensor, robot, lado="izquierda", n=1,
               borde="izquierdo", vel=150):
    """
    Sigue la línea y se detiene en la N-ésima intersección.
    
    sensor: ColorSensor (el que sigue la línea Y detecta cruces)
    robot:  DriveBase
    lado:   "izquierda", "derecha" o "ambas"
    n:      en cuál intersección parar (1, 2, 3...)
    borde:  qué borde seguir
    vel:    velocidad mm/s
    
    NOTA: Con 1 solo sensor, la detección de cruces es limitada.
    El sensor detecta negro extendido (más ancho que la línea normal)
    como indicador de intersección.
    """
    reset_pid()
    conteo = 0
    en_cruce = False
    lecturas_negro = 0

    while True:
        refl = sensor.reflection()

        # Seguimiento PD
        seguir_linea(sensor, robot, borde, vel)

        # Detección de cruce: el sensor ve negro sostenido
        # (más de 3 lecturas consecutivas bajo UMBRAL_CRUCE)
        if refl < UMBRAL_CRUCE:
            lecturas_negro += 1
        else:
            if lecturas_negro > 3 and not en_cruce:
                conteo += 1
                en_cruce = True
                if conteo >= n:
                    robot.stop()
                    return conteo
            lecturas_negro = 0
            en_cruce = False

        wait(10)


def seguir_y_girar(sensor, robot, lado_giro="izquierda",
                    en_cruce_n=1, borde="izquierdo", vel=150):
    """
    Sigue línea, llega a la intersección N, y gira para tomar la nueva línea.
    """
    ir_a_cruce(sensor, robot, lado_giro, en_cruce_n, borde, vel)
    robot.straight(40)
    if lado_giro == "izquierda":
        robot.turn(-90)
    else:
        robot.turn(90)
    robot.straight(25)
    reset_pid()


def seguir_hasta_fin(sensor, robot, borde="izquierdo", vel=120):
    """
    Sigue la línea hasta que se termina (sensor ve blanco sostenido).
    """
    reset_pid()
    contador_blanco = 0

    while True:
        seguir_linea(sensor, robot, borde, vel)

        if sensor.reflection() > 70:
            contador_blanco += 1
            if contador_blanco > 5:
                robot.stop()
                return
        else:
            contador_blanco = 0

        wait(10)


# ============================================================================
# BÚSQUEDA Y ALINEACIÓN
# ============================================================================

def buscar_linea(sensor, robot, max_mm=500, vel=120):
    """
    Avanza derecho hasta encontrar una línea negra.
    Retorna True si la encontró, False si recorrió max_mm sin encontrar.
    """
    robot.reset()
    robot.drive(vel, 0)

    while True:
        if sensor.reflection() < UMBRAL_CRUCE:
            robot.stop()
            return True
        if robot.distance() > max_mm:
            robot.stop()
            return False
        wait(10)


def alinear(sensor_izq, sensor_der, motor_izq, motor_der, vel=80):
    """
    Alinea el robot perpendicular a una línea transversal.
    Requiere 2 sensores de color (puertos E y F).
    
    Si tu robot solo tiene 1 sensor, no usar esta función.
    """
    izq_ok = False
    der_ok = False
    motor_izq.run(vel)
    motor_der.run(vel)

    while not (izq_ok and der_ok):
        if sensor_izq.reflection() < UMBRAL_CRUCE and not izq_ok:
            motor_izq.stop()
            izq_ok = True
        if sensor_der.reflection() < UMBRAL_CRUCE and not der_ok:
            motor_der.stop()
            der_ok = True
        wait(10)

    motor_izq.stop()
    motor_der.stop()


# ============================================================================
# MOVIMIENTO PRECISO
# ============================================================================

def avanzar_preciso(robot, distancia_mm):
    """
    Avanza con frenado suave: rápido la mayor parte, lento al final.
    """
    ZONA_FRENADO = 50
    if distancia_mm > ZONA_FRENADO * 2:
        perfil_normal(robot)
        robot.straight(distancia_mm - ZONA_FRENADO)
        perfil_preciso(robot)
        robot.straight(ZONA_FRENADO)
    else:
        perfil_preciso(robot)
        robot.straight(distancia_mm)
    perfil_normal(robot)


def girar_preciso(robot, angulo):
    """Gira con máxima precisión (perfil lento)."""
    perfil_preciso(robot)
    robot.turn(angulo)
    perfil_normal(robot)


# ============================================================================
# GIROSCOPIO
# ============================================================================

def init_gyro(hub):
    """
    Espera a que el giroscopio se calibre.
    Muestra luz roja mientras calibra, verde cuando está listo.
    Llamar al inicio del programa, ANTES de mover el robot.
    """
    hub.imu.settings(
        angular_velocity_threshold=5,
        acceleration_threshold=50
    )
    hub.light.on(Color.RED)
    while not hub.imu.ready():
        wait(100)
    hub.light.on(Color.GREEN)
    wait(300)
    hub.light.off()


def recalibrar(robot):
    """
    Recalibra el giroscopio. El robot DEBE estar quieto.
    Llamar antes de secuencias críticas de giros.
    """
    robot.stop()
    wait(1500)


# ============================================================================
# MECANISMO (GARRA)
# ============================================================================

def garra_abrir(motor, angulo=90, vel=300):
    """Abre la garra."""
    motor.run_angle(vel, angulo, then=Stop.HOLD)

def garra_cerrar(motor, angulo=90, vel=300):
    """Cierra la garra."""
    motor.run_angle(vel, -angulo, then=Stop.HOLD)


# ============================================================================
# HELPER: función universal para llamar desde bloques con un solo import
# ============================================================================

def fn(name, *args, **kwargs):
    """
    Helper para llamar cualquier función por nombre.
    Útil si el bloque External Task solo permite importar UNA función.
    
    Ejemplo desde bloques:
        Import from robot_lib: fn
        Run Task: fn("ir_a_cruce", sensor, robot, "derecha", 2)
    """
    return globals()[name](*args, **kwargs)
