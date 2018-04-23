import tkinter as tk
from model.event import *
from model.village import *
import random

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

    def switch_frame(self, frame_class):
        new_frame = frame_class(master=self.container, controller=self)
        self._frame.destroy()
        self._frame = new_frame

    def startGame(self, players):
        #starting game here.

        self.dorp = Village("Dorp 1", 100, 100, 50, players)
        self.switch_frame(VillagePage)

        includeIO = False

        if includeIO:
            from driver.nfcreader import NFC
            nfcThread = NFC("nfcThread", Village)
            nfcThread.start()

    def update(self):
        #call this function to refresh the resources.
        self.switch_frame(VillagePage)

    def nextTurn(self):
        # turn logic here.

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

        column_labels = 5;
        lblTurn.config(font=("Arial", 30))
        lblTurn.grid(row=1,column=column_labels)

        lblName = tk.Label(self, text="Naam : " + str(self.controller.dorp.getName()))
        lblName.grid(row=2, column=column_labels)

        lblPopulation = tk.Label(self, text="Bevolking : " + str(self.controller.dorp.getPopulation()))
        lblPopulation.grid(row=3,column=column_labels)
        
        lblWood = tk.Label(self, text="Hout : " + str(self.controller.dorp.getWood()))
        lblWood.grid(row=4,column=column_labels)

        lblWater = tk.Label(self, text="Water : " + str(self.controller.dorp.getWater()))
        lblWater.grid(row=5,column=column_labels)

        villageImg = tk.PhotoImage(file=r"img/giphy.gif", format="gif")
        lblVillageImg = tk.Label(self, image=villageImg)
        lblVillageImg.image = villageImg
        lblVillageImg.grid(row=2,column=5)
        
        nextTurn = tk.Button(self, text="Next turn (debug)", command=self.controller.nextTurn)

        nextTurn.grid(row=6,column=1)

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
