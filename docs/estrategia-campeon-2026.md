# Estrategia de Campeón — WRO Elementary 2026 "Robot Rockstars"

## Mentalidad de coach campeón mundial

> Los equipos que ganan el mundial de WRO no son los que tienen el robot más rápido ni el más complejo. Son los que tienen el robot **más confiable**. Un robot que hace 200 puntos en las 3 rondas le gana a uno que hace 255 en una ronda y 0 en las otras dos.

Este documento analiza las reglas del juego 2026 con la cabeza de un coach que quiere maximizar el puntaje **esperado**, no el puntaje máximo teórico.

---

## 1. Análisis del juego: desglose de puntos

### Tabla de scoring completa

| Misión | Puntos máx | Objetos | Dificultad | Fiabilidad requerida |
|--------|-----------|---------|------------|---------------------|
| 3.1 Cables en área gris | 30 | 2 cables, colocar verticales | Media | Alta (objetos delgados, deben quedar parados) |
| 3.2 Micrófono en área verde | 20 | 1 micrófono, colocar vertical | Media-Alta | Alta (debe quedar parado Y completamente adentro) |
| 3.2 Instrumentos en backstage | 45 | 3 instrumentos, empujar/llevar al área rosa | Baja-Media | Media (solo "completamente adentro", no necesitan estar parados) |
| 3.3 Notas en áreas de color | 120 | 6 notas, cada una a su color correspondiente | Alta | Muy alta (4 posiciones aleatorias, necesita detectar color) |
| 3.4 Bonus: no mover/dañar clave, altavoces, amplificador | 40 | 0 (no tocar) | Pasiva | Depende de ruta |
| **TOTAL** | **255** | | | |

### Análisis de retorno por esfuerzo

| Misión | Puntos | Complejidad mecánica | Complejidad software | Puntos/esfuerzo |
|--------|--------|---------------------|---------------------|----------------|
| Instrumentos al backstage | 45 | Baja (empujar) | Baja (navegar recto) | ⭐⭐⭐⭐⭐ Excelente |
| Bonus (no tocar cosas) | 40 | Nula | Media (ruta limpia) | ⭐⭐⭐⭐⭐ Excelente |
| Cables en área gris | 30 | Alta (colocar vertical) | Media | ⭐⭐⭐ Regular |
| Micrófono en target | 20 | Alta (colocar vertical) | Media | ⭐⭐ Bajo |
| 2 notas fijas (roja, verde) | 40 | Media (agarrar y llevar) | Media (posiciones conocidas) | ⭐⭐⭐⭐ Bueno |
| 4 notas aleatorias | 80 | Media (agarrar y llevar) | MUY ALTA (detectar color, decidir destino) | ⭐⭐ Bajo |

---

## 2. La estrategia: priorizar puntos fáciles y confiables

### Nivel 1: "Piso seguro" — 85 puntos, 95% de éxito esperado

**Objetivo:** Misiones que NO requieren manipulación precisa ni detección de color.

1. **Instrumentos al backstage (45 pts):** Los 3 instrumentos empiezan en el camión (esquina inferior). El backstage es el área rosa (esquina inferior izquierda). El robot solo necesita empujarlos. No necesitan estar parados ni orientados.

2. **Bonus completo (40 pts):** No tocar la clave (centro izquierda), los 2 altavoces (escenario), ni el amplificador (escenario). Requiere una ruta que evite estas piezas.

**¿Por qué esto primero?** Son 85 puntos con una mecánica simple (empujar) y sin detección de color. Si el robot solo hace esto, ya es competitivo.

### Nivel 2: "Escalar puntos" — +70 puntos = 155 total, 80% éxito

3. **Cables en área gris (30 pts):** Los cables están cerca del escenario. El robot los recoge y coloca en las áreas grises entre altavoces y amplificador. Puntos parciales (5 pts) si no quedan perfectos.

