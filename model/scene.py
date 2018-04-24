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

        self.resizable(width=False, height=True)
        self.container.pack(side="top", expand="1", fill="x")
        self._frame = StartPage(master=self.container, controller=self)

    def switch_frame(self, frame_class):
        new_frame = frame_class(master=self.container, controller=self)
        self._frame.destroy()
        self._frame = new_frame

    def startGame(self, players):
        # starting game here.

        self.dorp = Village("Trouble Village", 100, 100, 50, players)
        self.switch_frame(VillagePage)

        if includeIO:
            nfcThread = NFC("nfcThread", self.dorp, self)
            nfcThread.start()
            self.spullen = Resources()

    def update(self):
        # call this function to refresh the resources.
        self.switch_frame(VillagePage)

    # for next turn use this one
    def nextTurn(self):
        # turn logic here.
        if includeIO:
            position = self.spullen.getOccupiedResources()
            if position[0]:
                self.dorp.addWood(100)
            if position[1]:
                self.dorp.addWood(200)
            if position[2]:
                self.dorp.addWood(300)
            if position[3]:
                self.dorp.addWater(100)
            if position[4]:
                self.dorp.addWater(200)
            if position[5]:
                self.dorp.addWater(300)

        # subtract a number between 0 and 5 from the population count per turn.
        self.dorp.lowerPopulation(random.randint(0,5))

        # if there's an event active we apply a double population penalty.
        if self.dorp.getState() != 0:
            self.dorp.lowerPopulation(random.randint(5,10))


        self.dorp.setPoints()
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
        tk.Frame.__init__(self, master, bg="black")
        self.controller = controller

        dorp = self.controller.dorp
        current_turn = dorp.getTurn()
        current_wood = dorp.getWood()
        current_water = dorp.getWater()
        current_pop = dorp.getPopulation()
        current_points = dorp.getPoints()

        resource_font = "Times 20 bold"
        resource_color = "black"

        canvas = tk.Canvas(self, width=800, height=480, bg="white")
        canvas.pack()

        bgimg = tk.PhotoImage(file='img/background.png')
        canvas.bgimg = bgimg
        canvas.create_image(0, 0, image=canvas.bgimg, anchor="nw")

        canvas.create_rectangle(0, 40, 800, 80, fill="white")

        icon_water = tk.PhotoImage(file='img/water.png')
        canvas.icon_water = icon_water
        canvas.create_image(290, 45, image=canvas.icon_water, anchor="nw")

        icon_wood = tk.PhotoImage(file='img/logs.png')
        canvas.icon_wood = icon_wood
        canvas.create_image(130, 45, image=canvas.icon_wood, anchor="nw")

        icon_pop = tk.PhotoImage(file='img/pop.png')
        canvas.icon_pop = icon_pop
        canvas.create_image(450, 45, image=canvas.icon_pop, anchor="nw")

        icon_points = tk.PhotoImage(file='img/points.png')
        canvas.icon_points = icon_points
        canvas.create_image(610, 45, image=canvas.icon_points, anchor="nw")

        if (dorp.well):
            icon_well = tk.PhotoImage(file='img/well.png')
            canvas.icon_well = icon_well
            canvas.create_image(500, 300, image=canvas.icon_well, anchor="nw")

        if (dorp.stockpile):
            icon_stockpile = tk.PhotoImage(file='img/stockpile.png')
            canvas.icon_stockpile = icon_stockpile
            canvas.create_image(375, 175, image=canvas.icon_stockpile, anchor="nw")

        canvas.create_text(400, 20, fill=resource_color, font=resource_font, text="Turn : " + str(current_turn))
        canvas.create_text(195, 60, fill=resource_color, font=resource_font, text="" + str(current_wood))
        canvas.create_text(345, 60, fill=resource_color, font=resource_font, text="" + str(current_water))
        canvas.create_text(515, 60, fill=resource_color, font=resource_font, text="" + str(current_pop))
        canvas.create_text(665, 60, fill=resource_color, font=resource_font, text="" + str(current_points))

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
