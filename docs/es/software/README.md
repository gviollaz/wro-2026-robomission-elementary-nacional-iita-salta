# Software - Elementary (Pybricks Bloques)

## Plataforma

- **Firmware:** Pybricks (instalado en Spike Prime)
- **IDE:** [code.pybricks.com](https://code.pybricks.com)
- **Lenguaje:** Bloques visuales (generan Python internamente)

## Estructura de programas

```
software/
  programs/
    main.py                  # Programa principal de competencia
    base_config.py           # Configuracion base del robot
  calibration/
    calibrar_color.py        # Calibracion sensor de color
    calibrar_distancias.py   # Verificar distancias DriveBase
  tools/
    test_motores.py          # Test basico de motores
```

## Conceptos clave Pybricks

- **DriveBase**: control coordinado de 2 motores con `straight()` y `turn()`
- **Motor.run_angle()**: mover motor un angulo exacto (para garra)
- **ColorSensor.color()**: detectar color (para notas randomizadas)
- **ColorSensor.hsv()**: valores HSV para deteccion mas precisa
- **wait()**: pausas entre movimientos

## Estrategia de misiones

1. Definir rutas como secuencias de `straight()` + `turn()`
2. Crear funciones/"My Blocks" para cada sub-tarea
3. Usar sensor de color para mision 3 (notas randomizadas)
4. Priorizar misiones por puntos/dificultad
