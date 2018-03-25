import tkinter as tk
from model.event import *
from model.village import *
import random

class TroubleVillage(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.container = tk.Frame(self)

        self.title('Trouble Village')
        self.geometry('800x550')
        self.resizable(width=False, height=False)

        self.container.pack(side="top", fill=None, expand=True)
        self._frame = StartPage(master=self.container, controller=self)

    def switch_frame(self, frame_class):
        new_frame = frame_class(master=self.container, controller=self)
        self._frame.destroy()
        self._frame = new_frame

    def startGame(self, players):
        #starting game here.

        self.dorp = Village("Dorp 1", 100, 100, 50, players)
        self.switch_frame(VillagePage)

    def update(self):
        #call this function to refresh the resources.
        self.switch_frame(VillagePage)

    def nextTurn(self):
        # turn logic here.

        # subtract a number between 0 and 5 from the population count per turn.
        self.dorp.setPopulation(self.dorp.getPopulation() - random.randint(0,5))

        #set the village on fire.
        if(self.dorp.getState() != 1):
            Burn(self.dorp, self)

        self.dorp.nextTurn()
        self.update()

class StartPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        
        start_label = tk.Label(self, text="Trouble Village")
        page_1_button = tk.Button(self, text="Start Game",
                                  command=lambda: controller.switch_frame(ClassSelectionPage))
        page_1_button.pack()
        self.pack()


class VillagePage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        lblTurn = tk.Label(self, text="Turn : " + str(self.controller.dorp.getTurn()))

        lblTurn.config(font=("Times", 44))
        lblTurn.pack(side="top")

        villageImg = tk.PhotoImage(file=r"img/giphy.gif", format="gif")
        lblVillageImg = tk.Label(self, image=villageImg)
        lblVillageImg.image = villageImg

        lblName = tk.Label(self, text="Naam : " + str(self.controller.dorp.getName()))
        lblName.pack(side="top", fill="x", pady=1)

        lblPopulation = tk.Label(self, text="Bevolking : " + str(self.controller.dorp.getPopulation()))
        lblPopulation.pack(side="top", fill="x", pady=1)

        lblWood = tk.Label(self, text="Hout : " + str(self.controller.dorp.getWood()))
        lblWood.pack(side="top", fill="x", pady=1)

        lblWater = tk.Label(self, text="Water : " + str(self.controller.dorp.getWater()))
        lblWater.pack(side="top", fill="x", pady=1)

        lblVillageImg.pack(side="top", fill="x", pady=10)

        nextTurn = tk.Button(self, text="Next turn (debug)", command=self.controller.nextTurn)

        nextTurn.pack(side="bottom")

        self.pack()

class ClassSelectionPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        label1 = tk.Label(self, text="How many players ?")
        label1.pack()

        self.playerAmount = tk.Entry(self)
        self.playerAmount.insert(0 , "4") # default 4 players for now.
        self.playerAmount.pack()

        start_button = tk.Button(self, text="Go!", command=self.setPlayers)
        start_button.pack()

        self.pack()

    def setPlayers(self):
        self.controller.startGame(self.playerAmount.get()) #get players and start game.

    #after playerAmount we should let the players choose their class here.
