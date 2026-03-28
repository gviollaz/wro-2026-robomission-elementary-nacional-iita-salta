# Diseño para 255/255 — Robot Rockstars WRO Elementary 2026

## Filosofía: diseñar para el máximo desde el día 1

> Un robot diseñado para 155 puntos que después querés que haga 255 va a fallar. Los mecanismos, la distribución de motores, la posición de sensores — todo cambia si apuntás al máximo. Diseñá el robot para 255 desde el principio, y después decidí cuántas misiones activar según la confiabilidad que logres.

Este documento reemplaza la versión conservadora. Acá diseñamos para ganar, no para participar.

---

## 1. Mapa del juego con coordenadas

```
     PARED SUPERIOR (railing 5cm)
  ┌──────────────────────────────────────────────────────────┐
  │                                                          │
  │  ♪₁  ♪₂  ♪₃  ♪₄   ← 4 notas aleatorias (cuadrados     │
  │  [?] [?] [?] [?]      verdes claros, parte superior)    │
  │                                                          │
  │  ♫ Nota ROJA (fija)        ♫ Nota VERDE (fija)          │
  │                                                          │
  │  ═══════════════════════════  ← Líneas del pentagrama    │
  │  🎼 Clave  [R][Az][Ve][Am][Bl][Ne] ← Destino notas     │
  │                                                          │
  │  🔊──[AMP]──🔊   ← Amplificador + 2 altavoces          │
  │    [gris][gris]   ← Áreas grises para cables            │
  │                                                          │
  │  ┌─────────────┐  ← Escenario                           │
  │  │ 🎤 target   │  ← Área verde para micrófono           │
  │  └─────────────┘                                         │
  │                                                          │
  │  ┌──BACKSTAGE──┐  ← Área rosa (destino instrumentos)    │
  │  │  (pink)     │                                         │
  │  └─────────────┘                                         │
  │                                                          │
  │  🎸🎹🥁🎤      ← Camión con instrumentos + micrófono   │
  │  [TRUCK]        (inicio, esquina inferior derecha)       │
  │                                        ┌──────┐          │
  │                                        │START │          │
  │                                        │AREA  │          │
  │                                        └──────┘          │
  └──────────────────────────────────────────────────────────┘
     PARED INFERIOR (railing 5cm)
```

---

## 2. Presupuesto de tiempo: 120 segundos para 255 puntos

Los equipos que hacen 255 tienen cada segundo planificado. Analicemos cuánto tarda cada acción:

| Acción | Tiempo estimado | Acumulado |
|--------|----------------|-----------|
| Init (gyro, sensores) | 3s | 3s |
| Esperar botón + arrancar | 1s | 4s |
| Ir al camión, cargar instrumentos | 8s | 12s |
| Llevar instrumentos al backstage | 10s | 22s |
| Ir a cables, recoger cable 1 | 8s | 30s |
| Colocar cable 1 en área gris | 6s | 36s |
| Recoger cable 2 | 6s | 42s |
| Colocar cable 2 en área gris | 6s | 48s |
| Recoger micrófono del camión | 8s | 56s |
| Colocar micrófono vertical en target | 8s | 64s |
| **Escaneo**: recorrer 4 posiciones aleatorias leyendo color | 15s | 79s |
| Recoger nota roja (fija) + llevar a destino | 10s | 89s |
| Recoger nota verde (fija) + llevar a destino | 10s | 99s |
| Recoger 2 notas aleatorias (ruta optimizada) | 15s | 114s |
| Recoger 2 notas aleatorias restantes | 15s | **129s ⚠️** |

**Problema:** No alcanza con rutas secuenciales. Necesitamos optimizar.

### Optimizaciones que hacen los campeones

**1. Carga múltiple:** El robot carga 2-3 objetos a la vez en vez de ir y volver por cada uno. Esto requiere un mecanismo de almacenamiento (container/bandeja).

**2. Ruta combinada:** En el mismo viaje que lleva instrumentos al backstage, al volver recoge un cable. No hay viajes vacíos.

**3. Escaneo integrado:** Al pasar por las posiciones de notas para hacer otra misión, lee los colores de paso (sin detenerse extra para escanear).

