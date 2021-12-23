# Base class for all items
class Item():
    # __init__ is the contructor method
    def __init__(self, name, description, value):
        self.name = name   # attribute of the Item class and any subclasses
        self.description = description # attribute of the Item class and any subclasses
        self.value = value # attribute of the Item class and any subclasses
    
    # __str__ method is used to print the object
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

# Extend the Items class
# Food class will be a child or subclass of the superclass Item
class Food(Item):
    # __init__ is the contructor method
    def __init__(self, amt): 
        self.amt = amt # attribute of the Gold class
        super().__init__(name="Food",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
 
class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=5)
 
class Shotgun(Weapon):
    def __init__(self):
        super().__init__(name="Shotgun",
                         description="A Shotgun with some rust.",
                         value=1,
                         damage=10)
class Knife(Weapon):
    def __init__(self):
        super().__init__(name="Knife",
                         description="A sharp Knife.",
                         value=1,
                         damage=5)

class MachineGun(Weapon):
    def __init__(self):
        super().__init__(name="Machine Gun",
                         description="A heavy Machine Gun.",
                         value=1,
                         damage=20)
class Pistol(Weapon):
    def __init__(self):
        super().__init__(name="Pistol",
                         description="An old pistol.",
                         value=1,
                         damage=10)