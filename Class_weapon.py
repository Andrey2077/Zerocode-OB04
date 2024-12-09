from abc import ABC, abstractmethod


class Weapon(ABC):

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @abstractmethod
    def attack(self):
        pass


