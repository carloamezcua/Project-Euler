# Project Euler Solutions

![Language](https://img.shields.io/badge/Language-Python-blue)
![Project Euler](https://img.shields.io/badge/Project%20Euler-Mathematics-green)
![No external dependencies](https://img.shields.io/badge/Dependencies-0%20external-success)
![Problems Solved](https://img.shields.io/badge/Problems%20Solved-12-blueviolet)

This repository contains my personal solutions to [Project Euler](https://projecteuler.net/) computational problems. The goal is to practice programming skills, mathematical thinking, and efficient algorithm design while documenting my learning process.

Every solution is verified on the official Project Euler website before being marked as complete.

## My Approach

My methodology focuses on understanding the mathematical concepts behind each problem rather than just finding a working solution.

Priorities:
- Clear, readable Python code
- Mathematical explanations and thought process documentation
- Verification of results on the official Project Euler website
- Iterative improvement and optimization of solutions
- **No external libraries**: build my own tools when needed

## Dependency Philosophy

This project follows a simple rule:

> Solve with pure Python and custom utilities — no third-party packages.

When a problem requires reusable functions (primes, factors, divisors, etc.), they are built into the project's internal library.

## Internal Library: `euler_lib`

The `euler_lib/` folder contains a custom support library for the notebooks with reusable mathematical functions.

### Available Functions

| Function | Module | Description |
|---|---|---|
| `criba_eratostenes(n)` | `criba_eratostenes.py` | Sieve of Eratosthenes — returns all primes up to `n` |
| `es_primo(n)` | `es_primo.py` | Primality test via trial division up to $\sqrt{n}$ |
| `factores_primos(n)` | `factores_primos.py` | Prime factorization — returns list of prime factors (with repetition) |
| `numeros_divisibles(n)` | `numeros_divisibles.py` | Returns a sorted list of all divisors of `n` |
| `potencias_factores(factors)` | `potencias_factores.py` | Maps a list of prime factors to a `{prime: exponent}` dict |

### Usage

```python
import euler_lib as euler

euler.factores_primos(600851475143)   # [71, 839, 1471, 6857]
euler.criba_eratostenes(30)           # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
euler.es_primo(7)                     # True
euler.numeros_divisibles(28)          # [1, 2, 4, 7, 14, 28]
euler.potencias_factores([2, 2, 3])   # {2: 2, 3: 1}
```

## Problems Solved

| # | Problem | Status | Uses `euler_lib`? |
|--:|---|---|---|
| 001 | [Multiples of 3 or 5](problems/001_multiples_of_3_or_5.ipynb) | ✅ Solved | — |
| 002 | [Even Fibonacci Numbers](problems/002_even_fibonacci_numbers.ipynb) | ✅ Solved | — |
| 003 | [Largest Prime Factor](problems/003_largest_prime_factor.ipynb) | ✅ Solved | `factores_primos` |
| 004 | [Largest Palindrome Product](problems/004_largest_palindrome_product.ipynb) | ✅ Solved | — |
| 005 | [Smallest Multiple](problems/005_smallest_multiple.ipynb) | ✅ Solved | `factores_primos`, `potencias_factores` |
| 006 | [Sum Square Difference](problems/006_sum_square_difference.ipynb) | ✅ Solved | — |
| 007 | [10 001st Prime](problems/007_10001st_prime.ipynb) | ✅ Solved | `es_primo` |
| 008 | [Largest Product in a Series](problems/008_largest_product_in_a_series.ipynb) | ✅ Solved | — |
| 009 | [Special Pythagorean Triplet](problems/009_special_pythagorean_triplet.ipynb) | ✅ Solved | — |
| 010 | [Summation of Primes](problems/010_summation_of_primes.ipynb) | ✅ Solved | `criba_eratostenes` |
| 011 | [Largest Product in a Grid](problems/011_largest_product_in_a_grid.ipynb) | ⚠️ In progress | — |
| 012 | [Highly Divisible Triangular Number](problems/012_highly_divisible_triangular_number.ipynb) | ✅ Solved | `numeros_divisibles` |
| 013 | [Large Sum](problems/013_large_sum.ipynb) | ✅ Solved | — |

## Technical Details

- **Language:** Python (pure, no external libraries)
- **Main format:** Jupyter Notebooks (`.ipynb`)
- **Internal utilities:** custom `euler_lib/` module

## How to Use

Each notebook in the `problems/` folder contains:
1. Original problem statement
2. Python solution
3. (Optional) mathematical notes or insights

You can open them in Jupyter, VS Code, or any notebook-compatible viewer.

## Repository Structure

```
Project-Euler/
├── problems/
│   ├── 000_TEST.ipynb
│   ├── 001_multiples_of_3_or_5.ipynb
│   ├── ...
│   └── 013_large_sum.ipynb
├── euler_lib/
│   ├── __init__.py
│   ├── criba_eratostenes.py
│   ├── es_primo.py
│   ├── factores_primos.py
│   ├── numeros_divisibles.py
│   └── potencias_factores.py
└── README.md
```

## About Project Euler

Project Euler is a series of challenging mathematical and computational problems that require more than just mathematical knowledge to solve.

Visit [projecteuler.net](https://projecteuler.net/) to explore all problems.

---

*This repository serves as both a learning journey and a technical portfolio. Solutions and the internal library evolve continuously for educational purposes.*
