# 02 - Seguimiento de Línea con 1 Sensor

## La idea principal

Con un solo sensor de color, el robot sigue el **borde** de la línea (izquierdo o derecho). El sensor "baila" en zigzag entre el negro y el blanco, intentando mantenerse justo en el borde.

```
Vista desde arriba (siguiendo borde izquierdo):
                                    
  Blanco  │████ Negro ████│  Blanco
          │               │
    ←─ ·  │  · ─→         │
       ↑  │↗              │
       · ─┤               │
          │← ·             │
          │  ↑             │
          │  · ─→          │
          │     ↑          │
          │     · ──       │

  El sensor zigzaguea sobre el borde
```

## Nivel 1: Control ON/OFF (solo para entender, NO usar en competencia)

```python
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

hub = PrimeHub()
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
sensor = ColorSensor(Port.C)

NEGRO = 10
BLANCO = 90
UMBRAL = (NEGRO + BLANCO) / 2
VELOCIDAD = 200

while True:
    if sensor.reflection() < UMBRAL:
        left_motor.run(VELOCIDAD * 0.2)
        right_motor.run(VELOCIDAD)
    else:
        left_motor.run(VELOCIDAD)
        right_motor.run(VELOCIDAD * 0.2)
    wait(10)
```

**Problema:** El robot se sacude mucho porque solo tiene dos estados.

## Nivel 2: Control Proporcional (P) — Recomendado para empezar

La corrección es **proporcional** al error. Si se desvía poquito, corrige poquito.

### Fórmula
```
error = reflexión_actual - umbral
corrección = Kp × error
```

### Seguir borde IZQUIERDO con control P

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
sensor = ColorSensor(Port.C)

NEGRO = 10
BLANCO = 90
UMBRAL = (NEGRO + BLANCO) / 2
VELOCIDAD = 150
Kp = 1.5

while True:
    error = sensor.reflection() - UMBRAL
    correccion = Kp * error
    robot.drive(VELOCIDAD, correccion)
    wait(10)
```

### Seguir borde DERECHO: invertir el signo
```python
    error = UMBRAL - sensor.reflection()  # ← invertido
```

| Borde | Sensor ve blanco | Sensor ve negro |
|-------|-----------------|----------------|
| Izquierdo | error + → girar der | error - → girar izq |
| Derecho | error - → girar izq | error + → girar der |

## Nivel 3: Control PID — Para máxima precisión

- **P:** "¿Qué tan lejos estoy?"
- **I:** "¿Hace rato que estoy desviado?"
- **D:** "¿Estoy empeorando o mejorando?"

```
P = Kp × error
I = Ki × suma_de_errores
D = Kd × (error - error_anterior)
corrección = P + I + D
```

### Seguidor PID borde IZQUIERDO completo

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
sensor = ColorSensor(Port.C)

NEGRO = 10
BLANCO = 90
UMBRAL = (NEGRO + BLANCO) / 2
VELOCIDAD = 150
Kp = 1.5
Ki = 0.01
Kd = 5.0
error_anterior = 0
integral = 0
INTEGRAL_MAX = 100

while True:
    error = sensor.reflection() - UMBRAL
    P = Kp * error
    integral = integral + error
    if integral > INTEGRAL_MAX:
        integral = INTEGRAL_MAX
    elif integral < -INTEGRAL_MAX:
        integral = -INTEGRAL_MAX
    I = Ki * integral
    D = Kd * (error - error_anterior)
    error_anterior = error
    correccion = P + I + D
    robot.drive(VELOCIDAD, correccion)
    wait(10)
```

## Cómo ajustar Kp, Ki, Kd

1. **Empezá solo con P (Ki=0, Kd=0)** → Kp=0.5, subí hasta que oscile un poco
2. **Agregá D** → Kd=3.0, "frena" las oscilaciones
3. **Agregá I solo si es necesario** → Ki=0.005 (muy bajo!)

| Parámetro | Valor inicial | Rango típico |
|-----------|--------------|--------------|
| Kp | 1.5 | 0.5 - 4.0 |
| Ki | 0.01 | 0.0 - 0.05 |
| Kd | 5.0 | 1.0 - 15.0 |
| VELOCIDAD | 150 mm/s | 80 - 300 mm/s |

## Función reutilizable

```python
def seguir_linea_1sensor(sensor, robot, borde="izquierdo",
                          velocidad=150, kp=1.5, ki=0.01, kd=5.0,
                          negro=10, blanco=90):
    umbral = (negro + blanco) / 2
    if not hasattr(seguir_linea_1sensor, "error_ant"):
        seguir_linea_1sensor.error_ant = 0
        seguir_linea_1sensor.integral = 0
    if borde == "izquierdo":
        error = sensor.reflection() - umbral
    else:
        error = umbral - sensor.reflection()
    seguir_linea_1sensor.integral += error
    seguir_linea_1sensor.integral = max(-100, min(100, seguir_linea_1sensor.integral))
    P = kp * error
    I = ki * seguir_linea_1sensor.integral
    D = kd * (error - seguir_linea_1sensor.error_ant)
    seguir_linea_1sensor.error_ant = error
    correccion = P + I + D
    robot.drive(velocidad, correccion)
    return error
```

## Limitaciones con 1 sensor

- No detecta intersecciones
- No sabe si llegó al final de la línea
- Puede confundirse en curvas cerradas
- Velocidad limitada en curvas

**Para resolver → ver documentos de 2 y 3 sensores.**
