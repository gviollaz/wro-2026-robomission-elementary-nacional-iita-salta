# 04 - Seguimiento de Línea con 3 Sensores

## ¿Por qué 3 sensores?

Con 3 sensores tenés **lo mejor de ambos mundos**: el sensor central sigue el borde (navegación suave), los laterales detectan intersecciones (conteo confiable).

```
   [S_Izq]   [S_Centro]   [S_Der]
      ○          ○           ○
 Blanco  │████ NEGRO ████│  Blanco
```

## Configuración física

- Sensor central: sobre el borde de la línea
- Laterales: ~15-20mm a cada lado, sobre blanco
- Distancia al piso: 5-15mm
- Líneas WRO: ~20mm de ancho

## Algoritmo completo

```python
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)
sensor_izq = ColorSensor(Port.C)
sensor_centro = ColorSensor(Port.D)
sensor_der = ColorSensor(Port.E)

NEGRO = 10
BLANCO = 90
UMBRAL = (NEGRO + BLANCO) / 2
UMBRAL_INTERSECCION = 25
VELOCIDAD = 180
Kp = 1.5
Ki = 0.01
Kd = 5.0
error_anterior = 0
integral = 0

def leer_todo():
    return {
        "izq": sensor_izq.reflection(),
        "centro": sensor_centro.reflection(),
        "der": sensor_der.reflection(),
        "inter_izq": sensor_izq.reflection() < UMBRAL_INTERSECCION,
        "inter_der": sensor_der.reflection() < UMBRAL_INTERSECCION,
    }

def seguir_linea_3s(borde="izquierdo"):
    global error_anterior, integral
    if borde == "izquierdo":
        error = sensor_centro.reflection() - UMBRAL
    else:
        error = UMBRAL - sensor_centro.reflection()
    integral = max(-100, min(100, integral + error))
    correccion = Kp*error + Ki*integral + Kd*(error - error_anterior)
    error_anterior = error
    robot.drive(VELOCIDAD, correccion)

def resetear_pid():
    global error_anterior, integral
    error_anterior = 0
    integral = 0
```

## Seguir y detenerse en la N-ésima intersección

```python
def seguir_hasta_interseccion(lado="izquierda", numero=1,
                               borde="izquierdo", velocidad=180):
    global VELOCIDAD
    vel_original = VELOCIDAD
    VELOCIDAD = velocidad
    resetear_pid()
    conteo = 0
    en_interseccion = False
    while True:
        lecturas = leer_todo()
        seguir_linea_3s(borde)
        if lado == "izquierda":
            detectado = lecturas["inter_izq"]
        elif lado == "derecha":
            detectado = lecturas["inter_der"]
        else:
            detectado = lecturas["inter_izq"] and lecturas["inter_der"]
        if detectado and not en_interseccion:
            conteo += 1
            en_interseccion = True
            hub.light.on(Color.GREEN)
            if conteo >= numero:
                robot.stop()
                VELOCIDAD = vel_original
                hub.light.off()
                return conteo
        elif not detectado:
            en_interseccion = False
            hub.light.off()
        wait(10)
    VELOCIDAD = vel_original
```

### Ejemplos de uso
```python
seguir_hasta_interseccion(lado="izquierda", numero=2)
seguir_hasta_interseccion(lado="derecha", numero=1)
seguir_hasta_interseccion(lado="ambas", numero=3)
```

## Desviarse en una intersección

```python
def seguir_y_girar(lado_giro="izquierda", en_interseccion_numero=1,
                    borde="izquierdo", velocidad=180):
    seguir_hasta_interseccion(lado=lado_giro, numero=en_interseccion_numero,
                               borde=borde, velocidad=velocidad)
    angulo_giro = -90 if lado_giro == "izquierda" else 90
    robot.straight(30)
    robot.turn(angulo_giro)
    robot.straight(20)
    resetear_pid()
```

## Girar y buscar la línea (más preciso)

```python
def girar_y_buscar_linea(angulo, sensor_busqueda, velocidad_giro=100):
    UMBRAL_NEGRO = 30
    robot.turn(angulo * 0.5)
    if angulo > 0:
        robot.drive(0, velocidad_giro)
    else:
        robot.drive(0, -velocidad_giro)
    while sensor_busqueda.reflection() > UMBRAL_NEGRO:
        wait(10)
    robot.stop()
    resetear_pid()
```

## Fin de línea

```python
def seguir_hasta_fin_de_linea(borde="izquierdo", velocidad=150):
    global VELOCIDAD
    VELOCIDAD = velocidad
    resetear_pid()
    UMBRAL_BLANCO = 70
    contador_blanco = 0
    while True:
        seguir_linea_3s(borde)
        if (sensor_izq.reflection() > UMBRAL_BLANCO and
            sensor_centro.reflection() > UMBRAL_BLANCO and
            sensor_der.reflection() > UMBRAL_BLANCO):
            contador_blanco += 1
            if contador_blanco > 5:
                robot.stop()
                return
        else:
            contador_blanco = 0
        wait(10)
```

## Comparativa: 1 vs 2 vs 3 sensores

| Capacidad | 1 | 2 | 3 |
|-----------|---|---|---|
| Seguir línea | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Detectar intersección | ❌ | ⚠️ | ✅ |
| Distinguir curva/intersección | ❌ | ❌ | ✅ |
| Fin de línea | ❌ | ⚠️ | ✅ |
| Alinearse | ❌ | ✅ | ✅ |

## Recomendación WRO

**Usá 3 sensores siempre que puedas.** Puertos SPIKE: 2 motores tracción + 3 sensores color + 1 motor mecanismo = 6 puertos (todos).