**4. Priorización por cercanía:** Después del escaneo, el software calcula qué nota llevar primero según la distancia al destino.

### Presupuesto optimizado

| Acción | Tiempo |
|--------|--------|
| Init + arrancar | 4s |
| Viaje 1: Start → camión → cargar 3 instrumentos + micrófono → empujar instrumentos al backstage | 18s |
| Viaje 2: Backstage → escenario → colocar micrófono → recoger cable 1 → colocar cable 1 | 16s |
| Viaje 3: Cable 2 → colocar cable 2 | 10s |
| Viaje 4: Escaneo rápido de 4 notas (sin parar, leer al pasar) | 10s |
| Viaje 5: Nota fija roja + 1 nota aleatoria cercana → depositar ambas | 14s |
| Viaje 6: Nota fija verde + 1 nota aleatoria cercana → depositar ambas | 14s |
| Viaje 7: 2 notas aleatorias restantes → depositar | 14s |
| Volver a base (evitar tocar bonus objects) | 6s |
| **Total** | **106s** ✅ |
| **Margen de seguridad** | **14s** |

Esto solo funciona si el robot puede **cargar 2 objetos al mismo tiempo** en algunos viajes.

---

## 3. Mecanismo: el diseño que permite 255

### El concepto: "Garra articulada con container"

```
Vista lateral del robot:

        ┌───[Sensor color ALTO]──── Para leer notas
        │
  ┌─────┤ BRAZO (Motor D, sube/baja)
  │     │
  │     └──[GARRA] (Motor C, abre/cierra)
  │         │
  │    ┌────┴────┐
  │    │CONTAINER│  ← Zona de carga (puede tener 2 objetos)
  │    └─────────┘
  │  ┌──────────────┐
  │  │  SPIKE HUB   │
  │  │ (horizontal) │
  │  └──────────────┘
  │  [Motor A]──⊙──[Motor B]
  │    ↑              ↑
  └──[Sensor color BAJO]──── Para seguir líneas
       │              │
      ◎ Rueda izq    ◎ Rueda der
           ◎ Rueda loca (atrás)
```

### Distribución de 4 motores

| Motor | Puerto | Función | Tipo |
|-------|--------|---------|------|
| Tracción izquierda | A | Mover robot | Motor Grande |
| Tracción derecha | B | Mover robot | Motor Grande |
| Garra | C | Abrir/cerrar para agarrar objetos | Motor Mediano |
| Brazo | D | Subir/bajar garra (3 posiciones) | Motor Mediano |

### 3 posiciones del brazo

| Posición | Ángulo | Para qué |
|----------|--------|----------|
| ABAJO | 0° | Agarrar objetos del piso, empujar instrumentos |
| TRANSPORTE | -45° | Llevar objetos levantados (no arrastran) |
| ALTO | -90° | Depositar objetos en posición elevada, leer color de notas |

### Garra: diseño para objetos variados

Los objetos del juego tienen formas muy diferentes (notas con base, cables cilíndricos, micrófono con base, instrumentos). La garra debe ser **ancha y adaptable**.

**Principio clave:** Garra tipo "V" o "U" que se cierra. Los laterales en V guían el objeto al centro aunque el robot no esté perfectamente alineado. Esto da **tolerancia de ±10mm** en posicionamiento.

```
Vista superior de la garra:

  Abierta:           Cerrándose:        Cerrada:
  
  ╲             ╱    ╲           ╱      ╲    ╱
   ╲           ╱      ╲  [obj] ╱        ╲[o]╱
    ╲         ╱        ╲      ╱          ╲ ╱
     ╲       ╱          ╲    ╱            V
```

### El container/bandeja trasera

Para cargar 2 objetos simultáneamente, una bandeja o zona de contención detrás de la garra. Cuando la garra agarra un objeto y el brazo sube, lo deposita en el container. Luego la garra puede bajar y agarrar otro.

Esto es crítico para los viajes combinados que permiten hacer todo en 106 segundos.

### Depositado vertical (cables y micrófono)

Los cables y el micrófono necesitan quedar **parados** para puntaje máximo (15 y 20 pts vs 5 y 10 pts parcial). Esto es el desafío mecánico más difícil.

