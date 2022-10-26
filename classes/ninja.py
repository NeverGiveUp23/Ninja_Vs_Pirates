class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 96
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        return self
    
    def throw_darts(self, pirate):
        pirate.health -= 15
        print("Can't touch this!")
        return self
    
    def eat(self):
        if self.health >= 100:
            if self.health > 100:
                self.health = 100
        else:
            self.health += 5
            if self.health > 100:
                self.health = 100
        return self