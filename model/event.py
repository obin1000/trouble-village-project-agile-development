import tkinter as tk

# Abstracte weergaven van een dorp
class VillageEvent:
    # Constructor voor Village

    def __init__(self):
        print("test")


class Burn(VillageEvent):
    def __init__(self, dorp, main):
        #requirement of resource to fix
        self.requirement = 200
        self.dorp = dorp
        self.main = main
        
        self.dorp.setState(1)

        print("Your village is on fire! You'll need : "+ str(self.requirement) +"L water to put it out.")
        nextTurn = tk.Button(main, text="Put out fire!", command=self.fix)
        nextTurn.pack(side="bottom" , pady="1")

    def fix(self):
        if(self.dorp.getWater() >= 200):
            self.dorp.setWater(self.dorp.getWater() - self.requirement)
            self.main.update()
        else:
            print("Not enough water! , you'll need to gather some first!")

class Flood():
    def __init__():
        print("test")
