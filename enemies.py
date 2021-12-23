class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0

class Zombie(Enemy):
    def __init__(self):
        super().__init__(name="Zombie", hp=10, damage=5)
 
class BossZombie(Enemy):
    def __init__(self):
        super().__init__(name="Boss Zombie", hp=70, damage=20)

class Zombie2(Enemy):
    def __init__(self):
        super().__init__(name="Zombie2", hp=20, damage=10)

class ZombieWolf(Enemy):
    def __init__(self):
        super().__init__(name="Zombie Wolf", hp=15, damage=10)

class Demogorgan(Enemy):
    def __init__(self):
        super().__init__(name="Demogorgan", hp=15, damage=10)

class ZombieTyrant(Enemy):
    def __init__(self):
        super().__init__(name="Zombie Tyrant", hp=25, damage=15)

class Nemesis(Enemy):
    def __init__(self):
        super().__init__(name="Nemesis", hp=50, damage=15)

class Dracula(Enemy):
    def __init__(self):
        super().__init__(name="Dracula", hp=20, damage=5)

class Tyrant(Enemy):
    def __init__(self):
        super().__init__(name="Tyrant", hp=30, damage=15)

class AlphaWerewolf(Enemy):
    def __init__(self):
        super().__init__(name="Alpha Werewolf", hp=50, damage=15)


