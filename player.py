import random 
import items, world
 
class Player():
    def __init__(self):
        self.inventory = [items.Food(15), items.Pistol(), items.Knife()] #Inventory on startup
        self.hp = 100 # Health Points
        self.location_x, self.location_y = world.starting_position  #(0, 0)
        self.victory = False #no victory on start up
        self.current_weapon=self.inventory[1]
    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    # is_alive method
    def is_alive(self):
        return self.hp > 0   #Greater than zero value then you are still alive

    # is_dead method
    def is_dead(self):
        return self.hp == 0   #Equal to zero then you are dead

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')
    
    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())
 
    def move_north(self):
        self.move(dx=0, dy=-1)
 
    def move_south(self):
        self.move(dx=0, dy=1)
 
    def move_east(self):
        self.move(dx=1, dy=0)
 
    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        current_weapon = self.current_weapon

        print("You use {} against {}!".format(current_weapon.name, enemy.name))
        enemy.hp -= current_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def do_action(self, action, **kwargs):
     action_method = getattr(self, action.method.__name__)
     if action_method:
        action_method(**kwargs)

    def select_weapon(self,tile):
        selected_weapon_index = input('Please select weapon index: ')
        self.current_weapon = self.inventory[int(selected_weapon_index)]

    def healthUp(self):
        self.hp=100
        print('Your health is regained')

