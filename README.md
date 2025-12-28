# Simulación de Movimiento Rectilíneo Uniformemente Acelerado (MRUA)

Este proyecto implementa una simulación física unidimensional de un móvil con aceleración constante (MRUA) utilizando Python.

El objetivo es traducir las ecuaciones fundamentales de la cinemática a código ejecutable y analizar el comportamiento físico del sistema de forma programática.

---

## Descripción

El script calcula la **posición** y la **velocidad** de un móvil que se desplaza en una dimensión bajo aceleración constante en función del tiempo.

Para distintos instantes discretos, el programa imprime:
- La velocidad instantánea
- La posición del móvil
- El instante en el que el móvil se detiene
- El cambio de sentido del movimiento cuando la velocidad se vuelve negativa

---

## Modelo físico

La simulación se basa en las ecuaciones cinemáticas:

- Velocidad:  
  v(t) = v₀ + a · t

- Posición:  
  x(t) = x₀ + v₀ · t + (1/2) · a · t²

donde:
- x₀ es la posición inicial  
- v₀ es la velocidad inicial  
- a es la aceleración constante  
- t es el tiempo  

---

## Detalles de implementación

- Las ecuaciones físicas se implementan como funciones reutilizables en Python.
- Se utiliza un bucle para evaluar la evolución temporal del sistema.
- Mediante estructuras condicionales se detecta:
  - el instante en el que la velocidad se anula
  - el cambio de sentido del movimiento

---

## Parámetros de ejemplo

```python
x0 = 5    # m
v0 = 8    # m/s
a  = -2   # m/s²
