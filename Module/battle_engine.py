# ----------battle_engine.py----------

import random

def attack():
    return random.randint(10,25)

def enemy_attack():
    return random.randint(10,25)

def critical_hit():
    return random.random() < 0.20

def heal():
    return random.randint(15,30)