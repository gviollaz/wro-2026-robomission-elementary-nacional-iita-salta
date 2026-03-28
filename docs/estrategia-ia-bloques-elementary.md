# Estrategia de Programación con IA en Pybricks Bloques para WRO Elementary

## Contexto del problema

En WRO Elementary, los alumnos de IITA (8-12 años) necesitan programar robots SPIKE Prime. La categoría permite cualquier software, pero los chicos trabajan mejor con **bloques visuales**. La pregunta es: ¿cómo puede una IA como Claude ayudar a programar en bloques?

## Análisis técnico de Pybricks Blocks

### ¿Cómo funciona internamente?

Pybricks Blocks usa **Google Blockly** como motor. Internamente:

1. Los bloques se representan como **estructuras JSON/XML** en memoria del navegador
2. Cada bloque genera **código Python equivalente** en tiempo real (panel derecho, READ-ONLY)
3. Los programas se guardan en **IndexedDB del navegador** (localStorage)
4. Los backups se exportan como archivos `.zip` que contienen archivos `.py` y metadatos

### Limitaciones clave

- **No hay formato estándar de archivo de bloques** que se pueda crear externamente — los bloques solo se crean dentro del editor web de Pybricks
- **El panel Python junto a los bloques es de solo lectura** — no se puede editar Python en un proyecto de bloques
- **Los bloques requieren licencia** — Pybricks Block coding requiere Patreon/licencia
- **No hay integración Git** — los archivos se manejan dentro del navegador, no hay sync con repos

## ¿Qué puede hacer Claude con bloques?

### ✅ Lo que SÍ puedo hacer

| Capacidad | Cómo | Utilidad |
|-----------|------|---------|
| **Generar código Python equivalente** | Escribo el Python que producirían los bloques | Los chicos pueden copiar y entender la lógica |
| **Describir bloques paso a paso** | Describo qué bloques arrastrar y dónde | Como un instructor guiando al alumno |
| **Leer Python generado por bloques** | Si me pasan el código Python del panel derecho, lo analizo | Debugging y mejora de programas existentes |
| **Crear módulos Python importables** | Escribo archivos `.py` que los bloques pueden importar como "External Task" | Funciones complejas accesibles desde bloques |
| **Generar pseudocódigo de bloques** | Describo la estructura en formato visual textual | Planificar antes de armar en el editor |
| **Revisar y optimizar lógica** | Analizo la estrategia del programa | Mejorar sin tocar los bloques directamente |

### ❌ Lo que NO puedo hacer

| Limitación | Por qué | Alternativa |
|-----------|---------|-------------|
| Crear archivos de bloques directamente | No existe formato público de archivo de bloques Pybricks | Generar Python equivalente + guía de armado |
| Editar programas de bloques en el editor | El editor es web-only, sin API | Describir los cambios que el alumno debe hacer |
| Ver los bloques del alumno | Solo puedo ver el Python generado | Pedir que copien el código Python del panel derecho |
| Crear bloques personalizados en Pybricks | Pybricks no soporta bloques custom del usuario | Usar "External Task" como alternativa |

## Las 4 estrategias posibles

---

### ESTRATEGIA A: "Python puro" (sin bloques)

**Los alumnos programan directamente en Python dentro de Pybricks.**

**Cómo funciona:**
- Claude genera el código `.py` completo
- Los alumnos crean un "Python project" en Pybricks (no "Block project")
- Copian y pegan el código, o lo importan

**Ventajas:**
- Claude tiene control total del código
- Máxima flexibilidad y poder
- Fácil de versionar en Git

**Desventajas:**
- Los chicos de Elementary (8-12 años) pueden tener dificultad con texto
- Menos visual e intuitivo
- Errores de tipeo causan frustración

**Recomendación:** Para equipos con al menos un miembro que lee y escribe código cómodo.

**Nivel de dificultad para el alumno: ⭐⭐⭐⭐ (Alto)**

---

### ESTRATEGIA B: "Bloques guiados por IA" (recomendada para Elementary)

**Claude describe paso a paso qué bloques arrastrar y el alumno los arma en Pybricks.**

**Cómo funciona:**
1. El alumno describe qué quiere que haga el robot
2. Claude genera instrucciones paso a paso en lenguaje natural:
   ```
   PASO 1: En la categoría "Setup", arrastrá el bloque "SPIKE Prime Hub"
   PASO 2: En "Motors", arrastrá "Motor" y configurá Puerto A, Sentido Antihorario
   PASO 3: En "Motors", arrastrá otro "Motor" y configurá Puerto B
   PASO 4: En "DriveBase", arrastrá "DriveBase" y conectá Motor A (izq) y Motor B (der)
           Poné diámetro rueda = 56 y distancia entre ruedas = 112
   PASO 5: Marcá la opción "Use Gyro" en el bloque DriveBase
   ...
   ```
3. El alumno sigue las instrucciones arrastrando bloques
4. Claude también genera el Python equivalente para que el alumno pueda comparar

