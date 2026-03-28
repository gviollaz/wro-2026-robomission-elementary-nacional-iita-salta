# 02 - Odometría Precisa

## Los dos valores que definen todo

```python
robot = DriveBase(motor_izq, motor_der,
    wheel_diameter=56,   # CALIBRAR
    axle_track=112)      # CALIBRAR
```

## Calibrar wheel_diameter

### Método calibre
Medir diámetro con calibre incluyendo goma.

### Método cinta
Marcar rueda, rodar 1 vuelta, medir distancia, diámetro = distancia / π.

### Método software (más preciso)
```python
robot.straight(1000)  # Con valor nominal
# Medir distancia real
# diámetro_correcto = nominal × (1000 / distancia_real)
```

## Calibrar axle_track

```python
robot.turn(3600)  # 10 vueltas
# Giró de más → subir axle_track
# Giró de menos → bajar axle_track
```

Calibrar SIN giroscopio primero, activar gyro después.

## Fuentes de error

| Error | Solución |
|-------|----------|
| Patinaje | Arranque suave, ruedas limpias |
| Compresión goma | Calibrar con robot armado |
| Desgaste desigual | Rotar ruedas |
| Backlash | Transmisión directa |
| Superficie irregular | Usar giroscopio |

## Combinar odometría + gyro + sensores

```python
robot.use_gyro(True)
# Distancia → ruedas, Dirección → gyro

def avanzar_hasta_linea_o_distancia(sensor, distancia_max, velocidad=150):
    robot.reset()
    robot.drive(velocidad, 0)
    while True:
        if sensor.reflection() < 25:
            robot.stop()
            return "linea"
        if robot.distance() >= distancia_max:
            robot.stop()
            return "distancia"
        wait(10)
```

## Orden: 1° wheel_diameter → 2° axle_track → 3° heading_correction → 4° gyro
