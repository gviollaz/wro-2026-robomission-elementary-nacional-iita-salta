# 04 - Calibración de PID para Color y Giroscopio

## Método Ziegler-Nichols simplificado

### Paso 1: Encontrar Kp crítico (Ki=0, Kd=0)
Empezar Kp=0.5, subir hasta oscilación violenta = Kp_critico.

### Paso 2: Kp_trabajo = Kp_critico × 0.6
### Paso 3: Kd_inicial = Kp_trabajo × 4
### Paso 4: Ki solo si error constante. Ki = Kp_trabajo × 0.01

### Tabla de ajuste

| Si el robot... | Ajustar | Dirección |
|----------------|---------|-----------|
| Reacciona lento | Kp | ↑ Subir |
| Oscila mucho | Kp | ↓ Bajar |
| Sacude | Kd | ↑ Subir |
| Lento en curvas | Kd | ↓ Bajar |
| Error constante | Ki | ↑ Subir (poco!) |
| Se vuelve loco | Ki | ↓ Bajar o = 0 |

## Valores por escenario

| Escenario | Kp | Ki | Kd | Vel |
|-----------|----|----|----|----|
| 1 sensor lento | 1.5 | 0 | 5 | 120 |
| 1 sensor curvas | 2.0 | 0.01 | 7 | 150 |
| 2 sensores | 0.8 | 0 | 4 | 200 |
| 2 sensores curvas | 1.2 | 0.005 | 6 | 150 |
| Rápido | 2.5 | 0 | 10 | 300 |

## PID depende de la velocidad

```python
Kp_lento, Kd_lento = 1.5, 5.0     # 100-150 mm/s
Kp_rapido, Kd_rapido = 2.5, 10.0  # 250-350 mm/s
```

## Programa interactivo

```python
hub = PrimeHub()
while not hub.imu.ready():
    wait(100)
robot = DriveBase(motor_izq, motor_der, wheel_diameter=56, axle_track=112)
robot.use_gyro(True)
sensor = ColorSensor(Port.E)

Kp, Ki, Kd = 1.5, 0.0, 5.0
error_ant, integral = 0, 0

while True:
    error = sensor.reflection() - 50
    integral = max(-100, min(100, integral + error))
    correccion = Kp*error + Ki*integral + Kd*(error - error_ant)
    error_ant = error
    robot.drive(150, correccion)
    if Button.LEFT in hub.buttons.pressed():
        Kp = max(0.1, Kp - 0.1)
    if Button.RIGHT in hub.buttons.pressed():
        Kp += 0.1
    wait(10)
```

## Anti-windup

```python
INTEGRAL_MAX = 100
integral = max(-INTEGRAL_MAX, min(INTEGRAL_MAX, integral + error))

def resetear_pid():
    global error_ant, integral
    error_ant, integral = 0, 0
```

**Siempre calibrá con TU robot en el tapete real.**
