# Analisis detallado de misiones WRO RoboMission 2026 Elementary

## Objetivo de este documento

Este documento analiza de forma **especifica** las misiones de **WRO RoboMission Elementary 2026 - Robot Rockstars** y propone ideas de estrategia, mecanismos y decisiones de diseño pensadas para equipos que quieren competir bien a nivel nacional.

La idea no es solo describir las reglas, sino responder preguntas utiles de coach:

- Que misiones conviene priorizar.
- Que partes del juego son realmente dificiles este ano.
- Donde conviene empujar, donde conviene transportar, y donde conviene soltar con precision.
- Cuando tiene sentido llevar 1, 2, 3 o mas objetos al mismo tiempo.
- Que tipo de mecanismos tienen mejor relacion entre simplicidad, robustez y puntaje.

La redaccion esta pensada para alumnos, pero con criterio tecnico real.

---

## 1. Lectura general del desafio 2026 Elementary

En Elementary 2026 el robot prepara un festival de musica. Las misiones se agrupan asi:

1. **Conectar amplificador y parlantes** con 2 cables.
2. **Preparar el show** llevando microfono e instrumentos.
3. **Tocar la cancion** llevando 6 notas a sus areas de color.
4. **Cuidar el escenario** para no perder bonus.

### Lo mas importante del tablero
Este ano el puntaje esta muy concentrado en una mision:

- cables: **30 puntos**
- microfono + instrumentos: **65 puntos**
- notas: **120 puntos**
- bonus: **40 puntos**
- total: **255 puntos**

### Primera conclusion estrategica
La mision de **notas** es claramente la mas importante. Pero eso no significa que haya que empezar por ahi.

Muchas veces, para un equipo en crecimiento, conviene construir una base fuerte con:
- cables,
- instrumentos,
- microfono,
- bonus protegido,

y recien despues ir a una estrategia ambiciosa de notas.

---

## 2. Que hace dificil a Elementary 2026

Este ano la dificultad no esta en levantar objetos muy altos ni en randomizaciones muy caoticas del campo completo. La dificultad esta en una combinacion de cuatro cosas:

1. **muchos objetos transportables**,
2. **varios depositos con condicion upright**,
3. **notas de colores con randomizacion parcial**,
4. **zona de escenario con bonus sensible a choques**.

### Traducido a lenguaje de equipo
No alcanza con hacer un robot que agarre cosas.
Hace falta un robot que:
- cargue bien,
- no mezcle piezas,
- no las haga caer,
- y pueda acercarse a zonas con objetos delicados sin romper nada.

---

## 3. Datos del reglamento que condicionan toda la estrategia

### 3.1. Las reglas son internacionales
Las reglas Elementary 2026 publicadas por WRO estan hechas para la Final Internacional y aclaran que los organizadores nacionales pueden simplificar misiones o adaptar reglas locales.

### 3.2. El orden de las misiones es libre
WRO explica las misiones por secciones, pero deja a cada equipo decidir que hace y en que orden.

### 3.3. Hay randomizacion real en las notas
Las notas **negra, blanca, amarilla y azul** cambian de lugar entre 4 cuadrados verde claro. Las notas **roja y verde** no cambian de posicion.

### 3.4. Las notas dan muchisimos puntos, pero exigen color correcto
Cada nota vale **20 puntos** si queda completamente en su area de color correcta y upright. Si queda solo parcial o no upright, baja a **10 puntos**. Si va al color incorrecto, vale **0**.

### 3.5. Hay detalles de area que importan mucho
- En las **notas**, el area objetivo incluye el **borde gris**.
- En el **backstage**, cuenta el area rosa incluyendo el mobiliario, pero **sin** el borde gris.
- En los **cables**, solo **un cable por area gris** suma puntos.

### 3.6. Bonus este ano pesa bastante
El bonus vale **40 puntos** si no se mueve o daña:
- la clave de sol,
- los dos parlantes,
- el amplificador.

En un tablero con maximo 255, perder bonus duele mucho.

### 3.7. En la Q&A oficial aun no hay aclaraciones especificas para Elementary 2026
Eso significa que conviene revisar periodicamente la pagina oficial, porque cualquier aclaracion futura pasa a ser parte practica de las reglas.

---

## 4. Analisis mision por mision

# 4.1. Mision 1 - Conectar el amplificador con los parlantes

## Que pide la regla
Hay 2 cables. Cada cable debe quedar en una de las areas grises entre los parlantes y el amplificador.

- cable completamente en el area gris y upright: **15 puntos**
- cable parcial o no upright: **5 puntos**
- maximo: **30 puntos**

