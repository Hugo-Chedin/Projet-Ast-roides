import random
from pygame.math import Vector2

import core

def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 800]

def run():
    core.cleanScreen()

    core.memory("position",core.memory("position") + core.memory("vitesse"))

    #controle
    if core.getKeyPressList("z"):
        core.memory("vitesse").scale_to_length(core.memory("vitesse").length()+5)

    if core.getKeyPressList("d"):
        core.memory("vitesse",core.memory("vitesse").rotate(5))

    print(core.memory("vitesse"))

    vectP2 = Vector2(core.memory("vitesse"))

    vectP2.scale_to_length(40)
    p2 = core.memory("position") + vectP2

    vectP1 = core.memory("vitesse")
    vectP1 = vectP1.rotate(90)
    vectP1.scale_to_length(10)
    p1 = core.memory("position") + vectP1

    vectP1 = core.memory("vitesse")
    vectP1 = vectP1.rotate(90)
    vectP1.scale_to_length(10)
    p1 = core.memory("position") + vectP1

    vectP3 = core.memory("vitesse")
    vectP3 = vectP3.rotate(-90)
    vectP3.scale_to_length(10)
    p3 = core.memory("position") + vectP1

if core.getKeyPressList("SPACE"):
    if len(core.memory("projectiles")) > 0:
        if time.time() - core.memory("projectiles")[-1]["startTime"] > 0.01:
            creationProjectile()

        else :
            creationProjectile()

core.memory("position"), core.memory("position") + core.memory("vitesse"))
for p in core.memory("projectiles"):
    p["position"] = p["position"] + p["vitesse"]

    