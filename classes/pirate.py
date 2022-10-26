class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 50
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        return self
    
    def eat(self):
        self.health += 5
        return self
    
    def ship(self, in_water):
        # self.in_water = False
        if in_water == True:
            self.speed += 25
        else:
            self.speed -= 10
        return self
    
    def died(self):
        if self.health <= 0:
            print("RUN AWAY!")
