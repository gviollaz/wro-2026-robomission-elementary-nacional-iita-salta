# Arquitecturas de robot para WRO RoboMission Elementary 2026

## Objetivo

Este documento propone **3 arquitecturas concretas de robot** para **WRO RoboMission Elementary 2026 - Robot Rockstars**, pensadas para el contexto real de este repo:

- LEGO Spike Prime
- firmware Pybricks
- 2 motores grandes de traccion
- 1 motor mediano para accesorio
- 1 sensor de color

La idea no es decir que existe un unico robot correcto. La idea es mostrar que, para este tablero, hay **distintas formas inteligentes de construir**, segun el nivel del equipo y la estrategia de puntaje.

---

## 1. Punto de partida comun a las 3 propuestas

Antes de comparar arquitecturas, hay una recomendacion base que vale para casi todos los equipos de Elementary 2026:

> **usar una base diferencial de 2 ruedas motrices + 1 apoyo pasivo, compacta, baja y rigida.**

### Por que esta base tiene sentido
Pybricks modela de forma natural un `DriveBase` con **dos ruedas motrices y un apoyo pasivo o caster**, y ademas deja muy claro que las distancias y giros son estimaciones que dependen de `wheel_diameter` y `axle_track`, por lo que una base simple y bien calibrada suele dar mejor repetibilidad que una mecanica mas compleja. citeturn690346view1

### Que significa esto en la practica
- 2 motores grandes, uno por rueda
- chasis simetrico
- apoyo pasivo liviano o patin de bajo rozamiento
- cara frontal util para empujar o capturar
- sensor de color montado de forma muy rigida

### Por que no conviene empezar por algo mas complejo
El tablero 2026 ya es bastante exigente por:
- muchas piezas,
- randomizacion parcial de notas,
- objetos delicados cerca del escenario,
- bonus de 40 puntos.

Si encima se suma una base dificil de calibrar, el equipo va a perder mucho tiempo en mecanica y muy poco en estrategia.

---

## 2. Que pide el juego y como afecta al diseno

En Elementary 2026 el robot debe resolver:
- **2 cables** en areas grises, upright, hasta 30 puntos,
- **1 microfono** upright en area verde y **3 instrumentos** completos en backstage, hasta 65 puntos,
- **6 notas** en sus areas de color, upright, hasta 120 puntos,
- y cuidar **clave, parlantes y amplificador** para no perder 40 puntos de bonus. Las notas negra, blanca, amarilla y azul cambian de lugar cada ronda, mientras que roja y verde quedan fijas. citeturn619370view3turn468039view1

### Primera consecuencia de diseno
No hace falta un robot que haga “de todo” desde el primer dia.

Hace falta un robot que resuelva bien esta mezcla:
- **objetos faciles de mover en lote**: instrumentos,
- **objetos delicados por upright**: cables, microfono, notas,
- **zona riesgosa**: escenario y bonus,
- **clasificacion por color**: notas.

### Segunda consecuencia de diseno
Las **notas** son la mision estrella del ano, pero no siempre conviene construir el robot pensando solo en las 6 notas desde el primer prototipo.

Muchas veces conviene diseñar primero un robot que:
- haga muy bien instrumentos,
- haga microfono y cables con limpieza,
- proteja bonus,
- y luego escale a una estrategia de notas mas ambiciosa.

---

## 3. Criterios para evaluar una arquitectura

Voy a comparar las 3 propuestas usando estos criterios:

### 3.1. Techo de puntaje
Cuanto potencial tiene la arquitectura si se domina bien.

### 3.2. Tiempo de desarrollo
Cuanto tarda normalmente un equipo en volverla realmente repetible.

### 3.3. Robustez
Que tan bien tolera pequeños errores de llegada, choques o diferencias de tablero.

### 3.4. Complejidad mecanica
Cuantas piezas, ajustes y modos de falla agrega.

### 3.5. Complejidad logica
Cuanta programacion y control del orden interno exige.

### 3.6. Afinidad con el tablero 2026
Que tan bien se adapta a:
- transportar instrumentos,
- dejar upright cables y microfono,
- clasificar notas,
- y no tocar bonus.

---