**Ventajas:**
- El alumno aprende a usar los bloques
- Mantiene la experiencia visual
- Claude puede generar instrucciones muy detalladas
- El alumno entiende qué hace cada bloque

**Desventajas:**
- Más lento que copiar código
- Requiere que el alumno tenga Pybricks blocks abierto
- Si hay muchos bloques, las instrucciones se hacen largas

**Recomendación: MEJOR OPCIÓN para Elementary.** Los chicos aprenden, la IA guía, y el resultado es un programa de bloques real.

**Nivel de dificultad para el alumno: ⭐⭐ (Bajo)**

---

### ESTRATEGIA C: "Híbrida: Bloques + External Task en Python"

**El programa principal se arma en bloques. Las funciones complejas van en un archivo Python que los bloques importan.**

**Cómo funciona:**
1. Claude crea un archivo Python (`robot_lib.py`) con funciones complejas:
   ```python
   # robot_lib.py - Biblioteca del equipo
   def seguir_linea(sensor, robot, velocidad=150, kp=1.5):
       error = sensor.reflection() - 50
       robot.drive(velocidad, kp * error)
   
   def ir_a_interseccion(sensor_izq, sensor_der, robot, ...):
       # ... lógica compleja de conteo de intersecciones
   ```

2. En Pybricks, el alumno crea un proyecto Python llamado `robot_lib` con ese código

3. El alumno crea un proyecto de **bloques** para la misión:
   - En el Setup, configura hub, motores, sensores con bloques normales
   - Usa el bloque "External Task" para importar `robot_lib`
   - En el programa principal, usa el bloque "Run Task" para llamar funciones

**Ejemplo del flujo:**
```
[Setup Block]
  Hub = SPIKE Prime
  Motor A = Izquierdo (antihorario)
  Motor B = Derecho
  DriveBase = Motor A + Motor B, rueda 56mm, track 112mm
  Sensor Color = Puerto E

[Import External Task: robot_lib]
  Import: seguir_linea

[Start Block]
  Repetir por siempre:
    [Run Task: seguir_linea(sensor, robot)]
```

**Ventajas:**
- Lo mejor de ambos mundos: visual para el flujo, Python para la complejidad
- Claude puede escribir las funciones complejas
- Los bloques mantienen el programa principal simple y legible
- Las funciones se pueden reusar entre misiones

**Desventajas:**
- Requiere entender el concepto de "importar"
- El alumno necesita manejar dos tipos de archivos
- Más setup inicial

**Recomendación:** Para equipos que ya tienen experiencia con bloques y quieren subir de nivel.

**Nivel de dificultad para el alumno: ⭐⭐⭐ (Medio)**

---

### ESTRATEGIA D: "Claude genera Python, alumno lo compara con bloques"

**Claude genera Python y el alumno lo usa como referencia para armar bloques equivalentes.**

**Cómo funciona:**
1. Claude genera código Python con comentarios claros
2. El alumno abre un proyecto de bloques y arma el equivalente
3. El alumno compara el Python generado por sus bloques (panel derecho) con el de Claude
4. Si coinciden → el programa es correcto

**Ventajas:**
- Excelente para aprender la relación bloques↔Python
- El alumno puede verificar su trabajo
- Desarrolla habilidades de debugging

**Desventajas:**
- El alumno necesita hacer la "traducción" manual
- Más trabajo para el alumno

**Recomendación:** Como ejercicio de aprendizaje, no para velocidad de competencia.

**Nivel de dificultad para el alumno: ⭐⭐⭐ (Medio)**

---

## Cómo puede Claude leer programas existentes de los alumnos

### Opción 1: Copiar el Python generado (MÁS FÁCIL)

En Pybricks Blocks, al lado derecho de los bloques aparece el código Python equivalente. El alumno puede:

1. Hacer clic derecho en el panel Python → "Select All" → "Copy"
2. Pegarlo en el chat con Claude
3. Claude analiza, sugiere mejoras, detecta errores

**Instrucciones para el alumno:**
```
"Abrí tu programa de bloques en Pybricks.
 Mirá el panel derecho donde aparece el código Python.
 Seleccioná todo el texto (Ctrl+A) y copiá (Ctrl+C).
 Pegalo acá en el chat."
```

### Opción 2: Backup y subir al repo

1. En Pybricks → Files → "Back up all programs" (descarga un .zip)
2. Subir el .zip al repo en `software/programs/backups/`
3. Claude puede leer los archivos `.py` dentro del backup

### Opción 3: Screenshot + descripción

Si todo lo demás falla, el alumno puede:
1. Sacar screenshot de los bloques
2. Describir qué hace el programa
3. Claude interpreta y sugiere

## Formato de pseudocódigo de bloques para Claude

Para que Claude pueda "hablar en bloques", definimos este formato de pseudocódigo:

```
=== PROGRAMA: [nombre] ===

[SETUP]
  Hub: SPIKE Prime
  Motor Izq: Puerto A, Antihorario
  Motor Der: Puerto B
  DriveBase: Izq=A, Der=B, Rueda=56mm, Track=112mm, Gyro=Sí
  Sensor Color 1: Puerto C
  Sensor Color 2: Puerto D
  Sensor Color 3: Puerto E

[INICIO]
  |  Esperar hasta que Botón Centro presionado
  |  Esperar 0.5 segundos
  |  
  |  [Repetir por siempre]
  |  |  error ← (Reflexión Sensor D) - 50
  |  |  corrección ← 1.5 × error
  |  |  Conducir a 150 mm/s girando a (corrección) °/s
  |  |  
  |  |  [Si (Reflexión Sensor C) < 25]
  |  |  |  Parar
  |  |  |  Salir del bucle
  |  |  [Fin Si]
  |  |  
  |  |  Esperar 0.01 segundos
  |  [Fin Repetir]
```

Este formato permite que Claude:
- Genere programas que los alumnos pueden traducir a bloques
- Lea descripciones de programas existentes
- Sugiera modificaciones de forma clara

## Workflow recomendado para IITA Elementary

### Fase 1: Aprendizaje (primeras semanas)

1. **Alumnos aprenden bloques básicos** en Pybricks con la guía interactiva
2. **Claude genera pseudocódigo** que los alumnos traducen a bloques
3. **Estrategia B** (bloques guiados) para programas simples

### Fase 2: Desarrollo (semanas intermedias)

1. **Alumnos crean programas en bloques** para cada subtarea
2. **Comparten el Python generado** con Claude para revisión
3. Claude sugiere mejoras y optimizaciones
4. **Estrategia B + C** según complejidad

### Fase 3: Competencia (últimas semanas)

1. **Funciones complejas en Python** (biblioteca del equipo) creadas por Claude
2. **Programa principal en bloques** que importa la biblioteca
3. **Estrategia C** (híbrida) para máximo rendimiento
4. Claude ayuda con debugging leyendo el Python generado

### Flujo de trabajo con Claude en cada sesión

```
1. Alumno describe qué quiere hacer
   → "Quiero que el robot siga la línea hasta la 2da intersección a la derecha"

2. Claude genera:
   a) Pseudocódigo de bloques (para armar en Pybricks)
   b) Python equivalente (para verificar)
   c) Instrucciones paso a paso si es necesario

3. Alumno arma los bloques en Pybricks

4. Alumno copia el Python generado y lo pega en el chat
   → Claude compara con lo esperado y sugiere correcciones

5. Alumno prueba en el robot

6. Si hay problemas, alumno describe qué pasó
   → Claude sugiere ajustes
```

## Crear "nuestros propios bloques": alternativas reales

Pybricks **no permite crear bloques personalizados del usuario**. Pero hay alternativas:

### Alternativa 1: Funciones en "My Blocks" (Pybricks built-in)

Pybricks Blocks tiene la funcionalidad de crear **"My Blocks"** (funciones definidas por el usuario). El alumno puede:

1. Seleccionar un grupo de bloques
2. Convertirlos en un "My Block" con nombre y parámetros
3. Reutilizar ese bloque en otras partes del programa

**Limitación:** Solo dentro del mismo programa, no se comparten entre programas.

### Alternativa 2: External Task (biblioteca Python)

Como se explicó en Estrategia C, el equipo puede tener un archivo Python con funciones que se importan desde bloques.

### Alternativa 3: Plantillas de programa

Claude puede generar **programas plantilla** completos que los alumnos personalizan:

1. Programa plantilla de seguimiento de línea
2. Programa plantilla de calibración
3. Programa plantilla de misión con menú

Los alumnos modifican valores (velocidades, puertos, etc.) sin cambiar la estructura.

## Próximos pasos concretos para IITA

1. **Verificar licencia Pybricks Blocks** — ¿los equipos tienen acceso a Block coding?
2. **Definir puertos estándar** del robot Elementary para que las plantillas funcionen
3. **Crear biblioteca `robot_lib.py`** con las funciones de navegación
4. **Probar el workflow de External Task** con un programa simple
5. **Entrenar a los alumnos** en el flujo: describir → pseudocódigo → bloques → probar → debugging con Claude

## Resumen de estrategias

| Estrategia | Para quién | Claude hace | Alumno hace | Dificultad |
|-----------|-----------|-------------|-------------|------------|
| A: Python puro | Avanzados | Genera código | Copia y pega | ⭐⭐⭐⭐ |
| **B: Bloques guiados** | **Elementary** | **Instrucciones paso a paso** | **Arma bloques** | **⭐⭐** |
| C: Híbrida | Intermedios | Biblioteca Python + pseudocódigo | Bloques + import | ⭐⭐⭐ |
| D: Comparación | Aprendizaje | Python de referencia | Traduce a bloques | ⭐⭐⭐ |

**Recomendación para IITA Elementary: empezar con B, evolucionar a C cuando estén cómodos.**
