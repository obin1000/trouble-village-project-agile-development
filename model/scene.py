includeIO = False

import tkinter as tk
from model.event import *
from model.village import *
import random
if includeIO:
    from driver.nfcreader import NFC
    from driver.hokjesreader import Resources

class TroubleVillage(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.container = tk.Frame(self)

        self.title('Trouble Village')
        self.geometry('800x480')
        #self.attributes("-fullscreen", True)
        self.resizable(width=False, height=False)

        self.container.pack(side="top", fill=None, expand=True)
        self._frame = StartPage(master=self.container, controller=self)

        #self.spullen = Resources()

    def switch_frame(self, frame_class):
        new_frame = frame_class(master=self.container, controller=self)
        self._frame.destroy()
        self._frame = new_frame

    def startGame(self, players):
        #starting game here.

        self.dorp = Village("Dorp 1", 100, 100, 50, players)
        self.switch_frame(VillagePage)

        if includeIO:
            nfcThread = NFC("nfcThread", Village)
            nfcThread.start()

    def update(self):
        #call this function to refresh the resources.
        self.switch_frame(VillagePage)

    def nextTurn(self):
        # turn logic here.
        if includeIO:
            position = self.spullen.getOccupiedResources()
            if position[0]:
                self.dorp.setWood(self.dorp.getWood() + 100)
            if position[1]:
                self.dorp.setWood(self.dorp.getWood() + 200)
            if position[2]:
                self.dorp.setWood(self.dorp.getWood() + 300)
            if position[3]:
                self.dorp.setWater(self.dorp.getWater() + 100)
            if position[4]:
                self.dorp.setWater(self.dorp.getWater() + 200)
            if position[5]:
                self.dorp.setWater(self.dorp.getWater() + 300)

        # subtract a number between 0 and 5 from the population count per turn.
        self.dorp.setPopulation(self.dorp.getPopulation() - random.randint(0,5))

        #if there's an event active we apply a double population penalty.
        if(self.dorp.getState() != 0):
            self.dorp.setPopulation(self.dorp.getPopulation() - random.randint(5,10))

        #TEST: set the village on fire.
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

        img = "2"
        if img == "1":
            villageImg = tk.PhotoImage(file=r"img/Base.png", format="png")
        elif img == "2":
            villageImg = tk.PhotoImage(file=r"img/Fire.gif", format="gif")
        elif img == "3":
            villageImg = tk.PhotoImage(file=r"img/giphy.gif", format="gif")
        elif img == "4":
            villageImg = tk.PhotoImage(file=r"img/giphy.gif", format="gif")

        lblVillageImg = tk.Label(self, image=villageImg)
        lblVillageImg.image = villageImg
        lblVillageImg.pack(side="top", fill="x", pady=10)


        lblName = tk.Label(self, text="Naam : " + str(self.controller.dorp.getName()))
        lblName.pack(side="top", fill="x", pady=1)

        lblPopulation = tk.Label(self, text="Bevolking : " + str(self.controller.dorp.getPopulation()))
        lblPopulation.pack(side="top", fill="x", pady=1)

        lblWood = tk.Label(self, text="Hout : " + str(self.controller.dorp.getWood()))
        lblWood.pack(side="top", fill="x", pady=1)

        lblWater = tk.Label(self, text="Water : " + str(self.controller.dorp.getWater()))
        lblWater.pack(side="top", fill="x", pady=1)

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
        self.playerAmount.insert(0, "4") # default 4 players for now.
        print(self.playerAmount.get())

        self.playerAmount.pack()

        start_button = tk.Button(self, text="Go!", command=self.setPlayers)
        start_button.pack()

        self.pack()

    def setPlayers(self):
        if int(self.playerAmount.get()) > 4 or int(self.playerAmount.get()) < 1:
            print("Aantal spelers moet tussen de 1-4 zijn.")
        else:
            self.controller.startGame(self.playerAmount.get()) #get players and start game.

    #after playerAmount we should let the players choose their class here.