Ademas, solo cuenta **un cable por area**.

## Que tiene de dificil
A primera vista parece una mision facil, pero tiene dos trampas:

1. el cable es un objeto largo y fino,
2. pide quedar **upright**, no solo “tirado adentro”.

Eso cambia mucho el tipo de mecanismo conveniente.

## Lectura tecnica de la mision
Esta no es una mision de empuje bruto. Es una mision de:
- traslado suave,
- control de orientacion,
- y liberacion prolija.

## Mecanismos posibles
### Opcion A - empujador simple
Empujar el cable hasta la zona.

**Ventajas**
- muy simple,
- facil de construir.

**Desventajas**
- alto riesgo de que no quede upright,
- riesgo de que quede cruzado o parcial.

### Opcion B - bandeja o cuna baja
Transportar el cable apoyado en una guia y soltarlo.

**Ventajas**
- mucho mejor control de orientacion,
- buena repetibilidad.

**Desventajas**
- hay que cuidar que no rebote o gire al soltar.

### Opcion C - pinza o retenedor superior
Sujetar el cable y presentarlo arriba de la zona.

**Ventajas**
- control muy bueno,
- puede dejarlo mas limpio.

**Desventajas**
- mas lento,
- probablemente demasiado complejo para solo 30 puntos.

## Conviene llevar 1 o 2 cables a la vez
### Llevar 1
Es la opcion mas robusta.

### Llevar 2
Puede ser muy buena idea, porque ambas zonas estan en el mismo sector del escenario.
Pero solo si el mecanismo:
- mantiene los dos ordenados,
- no los enreda,
- permite soltarlos en dos zonas distintas sin tocar parlantes o amplificador.

## Recomendacion de coach
Para la mayoria de equipos Elementary, la mejor idea suele ser:
- **capturar ambos cables**,
- pero **resolver la entrega de manera controlada**, uno por zona.

No es una mision donde convenga ganar 1 segundo y perder 20 puntos por una mala orientacion.

---

# 4.2. Mision 2 - Preparar el show

Esta mision se divide en dos subproblemas distintos:
- **microfono al area verde del escenario**,
- **3 instrumentos al backstage rosa**.

Aunque estan dentro de la misma seccion, no son iguales desde el punto de vista mecanico.

## 4.2.1. Microfono

### Que pide la regla
El microfono debe quedar en el area verde clara del escenario y upright.

- completamente en area y upright: **20 puntos**
- parcial o no upright: **10 puntos**

### Que tiene de dificil
El microfono es un objeto alto comparado con su base. Eso significa:
- mas riesgo de vuelco,
- mas sensibilidad a frenadas bruscas,
- mas necesidad de una descarga prolija.

### Mecanismos recomendables
#### Opcion A - bolsillo centrador
Una cuna que lo mantenga firme por la base y con apoyo lateral.

**Ventajas**
- muy robusto,
- minimiza caidas.

**Desventajas**
- ocupa algo de volumen.

#### Opcion B - empujador con guia lateral
**Ventajas**
- simple,
- rapido.

**Desventajas**
- si el microfono gira, puede llegar mal parado.

### Recomendacion de coach
Tratar al microfono como objeto **delicado**, no como objeto masivo. Para 20 puntos, vale la pena un submecanismo que lo estabilice bien.

---

## 4.2.2. Instrumentos

### Que pide la regla
Hay 3 instrumentos en el camion, y deben terminar completamente en el backstage rosa.
Cada uno vale **15 puntos**, maximo **45**.

A diferencia del microfono, aqui la regla no exige upright.

### Por que esto cambia la estrategia
Como no hace falta que queden parados, esta es una mision mucho mas favorable para:
- empuje,
- barrido,
- transporte multiple,
- y suelta masiva.

## Que tiene de dificil
- los instrumentos tienen formas distintas,
- parten agrupados en el camion,
- hay que meterlos completamente en backstage,
- el area backstage tiene geometria particular e incluye mobiliario, pero excluye el borde gris.

### Esto es importante
No alcanza con “tocarlo” o “entrarlo un poco”. Debe quedar **completamente in**.

## Mecanismos posibles
### Opcion A - pala ancha / corral
Empujar o envolver los 3 instrumentos desde el camion hasta el backstage.

**Ventajas**
- excelente eficiencia,
- probablemente la mejor relacion dificultad/puntaje.

**Desventajas**
- si el corral es demasiado estrecho, las formas raras pueden trabarse.

### Opcion B - bandeja frontal abierta
Buena para llevar varios objetos a la vez.

**Ventajas**
- simple,
- rapida.

**Desventajas**
- puede perder piezas al girar.