**Solución 1: Depósito por gravedad controlada**
La garra sujeta el objeto vertical. El brazo lo baja hasta que la base toque el piso. La garra abre lentamente. El objeto queda parado por su propio peso.

**Requisitos:**
- La garra debe sujetar el objeto en su punto medio o superior (no en la base)
- El brazo debe bajar LENTO (velocidad 100°/s, no 300)
- El piso debe estar limpio (no hay inclinación en el tapete WRO)

**Solución 2: Guía con rampa integrada**
Un canal en la garra guía el objeto a posición vertical al soltarlo.

### Empujador frontal para instrumentos

Los instrumentos solo necesitan estar "completamente adentro" del backstage, sin estar parados. El robot puede empujarlos. Un empujador frontal ancho (toda la parte delantera del robot) empuja los 3 instrumentos juntos desde el camión hasta el backstage.

**Diseño dual:** El empujador es la posición ABAJO de la garra abierta. Cuando la garra está abierta y el brazo abajo, el frente del robot actúa como empujador.

---

## 4. Sensores: ubicación estratégica

### 2 sensores de color (mínimo recomendado)

| Sensor | Puerto | Posición | Altura | Función |
|--------|--------|----------|--------|---------|
| Sensor PISO | E | Frente-centro, entre ruedas | 8mm del piso | Seguir líneas, detectar zonas de color del tapete |
| Sensor OBJETOS | F | En el brazo/garra | Móvil (sube con brazo) | Leer color de notas a distancia 10-15mm |

### ¿Por qué 2 sensores?

Un solo sensor no puede hacer ambas cosas bien:
- Leer líneas del piso requiere altura 8mm, apuntando abajo
- Leer color de notas requiere apuntar al objeto (horizontal), a la altura de la nota (~20-30mm del piso)

Si usás un solo sensor, tenés que elegir: ¿sigo líneas O leo colores de objetos? Con dos sensores, hacés ambas cosas sin compromisos.

### Sensor de color de notas: montaje en el brazo

El sensor F va montado en el brazo, apuntando hacia adelante. Cuando el brazo sube a posición ALTO, el sensor queda a la altura de las notas y puede leer su color desde ~15mm de distancia.

```
Brazo ABAJO:                    Brazo ALTO:
  [sensor] apunta al piso       [sensor]→ apunta a la nota
  │                                      │
  └── no sirve para notas               ♪ nota (lee color)
```

---

## 5. Software: arquitectura para 255

### Modo de configuración adaptativo

Antes de cada ronda, el equipo observa la randomización (qué color en qué posición) y selecciona el programa correspondiente O ejecuta el escaneo automático.

**Opción A: Pre-programar las 24 combinaciones**

Solo hay 24 formas posibles de distribuir 4 notas en 4 posiciones. Se puede pre-calcular la ruta óptima para cada combinación.

```python
RUTAS_OPTIMAS = {
    # (pos1, pos2, pos3, pos4): orden de recogida
    ("NEGRO", "BLANCO", "AMARILLO", "AZUL"): [3, 0, 1, 2],
    ("NEGRO", "BLANCO", "AZUL", "AMARILLO"): [3, 0, 2, 1],
    # ... las 24 combinaciones
}
```

El equipo mira la randomización, carga el programa correspondiente. No pierde tiempo escaneando.

**Ventaja:** 10-15 segundos ahorrados (no hay escaneo).
**Desventaja:** Necesita 24 programas o un menú de selección.

**Opción B: Escaneo automático + routing dinámico (más robusto)**

```python
def escanear_y_planificar():
    mapa = {}
    for i, pos in enumerate(POSICIONES_NOTAS):
        navegar_a(pos)
        brazo_alto()  # Sensor a altura de nota
        wait(200)
        color = leer_color_preciso(sensor_objetos)
        mapa[i] = color
        brazo_transporte()
    
    # Calcular ruta óptima (nearest-neighbor heuristic)
    ruta = calcular_ruta_optima(mapa, DESTINOS_NOTAS)
    return ruta
```

**Recomendación para 255:** Opción B con Opción A como fallback. El escaneo automático es más robusto ante errores de lectura (puede re-leer si no está seguro).

