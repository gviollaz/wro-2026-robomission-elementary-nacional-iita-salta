# 03 - Seguimiento de Línea con 2 Sensores

## ¿Por qué usar 2 sensores?

Con 2 sensores separados, el robot puede seguir la línea más estable, detectar intersecciones, alinearse perpendicular, y saber si llegó al final.

## Sensores "a caballo" de la línea

```
        [Sensor L]  [Sensor R]
            ○          ○
   Blanco   │██ NEGRO ██│   Blanco
```

Ambos ven blanco cuando el robot está centrado.

## Método diferencial

```
error = sensor_izq.reflection() - sensor_der.reflection()
```

- error = 0 → ambos ven igual → ir derecho
- error + → desviado a la derecha → corregir izquierda
- error - → desviado a la izquierda → corregir derecha

```python
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)
sensor_izq = ColorSensor(Port.C)
sensor_der = ColorSensor(Port.D)

VELOCIDAD = 200
Kp = 0.8
Ki = 0.005
Kd = 4.0
error_anterior = 0
integral = 0

while True:
    error = sensor_izq.reflection() - sensor_der.reflection()
    integral = max(-100, min(100, integral + error))
    P = Kp * error
    I = Ki * integral
    D = Kd * (error - error_anterior)
    error_anterior = error
    correccion = P + I + D
    robot.drive(VELOCIDAD, correccion)
    wait(10)
```

## Detección de intersecciones

```python
UMBRAL_NEGRO = 25

def detectar_interseccion(sensor_izq, sensor_der):
    izq = sensor_izq.reflection() < UMBRAL_NEGRO
    der = sensor_der.reflection() < UMBRAL_NEGRO
    if izq and der: return "ambas"
    elif izq: return "izquierda"
    elif der: return "derecha"
    else: return "ninguna"
```

## Seguir y contar intersecciones

```python
def seguir_hasta_interseccion(robot, sensor_izq, sensor_der,
                               lado="izquierda", numero=1,
                               velocidad=150, kp=0.8, kd=4.0):
    UMBRAL_NEGRO = 25
    conteo = 0
    en_interseccion = False
    error_anterior = 0
    while True:
        refl_izq = sensor_izq.reflection()
        refl_der = sensor_der.reflection()
        error = refl_izq - refl_der
        D = kd * (error - error_anterior)
        error_anterior = error
        correccion = kp * error + D
        robot.drive(velocidad, correccion)
        if lado == "izquierda":
            det = refl_izq < UMBRAL_NEGRO
        elif lado == "derecha":
            det = refl_der < UMBRAL_NEGRO
        else:
            det = refl_izq < UMBRAL_NEGRO and refl_der < UMBRAL_NEGRO
        if det and not en_interseccion:
            conteo += 1
            en_interseccion = True
            if conteo >= numero:
                robot.stop()
                return conteo
        elif not det:
            en_interseccion = False
        wait(10)
```

## Anti-rebote (debounce)

La variable `en_interseccion` evita contar la misma intersección varias veces.

```
Sin debounce: entra negro → conteo=1, sigue negro → conteo=2 ¡ERROR!
Con debounce: entra negro → conteo=1 + flag=True, sigue negro → flag ya True → no contar
```

## Alineación (squaring)

```python
def alinear_en_linea(left_motor, right_motor, sensor_izq, sensor_der, velocidad=100):
    UMBRAL_NEGRO = 25
    izq_ok = False
    der_ok = False
    left_motor.run(velocidad)
    right_motor.run(velocidad)
    while not (izq_ok and der_ok):
        if sensor_izq.reflection() < UMBRAL_NEGRO and not izq_ok:
            left_motor.stop()
            izq_ok = True
        if sensor_der.reflection() < UMBRAL_NEGRO and not der_ok:
            right_motor.stop()
            der_ok = True
        wait(10)
    left_motor.stop()
    right_motor.stop()
```

## Resumen

| Capacidad | 2 Sensores |
|-----------|------------|
| Seguir línea | ⭐⭐⭐ Excelente |
| Detectar intersecciones | ⭐⭐ Buena |
| Alinearse | ⭐⭐⭐ Excelente |
| Seguir + detectar simultáneo | ⚠️ Parcial |

**Limitación:** Puede confundir curvas con intersecciones. Para resolver → ver 3 sensores.
