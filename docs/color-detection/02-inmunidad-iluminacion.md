# Inmunidad ante Cambios de Iluminación — Guía para Elementary

## El problema en competencia

Calibras colores a las 9am con luz natural, pero la ronda es a las 3pm bajo lámparas. O la mesa tiene sol de un lado y sombra del otro. Los equipos novatos recalibran cada ronda. Los equipos ganadores usan técnicas que hacen sus lecturas **inmunes a la iluminación**.

## Estrategia 1: Cromaticidad normalizada RGB

### La idea

Cuando la luz cambia, R, G, B cambian proporcionalmente. Si la luz es el doble, los tres se duplican. Pero si dividimos cada canal por la suma total, el factor se cancela:

```
r' = R / (R + G + B)
g' = G / (R + G + B)
b' = B / (R + G + B)
```

Estos valores `r', g', b'` se llaman **cromaticidad** y son prácticamente constantes:

```
Pieza ROJA oscura:    R=80,  G=15, B=10  → r'=0.76, g'=0.14, b'=0.10
Pieza ROJA iluminada: R=200, G=38, B=25  → r'=0.76, g'=0.14, b'=0.10
Pieza ROJA con sol:   R=350, G=65, B=44  → r'=0.76, g'=0.14, b'=0.10
¡Misma cromaticidad con tres luces distintas!
```

### Implementación en robot_lib.py

Pybricks da HSV, así que convertimos a RGB primero:

```python
def hsv_a_rgb(h, s, v):
    s_f = s / 100.0
    v_f = v / 100.0
    c = v_f * s_f
    h_sec = h / 60.0
    x = c * (1 - abs(h_sec % 2 - 1))
    m = v_f - c
    if h_sec < 1:   r, g, b = c, x, 0
    elif h_sec < 2: r, g, b = x, c, 0
    elif h_sec < 3: r, g, b = 0, c, x
    elif h_sec < 4: r, g, b = 0, x, c
    elif h_sec < 5: r, g, b = x, 0, c
    else:           r, g, b = c, 0, x
    return int((r+m)*255), int((g+m)*255), int((b+m)*255)

def cromaticidad(sensor):
    hsv = sensor.hsv()
    r, g, b = hsv_a_rgb(hsv.h, hsv.s, hsv.v)
    total = r + g + b
    if total == 0:
        return 0.33, 0.33, 0.33
    return r/total, g/total, b/total
```

**Limitación:** No distingue blanco de negro (ambos ≈0.33, 0.33, 0.33). Para eso se usa V directo.

## Estrategia 2: Ignorar el brillo (V) para colores cromáticos

La más simple. V es lo que más cambia con la luz. Si lo ignoramos para rojo, azul, verde, amarillo y solo lo usamos para blanco/negro:

```python
def clasificar_inmune(sensor):
    hsv = sensor.hsv()
    h, s, v = hsv.h, hsv.s, hsv.v
    
    # ¿Es acromático? (saturación baja → blanco/negro/gris)
    if s < 20:
        if v > 60: return "BLANCO"
        elif v < 15: return "NEGRO"
        else: return "GRIS"
    
    # Cromático → clasificar SOLO por H (inmune a luz)
    if h > 330 or h < 30:  return "ROJO"
    elif 30 <= h < 70:     return "AMARILLO"
    elif 70 <= h < 170:    return "VERDE"
    elif 170 <= h < 270:   return "AZUL"
    else:                  return "DESCONOCIDO"
```

## Estrategia 3: Pieza blanca de referencia en el robot

Los mejores equipos llevan una pieza blanca pegada donde el sensor la puede leer. Antes de lecturas importantes, leen esa pieza para saber cuánta luz hay.

## Estrategia 4: Lecturas con rechazo de outliers

En vez de promediar todo, descartar las lecturas más extremas:

```python
def leer_rechazo(sensor, n=7, descartar=2):
    lecturas_v = []
    lecturas_h = []
    for i in range(n):
        hsv = sensor.hsv()
        lecturas_h.append(hsv.h)
        lecturas_v.append(hsv.v)
        wait(30)
    lecturas_h.sort()
    lecturas_v.sort()
    # Mediana de H, promedio del centro de V
    h = lecturas_h[n // 2]
    v_centro = lecturas_v[descartar : n - descartar]
    v = sum(v_centro) // len(v_centro)
    return h, v
```

## Estrategia 5: Clasificador combinado (el más robusto)

Combina todo: parar → N lecturas → descartar outliers → separar cromáticos/acromáticos → H-only para cromáticos → V para blanco/negro.

Esta función va en `robot_lib.py` y los bloques la llaman con un simple "Run Task".

---

## Posicionamiento del sensor

### Para leer PISO (líneas, zonas de color)

```
  Robot
  ┌──────────┐
  │  [Sensor] │
  │    ↓      │
  └──────────┘
     │ 5-12mm
  ═══════════  ← Piso
```

**Distancia óptima al piso: 5-12mm**

| Distancia | Resultado |
|-----------|-----------|
| < 5mm | Satura (V=100 siempre) |
| 5-8mm | Punto de luz pequeño (~8mm), bueno para líneas finas |
| 8-12mm | Óptimo: lectura balanceada, punto ~12mm |
| 12-16mm | Aceptable pero más débil |
| > 20mm | NO confiable, H ruidoso |

### Para leer OBJETOS

```
  Robot           Sensor a la
  ┌──────────┐    altura del
  │      ○───┼─── CENTRO del     8-16mm
  │          │    objeto
  └──────────┘   ┌───┐
                 │OBJ│  ← Objeto de color
  ══════════════════════  ← Piso
```

**Distancia óptima al objeto: 8-16mm**

**Regla clave:** el sensor debe apuntar al **CENTRO** del objeto, no a su base. Así el piso queda fuera del cono de visión.

### El problema de la contaminación por piso

Si el sensor está bajo, su cono de visión ve el piso Y el objeto mezclados. Resultado: color incorrecto.

**Soluciones:**
1. Sensor a la altura del centro del objeto
2. Escudo anti-piso: piezas LEGO negras debajo del sensor que bloquean la vista del piso
3. Dos sensores dedicados: D para piso, E para objetos

### Tabla de alturas por objeto LEGO

| Objeto | Altura | Sensor desde piso |
|--------|--------|-------------------|
| Cubo 2x2 | 19mm | 10-15mm |
| Cubo 2x4 | 19mm | 10-15mm |
| 3 bricks apilados | 29mm | 15-20mm |
| Bola | ~24mm | 12-16mm |
| Marcador en piso | 0mm | 5-12mm |

### Tubo oscuro

Piezas LEGO Technic alrededor del sensor que bloquean la luz ambiente. El sensor solo ve su propia luz reflejada. Muy efectivo.

## Resumen de estrategias

| Estrategia | Inmunidad | Para quién |
|-----------|-----------|------------|
| Tubo oscuro (hardware) | ⭐⭐⭐⭐⭐ | TODOS |
| HSV ignorando V | ⭐⭐⭐⭐ Alta | Elementary (en robot_lib) |
| Cromaticidad RGB normalizada | ⭐⭐⭐⭐⭐ Muy alta | Junior/Senior |
| Referencia blanca | ⭐⭐⭐⭐ Alta | Avanzados |
| Rechazo de outliers | ⭐⭐⭐ Media | TODOS |
| Sensor a altura de objeto | ⭐⭐⭐⭐⭐ Elimina contaminación | TODOS |

**Para IITA Elementary:** empezar con tubo oscuro + `detectable_colors()` calibrado + protocolo parar-leer. Las funciones avanzadas van en `robot_lib.py`.
