# Soluciones de Project Euler

![Language](https://img.shields.io/badge/Language-Python-blue)
![Project Euler](https://img.shields.io/badge/Project%20Euler-Mathematics-green)
![Sin dependencias externas](https://img.shields.io/badge/Dependencias-0%20externas-success)
![Problemas resueltos](https://img.shields.io/badge/Resueltos-12%20de%2013-informational)

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

## Problemas

| # | Problema | Estado | Funciones de `euler_lib` |
|---|----------|--------|--------------------------|
| 001 | Multiples of 3 or 5 | ✅ Resuelto | — |
| 002 | Even Fibonacci Numbers | ✅ Resuelto | — |
| 003 | Largest Prime Factor | ✅ Resuelto | `factores_primos` |
| 004 | Largest Palindrome Product | ✅ Resuelto | — |
| 005 | Smallest Multiple | ✅ Resuelto | `factores_primos`, `potencias_factores` |
| 006 | Sum Square Difference | ✅ Resuelto | — |
| 007 | 10001st Prime | ✅ Resuelto | `es_primo` |
| 008 | Largest Product in a Series | ✅ Resuelto | — |
| 009 | Special Pythagorean Triplet | ✅ Resuelto | — |
| 010 | Summation of Primes | ✅ Resuelto | `criba_eratostenes` |
| 011 | Largest Product in a Grid | 🔧 En progreso | — |
| 012 | Highly Divisible Triangular Number | ✅ Resuelto | `numeros_divisibles` |
| 013 | Large Sum | ✅ Resuelto | — |

## Librería interna: `euler_lib`

La carpeta `euler_lib/` contiene una librería propia de apoyo a los notebooks con funciones matemáticas reutilizables.

### Funciones disponibles

| Función | Módulo | Descripción |
|---------|--------|-------------|
| `criba_eratostenes(n)` | `criba_eratostenes.py` | Criba de Eratóstenes: devuelve lista de primos hasta `n` |
| `es_primo(n)` | `es_primo.py` | Test de primalidad por división de prueba hasta √n |
| `factores_primos(n)` | `factores_primos.py` | Descompone un número entero en sus factores primos |
| `numeros_divisibles(n)` | `numeros_divisibles.py` | Devuelve lista ordenada de todos los divisores de `n` |
| `potencias_factores(factores)` | `potencias_factores.py` | Recibe lista de factores y devuelve dict `{factor: exponente}` |

### Uso

```python
import euler_lib as euler

euler.factores_primos(600851475143)   # [71, 839, 1471, 6857]
euler.criba_eratostenes(30)           # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
euler.es_primo(7)                     # True
euler.numeros_divisibles(28)          # [1, 2, 4, 7, 14, 28]
euler.potencias_factores([2, 2, 3])   # {2: 2, 3: 1}
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

## Estructura del repositorio

```
project-euler/
├── 000_TEST.ipynb
├── 001_multiples_of_3_or_5.ipynb
├── 002_even_fibonacci_numbers.ipynb
├── ...
├── 013_large_sum.ipynb
├── euler_lib/
│   ├── __init__.py
│   ├── criba_eratostenes.py
│   ├── es_primo.py
│   ├── factores_primos.py
│   ├── numeros_divisibles.py
│   └── potencias_factores.py
└── README.md
```

## Sobre Project Euler

Project Euler es una serie de problemas desafiantes de matemáticas/programación que requieren más que solo conocimientos matemáticos para resolver.

Visita [projecteuler.net](https://projecteuler.net/) para explorar todos los problemas.

---

## English Summary

This repository contains my personal solutions to **Project Euler** computational problems, written in pure Python with no external dependencies. A custom internal library (`euler_lib`) provides reusable math utilities (prime factorization, sieve of Eratosthenes, primality testing, divisor listing, etc.). Currently **12 of 13 problems solved**, with problem 011 in progress.

---

*Este repositorio funciona como viaje de aprendizaje y portafolio técnico. Las soluciones y la librería interna evolucionan de forma continua con fines educativos.*
