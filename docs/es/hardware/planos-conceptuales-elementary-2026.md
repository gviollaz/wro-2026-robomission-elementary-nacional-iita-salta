# Planos conceptuales de arquitecturas de robot para WRO RoboMission Elementary 2026

## Objetivo

Este documento complementa `arquitecturas-robot-elementary-2026.md` con **planos conceptuales** de las 3 propuestas de robot para **WRO RoboMission Elementary 2026 - Robot Rockstars**.

No son planos CAD ni instrucciones de armado paso a paso.
Son **mapas conceptuales de diseño** para ayudar al equipo a decidir:

- donde ubicar ruedas, hub y sensor,
- como podria ser el frente del robot,
- como circularian los objetos dentro del mecanismo,
- que partes deben ser mas rigidas,
- y que errores de diseño conviene evitar.

La idea es que un alumno pueda mirar estos esquemas y entender rapidamente:
- como esta pensado el robot,
- para que estrategia sirve,
- y donde estan sus puntos delicados.

---

## 1. Convenciones de lectura de los esquemas

### Simbolos usados
- `O` = rueda motriz
- `o` = apoyo pasivo / caster / patin
- `[HUB]` = Spike Prime Hub
- `[M]` = motor mediano de accesorio
- `[CS]` = sensor de color
- `====` = frente o pala principal
- `| |` = guias laterales / canales
- `[]` = zona de carga o retencion

### Vista superior
Los diagramas principales estan pensados como **vista desde arriba**.
La parte de arriba del dibujo representa el **frente del robot**.

### Vista lateral
En algunos casos agrego un esquema lateral simple para mostrar:
- altura del sensor,
- inclinacion del frente,
- o ubicacion relativa del accesorio.

---

## 2. Base comun recomendada para las 3 arquitecturas

Antes de entrar a cada propuesta, conviene fijar una base comun.

## Vista superior base comun

```text
        FRENTE
   ___________________
  /                   \
 /     accesorio       \
|                       |
|        [CS]           |
|                       |
|   O             O     |
|                       |
|        [HUB]          |
|          [M]          |
|            o          |
 \_____________________/
          ATRAS
```

## Lectura del esquema
- El **sensor de color** va adelantado y centrado o casi centrado.
- Las **ruedas motrices** quedan cerca del centro del robot.
- El **hub** va bajo y centrado.
- El **motor mediano** queda cerca del mecanismo que mueve.
- El **apoyo pasivo** queda atras para estabilizar sin robar demasiado espacio frontal.

## Recomendaciones practicas
- frente bajo y util,
- chasis corto y rigido,
- nada de piezas altas decorativas,
- cables cortos y ordenados,
- cara frontal facil de reparar y ajustar.

---

# 3. Propuesta 1 - Robot robusto de corral frontal

## Idea general
Esta arquitectura esta pensada para:
- instrumentos en lote,
- microfono con buena estabilidad,
- cables con cuidado razonable,
- y 1 o 2 notas como extension natural.

La clave es un frente ancho pero simple, con guias laterales y algo de retencion.

---

## 3.1. Plano conceptual - vista superior

```text
                   FRENTE
      __________________________________
     /                                  \
    /   \============================/   \
   /     \                          /     \
  |       |        zona de         |       |
  |       |        captura         |       |
  |       |      [objeto/s]        |       |
  |       |________________________|       |
  |                [CS]                    |
  |                                        |
  |          O                O            |
  |                                        |
  |                [HUB]                   |
  |                  [M]                   |
  |                    o                   |
   \______________________________________/
                    ATRAS
```

## Que representa
- el frente en forma de **corral** o pala,
- paredes laterales suaves para centrar,
- una cavidad frontal para empujar o contener,
- el sensor de color por detras o por debajo del frente.

## Para que sirve bien
- levantar o arrastrar **3 instrumentos** juntos,
- contener el **microfono** mejor que una pala totalmente abierta,
- transportar una o dos notas si no se exige orden interno muy estricto.

---

## 3.2. Plano lateral simplificado

