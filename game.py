__author__ = 'Justin M'
from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll



class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Troll(),
            Dragon()
        ]

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None
