import random

from Class_weapon import Weapon


class Sword(Weapon):

    def __init__(self, name):
        super().__init__(name)

    def attack(self, fighter) -> int:
        damage = random.randint(0, 100)
        print(f"{fighter.get_name()} наносит удар мечом, урон: {damage}")
        return damage