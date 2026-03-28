# 05 - Intersecciones y Bifurcaciones

## ¿Qué es una intersección?

Una intersección es un punto donde **una línea se cruza con otra**. En los tapetes de WRO RoboMission, encontrás varios tipos:

```
CRUCE EN T (izquierda)     CRUCE EN T (derecha)      CRUCE EN +
                                                        │
━━━━━━┓                        ┏━━━━━━                ━━┿━━
      ┃                        ┃                        │

CURVA A 90°                FIN DE LÍNEA
━━━━━━┓                    ━━━━━━╸
      ┃
```

## Estrategia 1: Contar intersecciones por lado

```python
seguir_hasta_interseccion(lado="izquierda", numero=2)  # Para en la 2da izq.
seguir_hasta_interseccion(lado="derecha", numero=1)     # Para en la 1ra der.
```

## Acciones en intersecciones

### Detenerse
```python
def parar_en_interseccion(lado, numero, borde="izquierdo"):
    seguir_hasta_interseccion(lado, numero, borde)
    robot.stop()
```

### Girar 90°
```python
def girar_en_interseccion(lado_deteccion, numero, lado_giro, borde="izquierdo"):
    seguir_hasta_interseccion(lado_deteccion, numero, borde)
    robot.straight(40)
    robot.turn(-90 if lado_giro == "izquierda" else 90)
    robot.straight(25)
    resetear_pid()
```

### Girar buscando línea (más preciso)
```python
def girar_buscando_linea(lado_deteccion, numero, lado_giro, borde="izquierdo"):
    seguir_hasta_interseccion(lado_deteccion, numero, borde)
    robot.straight(40)
    vel_giro = -80 if lado_giro == "izquierda" else 80
    robot.drive(0, vel_giro)
    while sensor_centro.reflection() < 60:
        wait(10)
    while sensor_centro.reflection() > 30:
        wait(10)
    robot.stop()
    resetear_pid()
```

## Versión mejorada con distancia mínima

```python
def seguir_hasta_interseccion_v2(lado, numero, borde="izquierdo", distancia_minima=30):
    conteo, en_interseccion = 0, False
    robot.reset()
    distancia_ultima = 0
    while True:
        seguir_linea_3s(borde)
        lecturas = leer_todo()
        if lado == "izquierda":
            detectado = lecturas["inter_izq"]
        elif lado == "derecha":
            detectado = lecturas["inter_der"]
        else:
            detectado = lecturas["inter_izq"] and lecturas["inter_der"]
        distancia_actual = robot.distance()
        if (detectado and not en_interseccion and
            distancia_actual - distancia_ultima > distancia_minima):
            conteo += 1
            en_interseccion = True
            distancia_ultima = distancia_actual
            if conteo >= numero:
                robot.stop()
                return conteo
        elif not detectado:
            en_interseccion = False
        wait(10)
```

## Problemas comunes

| Problema | Solución |
|----------|----------|
| Cuenta de más | Debounce + distancia mínima |
| No detecta | Bajar velocidad, ajustar umbral |
| Confunde curva | Usar 3 sensores |
| No encuentra línea después de girar | Usar girar_buscando_linea |
