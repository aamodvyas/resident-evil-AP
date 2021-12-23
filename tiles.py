import items, enemies, actions, world
 
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def intro_text(self):
        raise NotImplementedError()
 
    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves
 
    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.HealthUp())
        return moves


class StartingRoom1(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        You find yourself in your dorm room with a flickering light on the wall.
        
        There is a crazy T-Virus which has infected the entire world.Turning all humans into flesh-eating zombies.
        The entire city of Hof has turned into Zombies. You are the only survivor.
        You need to survive and fight off zombies as long as you can.
        
        There might be more humans alive but you have to survive long enough to see them.
        You can make out four paths, which would lead you into the abandoned city where the zombie's are lurking.
        You can save yourself by fighting them or fleeing to a Shelter Room.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
 
    def add_loot(self, player):
        player.inventory.append(self.item)
 
    def modify_player(self, player):
        self.add_loot(player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
 
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy),actions.Selectweapon('Select your weapon'),actions.HealthUp()]
        else:
            return self.adjacent_moves()

class EmptyCityPath(MapTile):
    def intro_text(self):
        return """
        Another Dark part of the City. You must forge onwards.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
 
class HofCity(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zombie())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A Zombie is approaching you!
            He looks like someone you already know in Hof but now is a blood thirsty enemy
            You cannot be emotional now and it's time to defend yourself!!!
            """
        else:
            return """
            The corpse of a dead zombie rots on the ground.
            """


class SaalePark(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zombie2())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Another Zombie is approaching you!
            It's your former roommate who has now been infected by the T-virus and is a zombie now.
            You think of all the great memories you shared but this is not the time to reminisce 
            Defend yourself!!
            """
        else:
            return """
            The corpse of a dead zombie rots on the ground.
            """
class Wunseidel(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.BossZombie())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Final Boss Zombie is approaching you!
            He is very huge and much much stronger
            You will need all of your strength and intelligence to defeat him
            
            He is the only one standing between you and the city borders.
            """
        else:
            return """
            Huge corpse of a dead boss zombie rots on the ground.
            """

class Munchberg(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.ZombieWolf())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Another Zombie Wolf is approaching you!
            There are alot of wolves that have been converted to Zombies.
            Watch out for them! They are quick and dangerous!!
            """
        else:
            return """
            The corpse of a dead zombie wolf rots on the ground.
            """

class ZombieRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zombie())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A zombie wolf jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead wolf is on the ground.
             """


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())
 
    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a dagger! You pick it up.
        """

class SafeHouse(MapTile):
    def intro_text(self):
        return """
        You have found the safe house and you can rest and you can pick up the health potion to regain your stamina.
        """

class FindSafeRoom(MapTile):
    def intro_text(self):
        return """
        You have found the safe room and other people you are safe for now......

        Victory is yours!
            """
    def modify_player(self, player):
        player.victory = True


#  LEVEL 2

class SafeRoom(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        You find yourself in a new city. The sign says Mannheim, it looks normal.... way tooo quiet
        you suspect something, some faraway noises of animals/zombies growling
        
        The lively city of Mannheim is now super quiet. Guess the virus has reached here as well.
        You thought you would were safe but NO... 
        Your quest continues......
  
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


class EmptyCityPath(MapTile):
    def intro_text(self):
        return """
        Another Dark part of the City. You must forge onwards.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class MannheimCity(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zombie())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A Demogorgan is approaching you!
            It looks like some blood thirsty creature
            It's time to defend yourself!!!
            """
        else:
            return """
            The corpse of a dead Demogorgan rots on the ground.
            """


class Wasserturm(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zombie2())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A big Zombie Tyrant is approaching you!
            It's a huge zombie creature with long hands. You don't want to die with it's hands 
            Defend yourself!!
            """
        else:
            return """
            The corpse of a dead Tyrant rots on the ground.
            """


class CarlZuckMayer(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.BossZombie())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Final Boss Nemesis is approaching you!
            He is extremely huge and so much stronger
            You will need all of your strength and intelligence to defeat him

            He is the only one standing between you and the city borders.
            """
        else:
            return """
            Huge corpse of a dead Nemesis zombie rots on the ground.
            """


class L2(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.ZombieWolf())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Another Zombie creature is approaching you!
            There are alot of wolves that have been converted to Zombies.
            Watch out for them! They are quick and dangerous!!
            """
        else:
            return """
            The corpse of a dead zombie creature rots on the ground.
            """


class ZombieRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zombie())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A zombie wolf jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead wolf is on the ground.
             """


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a dagger! You pick it up.
        """


class LeaveSafeRoom(MapTile):
    def intro_text(self):
        return """
        You have found the safe room and other people you are safe for now......

        Victory is yours!
        """


class FindSafeRoom(MapTile):
    def intro_text(self):
        return """
        You have found the safe room and other people you are safe for now......

        Victory is yours!
            """

    def modify_player(self, player):
        player.victory = True


class StartingRoom2(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
      You find yourself in a new city. The sign says Mannheim, it looks normal.... way tooo quiet
        you suspect something, some faraway noises of animals/zombies growling
        
        The lively city of Mannheim is now super quiet. Guess the virus has reached here as well.
        You thought you would were safe but NO... 
        Your quest continues......
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


# Level 3

class StartingRoom3(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        You find yourself in a new city. The sign says Hildesheim, it looks weird... like something very evil has
        happened here.... 
        It's not just zombies here....
        You see something flying over the buildings...
        it's not a bird, It's not a human....
        It's some kind of human/bird hybrid....
        
        Could it be a VAMPIRE ??? or a DRACULA??!!!!!


        You thought you were safe but NO!!
        Your quest continues......

        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


class EmptyPath(MapTile):
    def intro_text(self):
        return """
        Another Dark part of the City. You must move ahead.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class Hildesheim(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zombie())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A Dracula is approaching you!
            It looks like a blood thirsty creature, And it can fly
            It's time to defend yourself!!!
            """
        else:
            return """
            The corpse of a dead Dracula rots on the ground.
            """


class Paderborn(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zombie2())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A big Tyrant is approaching you!
            It's a huge Dracula+Zombie hybrid creature with sharp claws and teeth. 
            Defend yourself!!
            """
        else:
            return """
            The corpse of a dead Tyrant rots on the ground.
            """


class Stuttgart(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.BossZombie())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Final Boss an Alpha Werewolf is approaching you!
            He is extremely huge and so much stronger and he can jump and rip your head off with one Bite
            You will need all of your strength and intelligence to defeat him

            He is the only one standing between you and the city borders.
            """
        else:
            return """
            Huge corpse of a dead Alpha Werewolf rots on the ground.
            """


class Kiel(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.ZombieWolf())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A new Zombie+Werewolf hybrid creature is approaching you!
            There are alot of werewolves that have been converted to Zombies.
            Watch out for them! They are ferocious and dangerous!!
            """
        else:
            return """
            The corpse of a dead Zombie-Werewolf creature rots on the ground.
            """


class ZombieRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zombie())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A zombie wolf jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead wolf is on the ground.
             """


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a dagger! You pick it up.
        """


class LeaveSafeRoom(MapTile):
    def intro_text(self):
        return """
        You have found the safe room and other people you are safe for now......

        Victory is yours!
        """


class FindSafeRoom(MapTile):
    def intro_text(self):
        return """
        You have found the safe room and other people you are safe for now......

        Victory is yours!
            """

    def modify_player(self, player):
        player.victory = True