# 4. Propuesta 1 - Robot robusto de corral frontal

## Idea central
Un robot compacto con:
- frente ancho y simple,
- un **corral frontal** o pala con guias,
- una pequeña retencion superior o lateral,
- y una base muy estable.

La filosofia de esta arquitectura es:

> **resolver bien instrumentos, microfono, cables y una cantidad limitada de notas con un mecanismo simple y muy repetible.**

## Perfil de equipo al que conviene
- equipos nuevos o intermedios,
- equipos que quieren sumar fuerte a nivel nacional sin depender de una mecanica muy sofisticada,
- equipos que priorizan consistencia antes que techo maximo.

## Estrategia de juego que habilita
- capturar los **3 instrumentos juntos** y llevarlos al backstage,
- resolver el **microfono** con una cuna centradora,
- tomar **1 o 2 cables** con transporte controlado,
- y luego hacer **1 o 2 notas** bien resueltas.

## Como se ve fisicamente
### Base
- 2WD + apoyo pasivo
- frente bajo
- chasis rigido y angosto-moderado

### Accesorio principal
- una pala o corral frontal con paredes laterales suaves
- un retenedor superior simple, elastico o rigido, para que los objetos no salten al frenar

### Sensor de color
- montado en la parte frontal baja, centrado o levemente desplazado segun la rutina de busqueda de notas
- soporte muy rigido para que no cambie la altura

## Ventajas
- muy facil de construir y reparar,
- excelente para **instrumentos**,
- bastante buena para **microfono** si se centra bien,
- puede servir tambien para **notas de a una** o **de a dos** si hay algo de separacion interna,
- poca complejidad de software,
- buena robustez general.

## Desventajas
- el control fino de multiples notas es limitado,
- los **cables upright** pueden costar si no hay una cuna especifica,
- dificil escalar a estrategias de 4 o mas notas sin rehacer bastante el accesorio.

## Trade-offs reales
### Que se gana
- velocidad de desarrollo,
- consistencia,
- menos modos de falla.

### Que se sacrifica
- techo de puntaje en notas,
- elegancia en la separacion interna de objetos,
- posibilidad de magazine grande.

## Puntaje realista que habilita
Si esta bien hecho, puede aspirar a:
- instrumentos completos,
- microfono,
- cables,
- bonus,
- y 1 o 2 notas.

Eso ya puede construir una ronda muy competitiva para muchos torneos nacionales.

## Mi recomendacion de coach
Esta es la **mejor arquitectura para empezar** si el equipo todavia no sabe con certeza si va a querer una estrategia agresiva de notas.

---

# 5. Propuesta 2 - Robot hibrido de dos canales

## Idea central
Un robot con una base muy similar a la anterior, pero con un frente mas organizado internamente:
- **dos canales** o dos bolsillos,
- un pequeno separador central,
- una compuerta o retenedor simple,
- y una geometria pensada para transportar pares de objetos con mas orden.

La filosofia es esta:

> **mantener la robustez de un robot simple, pero ganar eficiencia real en notas, cables o piezas pares.**

## Perfil de equipo al que conviene
- equipos intermedios o fuertes a nivel nacional,
- equipos que ya dominan una base estable y quieren subir el techo de puntaje,
- equipos que quieren una arquitectura equilibrada, no extrema.

## Estrategia de juego que habilita
- capturar **3 instrumentos** con el frente completo,
- resolver **microfono** con uno de los canales o con una posicion central de alta estabilidad,
- capturar **2 cables** con mejor orden,
- transportar **2 notas por viaje** con mucho mejor control que una pala simple.

## Como se ve fisicamente
### Base
- misma filosofia 2WD + apoyo pasivo
- robot un poco mas ancho que la propuesta 1, pero sin exagerar

### Accesorio principal
- boca ancha de entrada
- dos compartimentos internos
- retenedor frontal o superior
- salida limpia para no mezclar objetos al frenar

### Sensor de color
Puede ir:
- debajo del frente para leer piso o marcas,
- o en una “ventana” de lectura donde una nota se presente siempre igual.

Con un solo sensor, esta arquitectura se beneficia mucho de una rutina donde la nota quede brevemente estabilizada para leer color antes de llevarla a destino.