4. **Notas roja y verde (40 pts):** Estas dos notas tienen posición FIJA (no aleatoria). El robot sabe exactamente dónde están y adónde van. Es como los instrumentos pero con agarre+depósito.

### Nivel 3: "Ir a por todo" — +80 puntos = 235 total, 60% éxito

5. **4 notas aleatorias (80 pts):** Requiere detectar qué color tiene cada nota (negro, blanco, amarillo, azul) usando el sensor de color, y llevar cada una al área del color correspondiente. Las posiciones de origen son aleatorias (4 cuadrados verdes claros).

### Nivel 4: "Perfección" — +20 puntos = 255 total, 40% éxito

6. **Micrófono perfecto (20 pts):** Colocar el micrófono vertical y completamente dentro del área verde del escenario. La dificultad es que debe quedar parado.

---

## 3. Decisión estratégica: ¿cuántos niveles intentar?

### La matemática del campeón

Si tenemos 3 rondas y el mejor puntaje cuenta:

| Estrategia | Puntaje si sale bien | Probabilidad éxito | Puntaje esperado (3 rondas) |
|-----------|---------------------|--------------------|--------------------------|
| Solo Nivel 1 | 85 | 95% | ~85 (casi seguro) |
| Niveles 1+2 | 155 | 80% | ~148 (muy probable en al menos 1 ronda) |
| Niveles 1+2+3 | 235 | 60% | ~215 (probable en al menos 1 de 3) |
| Todo | 255 | 40% | ~230 (con suerte) |

**Recomendación: apuntar a Niveles 1+2+3 (235 pts) con fallback a 1+2 (155 pts)**

Programar el robot para intentar todo, pero si una misión falla, que siga con la siguiente en vez de quedarse trabado.

---

## 4. El problema central: las notas aleatorias

La misión 3.3 (notas) es donde se gana o pierde el campeonato. Analicemos:

### Notas fijas (roja y verde)
- Posiciones conocidas de antemano
- El robot va directo, agarra, lleva al destino
- No necesita sensor de color (ya sabemos qué color son)

### Notas aleatorias (negra, blanca, amarilla, azul)
- 4 notas repartidas aleatoriamente en 4 cuadrados verdes claros en la parte superior
- El robot necesita:
  1. Ir a cada cuadrado
  2. Leer el color de la nota
  3. Decidir adónde llevarla
  4. Llevarla al área correcta
  5. Repetir para las otras 3

### Opciones estratégicas para las notas aleatorias

**Opción A: Exploración secuencial (la más simple)**

El robot va a cada posición en orden, lee el color, y lleva la nota al destino. 4 viajes.

Ventaja: Simple de programar.
Desventaja: Lento (muchos viajes), riesgo de timeout en 2 minutos.

**Opción B: Exploración primero, acción después (la más inteligente)**

El robot primero recorre las 4 posiciones SIN tocar las notas, solo leyendo colores. Guarda en memoria qué nota está en qué posición. Luego planifica la ruta óptima y recoge/entrega en el orden más eficiente.

Ventaja: Ruta más corta, menos viajes.
Desventaja: Requiere más programación (memoria, planificación).

**Opción C: Ignorar el color (puntaje parcial)**

Llevar las 4 notas a cualquier área de color. Si por casualidad alguna coincide, suma puntos. Si no, 0 puntos por nota incorrecta.

Ventaja: No necesita sensor de color.
Desventaja: 0 puntos garantizados (el color incorrecto no suma).

**Recomendación: Opción B** (explorar primero) si el equipo tiene nivel. **Opción A** como fallback si no hay tiempo.

---

## 5. Diseño mecánico: principios de confiabilidad

### El robot ideal para esta misión

**Necesidades mecánicas:**
1. **Empujador frontal ancho** — para empujar instrumentos al backstage sin que se escapen por los costados
2. **Mecanismo de agarre** — para levantar/transportar notas, cables y micrófono
3. **Mecanismo de depósito** — para soltar objetos en posición vertical (los cables y el micrófono necesitan quedar parados)
4. **Sensor de color bajo** — para seguir líneas del tapete
5. **Sensor de color a altura de objeto** — para leer el color de las notas (diferente altura que el de líneas)