### Estructura del programa principal

```python
from pybricks.tools import StopWatch

crono = StopWatch()

def hay_tiempo(necesito_ms):
    return (120000 - crono.time()) > necesito_ms

# === MISIONES EN ORDEN OPTIMIZADO ===

init_robot()
esperar_inicio()
crono.reset()

# Viaje 1: Instrumentos + micrófono (65 pts potenciales)
if hay_tiempo(18000):
    viaje_instrumentos_y_microfono()

# Viaje 2-3: Cables (30 pts)
if hay_tiempo(26000):
    viaje_cables()

# Viaje 4: Escaneo de notas aleatorias
if hay_tiempo(10000):
    mapa_notas = escanear_notas()

# Viaje 5-7: 6 notas (120 pts)
if hay_tiempo(42000):
    viaje_notas(mapa_notas)

# Asegurar no tocar objetos bonus al terminar
retirar_a_zona_segura()
```

### Detección de color de notas: el desafío

Las notas tienen 6 colores: rojo, azul, verde, amarillo, blanco, negro. Las bases son todas iguales, el color está en la parte superior.

**Problema 1:** Negro y blanco son difíciles (bajo contraste HSV).
**Problema 2:** La nota azul y la nota negra pueden confundirse en salas oscuras.

**Solución:** Usar `detectable_colors()` calibrado SOLO con los 4 colores aleatorios (negro, blanco, amarillo, azul). No incluir rojo ni verde (esos son fijos, no necesitan detección).

```python
# Solo los 4 colores que necesitamos detectar
Color.MI_NEGRO   = Color(h=0, s=5, v=8)      # CALIBRAR
Color.MI_BLANCO  = Color(h=0, s=5, v=95)     # CALIBRAR
Color.MI_AMARILLO = Color(h=55, s=65, v=90)  # CALIBRAR
Color.MI_AZUL    = Color(h=218, s=85, v=50)  # CALIBRAR

sensor_objetos.detectable_colors((
    Color.MI_NEGRO, Color.MI_BLANCO,
    Color.MI_AMARILLO, Color.MI_AZUL,
    Color.NONE
))
```

Con solo 4 colores (+ NONE), la discriminación es mucho mejor que con 6.

---

## 6. Ruta maestra: el recorrido de 255 puntos

```
START (esquina inferior derecha)
  │
  ▼ Viaje 1: Start → Camión
  ├── Agarrar micrófono (garra, brazo transporte)
  ├── Empujar 3 instrumentos al backstage (empujador frontal)
  ├── Depositar micrófono en área verde del escenario (brazo baja, garra suelta)
  │
  ▼ Viaje 2: Escenario → Cables
  ├── Agarrar cable 1 (cerca del escenario superior)
  ├── Colocar cable 1 vertical en área gris
  ├── Agarrar cable 2 (cerca del escenario inferior)
  ├── Colocar cable 2 vertical en área gris
  │
  ▼ Viaje 3: Escaneo (pasando por las 4 posiciones de notas)
  ├── Leer color nota posición 1 (brazo alto, sensor apunta)
  ├── Leer color nota posición 2
  ├── Leer color nota posición 3
  ├── Leer color nota posición 4
  ├── Calcular ruta óptima
  │
  ▼ Viaje 4-6: Recoger y depositar 6 notas
  ├── Nota roja (fija) → destino rojo
  ├── Nota verde (fija) → destino verde
  ├── 4 notas aleatorias → destinos correspondientes
  │   (orden optimizado por cercanía al destino)
  │
  ▼ Retorno: Zona segura (no tocar bonus objects)
  └── Parar lejos de clave, altavoces, amplificador
```

---

## 7. Robustez mecánica: los 10 mandamientos

1. **Triangulación estructural.** Cada conexión LEGO Technic debe formar triángulos. Nunca rectángulos solos (se deforman bajo carga).

2. **Ejes con topes en ambos extremos.** Todo eje debe tener un bush o half-bush en ambos lados del punto donde se apoya. Si falta un tope, el eje se desliza con vibraciones.

3. **Engranajes con anti-backlash.** Si usás engranajes, agregar un segundo engranaje con resorte que presione contra el primero. Elimina el juego.

