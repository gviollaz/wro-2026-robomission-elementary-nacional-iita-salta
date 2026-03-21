# Arquitectura del Robot - Elementary

## Requisitos

- Caber en 250 x 250 x 250 mm antes del inicio
- LEGO Spike Prime con firmware Pybricks
- Sensor de color para detectar notas randomizadas
- Mecanismo para mover objetos (garra, pala, empujador)

## Diseno propuesto

> TODO: completar cuando se defina el diseno.

### Chasis
- Base diferencial (2 motores de traccion)
- Ruedas grandes (56mm) para mejor traccion

### Accesorios
- Garra/empujador frontal para mover cables, instrumentos, notas
- Sensor de color apuntando hacia abajo para detectar notas

### Puertos
| Puerto | Componente |
|--------|------------|
| A | Motor izquierdo (COUNTERCLOCKWISE) |
| B | Motor derecho |
| C | Motor garra/accesorio |
| D | Sensor de color |

## Consideraciones

- El robot debe ser compacto para no tocar objetos del bonus
- Velocidad baja cerca del escenario (amplificador, parlantes, clave)
- Priorizar consistencia sobre velocidad
