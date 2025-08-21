from vpython import *
from random import random

scene = canvas(
    title="VPython: ambas figuras se mueven a la misma esquina",
    width=900, height=600, background=color.white
)

def rand_color():
    return vector(random(), random(), random())


def crear_conos_vertical(posicion, altura, radio, n):
    if n == 0:
        return []
    c = cone(pos=posicion, axis=vector(0, altura, 0), radius=radio, color=rand_color())
    return [c] + crear_conos_vertical(
        posicion + vector(0, 1.4 * altura, 0),
        altura * 0.8, radio * 0.8, n - 1
    )

conos = crear_conos_vertical(vector(0, -4, 0), altura=1.2, radio=0.8, n=6)


cilindro = cylinder(pos=vector(-6, -4, 0), axis=vector(0, 1.2, 0), radius=0.6, color=color.red)
piramide = pyramid(pos=vector(4, -3, 0), size=vector(1.2, 1.2, 1.2), color=color.green)


LIM_X, LIM_Y = 6.5, 4.5
TARGET = vector(LIM_X, LIM_Y, 0)   


moviles = [
    {"obj": cilindro, "spd": 0.03, "tcol": 0.0, "per_col": 0.5},
    {"obj": piramide, "spd": 0.02, "tcol": 0.0, "per_col": 0.3},
]


t_conos, per_conos = 0.0, 0.6

dt = 1/240
while True:
    rate(240)

    
    for m in moviles:
        obj = m["obj"]
        v = TARGET - obj.pos
        d = mag(v)
        if d > 1e-3:
            
            step = min(m["spd"], d)
            obj.pos += (v / d) * step

        m["tcol"] += dt
        if m["tcol"] >= m["per_col"]:
            obj.color = rand_color()
            m["tcol"] = 0.0

    
    t_conos += dt
    if t_conos >= per_conos:
        for c in conos:
            c.color = rand_color()
        t_conos = 0.0