4. **Cables LEGO organizados.** Los cables (del hub a motores/sensores) deben estar fijados con clips o pasados por agujeros Technic. Un cable suelto se engancha en objetos del tapete.

5. **Garra con superficie de agarre.** Pegar goma (rueda LEGO cortada) en las superficies internas de la garra. La goma aumenta la fricción y evita que el objeto se resbale.

6. **Ruedas limpias antes de cada ronda.** Pasar un paño húmedo por las ruedas elimina polvo que causa patinaje.

7. **Sensor de color protegido.** Un anillo de piezas oscuras alrededor del sensor de piso elimina interferencia de luz ambiente. Para el sensor de objetos, un tubo corto.

8. **Hub montado con amortiguación.** Intercalar una capa de pines flexibles entre el hub y el chasis. Las vibraciones del movimiento no llegan al giroscopio.

9. **Motor del brazo con reducción.** El brazo debe tener reducción de engranajes (al menos 3:1) para que tenga torque suficiente para levantar objetos sin esforzar el motor. Un motor mediano con reducción 3:1 sostiene cualquier objeto WRO sin problemas.

10. **Test de caída de 10cm.** Si el robot se cae de 10cm (la altura de la mesa al piso si se resbala), ¿se desarma? Si sí, reforzar las uniones.

---

## 8. Detalle de las 24 randomizaciones

Las 4 notas aleatorias (N=negro, B=blanco, A=amarillo, Z=azul) se distribuyen en 4 posiciones. Hay P(4,4) = 24 combinaciones:

| # | Pos1 | Pos2 | Pos3 | Pos4 | Ruta sugerida |
|---|------|------|------|------|---------------|
| 1 | N | B | A | Z | 1→4→2→3 |
| 2 | N | B | Z | A | 1→3→2→4 |
| 3 | N | A | B | Z | 1→4→3→2 |
| ... | ... | ... | ... | ... | ... |
| 24 | Z | A | B | N | 4→1→3→2 |

La ruta óptima depende de las posiciones de las notas Y las posiciones de los destinos en el pentagrama. El programa debe calcular el nearest-neighbor path para minimizar distancia total.

**Tip de campeón:** Ensayar las combinaciones más difíciles (donde los destinos están lejos de las fuentes). Si las peores combinaciones funcionan, las fáciles van a funcionar seguro.

---

## 9. Plan de pruebas para 255

### Fase 1: Mecánica (antes de programar)

| Prueba | Criterio de éxito | Intentos |
|--------|-------------------|----------|
| Garra agarra nota y la suelta parada | 10/10 éxitos | 10 |
| Garra agarra cable y lo suelta parado | 10/10 éxitos | 10 |
| Garra agarra micrófono y lo suelta parado | 10/10 éxitos | 10 |
| Empujador lleva 3 instrumentos sin que se escapen | 10/10 éxitos | 10 |
| Brazo sube y baja al mismo ángulo (±2°) | 10/10 | 10 |
| Robot cabe en 25×25×25 | Sí/No | 1 |
| Robot pesa < 1500g | Sí/No | 1 |

### Fase 2: Navegación

| Prueba | Criterio | Intentos |
|--------|----------|----------|
| Ir de Start a cada zona del tapete y volver | < 3mm error | 5 por zona |
| Giro de 90° preciso | < 2° error | 20 |
| Recorrido completo sin tocar objetos bonus | 0 contactos | 10 |
| Seguir línea del pentagrama | Sin perder la línea | 10 |

### Fase 3: Misiones individuales

| Misión | Puntaje esperado | Criterio | Intentos |
|--------|-----------------|----------|----------|
| Instrumentos | 45/45 | 10/10 rondas | 10 |
| Cables | 30/30 (ambos verticales) | 8/10 rondas | 10 |
| Micrófono | 20/20 (vertical) | 7/10 rondas | 10 |
| Notas fijas | 40/40 | 9/10 rondas | 10 |
| Notas aleatorias | 80/80 | 6/10 rondas | 10 por randomización |
| Bonus | 40/40 | 9/10 rondas | 10 |

### Fase 4: Programa completo

