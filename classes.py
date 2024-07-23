import asyncio
import random
from abc import ABC, abstractmethod


class Frog(ABC):
    """Определяем базовый класс для сооздание жаб"""

    def __init__(self):
        """Даём основные характеристики"""
        self.attack = 15
        self.health = 150
        self.armor = 5

    @abstractmethod
    def class_bonus(self):
        """Даём бонусы в зависимости от класса"""
        pass

    def get_attack(self):
        """Рандоомный урон"""
        return random.uniform(self.attack / 2, self.attack)

    def get_armor(self):
        """Рандомная защита"""
        return random.uniform(0, self.armor)


class Assassin(Frog):
    def class_bonus(self):
        self.health *= 1.25


class Adventurer(Frog):
    def class_bonus(self):
        self.attack *= 1.5


class Artisan(Frog):
    def class_bonus(self):
        self.armor *= 2