## Ventajas
- muy buena para **2 notas por viaje**,
- muy buena para **2 cables** o **cable + microfono** si la secuencia es ordenada,
- conserva bastante robustez,
- sube mucho la eficiencia sin entrar todavia en magazine grande,
- excelente arquitectura “de nacional fuerte”.

## Desventajas
- mas trabajo de calibracion interna,
- si los canales estan mal dimensionados, los objetos pueden trabarse,
- el microfono pide una geometria cuidada para no caer,
- los giros bruscos se vuelven mas peligrosos si se viaja con dos objetos altos.

## Trade-offs reales
### Que se gana
- mucha eficiencia de ruta,
- capacidad real de atacar **3 a 4 notas** sin un robot exageradamente complejo,
- mejor control del orden interno.

### Que se sacrifica
- mas tiempo de ajuste,
- mas sensibilidad a detalles de ancho, paredes internas y retenedores,
- algo menos de simplicidad que la propuesta 1.

## Puntaje realista que habilita
Bien trabajada, esta arquitectura puede apuntar a:
- instrumentos,
- microfono,
- cables,
- bonus,
- y una corrida seria de notas con 2 por viaje o con 3 a 4 notas totales.

## Mi recomendacion de coach
Si un equipo me dijera “queremos pelear arriba en nacional, pero sin construir algo demasiado loco”, esta seria probablemente mi **primera recomendacion**.

Es el mejor equilibrio entre:
- techo de puntaje,
- robustez,
- tiempo de desarrollo.

---

# 6. Propuesta 3 - Robot avanzado con mini-magazine de notas

## Idea central
Una arquitectura mas ambiciosa, construida alrededor de la idea de que las **notas** son la mision principal del ano.

El robot incorpora:
- un sistema frontal de captura,
- una pequena zona de almacenamiento ordenado o **mini-magazine**,
- algun metodo de retencion por compuerta o selector,
- y una forma controlada de ir liberando notas en destinos distintos.

La filosofia es:

> **aceptar mayor complejidad mecanica a cambio de maximizar la eficiencia en la mision de 120 puntos.**

## Perfil de equipo al que conviene
- equipos avanzados,
- equipos con mucho tiempo de prueba,
- equipos capaces de tolerar iteraciones mecanicas y depuracion seria.

## Estrategia de juego que habilita
- capturar multiples notas del sector superior,
- leerlas y conservar orden interno,
- descargar varias en destinos distintos,
- combinar eso con una o dos misiones accesorias de alto retorno.

## Como se ve fisicamente
### Base
- 2WD + apoyo pasivo sigue siendo lo mas razonable
- pero el robot suele ser algo mas voluminoso o alto por el almacenamiento interno

### Accesorio principal
- entrada frontal guiada
- compuerta o retenedor
- 2 o 3 posiciones internas claras
- eventualmente un pequeño selector mecanico o una secuencia de liberacion por orden

### Sensor de color
En esta propuesta, la ubicacion del sensor importa mucho.
Puede convenir una “estacion de lectura” interna:
- la nota entra,
- queda quieta un instante,
- se lee color,
- y luego se reasigna por software o por orden de descarga.

## Ventajas
- mayor techo de puntaje en notas,
- mejor aprovechamiento del viaje hacia la zona superior,
- posibilidad de construir una estrategia muy eficiente de 4 o mas notas.

## Desventajas
- mucha mas complejidad,
- mas riesgo de atasco,
- mas peso y mas volumen frontal,
- mas dificil proteger bonus cerca del escenario,
- mas dificil mantener upright al descargar,
- si falla el orden interno, se cae gran parte del valor del robot.

## Trade-offs reales
### Que se gana
- techo competitivo alto,
- capacidad de exprimir la mision central del ano,
- mejor potencial para torneos muy exigentes.

### Que se sacrifica
- robustez inicial,
- facilidad de reparacion,
- velocidad de construccion,
- simplicidad para alumnos mas chicos.

## Puntaje realista que habilita
Si realmente se domina, puede habilitar corridas muy altas al resolver gran parte de las 6 notas, sumadas a una seleccion inteligente de otras misiones.

Pero si queda “a medio cocinar”, puede rendir peor que una propuesta 2 bien hecha.