### Opcion C - capturas parciales en dos viajes
**Ventajas**
- menos riesgo de atasco.

**Desventajas**
- peor uso del tiempo.

## Conviene llevar 1, 2 o 3 instrumentos juntos
### Llevar 1
Generalmente no conviene: mucho viaje para poco beneficio.

### Llevar 2
Ya es razonable.

### Llevar 3
Esta es una de las mejores candidatas del tablero para **transporte masivo**.

## Recomendacion de coach
Esta mision es ideal para que un equipo Elementary sume muchos puntos con un mecanismo relativamente simple.

Si el robot puede:
- capturar los 3 del camion,
- y soltarlos completamente dentro del backstage,

entonces obtiene **45 puntos** con muy buena eficiencia.

---

# 4.3. Mision 3 - Tocar la cancion

## Que pide la regla
Hay 6 notas, una por color:
- roja,
- azul,
- verde,
- amarilla,
- blanca,
- negra.

Cada nota debe ir a su area objetivo del mismo color sobre el pentagrama.
La nota vale:
- **20 puntos** si queda completamente en el area correcta y upright,
- **10 puntos** si queda parcial o no upright,
- **0 puntos** si queda en color incorrecto.

Maximo de la mision: **120 puntos**.

## Esta es la mision central del ano
No solo por el puntaje. Tambien porque combina:
- clasificacion por color,
- transporte multiple posible,
- necesidad de orden interno,
- y descarga con precision razonable.

## Que la hace dificil de verdad
### 1. Color correcto
No alcanza con llevar notas a cualquier lado.

### 2. Randomizacion parcial
La roja y la verde son fijas, pero negra, blanca, amarilla y azul cambian entre 4 posiciones.
Eso significa que el robot no puede asumir siempre el mismo layout completo.

### 3. Upright importa
Aunque la nota este bien de color, si cae, baja a la mitad.

### 4. Son muchos objetos
Seis notas es bastante carga para una categoria Elementary.

## Mecanismos posibles

### Opcion A - una nota por viaje
**Ventajas**
- logica simple,
- muy facil de depurar,
- buen control de color y descarga.

**Desventajas**
- lento,
- puede quedar corto de tiempo si se pretende resolver las 6.

### Opcion B - dos notas por viaje con separadores
**Ventajas**
- muy buen compromiso entre velocidad y control,
- permite leer y ordenar mejor.

**Desventajas**
- pide una pequena arquitectura interna para que no se mezclen.

### Opcion C - magazine de 3 o mas notas
**Ventajas**
- techo alto de eficiencia.

**Desventajas**
- aumenta mucho la complejidad,
- mayor riesgo de atasco,
- exige controlar muy bien cual nota es cual al momento de descargar.

## Conviene llevar 1, 2, 3 o mas notas a la vez
### Llevar 1
Muy recomendable para equipos que recien estan aprendiendo a resolver la randomizacion.

### Llevar 2
Probablemente la mejor zona de equilibrio para un equipo fuerte de nacional.

### Llevar 3
Puede funcionar si el mecanismo mantiene orden y si la descarga esta muy estudiada.

### Llevar 4, 5 o 6
Solo lo recomendaria para equipos muy avanzados y con mucho tiempo de prueba. El problema no es solo cargar; el problema es:
- identificar,
- conservar orden,
- y descargar correcto sin perder upright.

## Dos formas de pensar la mision
### Enfoque 1 - resolver primero las fijas
Hacer roja y verde con trayectorias casi fijas, y luego pasar a las randomizadas.

**Ventaja:** da una base estable.

**Desventaja:** puede fragmentar la ruta.

### Enfoque 2 - capturar por zona y clasificar en el robot
Levantar varias notas del sector superior y luego decidir destino.

**Ventaja:** alta eficiencia potencial.

**Desventaja:** mucha mayor complejidad mecanica y logica.

## Recomendacion de coach
Para un equipo serio que quiere crecer bien:
1. dominar primero **nota fija por nota fija**,
2. luego dominar **una randomizada a la vez**,
3. recien despues pasar a estrategias de 2 notas.

La clave de esta mision no es solo la lectura de color. La clave real es la **descarga correcta en el destino correcto**.

---

# 4.4. Bonus - Cuidar escenario y objetos

## Que pide la regla
Sumar bonus por no mover ni danar:
- la clave de sol: **10 puntos**,
- cada parlante: **10 puntos**, maximo **20**,
- el amplificador: **10 puntos**.

Total bonus: **40 puntos**.

