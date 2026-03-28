# 07 - Estrategias de Competición WRO RoboMission

## Biblioteca de movimientos

```python
seguir_hasta_interseccion(lado, numero, borde, velocidad)
seguir_y_girar(lado_giro, en_interseccion_numero, borde, velocidad)
seguir_hasta_fin_de_linea(borde, velocidad)
avanzar_hasta_linea(sensor, velocidad)
alinear_perpendicular(sensor_izq, sensor_der, ...)
robot.straight(distancia_mm)
robot.turn(angulo)
```

## Patrones comunes

### Ida y vuelta por ramal
```python
def ida_y_vuelta_ramal(interseccion_num, lado, tarea_func):
    girar_en_interseccion(lado, interseccion_num, lado)
    seguir_hasta_fin_de_linea()
    tarea_func()
    robot.turn(180)
    seguir_hasta_interseccion(lado="ambas", numero=1)
    robot.straight(40)
    robot.turn(-90 if lado == "derecha" else 90)
    avanzar_hasta_linea(sensor_centro)
```

### Decisión por color (randomización WRO)
```python
def navegar_con_decision(sensor):
    color = sensor.color()
    if color == Color.RED:
        girar_en_interseccion("izquierda", 1, "izquierda")
    elif color == Color.BLUE:
        girar_en_interseccion("derecha", 1, "derecha")
```

### Velocidad adaptativa
```python
VELOCIDAD_RAPIDA = 250
VELOCIDAD_NORMAL = 180
VELOCIDAD_PRECISA = 100
VELOCIDAD_BUSQUEDA = 80
```

## Estructura del programa
```
1. IMPORTS → 2. INICIALIZACIÓN → 3. CONSTANTES → 4. FUNCIONES NAVEGACIÓN → 5. FUNCIONES TAREAS → 6. MAIN → 7. EJECUTAR
```

## Checklist de competición
- [ ] Batería cargada
- [ ] Calibración en el tapete de competición
- [ ] Sensores a la altura correcta
- [ ] Ruedas limpias
- [ ] Robot cabe en 250×250×250mm
- [ ] Plan B si algo falla

## Consejo final
> **La constancia gana competencias, no la velocidad.** Primero hacelo funcionar, después hacelo rápido.
