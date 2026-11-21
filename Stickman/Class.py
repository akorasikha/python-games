class player:
    def __init__(self, Number, Jersey):
        self.player_Number = Number
        self.player_Jersey = Jersey

    def running (self):
        print("Running")
    
    def jumping (self):
        print("Jumping")

    def walking (self):
        print("Walking")

    def sprinting (self):
        print("Sprinting")

class Soccer_Player(player):
    def dribbling(self):
        print("Dribbling")
    
    def shooting(self):
        print("Shooting")

    def passing(self):
        print("Passing")

    def scoring(self):
        print("Scored")

    def Make_A_Goal(self):
        self.sprinting()
        self.running()
        self.passing()
        self.dribbling()
        self.shooting()
        self.scoring()

##Mahomes = player(15,"Red")
##Jordan = player(23, "Black and Red")
Messi = Soccer_Player(10, "Blue and White")
print(Messi.player_Number)
Messi.Make_A_Goal()








