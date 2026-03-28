# Detección de Colores en WRO RoboMission — Guía Completa

## ¿Por qué es difícil detectar colores?

El sensor de color de SPIKE Prime no "ve" colores como nuestros ojos. Mide la luz que rebota y la descompone. El problema es que la misma pieza roja se ve distinta según la luz del salón, la distancia, y la batería. Los equipos ganadores calibran sus propios colores.

## RGB vs HSV: por qué HSV es mejor

**RGB** mide cuánta luz roja, verde y azul rebota. Si la luz cambia, los TRES cambian.

**HSV** separa en tres partes independientes:
- **H (Tono):** QUÉ color es (0-359°). Rojo≈30°, Amarillo≈60°, Verde≈120°, Azul≈220°
- **S (Saturación):** Qué tan puro (0=gris, 100=puro)
- **V (Brillo):** Qué tan brillante (0=negro, 100=brillante)

Cuando la luz cambia, **el Hue casi no cambia**. Solo cambian S y V. Por eso HSV es mucho más confiable.

## Cómo calibrar colores en Pybricks

### Paso 1: Medir cada color

Poné cada objeto debajo del sensor a la distancia real. Usá `sensor.hsv()` para leer H, S, V. Anotá los valores.

### Paso 2: Definir colores personalizados

```python
Color.MI_ROJO = Color(h=355, s=82, v=45)   # Valores MEDIDOS
Color.MI_AZUL = Color(h=218, s=85, v=50)
Color.MI_VERDE = Color(h=140, s=70, v=35)

sensor.detectable_colors((Color.MI_ROJO, Color.MI_AZUL, Color.MI_VERDE, Color.NONE))
```

### Paso 3: Usar normalmente

```python
color = sensor.color()  # Retorna el más cercano de tus colores calibrados
```

**Tip:** Solo incluir los colores que realmente usás en la misión.

## Protocolo de lectura correcto

### ¡SIEMPRE parar antes de leer!

El error #1 es leer color mientras el robot se mueve. El sensor necesita estar quieto.

```
1. PARAR el robot
2. ESPERAR 200ms (que se estabilice)
3. LEER 5 veces
4. ELEGIR el color que apareció más (voto mayoritario)
```

## Feedback sin frenar el programa

Después de detectar, querés avisar qué color vio sin perder tiempo:

**Luz del hub** (instantánea):
```python
hub.light.on(Color.RED)   # No frena el programa
```

**Display** (instantáneo):
```python
hub.display.char("R")     # Muestra "R" en la pantalla 5x5
```

**Beep no-bloqueante** (el truco de la duración negativa):
```python
hub.speaker.beep(500, -1)  # Arranca el beep y sigue ejecutando
# El robot puede moverse mientras suena
hub.speaker.beep(0, 0)     # Para el sonido cuando quieras
```

**Multitasking** (beep en paralelo):
```python
await multitask(
    robot.straight(100),     # Se mueve
    hub.speaker.beep(600, 80),  # Suena al mismo tiempo
)
```

## Ubicación del sensor

- **Distancia óptima:** 8-16mm del objeto
- **< 5mm:** satura (todo V=100)
- **> 20mm:** señal débil, colores ruidosos
- **Truco del tubo oscuro:** poner piezas Technic alrededor del sensor para bloquear luz del salón
- **Perpendicular:** el sensor debe apuntar directo al objeto, no de costado

## Clasificador avanzado (distancia HSV ponderada)

Para distinguir colores difíciles (rojo vs naranja), se puede usar distancia euclidiana con pesos diferentes para H, S, V según el color:

- Colores puros (rojo, azul): peso alto en H
- Blanco: peso alto en V (debe ser alto) y S (debe ser baja)
- Negro: peso alto en V (debe ser bajo)

Cada color tiene un "umbral máximo" — si la lectura está más lejos, retorna DESCONOCIDO.

## Problemas comunes

| Problema | Solución |
|----------|----------|
| Confunde rojo/naranja | Calibrar con los objetos reales, subir peso de H |
| Todo BLANCO | Sensor muy lejos → acercar a 8-16mm |
| Todo NEGRO | Sensor tapado → verificar montaje |
| Cambia entre rondas | Recalibrar en el salón de competencia |
| Lectura lenta | Reducir a 3 lecturas, 30ms entre cada una |

## Regla de oro

> **Calibrá en el lugar de competencia, con los objetos reales, a la distancia real.**