### Restricciones WRO 2026 Elementary

| Restricción | Valor |
|-------------|-------|
| Tamaño máximo al inicio | 25×25×25 cm |
| Peso máximo | 1500 g |
| Motores máximos | 4 |
| Sensores | Sin límite de cantidad |
| Cámaras | ❌ Prohibidas en Elementary |
| Controladores | 1 (no se permite más de 1 hub) |
| Tiempo por ronda | 2 minutos |

### Distribución de motores (4 disponibles)

| Opción | Motor A | Motor B | Motor C | Motor D |
|--------|---------|---------|---------|--------|
| **A: Garra simple** | Tracción izq | Tracción der | Garra (abrir/cerrar) | Brazo (subir/bajar) |
| **B: Pala frontal** | Tracción izq | Tracción der | Pala (subir/bajar) | Garra auxiliar |
| **C: Minimalista** | Tracción izq | Tracción der | Garra multiuso | *(libre para sensor?)* |

**Recomendación: Opción A** — Garra + Brazo da máxima versatilidad para agarrar notas, cables y micrófono, y depositarlos verticales.

### Principios de construcción robusta

**1. Centro de gravedad bajo**
El hub SPIKE y la batería son lo más pesado. Ponerlos lo más abajo y centrado posible. Un robot con centro de gravedad alto se cae en giros rápidos.

**2. Chasis rígido, mecanismo flexible**
El chasis (tracción + hub) debe ser absolutamente rígido — sin juego, sin partes que se muevan. El mecanismo (garra) puede tener algo de flexibilidad para adaptarse a objetos.

**3. Ruedas grandes, tracción directa**
Ruedas de 56mm o 62.4mm sin engranajes de reducción. Los engranajes agregan juego (backlash) y puntos de falla. Si necesitás más torque, usá ruedas más chicas.

**4. Punto de contacto en el giro**
Usar 2 ruedas de tracción + 1 rueda loca trasera (o delantera), NO 4 ruedas. Con 4 ruedas, al girar las ruedas traseras arrastran y el giro es impreciso.

**5. Mecanismo pasivo vs activo**
Siempre preferir mecanismos pasivos (que funcionan por geometría) sobre activos (que dependen de un motor):
- Empujador: pasivo (el robot empuja con su cuerpo)
- Garra: activa (necesita motor)
- Guía para depositar: pasiva (rampa o canal que orienta el objeto)

**6. Tolerance al error de posición**
El mecanismo debe funcionar aunque el robot esté 5-10mm desviado del punto ideal. Una garra ancha que se cierra es más tolerante que una pinza fina.

**7. Repetibilidad del mecanismo**
Cada acción mecánica (abrir garra, subir brazo) debe dar el mismo resultado las 10 veces que la probés. Si a veces funciona y a veces no, hay un problema mecánico que DEBÉS resolver antes de programar.

---

## 6. Diseño de software: programación por misiones

### Arquitectura de programa

```
main.py
├── init_robot()          ← Calibrar gyro, sensores, perfiles
├── esperar_inicio()      ← Botón centro
├── mision_instrumentos() ← 45 pts (Nivel 1)
├── mision_cables()       ← 30 pts (Nivel 2)
├── mision_notas_fijas()  ← 40 pts (Nivel 2)
├── mision_notas_random() ← 80 pts (Nivel 3)
├── mision_microfono()    ← 20 pts (Nivel 4)
└── fin()                 ← Volver a base
```

Cada misión es una función independiente. Si una falla, el programa salta a la siguiente en vez de quedarse trabado.

### Programación defensiva

