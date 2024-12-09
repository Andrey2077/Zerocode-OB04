from Interface_fight import Fightable


class Fighter(Fightable):
    def __init__(self, name):
        self.__name = name
        self.__weapon = None
        self.__health = 100
        self.__status = True

    def get_name(self):
        return self.__name

    def get_weapon(self):
        return self.__weapon

    def change_weapon(self, weapon):
        self.__weapon = weapon
        print(f"Боец выбрал оружие: {self.__weapon.get_name()}")

    def get_health(self):
        return self.__health

    def get_status(self):
        return self.__status

    def set_status(self, value):
        self.__status = value

    def set_damage(self, damage):
        self.__health = self.get_health() - damage

        if self.__health <= 0:
            print(f"Боец  {self.get_name()} убит")
            self.set_status(False)
        else:
            print(f"Бойцу {self.get_name()} нанесен урон: {damage}")

