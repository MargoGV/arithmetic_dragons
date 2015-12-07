# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass

def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy

def generate_random_enemy_dragon():
    RandomEnemyType = choice(dragon_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy_dragon() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
     def set_answer(self, answer):
         answer=int(answer)
         self.__answer = answer
 
     def check_answer(self, answer):
        answer=int(answer)
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest

class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = randint(10,20)
        self._color = 'красный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest
        
class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = randint(15,35)
        self._color = 'черный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + 'x' + str(y)
        self.set_answer(x * y)
        return self.__quest

#FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.


enemy_types = [GreenDragon, RedDragon, BlackDragon]
