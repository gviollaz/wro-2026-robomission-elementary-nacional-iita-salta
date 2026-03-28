# SKILL: Detección de Colores en Bloques para WRO Elementary

## Descripción
Skill para guiar a alumnos en detección de colores usando Pybricks Blocks en WRO RoboMission Elementary. Cubre calibración, lectura con parada, feedback visual/sonoro no-bloqueante, y uso de robot_lib para funciones avanzadas.

## Lo que el alumno puede hacer con bloques

### Leer color con bloques

En Pybricks Blocks, el bloque **"Color of sensor D"** retorna el color detectado. Se usa dentro de bloques **"Si... entonces"** para tomar decisiones.

### Definir colores personalizados en bloques

Pybricks Blocks permite definir colores personalizados en el bloque **Setup**:
1. En el Setup, configurar el sensor de color
2. Usar el bloque **"Set detectable colors"** 
3. Agregar cada color con valores H, S, V medidos

### Pseudocódigo de bloques para leer color

```
[INICIO]
  |  … (el robot llegó al punto de lectura)
  |  Parar
  |  Esperar 0.2 segundos
  |  color_leido ← Color del Sensor D
  |  
  |  [Si color_leido = MI_ROJO]
  |  |  Luz del hub → ROJO
  |  |  Mostrar "R" en display
  |  |  … (hacer acción para rojo)
  |  [Sino si color_leido = MI_AZUL]
  |  |  Luz del hub → AZUL
  |  |  Mostrar "A" en display
  |  |  … (hacer acción para azul)
  |  [Sino]
  |  |  Luz del hub → apagar
  |  |  Mostrar "?" en display
  |  [Fin Si]
```

## Lo que va en robot_lib.py (Python, Claude lo escribe)

Las funciones avanzadas de color van en la biblioteca Python que los bloques importan:

```python
# En robot_lib.py

def configurar_colores(sensor):
    """Configurar colores calibrados. Llamar una vez al inicio."""
    Color.MI_ROJO    = Color(h=355, s=82, v=45)  # CALIBRAR
    Color.MI_AZUL    = Color(h=218, s=85, v=50)  # CALIBRAR
    Color.MI_VERDE   = Color(h=140, s=70, v=35)  # CALIBRAR
    Color.MI_AMARILLO = Color(h=55, s=65, v=90)  # CALIBRAR
    sensor.detectable_colors((
        Color.MI_ROJO, Color.MI_AZUL,
        Color.MI_VERDE, Color.MI_AMARILLO, Color.NONE
    ))

def leer_color_preciso(sensor, robot):
    """Para el robot, lee 5 veces, retorna el más frecuente."""
    robot.stop()
    wait(200)
    votos = {}
    for i in range(5):
        c = str(sensor.color())
        votos[c] = votos.get(c, 0) + 1
        wait(50)
    return max(votos, key=votos.get)

def feedback_color(hub, nombre):
    """Feedback visual + sonoro no-bloqueante."""
    colores = {
        "ROJO":    (Color.RED,   "R", 440),
        "AZUL":    (Color.BLUE,  "A", 660),
        "VERDE":   (Color.GREEN, "V", 550),
        "AMARILLO":(Color.YELLOW,"Y", 880),
    }
    if nombre in colores:
        luz, letra, freq = colores[nombre]
        hub.light.on(luz)
        hub.display.char(letra)
        hub.speaker.beep(freq, -1)
```

### Cómo se usa desde bloques

```
[SETUP]
  Import from robot_lib: configurar_colores, leer_color_preciso, feedback_color
  … (configurar hub, motores, sensor)
  Run Task: configurar_colores(sensor_color)

[INICIO]
  |  … (navegar hasta el punto de lectura)
  |  resultado ← Run Task: leer_color_preciso(sensor_color, robot)
  |  Run Task: feedback_color(hub, resultado)
  |  
  |  [Si resultado = "ROJO"]
  |  |  … (misión para rojo)
  |  [Sino si resultado = "AZUL"]
  |  |  … (misión para azul)
  |  [Fin Si]
```

## Programa de calibración (Python puro, copiar a Pybricks)

El programa de calibración se ejecuta una vez para medir los colores reales:

```
1. Crear proyecto Python "calibrar_colores" en Pybricks
2. Copiar el programa de calibración del doc README
3. Poner cada objeto debajo del sensor
4. Anotar los valores H, S, V que muestra
5. Copiar esos valores a robot_lib.py en configurar_colores()
```

## Reglas para generar pseudocódigo de bloques con color

1. SIEMPRE incluir bloque "Parar" antes de leer color de objetos
2. SIEMPRE incluir "Esperar 0.2 segundos" después de parar
3. SIEMPRE usar feedback visual (luz del hub) después de detectar
4. Las funciones avanzadas (promedio, clasificador) van en robot_lib.py
5. Los bloques solo llaman a las funciones con "Run Task"
6. Calibrar SIEMPRE en el lugar de competencia

## Mapeo bloques ↔ color

| Bloque | Python | Notas |
|--------|--------|-------|
| Color del sensor D | `sensor.color()` | Retorna color calibrado |
| HSV del sensor D | `sensor.hsv()` | Para calibración |
| Reflexión del sensor D | `sensor.reflection()` | Solo brillo, para líneas |
| Luz hub = Rojo | `hub.light.on(Color.RED)` | No-bloqueante |
| Mostrar "R" | `hub.display.char("R")` | No-bloqueante |
| Beep 500Hz 100ms | `hub.speaker.beep(500, 100)` | Bloqueante! |
| Beep no-bloqueante | No disponible en bloques | Usar robot_lib.py |

## Tip para Elementary

Para chicos de 8-12 años, la forma más simple de empezar es:

1. Calibrar colores con el programa Python (el coach lo ejecuta)
2. Poner los valores en `configurar_colores()` de robot_lib
3. En bloques, el alumno solo usa:
   - "Parar" → "Esperar 0.2s" → "Si Color = ROJO..." → hacer algo

La complejidad queda en la biblioteca, los bloques quedan simples.
