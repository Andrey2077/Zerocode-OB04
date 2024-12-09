#Задание: Применение Принципа Открытости/Закрытости (Open/Closed Principle) в Разработке Простой Игры
# Цель: Цель этого домашнего задание - закрепить понимание и навыки применения принципа открытости/закрытости (Open/Closed Principle),
# одного из пяти SOLID принципов объектно-ориентированного программирования.
# Принцип гласит, что программные сущности (классы, модули, функции и т.д.) должны быть открыты для расширения, но закрыты для модификации.
# Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
# Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия, не изменяя существующий код бойцов или механизм боя.
# Исходные данные:
# - Есть класс `Fighter`, представляющий бойца.
# - Есть класс `Monster`, представляющий монстра.
# - Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
# Шаг 1:Создайте абстрактный класс для оружия
# - Создайте абстрактный класс `Weapon`, который будет содержать абстрактный метод `attack()`.
# Шаг 2: Реализуйте конкретные типы оружия
# - Создайте несколько классов, унаследованных от `Weapon`, например, `Sword` и `Bow`. Каждый из этих классов реализует метод `attack()` своим уникальным способом.
# Шаг 3: Модифицируйте класс `Fighter`
# - Добавьте в класс `Fighter` поле, которое будет хранить объект класса `Weapon`.
# - Добавьте метод `change_weapon()`, который позволяет изменить оружие бойца.
# Шаг 4: Реализация боя
# - Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.
# Требования к заданию:
# - Код должен быть написан на Python.
# - Программа должна демонстрировать применение принципа открытости/закрытости: новые типы оружия можно легко добавлять, не изменяя существующие классы бойцов и механизм боя.
# - Программа должна выводить результат боя в консоль.
# Пример результата:
# Боец выбирает меч.
# Боец наносит удар мечом.
# Монстр побежден!
# Боец выбирает лук.
# Боец наносит удар из лука.
# Монстр побежден!

from  Class_fighter import Fighter
from  Class_bow import Bow
from  Сlass_sword import Sword
from  Class_monster import Monster


def check_for_continue(list_of_active_monsters, fighter) -> bool:
    if len(list_of_active_monsters) == 0:
        return False

    if fighter.get_status() == False:
        return False


fighter = Fighter("Обычный воин")
weapon_nice_sword = Sword("Крутой меч")
weapon_long_sword = Sword("Длинный меч")
weapon_long_bow = Bow("Длинный лук")
weapon_short_bow = Bow("Короткмй лук")
monster_bandit = Monster("Бандит")
monster_goblin = Monster("Злой гоблин")

list_of_active_monsters = []
list_of_active_monsters.append(monster_bandit)

fighter.change_weapon(weapon_nice_sword)
game_start = True
game_must_go = True
while game_start:

    if len(list_of_active_monsters) == 0:
        print("Все монстры убиты, вы победили")

    if fighter.get_status() == False:
        print(f"Ваш боец убит. Game over. Учитесь играть")

    if check_for_continue(list_of_active_monsters, fighter) == False:
        break

    while game_must_go:
        if check_for_continue(list_of_active_monsters, fighter) == False:
            break

        for monster in list_of_active_monsters:
            if check_for_continue(list_of_active_monsters, fighter) == False:
                break

            fight_begin = monster.find_target(fighter)
            while fight_begin:
                if check_for_continue(list_of_active_monsters, fighter) == False:
                    break

                fighter_damage = fighter.get_weapon().attack(fighter)
                monster.set_damage(fighter_damage)

                if monster_bandit.get_status() == False:
                    list_of_active_monsters.remove(monster)
                    break

                monster_damage = monster.attack()
                fighter.set_damage(monster_damage)




