# Estrategia C: Programación Híbrida (Bloques + Python) — Guía Completa

## Resumen

El equipo Elementary de IITA usa una estrategia de dos capas:

- **Capa 1 (Python):** Claude genera una biblioteca de funciones llamada `robot_lib.py` con toda la lógica compleja (seguimiento de línea, PID, intersecciones, calibración, giroscopio).
- **Capa 2 (Bloques):** Los alumnos arman el programa de misión en Pybricks Blocks, usando bloques visuales simples que llaman a las funciones de la biblioteca.

El resultado: los chicos trabajan con bloques fáciles de entender, pero el robot ejecuta lógica avanzada de competencia escrita por Claude.

## Arquitectura de archivos en Pybricks

```
Pybricks (en el navegador del alumno)
│
├── robot_lib          ← Proyecto Python (creado una vez)
│   └── robot_lib.py   ← Funciones complejas (Claude las escribe)
│
├── mision_1           ← Proyecto de Bloques (una misión)
│   └── (bloques)      ← Setup + Import robot_lib + llamadas simples
│
├── mision_2           ← Proyecto de Bloques (otra misión)
│   └── (bloques)      ← Setup + Import robot_lib + llamadas simples
│
└── calibrar           ← Proyecto Python (utilidad)
    └── calibrar.py    ← Programa de calibración (Claude lo escribe)
```

### En el repo GitHub

```
software/programs/
├── robot_lib.py       ← La biblioteca (fuente de verdad)
├── base_config.py     ← Config legada (reemplazada por robot_lib)
├── calibrar.py        ← Programa de calibración
└── misiones/          ← Python equivalente de cada misión (para referencia)
    ├── mision_1.py
    └── mision_2.py

hardware/
└── robot-definition.md ← Definición maestra del robot
```

## Paso a paso: cómo configurar todo

### Paso 1: Crear robot_lib.py en Pybricks

1. Abrir Pybricks (code.pybricks.com)
2. Ir a **Files → +** → elegir **Python** → nombre: `robot_lib`
3. Copiar el contenido de `software/programs/robot_lib.py` del repo
4. Pegar en el editor de Pybricks

**Este archivo NO se ejecuta solo.** Es una biblioteca que otros programas importan.

### Paso 2: Crear un programa de misión en Bloques

1. En Pybricks → **Files → +** → elegir **Block coding** → nombre: `mision_1`
2. En el Setup block, configurar:
   - Hub: SPIKE Prime
   - Motor A: Izquierdo, Antihorario
   - Motor B: Derecho
   - DriveBase: Motor A + Motor B, Rueda 56mm, Track 112mm, Gyro: Sí
   - Sensor Color D
3. Agregar bloque **"Import from: robot_lib"**
   - Seleccionar las funciones que necesitás

### Paso 3: Usar las funciones en bloques

Dentro del programa de bloques, usás el bloque **"Run Task"** para llamar funciones de la biblioteca:

```
[SETUP]
  Hub: SPIKE Prime
  Motor A (izq, antihorario) + Motor B (der) → DriveBase (56mm, 112mm, Gyro)
  Sensor Color: Puerto D
  Import from robot_lib: seguir_linea, ir_a_cruce, alinear

[INICIO]
  |  Esperar botón centro
  |  Esperar 0.5s
  |  
  |  Run Task: ir_a_cruce(sensor, robot, "derecha", 2)
  |  Avanzar 40mm
  |  Girar 90°
  |  Avanzar 25mm
  |  Run Task: ir_a_cruce(sensor, robot, "ambas", 1)
  |  Parar
```

## ¿Qué funciones tiene robot_lib.py?

La biblioteca organiza las funciones en categorías:

### Categoría 1: Seguimiento de línea
- `seguir_linea(sensor, robot, borde, vel, kp, kd)` — Un ciclo de PID
- `ir_a_cruce(sensor, robot, lado, n, borde, vel)` — Seguir hasta N-ésima intersección
- `seguir_y_girar(sensor, robot, lado, n, lado_giro)` — Seguir y desviarse
- `seguir_hasta_fin(sensor, robot, borde, vel)` — Seguir hasta que la línea se termine