```text
        FRENTE                            ATRAS
   ______________________________________________
  /   frente bajo / corral     [HUB]             \
 /_____/=============================\____________\\
       [CS]
          O                  O
                           o
```

## Idea importante
- el **frente debe ser bajo** para capturar facil,
- pero no tanto como para engancharse en la lona,
- el sensor debe quedar protegido y siempre a la misma altura.

---

## 3.3. Flujo de objetos en esta arquitectura

### Instrumentos
1. entrar al camion,
2. capturar los 3 con el corral,
3. trasladar en bloque,
4. descargar en backstage.

### Microfono
1. entrar con menos velocidad,
2. centrar el microfono dentro del corral,
3. llevarlo con frenado suave,
4. soltar limpio en el area verde.

### Notas
1. capturar 1 o 2,
2. leer color,
3. llevar una por vez o dos si se mantienen separadas de forma natural.

---

## 3.4. Zonas criticas del diseño

### Zona critica A - borde frontal
Si el borde frontal es muy recto y duro:
- puede golpear demasiado,
- puede hacer caer el microfono,
- puede mover objetos de bonus.

### Zona critica B - ancho del corral
Si es muy angosto:
- los instrumentos se traban.

Si es muy ancho:
- el robot se vuelve torpe en el escenario.

### Zona critica C - retencion
Si no existe una pequena retencion superior o lateral:
- los objetos saltan al frenar.

---

## 3.5. Recomendaciones de construccion

- usar vigas laterales lisas,
- evitar puntas o ganchos innecesarios,
- reforzar la union entre frente y chasis,
- mantener el frente liviano,
- si se agrega un retenedor, que no tape demasiado la carga.

---

# 4. Propuesta 2 - Robot hibrido de dos canales

## Idea general
Esta propuesta mantiene una base muy parecida a la anterior, pero convierte el frente en un sistema mas organizado.

La idea es tener:
- **dos canales internos**,
- una entrada ancha,
- un pequeno separador central,
- y control suficiente para mover pares de objetos con mas orden.

Es la arquitectura mas equilibrada para competir fuerte.

---

## 4.1. Plano conceptual - vista superior

```text
                      FRENTE
      __________________________________________
     /                                          \
    /     \==============================/       \
   /       |   canal A    ||   canal B   |       \
  |        |   [objeto]   ||   [objeto]  |        |
  |        |______________||_____________|        |
  |                    [CS]                       |
  |                                               |
  |            O                    O             |
  |                                               |
  |                  [HUB]                        |
  |                    [M]                        |
  |                      o                        |
   \_____________________________________________/
                       ATRAS
```

## Que representa
- un frente que sigue siendo bastante simple,
- pero con dos “carriles” o canales,
- separados por una pared central baja o media,
- permitiendo llevar pares con menos mezcla.

## Para que sirve bien
- **2 notas por viaje**,
- **2 cables** con mejor orden,
- **microfono** mas estable si uno de los canales funciona como cuna,
- **instrumentos** si el frente es lo bastante ancho para contener los 3 o si el separador no llega hasta adelante.

---

## 4.2. Variante de entrada abierta + separacion interna

A veces no conviene dividir el frente desde la punta.
Puede ser mejor que la separacion aparezca un poco mas atras.

```text
                      FRENTE
      __________________________________________
     /                                          \
    /      entrada abierta y ancha              \
   /_____________________________________________\\
  |                \            /                |
  |                 \ canal A  /                 |
  |                  \________/                  |
  |                  / canal B \                 |
  |                 /__________\\                |
  |                     [CS]                     |
  |          O                      O            |
  |                    [HUB]                     |
  |                      [M]                     |
  |                        o                     |
   \____________________________________________/
```

## Por que esta variante es interesante
- la boca grande ayuda a capturar mejor,
- y el orden aparece mas atras, cuando el objeto ya entro.

Esto suele ser muy bueno para equipos reales, porque tolera mejor errores de llegada.

---

## 4.3. Plano lateral simplificado

```text
       FRENTE                                 ATRAS
  _________________________________________________
 /  frente bajo + retenedor suave   [HUB]          \
/______/===============================\____________\\
      [CS]
         O                   O
                          o
```