| Prueba | Criterio | Intentos |
|--------|----------|----------|
| Programa completo, randomización aleatoria | > 230 pts promedio | 30 |
| Peor randomización | > 200 pts | 10 |
| Con batería al 30% | > 200 pts | 5 |
| En mesa diferente | > 200 pts | 10 |
| Las 24 randomizaciones | > 220 pts en todas | 24 |

---

## 10. Gestión de riesgo: qué hacer cuando algo falla

| Situación | Acción del programa | Puntos que se pierden |
|-----------|--------------------|-----------------------|
| Garra no agarra la nota | Reintentar 1 vez, si falla skip | 20 pts de esa nota |
| Sensor lee color incorrecto | Tomar 7 lecturas con rechazo outliers | Prevención |
| Robot chocó un altavoz | Parar, recalcular ruta evitándolo | 10 pts bonus |
| Tiempo < 30s y faltan 3 notas | Abandonar notas, asegurar retiro limpio | 60 pts notas pero salva bonus |
| Micrófono no queda parado | Aceptar 10 pts parciales, seguir | 10 pts |
| Cable no queda parado | Aceptar 5 pts parciales, seguir | 10 pts |

### El programa nunca se queda trabado

Cada acción tiene timeout. Si la garra no logra agarrar en 3 segundos, suelta y sigue. Si el robot no llega a una posición en 8 segundos, se detiene y recalcula.

```python
def accion_con_timeout(funcion, timeout_ms=5000):
    """Ejecuta una acción con timeout. Si falla, retorna False."""
    crono = StopWatch()
    try:
        resultado = funcion()
        if crono.time() > timeout_ms:
            robot.stop()
            return False
        return resultado
    except:
        robot.stop()
        return False
```

---

## 11. La diferencia entre 235 y 255: los detalles

Los últimos 20 puntos (micrófono perfecto + cables perfectos) son los más difíciles porque requieren que objetos queden **verticales**. Acá es donde los equipos top se diferencian.

### Secreto #1: Soltar desde la posición correcta

No soltar el objeto cuando la garra está alta. Bajar el brazo hasta que la base del objeto toque el piso, y DESPUÉS abrir la garra. Así el objeto ya está apoyado cuando lo soltás.

### Secreto #2: Velocidad de apertura de garra

Abrir la garra LENTO (100°/s en vez de 300°/s). Si abrís rápido, el movimiento sacude al objeto y lo tumba.

### Secreto #3: Retirarse sin tocar

Después de soltar, retroceder 5mm antes de girar. Si girás inmediatamente, la esquina del robot puede rozar el objeto y tumbarlo.

### Secreto #4: Posicionamiento con margen

No posicionar el objeto en el centro exacto del área target. Posicionar ligeramente hacia el interior (5mm hacia el centro del área). Así, incluso si hay un pequeño error, el objeto queda "completamente adentro" en vez de tocar el borde.

---

## 12. Actualización de la definición del robot

La definición en `hardware/robot-definition.md` necesita actualizarse para reflejar este diseño:

### Puertos actualizados

| Puerto | Dispositivo | Uso |
|--------|-------------|-----|
| A | Motor Grande (tracción izq) | DriveBase |
| B | Motor Grande (tracción der) | DriveBase |
| C | Motor Mediano (garra) | Abrir/cerrar con velocidad variable |
| D | Motor Mediano (brazo) | 3 posiciones: abajo/transporte/alto, con reducción 3:1 |
| E | Sensor Color (piso) | Seguir líneas, detectar zonas, a 8mm del piso |
| F | Sensor Color (objetos) | Montado en brazo, lee notas a 15mm, sube con brazo |

### Parámetros del mecanismo

| Parámetro | Valor |
|-----------|-------|
| Brazo posición ABAJO | 0° |
| Brazo posición TRANSPORTE | -45° (ajustar) |
| Brazo posición ALTO | -90° (ajustar) |
| Brazo velocidad depósito | 100°/s (LENTO para vertical) |
| Brazo velocidad normal | 300°/s |
| Garra apertura completa | 90° |
| Garra velocidad depósito | 100°/s (LENTO para vertical) |
| Garra velocidad normal | 300°/s |
| Reducción brazo | 3:1 mínimo |
