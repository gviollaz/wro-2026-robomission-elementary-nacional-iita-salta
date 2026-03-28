# 06 - Encontrar Línea y Alinearse con Precisión

## Estrategia 1: Avanzar hasta encontrar la línea

```python
def avanzar_hasta_linea(sensor, velocidad=150):
    UMBRAL_NEGRO = 30
    robot.drive(velocidad, 0)
    while sensor.reflection() > UMBRAL_NEGRO:
        wait(10)
    robot.stop()

def avanzar_hasta_linea_seguro(sensor, velocidad=150, max_mm=500):
    UMBRAL_NEGRO = 30
    robot.reset()
    robot.drive(velocidad, 0)
    while sensor.reflection() > UMBRAL_NEGRO:
        if robot.distance() > max_mm:
            robot.stop()
            return False
        wait(10)
    robot.stop()
    return True
```

## Estrategia 2: Buscar en barrido (sweep)

```python
def buscar_linea_barrido(sensor, angulo_max=120, velocidad_giro=80):
    UMBRAL_NEGRO = 30
    for angulo in range(30, angulo_max + 1, 30):
        robot.drive(0, velocidad_giro)
        inicio = robot.angle()
        while abs(robot.angle() - inicio) < angulo:
            if sensor.reflection() < UMBRAL_NEGRO:
                robot.stop()
                return True
            wait(10)
        robot.drive(0, -velocidad_giro)
        inicio = robot.angle()
        while abs(robot.angle() - inicio) < angulo * 2:
            if sensor.reflection() < UMBRAL_NEGRO:
                robot.stop()
                return True
            wait(10)
        robot.drive(0, velocidad_giro)
        inicio = robot.angle()
        while abs(robot.angle() - inicio) < angulo:
            wait(10)
    robot.stop()
    return False
```

## Alineación perpendicular (squaring)

```python
def alinear_perpendicular(sensor_izq, sensor_der, left_motor, right_motor, velocidad=80):
    UMBRAL_NEGRO = 30
    izq_ok, der_ok = False, False
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

def alinear_preciso(sensor_izq, sensor_der, left_motor, right_motor, repeticiones=2):
    for i in range(repeticiones):
        alinear_perpendicular(sensor_izq, sensor_der, left_motor, right_motor)
        if i < repeticiones - 1:
            robot.straight(-30)
            wait(200)
    alinear_perpendicular(sensor_izq, sensor_der, left_motor, right_motor, velocidad=40)
```

## Secuencia completa

```python
def iniciar_seguimiento(sensor_centro, sensor_izq, sensor_der, left_motor, right_motor, borde="izquierdo"):
    encontrada = avanzar_hasta_linea_seguro(sensor_centro)
    if not encontrada:
        return False
    robot.straight(50)
    robot.straight(-80)
    alinear_preciso(sensor_izq, sensor_der, left_motor, right_motor)
    robot.turn(-90 if borde == "izquierdo" else 90)
    avanzar_hasta_linea(sensor_centro)
    return True
```

## Tips: Velocidad baja para buscar (~80 mm/s), calibrar en el lugar, tener plan B.