## Por que el bonus pesa mucho
40 puntos es muchisimo en Elementary.
Perder el bonus equivale, por ejemplo, a perder:
- 2 notas perfectas,
- o casi toda la mision de cables,
- o 2 instrumentos completos mas parte del microfono.

## Que lo vuelve peligroso este ano
La zona del escenario esta muy cerca de:
- cables,
- microfono,
- parlantes,
- amplificador.

Eso significa que un accesorio demasiado ancho o una maniobra agresiva puede romper una ronda muy buena.

## Recomendacion de coach
El bonus debe tratarse como una mision pasiva de altisimo valor.
Eso se protege con:
- rutas limpias,
- mecanismos que no sobresalgan demasiado,
- topes fisicos,
- giros moderados cerca del escenario,
- y velocidades mas bajas en el sector izquierdo del tablero.

---

## 5. Recomendaciones sobre transporte multiple

# 5.1. Donde si conviene agrupar objetos

## Muy recomendable
### Instrumentos
Es la mejor mision del tablero para transportar 2 o 3 objetos juntos.

### Cables
Puede convenir capturar los 2, siempre que luego la suelta sea controlada.

## Recomendable con buen diseno
### Notas de a 2
Muy interesante para un equipo que ya domina color y descarga.

# 5.2. Donde hay que tener mas cuidado

## Microfono junto con otros objetos altos o inestables
No suele convenir.

## Notas de a 3 o mas
Solo si el robot realmente tiene magazine interno, separacion o una logica de orden muy clara.

## Cables + otro objeto en el mismo viaje
En teoria es posible, pero el riesgo de desorden y perdida de orientacion suele ser alto.

---

## 6. Mecanismos interesantes para este ano

# 6.1. Frontal tipo pala-corral
Muy util para:
- capturar instrumentos,
- trasladar 2 notas,
- envolver objetos sin agarrarlos individualmente.

**Ventajas**
- simple,
- liviano,
- rapido.

**Desventajas**
- menos fino para depositos upright delicados.

# 6.2. Bandeja baja con retenedor
Muy util para:
- cables,
- microfono,
- notas si se mantiene orden.

**Ventajas**
- mejor control de transporte.

**Desventajas**
- requiere una suelta limpia para no hacer rebotar las piezas.

# 6.3. Embudo o guias laterales
Muy util para:
- centrar objetos al capturarlos,
- asegurar orientacion aproximada,
- tolerar pequenos errores de llegada.

**Ventajas**
- mejora mucho la robustez.

**Desventajas**
- ocupa espacio frontal.

# 6.4. Selector simple o magazine corto
Interesante solo para equipos mas avanzados.

**Uso:** transportar 2 o 3 notas con algo de orden interno.

**Ventaja:** mejora fuerte de eficiencia.

**Desventaja:** mas riesgo de atasco y mas tiempo de ajuste.

# 6.5. Compuerta de liberacion
Puede ser muy util cuando se quiere:
- cargar varios objetos,
- pero soltarlos de a uno o de forma controlada.

Esto es especialmente atractivo para notas o cables.

---

## 7. Estrategias posibles de temporada

# 7.1. Estrategia conservadora y muy buena para nacional
### Perfil
- cables,
- instrumentos,
- microfono,
- bonus completo,
- 1 o 2 notas bien resueltas.

### Por que funciona
Porque se apoya en misiones con mejor relacion entre dificultad y puntaje.

### Rango orientativo
Aproximadamente **100 a 160 puntos**, dependiendo de cuantas notas entren y de si el bonus queda intacto.

# 7.2. Estrategia competitiva fuerte
### Perfil
- instrumentos completos,
- microfono,
- cables,
- 3 o 4 notas,
- bonus bien protegido.

### Por que funciona
Ataca la mision central sin depender todavia de un sistema super complejo de 6 notas.

### Rango orientativo
Aproximadamente **160 a 210 puntos**.

# 7.3. Estrategia de punta
### Perfil
- casi todo el tablero,
- varias notas con clasificacion rapida,
- objetos de escenario resueltos,
- bonus completo.

### Desafio
El gran problema no es solo el tiempo. Es la combinacion de:
- mucho transporte,
- descarga limpia,
- y cero errores cerca del escenario.

---

## 8. Desafios tecnicos especificos de Elementary 2026

# 8.1. La mision grande no es solo leer color
Muchos equipos van a pensar que el gran desafio del ano son los colores de las notas.
Eso es verdad solo en parte.

El verdadero desafio es este:

> leer color + mantener orden + descargar upright + no equivocarse de objetivo.

# 8.2. El escenario castiga robots muy agresivos
Si el accesorio frontal es demasiado ancho o sobresaliente, puede tocar:
- parlantes,
- amplificador,
- o arruinar cables al entrar o salir.