```python
def mision_instrumentos():
    try:
        # Navegar al camión
        # Empujar instrumentos al backstage
        pass
    except:
        # Si algo sale mal, parar y seguir con la siguiente misión
        robot.stop()
        print("ERROR en instrumentos, continuando...")

def ejecutar_misiones():
    cronometro = StopWatch()
    
    mision_instrumentos()      # 45 pts
    if cronometro.time() > 80000:  # Si pasaron 80s, saltar al final
        return
    
    mision_cables()            # 30 pts
    if cronometro.time() > 100000:
        return
    
    mision_notas_fijas()       # 40 pts
    if cronometro.time() > 110000:
        return
    
    mision_notas_random()      # 80 pts
```

### Control de tiempo

El robot debe saber cuánto tiempo le queda. Si quedan menos de 20 segundos y está en medio de una misión difícil, es mejor abandonarla y asegurar que no está tocando objetos de bonus cuando termine el tiempo.

---

## 7. Manejo de la randomización

Las 4 notas aleatorias son el desafío principal. Opciones:

### Escaneo previo (la estrategia campeón)

```python
def escanear_notas():
    """Recorre las 4 posiciones y lee qué color hay en cada una."""
    posiciones = [
        (x1, y1),  # Cuadrado verde 1
        (x2, y2),  # Cuadrado verde 2
        (x3, y3),  # Cuadrado verde 3
        (x4, y4),  # Cuadrado verde 4
    ]
    mapa_notas = {}  # {posicion: color}
    
    for i, (x, y) in enumerate(posiciones):
        navegar_a(x, y)
        robot.stop()
        wait(200)
        color = leer_color_preciso(sensor)
        mapa_notas[i] = color
        feedback_color(hub, color)
    
    return mapa_notas

def planificar_ruta(mapa_notas):
    """Calcula el orden óptimo de recolección."""
    # Ordenar por cercanía al destino correspondiente
    # Minimizar distancia total recorrida
    pass
```

---

## 8. Lista de pruebas: qué probar antes de competir

### Pruebas mecánicas (sin programa)

- [ ] La garra agarra y suelta notas de forma repetible (10/10 veces)
- [ ] El brazo sube y baja al mismo ángulo (medir con transportador)
- [ ] Al empujar instrumentos, ninguno se escapa por los costados
- [ ] Las ruedas no patinan en el tapete de competencia
- [ ] El robot cabe en 25×25×25 cm con mecanismo cerrado
- [ ] El robot pesa menos de 1500g

### Pruebas de navegación (programa básico)

- [ ] Avanzar 1000mm → medir real (calibrar wheel_diameter)
- [ ] Girar 3600° → queda alineado (calibrar axle_track)
- [ ] Girar 360° a mano → leer heading (calibrar heading_correction)
- [ ] Seguir línea recta 500mm sin desviarse >5mm
- [ ] Girar 90° preciso (medir con escuadra)

### Pruebas de misión (programa completo)

- [ ] Misión instrumentos: 10 intentos, cuántas veces suma 45 puntos?
- [ ] Misión cables: 10 intentos, cuántas veces suma 30 puntos?
- [ ] Misión notas fijas: 10 intentos, cuántas veces suma 40 puntos?
- [ ] Misión notas aleatorias: 10 intentos con CADA randomización posible
- [ ] Programa completo: 10 intentos, registrar puntaje y tiempo de cada uno
- [ ] Bonus: en las 10 pruebas, cuántas veces se mantiene el bonus completo?

### Prueba de estrés

- [ ] Ejecutar el programa 5 veces seguidas SIN tocar el robot entre ejecuciones
- [ ] Ejecutar con batería al 30% (simula batería baja en competencia)
- [ ] Ejecutar en una mesa diferente (simula mesa de competencia)
- [ ] Ejecutar con las 24 combinaciones posibles de randomización de notas

---

## 9. Plan de entrenamiento semanal

### Semana 1-2: Mecánica
- Diseñar y construir el chasis base (tracción + hub)
- Probar que anda recto con gyro
- Diseñar y construir el mecanismo de garra/brazo
- Probar que agarra notas de forma repetible

