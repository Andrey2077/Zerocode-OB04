import random

from Interface_fight import Fightable


class Monster (Fightable):
    def __init__(self, name):
        self.__name = name
        self.__health = 100
        self.__target = None
        self.__status = True

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_status(self):
        return self.__status

    def set_status(self, value):
        self.__status = value

    def set_damage(self, damage):
        self.__health = self.get_health() - damage

        if self.__health <= 0:
            print(f"Монстр {self.get_name()} убит")
            self.set_status(False)
        else:
            print(f"Монстру {self.get_name()} нанесен урон: {damage}")


    def attack(self) -> int:
        damage = random.randint(0, 100)
        print(f"{self.get_name()} бьет, урон: {damage}")
        return damage

    def find_target(self, fighter) -> bool:
        chance_to_find_target = random.randint(0,10)

        if chance_to_find_target > 7:
            self.__target = fighter;
            print(f"Монстр {self.get_name()} нашел бойца: {fighter.get_name()}.")
            return True
        else:
            return False