## Clave de esta arquitectura
El retenedor superior no deberia apretar demasiado.
Solo debe ayudar a que:
- el objeto no rebote,
- y el orden interno no se pierda.

---

## 4.4. Flujo de objetos

### Dos notas
1. capturar nota 1 y nota 2,
2. ordenarlas por canal o por posicion relativa,
3. leer color,
4. descargar una y luego la otra.

### Dos cables
1. capturar ambos,
2. transportar con menos riesgo de enredo,
3. resolver una descarga controlada por lado o por secuencia.

### Microfono
1. llevarlo en el canal mas estable,
2. frenar suave,
3. depositarlo con menor probabilidad de vuelco.

---

## 4.5. Zonas criticas del diseño

### Zona critica A - separador central
Si es muy alto:
- dificulta entrar instrumentos grandes.

Si es muy bajo:
- no ordena casi nada.

### Zona critica B - ancho de canales
Si el canal queda demasiado justo:
- los objetos se clavan.

Si queda demasiado holgado:
- no mantiene orientacion.

### Zona critica C - descarga
El gran secreto de esta arquitectura no es capturar; es **soltar sin mezclar**.

---

## 4.6. Recomendaciones de construccion

- probar el frente con piezas reales del juego antes de cerrarlo,
- dejar la parte central delantera lo mas liviana posible,
- reforzar mucho las paredes internas,
- si se usa compuerta, que sea corta y confiable,
- disenar los canales para tolerar pequenas variaciones de orientacion.

---

# 5. Propuesta 3 - Robot avanzado con mini-magazine de notas

## Idea general
Esta propuesta esta organizada alrededor de la mision de notas.
El frente ya no es solo un corral o dos canales. Es una **entrada hacia una pequena zona interna de almacenamiento**.

La idea es que el robot pueda:
- capturar varias notas,
- mantener algun orden interno,
- y soltarlas en secuencia.

---

## 5.1. Plano conceptual - vista superior

```text
                        FRENTE
      _____________________________________________
     /                                             \
    /       \==============================/        \
   /         \    entrada de captura      /          \
  |           \__________________________/            |
  |                 [zona buffer]                     |
  |            ________________________               |
  |           | slot 1 | slot 2 | slot 3 |            |
  |           |________|________|________|            |
  |                    [CS]                          |
  |                                                 |
  |            O                     O              |
  |                                                 |
  |                   [HUB]                         |
  |                     [M]                         |
  |                       o                         |
   \_______________________________________________/
                         ATRAS
```

## Que representa
- una boca de entrada,
- una zona buffer donde entra la nota,
- y un mini-magazine de 2 o 3 posiciones.

No implica necesariamente un selector mecanico complejo.
Puede funcionar por:
- orden de entrada,
- compuertas,
- o liberacion secuencial sencilla.

---

## 5.2. Variante con descarga lateral o frontal controlada

```text
                     FRENTE
      ________________________________________
     /                                        \
    /   entrada   [buffer]   [slot 1][slot 2] \
   /___________________________________________\\
  |                                             |
  |                [CS]                         |
  |                                             |
  |          O                    O             |
  |                    [HUB]                    |
  |                      [M]                    |
  |                        o                    |
   \___________________________________________/
```

### Lectura del esquema
A veces no hace falta un magazine largo.
Con dos posiciones internas claras ya puede hacerse un robot bastante poderoso.

---

## 5.3. Plano lateral simplificado

```text
         FRENTE                               ATRAS
  ___________________________________________________
 / entrada -> buffer -> slots      [HUB]             \
/_____/==================================\____________\\
      [CS]
         O                    O
                            o
```

## Riesgo principal que muestra la vista lateral
Esta arquitectura tiende a crecer en:
- altura,
- masa frontal,
- complejidad interna.

Por eso hay que cuidar mucho:
- centro de gravedad,
- rigidez,
- y limpieza de la trayectoria interna.

---

## 5.4. Flujo de objetos