### Semana 3-4: Navegación
- Calibrar odometría completa
- Programar funciones básicas (ir_a_punto, girar, seguir_linea)
- Mapear el tapete: coordenadas de cada zona

### Semana 5-6: Misiones fáciles
- Programar y probar misión instrumentos (45 pts)
- Programar y probar misión cables (30 pts)
- Probar bonus (40 pts) — ajustar ruta para no tocar piezas

### Semana 7-8: Misiones difíciles
- Programar misión notas fijas (40 pts)
- Calibrar sensor de color para las 6 notas
- Programar misión notas aleatorias (80 pts)
- Probar con TODAS las randomizaciones

### Semana 9-10: Integración y robustez
- Unir todas las misiones en un programa
- Agregar control de tiempo
- Pruebas de estrés (50+ ejecuciones)
- Ajustar velocidades y tiempos

### Semana 11-12: Competencia simulada
- Simular formato de competencia (3 rondas, randomización)
- Practicar rutina pre-ronda (calibrar, posicionar, verificar)
- El equipo debe ser capaz de hacer todo SIN el coach

---

## 10. Errores fatales que cometen equipos novatos

| Error | Por qué es fatal | Solución |
|-------|-----------------|----------|
| Robot complejo que falla | 0 puntos en 2 de 3 rondas | Priorizar confiabilidad sobre puntos máximos |
| No calibrar en el lugar | El tapete de competencia es diferente al de práctica | Calibrar odometría y colores en la mesa real |
| No probar todas las randomizaciones | La combinación que nunca probaron es la que sale en la ronda | Probar las 24 combinaciones posibles |
| Gastar los 2 minutos en una misión difícil | Pierden las misiones fáciles que ya funcionaban | Control de tiempo con timeouts por misión |
| Mecanismo frágil | Se rompe entre rondas, no hay tiempo de reparar | Construcción robusta, piezas de repuesto preparadas |
| Solo el coach sabe cómo funciona | Los jueces preguntan a los ALUMNOS, no al coach | Los alumnos deben entender y explicar todo |
| No tener plan B | Si la misión 3 falla, se pierden | Cada misión es independiente, saltear si falla |

---

## 11. El checklist del día de competencia

### Antes de cada ronda

- [ ] Verificar batería >70%
- [ ] Verificar que todas las piezas están firmes
- [ ] Verificar que la garra abre y cierra bien
- [ ] Calibrar sensor de color en el tapete oficial
- [ ] Verificar heading del gyro (debe ser 0 al inicio)
- [ ] Verificar que el programa correcto está cargado
- [ ] Verificar el tamaño del robot (25×25×25)
- [ ] Verificar la randomización de las notas (MIRAR qué color hay en cada posición)

### Durante la ronda

- El equipo NO toca el robot después de presionar el botón de inicio
- Observar qué misiones completó y cuáles falló
- Anotar mentalmente qué ajustar para la próxima ronda

### Entre rondas

- Analizar qué falló (mecánico? navegación? sensor?)
- Si fue mecánico → reparar
- Si fue navegación → recalibrar
- Si fue sensor → recalibrar colores en el tapete oficial
- Si fue tiempo → considerar saltear misión difícil

---

## 12. Estimación de puntaje realista para IITA

| Escenario | Puntaje estimado | Condiciones |
|-----------|-----------------|-------------|
| Conservador | 85-125 | Instrumentos + bonus + cables parcial |
| Realista | 155-195 | + notas fijas + cables completos |
| Optimista | 195-235 | + algunas notas aleatorias |
| Campeón | 235-255 | Todo, incluyendo micrófono perfecto |

**Meta IITA 2026: 155-195 puntos de forma confiable (2 de 3 rondas).**

Eso nos posiciona competitivamente a nivel nacional. Para el mundial, necesitamos estar en el rango 195-235.