## Mi recomendacion de coach
No empezaria la temporada con esta arquitectura salvo que:
- el equipo ya tenga experiencia,
- el coach sepa que puede iterar mucho,
- y haya claridad de que el objetivo es buscar un techo alto, no solo una ronda solida.

---

## 7. Comparacion directa entre las 3 propuestas

### Propuesta 1 - Corral frontal robusto
**Ideal para:** empezar fuerte, construir consistencia, puntuar bien sin gran complejidad.

**Mejor en:** instrumentos, microfono, cables, 1-2 notas.

**Peor en:** estrategias agresivas de muchas notas.

### Propuesta 2 - Hibrido de dos canales
**Ideal para:** competir muy bien a nivel nacional con una arquitectura equilibrada.

**Mejor en:** instrumentos, cables, microfono y 2 notas por viaje.

**Peor en:** magazine grande o secuencias extremadamente sofisticadas.

### Propuesta 3 - Mini-magazine de notas
**Ideal para:** equipos avanzados que quieren ir a un techo alto.

**Mejor en:** maximizar eficiencia de notas.

**Peor en:** simplicidad, robustez inicial y tiempo de desarrollo.

---

## 8. Cual elegir segun el objetivo del equipo

## Caso A - “Queremos una ronda fuerte y repetible cuanto antes”
Elegiria la **Propuesta 1**.

## Caso B - “Queremos pelear arriba en nacional con una arquitectura realista”
Elegiria la **Propuesta 2**.

## Caso C - “Queremos apostar por un techo muy alto y tenemos tiempo de iterar”
Elegiria la **Propuesta 3**.

---

## 9. Mi recomendacion honesta como coach

Si yo estuviera guiando un equipo Elementary para 2026, haria esto:

### Paso 1
Construiria primero una **Propuesta 1** funcional.

### Paso 2
Si el equipo domina rapido:
- la evolucionaria hacia una **Propuesta 2**.

### Paso 3
Solo si de verdad sobra tiempo y el equipo esta maduro:
- exploraria una **Propuesta 3**.

### Por que
Porque en competencias reales, una arquitectura un poco menos brillante pero bien dominada suele ganarle a una arquitectura muy ambiciosa que todavia no esta estable.

---

## 10. Recomendacion final para este repo

Mirando el contexto de este repo, donde el hardware base previsto es Spike Prime con 2 motores grandes, 1 motor mediano, 1 sensor de color y accesorios tipo garra/empujador, la arquitectura mas coherente para desarrollar primero parece ser una **Propuesta 2 - Hibrido de dos canales**. Eso encaja bien con la base mecanica ya descrita y con la necesidad de combinar transporte multiple moderado con control razonable de notas y objetos delicados. fileciteturn31file0L1-L18

### En palabras simples
Si el equipo quiere una opcion seria y equilibrada para Elementary 2026:
- no construiria un robot demasiado simple,
- pero tampoco arrancaria con un magazine grande.

Iria por un robot que pueda:
- cargar los 3 instrumentos,
- estabilizar el microfono,
- manejar 2 cables con orden,
- y transportar 2 notas por viaje.

Eso, bien hecho, ya es una arquitectura muy potente.

---

## 11. Conclusiones

Las tres propuestas sirven, pero para objetivos distintos.

### La leccion mas importante
> **La mejor arquitectura no es la mas compleja. Es la que el equipo puede volver repetible durante la temporada.**

### Segunda leccion
> **En Elementary 2026, la gran tentacion es diseñar todo alrededor de las notas. Pero muchas veces la arquitectura ganadora es la que combina bien notas con objetos simples y con un bonus bien protegido.**

### En resumen
- **Propuesta 1:** la mas segura para empezar.
- **Propuesta 2:** la mejor equilibrada para competir fuerte.
- **Propuesta 3:** la de mayor techo, pero tambien la de mayor riesgo.

---

## Fuentes base

- WRO RoboMission Elementary 2026 Game Rules
- WRO RoboMission General Rules 2026
- Pybricks documentation sobre `DriveBase`
- `docs/es/competition/analisis-misiones-elementary-2026.md`
- `docs/es/hardware/README.md`
