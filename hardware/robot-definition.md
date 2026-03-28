# Definición del Robot — WRO Elementary 2026 "Robot Rockstars"

## ESTE ES EL ARCHIVO MAESTRO DE CONFIGURACIÓN

Todos los programas (Python y bloques) deben usar estos valores.
Si algo cambia en el robot físico, actualizar este archivo PRIMERO
y luego propagar a `base_config.py` y `robot_lib.py`.

## Identificación

- **Equipo:** Robot Rockstars
- **Categoría:** WRO RoboMission Elementary 2026
- **Instituto:** IITA — Instituto de Innovación y Tecnología Aplicada, Salta
- **Hub:** LEGO SPIKE Prime
- **Firmware:** Pybricks v3.6+

## Asignación de puertos

```
┌──────────────────────────────────────────┐
│              SPIKE PRIME HUB             │
│                                          │
│   Puerto A ← Motor Izquierdo (grande)    │
│   Puerto B ← Motor Derecho (grande)      │
│   Puerto C ← Motor Garra/Mecanismo       │
│   Puerto D ← Sensor Color (centro)       │
│   Puerto E ← (libre o 2do sensor color)  │
│   Puerto F ← (libre o 3er sensor color)  │
└──────────────────────────────────────────┘
```

### Detalle de cada puerto

| Puerto | Dispositivo | Tipo | Notas |
|--------|-------------|------|-------|
| A | Motor tracción izquierdo | Motor Grande | `Direction.COUNTERCLOCKWISE` |
| B | Motor tracción derecho | Motor Grande | `Direction.CLOCKWISE` (default) |
| C | Motor mecanismo (garra) | Motor Mediano | Para manipular objetos |
| D | Sensor color centro | Color Sensor | Para seguimiento de línea (borde) |
| E | *Disponible* | — | Puede ser 2do sensor color lateral |
| F | *Disponible* | — | Puede ser 3er sensor color lateral |

## Dimensiones del robot (CALIBRAR CON REGLA)

| Parámetro | Valor nominal | Valor calibrado | Fecha calibración |
|-----------|--------------|-----------------|-------------------|
| `wheel_diameter` | 56.0 mm | *PENDIENTE* | — |
| `axle_track` | 112.0 mm | *PENDIENTE* | — |
| `heading_correction` | 360 | *PENDIENTE* | — |

### Procedimiento de calibración

1. **wheel_diameter**: Robot avanza 1000mm → medir real → `56 × (1000 / real)`
2. **axle_track**: Robot gira 3600° (10 vueltas) → ajustar hasta que quede alineado
3. **heading_correction**: Girar robot 360° a mano → leer `hub.imu.heading()` → anotar

**IMPORTANTE:** Actualizar la tabla de arriba cada vez que se calibre.

## Configuración de velocidades

| Perfil | straight_speed | straight_accel | turn_rate | turn_accel |
|--------|---------------|----------------|-----------|------------|
| Preciso | 120 mm/s | 80 mm/s² | 80 °/s | 60 °/s² |
| Normal | 200 mm/s | 150 mm/s² | 120 °/s | 80 °/s² |
| Rápido | 350 mm/s | 200 mm/s² | 150 °/s | 100 °/s² |

## Configuración de sensores de color

| Parámetro | Valor nominal | Valor calibrado | Fecha |
|-----------|--------------|-----------------|-------|
| `NEGRO` (reflexión línea) | 10 | *PENDIENTE* | — |
| `BLANCO` (reflexión fondo) | 90 | *PENDIENTE* | — |
| `UMBRAL` | 50 | *PENDIENTE* | — |
| `UMBRAL_INTERSECCION` | 25 | *PENDIENTE* | — |

## Configuración PID

| Parámetro | Valor inicial | Valor calibrado | Fecha |
|-----------|--------------|-----------------|-------|
| `Kp` | 1.5 | *PENDIENTE* | — |
| `Ki` | 0.0 | *PENDIENTE* | — |
| `Kd` | 5.0 | *PENDIENTE* | — |

## Configuración del giroscopio

| Parámetro | Valor |
|-----------|-------|
| `use_gyro` | True |
| `angular_velocity_threshold` | 5 |
| `acceleration_threshold` | 50 |
| `heading_correction` | *PENDIENTE* (medir para este hub) |
| Orientación del hub | Horizontal, plano (default) |

## Mecanismo de garra

| Parámetro | Valor |
|-----------|-------|
| Motor | Puerto C, Motor Mediano |
| Ángulo abrir | +90° |
| Ángulo cerrar | -90° |
| Velocidad | 300 °/s |
| Stop mode | HOLD |

## Archivos que dependen de esta definición

| Archivo | Qué usa |
|---------|---------|
| `software/programs/base_config.py` | Todo (puertos, dimensiones, velocidades) |
| `software/programs/robot_lib.py` | Funciones de navegación (PID, sensores, gyro) |
| Programas de bloques en Pybricks | Setup block debe coincidir con puertos |
| `docs/ai-skills/SKILL-*.md` | Valores de referencia para generación de código |

## Regla de oro

> Cuando algo cambie en el robot (rueda nueva, sensor en otro puerto, mecanismo diferente),
> actualizar PRIMERO este archivo y DESPUÉS propagar a los demás.
> Así todos los programas y la IA usan los mismos valores.
