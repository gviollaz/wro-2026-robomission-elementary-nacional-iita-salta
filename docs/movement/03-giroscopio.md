# 03 - Giroscopio: Guía Completa para WRO con SPIKE Prime

## ¿Qué es el giroscopio?

El SPIKE Prime tiene un IMU (giroscopio + acelerómetro). Mide rotación del hub directamente, sin depender de las ruedas.

## Activar

```python
robot.use_gyro(True)  # Todos los movimientos usan gyro
```

## Inicialización CRÍTICA

```python
hub = PrimeHub()
hub.imu.settings(angular_velocity_threshold=5, acceleration_threshold=50)
hub.light.on(Color.RED)
while not hub.imu.ready():
    wait(100)
hub.light.on(Color.GREEN)
```

NO MOVER el hub durante encendido. Hub QUIETO y PLANO.

## heading_correction

Cada hub tiene error de escala. Medir:
```python
hub.imu.reset_heading(0)
# Girar 360° a mano con marca de referencia
heading_medido = hub.imu.heading()
hub.imu.settings(heading_correction=heading_medido)
```
Hacer 3 veces, promediar, anotar (es específico del hub).

## Recalibración

```python
def recalibrar_gyro():
    robot.stop()
    wait(1500)  # Quieto 1.5s
```

Cuándo: antes de ronda, después de colisión, antes de giros críticos, cada 30-60s.

## Vibraciones en competencia

Subir umbrales:
```python
hub.imu.settings(angular_velocity_threshold=5, acceleration_threshold=50)
```

## Orientación del hub

Montar horizontal y centrado. Si no es posible:
```python
hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)
```

## 5 Limitaciones

1. **Drift** (~0.5-2°/min): recalibrar, usar líneas como referencia
2. **Error acumulativo en giros repetidos**: heading_correction, alternar dirección
3. **Rampas**: heading('3D') en Pybricks 3.6+
4. **Temperatura**: hub caliente driftea más
5. **Vibraciones**: amortiguación, alejar de motores

## Resumen

| Práctica | Importancia |
|----------|-------------|
| No mover al encender | CRÍTICA |
| hub.imu.ready() | CRÍTICA |
| heading_correction | ALTA |
| Thresholds competencia | ALTA |
| Recalibrar quieto | MEDIA |
| Hub horizontal | MEDIA |
| ≤80% velocidad máx | ALTA |
| Reset heading al inicio | ALTA |
