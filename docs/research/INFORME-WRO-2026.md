# Informe WRO 2026 — Hardware upgrade IITA Salta (Elementary)

## ⚠️ Restricciones Elementary (reglamento WRO 2026)

- ❌ **CÁMARAS PROHIBIDAS** (solo permitidas en Junior)
- ❌ LIDAR prohibido
- Máximo **4 motores** (Junior permite 5)
- Dimensiones máx: 250×250×250 mm
- Comunicación inalámbrica entre componentes PROHIBIDA
- Los alumnos (8-12 años) deben poder explicar TODO al jurado

## Arquitectura recomendada

SPIKE Prime + Pybricks + **LMS-ESP32 v2.0** (puente LPF2 por cable) + **Hiwonder 8-ch IR I2C** (array de línea).

El LMS-ESP32 se conecta al Spike Prime por cable LPF2 (legal) y expone 8 sensores IR via protocolo PUPRemote. Reemplaza al sensor de color LEGO individual con un array de 8 sensores → PID avanzado → seguimiento de línea mucho más rápido.

## BOM Elementary P0+P1 (~$89-105 USD)

| Componente | USD | Fuente |
|---|---|---|
| LMS-ESP32 v2.0 | 32 + 15 envío | antonsmindstorms.com |
| Hiwonder 8-ch IR I2C | 13 | AliExpress |
| Cable LPF2 extra | 5 | AliExpress/LEGO |
| Jumpers Dupont | 2 | AliExpress |

## Lo que NO recomendamos para Elementary

- ❌ PCB custom: muy complejo para explicar al jurado
- ❌ Cámaras: PROHIBIDAS por reglamento
- ❌ Motores Pololu/N20: requieren PID custom
- ❌ Bluetooth/WiFi entre componentes: PROHIBIDO

## Explicación para el jurado (preparar con los chicos)

"Este módulo lee 8 luces infrarrojas que detectan la línea negra del campo y le manda la información al Spike Prime por un cable. Lo programamos en MicroPython."

## Recursos

- Reglamento: wro-association.org/wp-content/uploads/WRO-2026-RoboMission-General-Rules.pdf
- PUPRemote: github.com/antonvh/PUPRemote
- LMS-ESP32: antonsmindstorms.com/product/wifi-python-esp32-board-for-mindstorms/

Ver el informe completo (Junior + Elementary + investigación con 30+ fuentes) en el repo Junior: `docs/research/INFORME-WRO-2026.md`.