### Categoría 2: Movimiento preciso
- `avanzar_preciso(robot, distancia)` — Avance con frenado suave
- `girar_preciso(robot, angulo)` — Giro con perfil preciso
- `perfil_preciso(robot)` / `perfil_normal(robot)` / `perfil_rapido(robot)`

### Categoría 3: Búsqueda y alineación
- `buscar_linea(sensor, robot, max_mm)` — Avanzar hasta encontrar línea
- `alinear(s_izq, s_der, m_izq, m_der)` — Alinearse perpendicular

### Categoría 4: Giroscopio
- `init_gyro(hub)` — Esperar calibración con feedback visual
- `recalibrar(robot)` — Recalibrar en medio de misión

### Categoría 5: Garra/Mecanismo
- `garra_abrir(motor)` / `garra_cerrar(motor)` — Controlar mecanismo

## Cómo el alumno trabaja día a día

### Sesión típica de entrenamiento

```
1. ALUMNO: "Quiero que el robot vaya hasta la 2da intersección
           a la derecha y recoja el objeto"

2. COACH/CLAUDE: Genera pseudocódigo de bloques:

   [INICIO]
   |  Esperar botón centro
   |  ir_a_cruce(sensor, robot, "derecha", 2)
   |  Avanzar 40mm
   |  Girar 90°
   |  buscar_linea(sensor, robot, 200)
   |  seguir_hasta_fin(sensor, robot)
   |  garra_cerrar(motor_garra)
   |  Esperar 0.5s

3. ALUMNO: Arma los bloques en Pybricks siguiendo el pseudocódigo

4. ALUMNO: Prueba en el robot

5. Si hay problemas → copia el Python del panel derecho
   y lo pega en el chat para que Claude diagnostique
```

### Flujo de actualización de robot_lib.py

```
1. Claude actualiza robot_lib.py en el repo
2. El alumno (o coach) copia el contenido nuevo
3. Abre el proyecto "robot_lib" en Pybricks
4. Selecciona todo → pega el nuevo contenido
5. Todos los programas de bloques que importan robot_lib
   automáticamente usan las funciones actualizadas
```

## Ventajas de esta estrategia para IITA

### Para los alumnos (8-12 años)
- Trabajan con bloques visuales, no texto
- No necesitan entender PID ni giroscopio internamente
- Cada misión es un programa de bloques cortito y claro
- Pueden experimentar cambiando el orden de los bloques
- Si algo no funciona, muestran el Python a Claude

### Para el coach (Gustavo)
- Claude genera y mantiene la biblioteca avanzada
- Los alumnos se enfocan en estrategia, no en programación compleja
- Los valores calibrados se centralizan en `robot-definition.md`
- Los programas de misión son intercambiables y modulares

### Para la IA (Claude)
- Puede leer el Python generado por los bloques del alumno
- Puede actualizar `robot_lib.py` con mejoras
- Puede generar pseudocódigo de bloques para nuevas misiones
- Puede diagnosticar problemas leyendo el Python del panel derecho

## Limitaciones y workarounds

| Limitación | Workaround |
|-----------|------------|
| Los bloques no pueden pasar el objeto DriveBase a robot_lib | El alumno configura DriveBase en el Setup de bloques, y pasa `robot` como argumento |
| Import en bloques requiere seleccionar funciones una por una | Usar una función helper `fn(name, *args)` si hay muchas funciones |
| No se puede versionar bloques en Git | Guardar el Python equivalente en `software/programs/misiones/` |
| Los bloques son específicos de cada computadora | Usar Backup/Restore de Pybricks para compartir entre PCs |

## Checklist para empezar

- [ ] Verificar que el equipo tiene licencia Pybricks Blocks
- [ ] Crear proyecto Python `robot_lib` en Pybricks con el contenido del repo
- [ ] Crear proyecto Python `calibrar` en Pybricks
- [ ] Ejecutar calibración y actualizar `hardware/robot-definition.md`
- [ ] Crear primer programa de bloques `mision_test` que importe robot_lib
- [ ] Probar que `ir_a_cruce` funciona desde bloques
- [ ] Entrenar a los alumnos en el flujo: describir → pseudocódigo → bloques → probar
