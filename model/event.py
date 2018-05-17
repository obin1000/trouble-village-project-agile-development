import tkinter as tk


# Abstracte weergaven van een dorp
class VillageEvent:
    # Constructor voor Village
    def __init__(self, requirement, dorp, main):
        self.requirement = 50
        self.dorp = dorp
        self.main = main

class Burn(VillageEvent):
    def __init__(self, dorp, main):
        # requirement of resource to fix
        requirement = 50

        VillageEvent.__init__(self, requirement, dorp, main)

        self.main = main
        
        self.dorp.setState(1)

        self.removeBurn = tk.Button(main, text="Your village is on Fire! Put it out!", command=self.fix)
        self.removeBurn.place(x=10,y=100)

    def fix(self):
        if(self.dorp.getWater() >= self.requirement):
            self.dorp.setWater(self.dorp.getWater() - self.requirement)
            self.dorp.setState(0);
            self.main.update()
            self.removeBurn.destroy()
            
        else:
            print("Not enough water! , you'll need to gather some first!")


class Flood(VillageEvent):
    def __init__(self, dorp, main):
        #requirement of resource to fix
        requirement = 200

        VillageEvent.__init__(self, requirement, dorp, main)

        self.dorp = dorp
        self.main = main
        
        self.dorp.setState(2)

        self.removeFlood = tk.Button(main, text="Your village is on Flooded! Repair it with wood!", command=self.fix)
        self.removeFlood.place(x=10,y=120)

    def fix(self):
        if(self.dorp.getWood() >= self.requirement):
            self.dorp.setWood(self.dorp.getWood() - self.requirement)
            self.main.update()
            self.removeFlood.destroy()
        else:
            print("Not enough wood! , you'll need to gather some first!")