### Notas
1. capturar la nota,
2. llevarla al buffer,
3. leer color,
4. decidir donde queda almacenada o en que orden se descargara,
5. transportar y soltar segun secuencia.

### Otros objetos
Esta arquitectura puede resolver algunos cables o incluso microfono, pero solo si no se compromete demasiado el frente.

En general, no conviene intentar que el mismo frente-magazine haga todo perfecto desde el primer prototipo.

---

## 5.5. Zonas criticas del diseño

### Zona critica A - transicion de entrada a buffer
Si hay escalones o bordes mal resueltos:
- la nota se frena,
- se gira raro,
- o se atasca.

### Zona critica B - slots internos
Si no estan muy claros:
- las notas se mezclan,
- el robot pierde orden,
- la descarga se vuelve caotica.

### Zona critica C - compuertas y retenedores
Cada compuerta agrega:
- peso,
- juego,
- y posibilidad de falla.

Por eso, cuanto mas simple sea el control interno, mejor.

---

## 5.6. Recomendaciones de construccion

- hacer primero un magazine de **2 posiciones**, no de 4,
- probar con piezas reales y muchas repeticiones,
- dejar accesos para destrabar rapido,
- mantener la trayectoria interna lisa,
- no usar compuertas largas o flexibles,
- y no cargar el frente con demasiado volumen si luego el robot debe pasar cerca del escenario.

---

## 6. Plano comparativo rapido de huella y complejidad

```text
PROPUESTA 1
frente ancho simple
[ captura abierta ]
robustez alta - complejidad baja

PROPUESTA 2
frente ordenado
[ canal A ][ canal B ]
robustez media-alta - complejidad media

PROPUESTA 3
frente + almacenamiento
[ entrada ][ buffer ][ slots ]
robustez media-baja al inicio - complejidad alta
```

---

## 7. Como elegir entre los planos conceptuales

## Si el equipo pregunta: “cual construimos primero?”

### Respuesta corta
- si el objetivo es **arrancar y puntuar pronto** -> Propuesta 1
- si el objetivo es **competir fuerte y equilibrado** -> Propuesta 2
- si el objetivo es **techo alto y mucho trabajo de iteracion** -> Propuesta 3

## Mi recomendacion concreta
Para este repo, seguiria este camino:
1. construir primero algo muy cercano a la **Propuesta 1**,
2. convertirlo luego en **Propuesta 2**,
3. explorar **Propuesta 3** solo si el equipo llega temprano y estable a mitad de temporada.

---

## 8. Consejos de coach para pasar del plano conceptual al prototipo real

### 8.1. Construir en capas
No armar todo junto.

Primero:
- base,
- sensor,
- ruedas,
- rigidez.

Despues:
- frente de captura.

Y recien despues:
- retenciones,
- compuertas,
- separadores finos.

### 8.2. Validar con objetos reales
No sirve que el plano “parezca lindo”.
Hay que probar:
- si entra facil,
- si rebota,
- si gira,
- si sale limpio,
- si el robot sigue girando bien con la carga.

### 8.3. No enamorarse del primer frente
Muchos equipos se bloquean por querer conservar una idea inicial.
Lo mejor es pensar el frente como una parte evolutiva.

### 8.4. Si un mecanismo necesita demasiada precision, simplificar
En Elementary casi siempre gana mas:
- una geometria tolerante,
- que una mecanica muy elegante pero sensible.

---

## 9. Conclusion final

Estos planos conceptuales no buscan cerrar el diseño. Buscan ordenar el pensamiento del equipo.

La pregunta correcta no es:
- “cual robot es el mas impresionante?”

La pregunta correcta es:
- “cual de estas arquitecturas podemos construir, entender, calibrar y volver repetible?”

### Idea final
> **El mejor plano conceptual es el que ayuda a construir un robot que funcione 8 o 9 veces de 10, no el que se ve mas sofisticado en papel.**

---

## Referencias internas relacionadas

- `docs/es/competition/analisis-misiones-elementary-2026.md`
- `docs/es/hardware/arquitecturas-robot-elementary-2026.md`
- `docs/es/hardware/README.md`
