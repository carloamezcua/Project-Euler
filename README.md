# Soluciones de Project Euler

![Language](https://img.shields.io/badge/Language-Python-blue)
![Project Euler](https://img.shields.io/badge/Project%20Euler-Mathematics-green)
![Sin dependencias externas](https://img.shields.io/badge/Dependencias-0%20externas-success)

Este repositorio contiene mis soluciones personales a los problemas computacionales de **Project Euler**. El objetivo de este proyecto es practicar habilidades de programación, pensamiento matemático y diseño eficiente de algoritmos mientras documento mi proceso de aprendizaje.

Cada solución se verifica en el sitio web oficial de Project Euler antes de marcarla como completa.

## Mi Enfoque

Mi metodología se enfoca en entender los conceptos matemáticos detrás de cada problema en lugar de solo encontrar una solución que funcione.

Priorizo:
- Código Python claro y legible
- Explicaciones matemáticas y documentación del proceso de pensamiento
- Verificación de resultados en el sitio web oficial de Project Euler
- Mejora iterativa de las soluciones para optimización
- **No usar librerías externas**: construir herramientas propias cuando sea necesario

## Filosofía de dependencias

Este proyecto sigue una regla simple:

> Resolver con Python puro y utilidades propias, sin paquetes de terceros.

Cuando un problema requiera funciones reutilizables (primos, factores, divisores, etc.), estas se incorporarán en una librería interna del proyecto.

## Librería interna: `euler_lib`

La carpeta `euler_lib/` contiene una librería propia de apoyo a los notebooks con funciones matemáticas reutilizables.

### Funciones disponibles

| Función | Módulo | Descripción |
|---|---|---|
| `factores_primos(n)` | `factores_primos.py` | Descompone un número entero en sus factores primos |

### Uso

```python
import euler_lib as euler

euler.factores_primos(600851475143)  # [71, 839, 1471, 6857]
```

Con el tiempo, esta librería se expandirá con más funciones matemáticas reutilizables para evitar duplicación de lógica entre problemas.

## Detalles Técnicos

- **Lenguaje:** Python (puro, sin librerías externas)
- **Formato principal:** Jupyter Notebooks (`.ipynb`)
- **Utilidades internas:** módulo propio `euler_lib/`

## Cómo Usar

Cada notebook contiene:
1. Enunciado original del problema
2. Solución en Python
3. (Opcional) notas o insights matemáticos

Puedes abrirlos en Jupyter o cualquier visor compatible con notebooks.

## Estructura del repositorio (resumen)

- `001_multiples_of_3_or_5.ipynb` … `013_large_sum.ipynb`
- `euler_lib/`
	- `__init__.py`
	- `factores_primos.py`
- `README.md`

## Sobre Project Euler

Project Euler es una serie de problemas desafiantes de matemáticas/programación que requieren más que solo conocimientos matemáticos para resolver.

Visita [projecteuler.net](https://projecteuler.net/) para explorar todos los problemas.

---

*Este repositorio funciona como viaje de aprendizaje y portafolio técnico. Las soluciones y la librería interna evolucionan de forma continua con fines educativos.*
