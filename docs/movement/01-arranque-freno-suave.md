# 01 - Arranque Suave, Freno Suave y Perfiles de Velocidad

## ¿Por qué no arrancar a toda velocidad?

Cuando le decís al robot "andá a 300 mm/s", los motores intentan llegar instantáneamente. Esto causa patinaje de ruedas, error de odometría, y sacudones mecánicos. Los equipos ganadores usan **aceleración progresiva**.

## DriveBase.settings()

```python
robot.settings(
    straight_speed=200,
    straight_acceleration=150,
    turn_rate=120,
    turn_acceleration=80
)
```

### Perfiles recomendados

```python
def perfil_preciso():
    robot.settings(120, 80, 80, 60)
def perfil_normal():
    robot.settings(200, 150, 120, 80)
def perfil_rapido():
    robot.settings(350, 200, 150, 100)
```

## Velocidad máxima SPIKE Prime

Motores: ~1000°/s. Ruedas 56mm: máx ~488 mm/s. Usar máximo 80% = ~350-400 mm/s. Más que eso impide correcciones de dirección.

## Freno suave

```python
def avanzar_preciso(distancia_mm):
    ZONA_FRENADO = 50
    if distancia_mm > ZONA_FRENADO * 2:
        perfil_normal()
        robot.straight(distancia_mm - ZONA_FRENADO)
        perfil_preciso()
        robot.straight(ZONA_FRENADO)
    else:
        perfil_preciso()
        robot.straight(distancia_mm)
```

## Stop modes

| Situación | Stop recomendado |
|-----------|------------------|
| Antes de recoger objeto | HOLD |
| Antes de girar | COAST o BRAKE |
| Final de misión | HOLD |
| Entre movimientos rápidos | BRAKE |

## Curvas > giro + recto

```python
robot.curve(radius=80, angle=90)  # Más fluido que turn(90)+straight(100)
```

## Reglas de oro

1. Nunca superar 80% velocidad máxima
2. Aceleración < 200 mm/s²
3. Frenar suave antes de posiciones críticas
4. Preferir curvas a giro+recto
5. Probar perfiles y medir desviación con giroscopio