# 8.3. Hay una mezcla rara de objetos “faciles” y “delicados”
- instrumentos: buenos para lote,
- microfono: delicado,
- cables: delicados por orientacion,
- notas: muchas y de alto valor.

Eso obliga a que el robot no sea solo un gran empujador. Tiene que tener algo de fineza.

# 8.4. El tablero favorece secuencias inteligentes por zona
Como los objetos estan agrupados por sectores, una buena estrategia debe pensar por zonas y no solo por misiones escritas en el reglamento.

Ejemplo:
- sector camion: instrumentos y microfono,
- sector superior: notas,
- sector escenario izquierdo: cables y bonus sensible.

---

## 9. Ideas de rutas utiles

# 9.1. Ruta por sectores
1. resolver primero zona camion,
2. luego atacar notas,
3. dejar escenario fino para un momento controlado,
4. o al reves, si el robot necesita el frente libre para el escenario.

### Ventaja
Menos viajes cruzados y menos caos.

# 9.2. Ruta de puntaje rapido
1. 3 instrumentos,
2. microfono,
3. 1 o 2 notas fijas,
4. bonus intacto.

### Ventaja
Da una ronda fuerte relativamente pronto.

# 9.3. Ruta de crecimiento competitivo
1. construir una corrida base que sume bien sin randomizacion compleja,
2. agregar una randomizada,
3. luego dos,
4. recien despues pensar en alta carga multiple.

---

## 10. Recomendaciones concretas de coach

### 10.1. Si el equipo esta en fase inicial
Priorizar:
- instrumentos,
- microfono,
- cables,
- bonus.

Y resolver notas primero como rutina simple de una por vez.

### 10.2. Si el robot ya es estable
Pasar a:
- 2 notas por viaje,
- o una estrategia muy consistente de 3 o 4 notas totales.

### 10.3. Si los objetos llegan pero se caen
No acelerar.
Primero revisar:
- forma del mecanismo,
- suelta,
- frenado,
- alineacion,
- y altura de descarga.

### 10.4. Si el robot pierde bonus
Eso suele ser mas grave que tardar 2 o 3 segundos mas.
Conviene:
- achicar el envelope del accesorio,
- bajar velocidad en escenario,
- y separar mejor las maniobras de zona izquierda.

### 10.5. Si el robot mezcla notas
No intentar todavia un magazine grande.
Primero hacer una arquitectura interna mas simple, por ejemplo:
- 2 canales,
- separadores,
- o una captura de a una con mucho control.

---

## 11. Que intentaria yo como plan de desarrollo del equipo

Si yo estuviera coachando al equipo para nacional, propondria este orden de trabajo:

### Etapa 1
- robot base estable,
- una ruta fuerte de instrumentos,
- bonus protegido.

### Etapa 2
- microfono consistente.

### Etapa 3
- cables con buena orientacion final.

### Etapa 4
- nota roja y verde, que no son random.

### Etapa 5
- una nota random con deteccion simple.

### Etapa 6
- estrategia de 2 notas por viaje o 3-4 notas totales.

### Etapa 7
- optimizacion general de tiempo.

Este orden tiene una logica clara:
- primero puntos relativamente accesibles,
- despues objetos delicados,
- y recien al final la parte de mayor complejidad combinada.

---

## 12. Conclusiones finales

Elementary 2026 es un tablero muy lindo porque permite crecer por niveles.
No obliga a que todos los equipos hagan lo mismo.

Un equipo principiante puede disfrutar y sumar puntos con:
- instrumentos,
- microfono,
- cables.

Un equipo mas fuerte puede escalar con:
- notas,
- transporte multiple,
- y rutas optimizadas.

### La gran leccion estrategica del ano
> **No gana solo el robot que mas objetos mueve. Gana el robot que los mueve con orden, sin caidas, y sin perder bonus.**

### Segunda leccion
> **Las notas son la mision estrella, pero la base competitiva suele construirse antes con instrumentos, microfono, cables y una mecanica muy estable.**

### Recomendacion final de coach
Para pelear arriba en nacional, yo buscaria un robot que haga muy bien estas tres cosas:
1. transporte multiple robusto para instrumentos,
2. descarga limpia para microfono y cables,
3. una estrategia realista de notas, empezando por 1 o 2 por viaje, no por 6 de golpe.

---

## Fuentes base

- Reglas oficiales WRO RoboMission Elementary 2026
- Reglas generales WRO RoboMission 2026
- Q&A oficial WRO
- `README.md` y `docs/es/competition/README.md` de este repo
