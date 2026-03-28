# SKILL: Mejores Prácticas de Movimiento para WRO RoboMission (Pybricks)

## Descripción
Skill para generar código Pybricks Python con mejores prácticas de movimiento de competencia.

## Reglas obligatorias

### 1. Gyro init
```python
hub = PrimeHub()
hub.imu.settings(angular_velocity_threshold=5, acceleration_threshold=50, heading_correction=358)
while not hub.imu.ready():
    wait(100)
robot.use_gyro(True)
```

### 2. Velocidad máxima
NUNCA > 400 mm/s. Recomendado: 150-250 navegación, 80-120 precisión.

### 3. Perfiles
```python
def perfil_preciso(): robot.settings(120, 80, 80, 60)
def perfil_normal(): robot.settings(200, 150, 120, 80)
def perfil_rapido(): robot.settings(350, 200, 150, 100)
```

### 4. Calibración
wheel_diameter y axle_track SIEMPRE con comentario CALIBRAR.

### 5. Stop modes
HOLD para posiciones críticas, COAST para transiciones.

## PID por escenario

| Escenario | Kp | Ki | Kd | Vel |
|-----------|----|----|----|----|
| 1 sensor lento | 1.5 | 0 | 5 | 120 |
| 1 sensor curvas | 2.0 | 0.01 | 7 | 150 |
| 2 sensores | 0.8 | 0 | 4 | 200 |
| Rápido | 2.5 | 0 | 10 | 300 |

## Orden calibración
1. wheel_diameter 2. axle_track 3. heading_correction 4. use_gyro(True) 5. PID

## Plantilla

```python
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Stop, Color, Button
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
hub.imu.settings(angular_velocity_threshold=5, acceleration_threshold=50, heading_correction=358)
hub.light.on(Color.RED)
while not hub.imu.ready():
    wait(100)
hub.light.on(Color.GREEN)

motor_izq = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_der = Motor(Port.B)
robot = DriveBase(motor_izq, motor_der, wheel_diameter=56, axle_track=112)
robot.use_gyro(True)
robot.settings(200, 150, 120, 80)

while Button.CENTER not in hub.buttons.pressed():
    wait(50)
wait(500)
hub.imu.reset_heading(0)
```

## Errores a evitar
- NO velocidades > 400 mm/s
- NO olvidar wait(10) en loops
- NO olvidar hub.imu.ready()
- NO Ki > 0.05
- NO olvidar reset_pid() al cambiar tramo
