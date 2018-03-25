import tkinter as tk
from model.event import *
from model.village import *

class TroubleVillage(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.container = tk.Frame(self)

        self.title('Trouble Village')
        self.geometry('800x480')
        self.resizable(width=False, height=False)

        self.container.pack(side="top", fill=None, expand=True)
        self._frame = StartPage(master=self.container, controller=self)

    def switch_frame(self, frame_class):
        new_frame = frame_class(master=self.container, controller=self)
        self._frame.destroy()
        self._frame = new_frame

    def startGame(self, players):
        #starting game here
        self.dorp = Village("Dorp 1", 100, 100, 50, players)
        self.switch_frame(VillagePage)


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

        villageImg = tk.PhotoImage(file=r"img/giphy.gif")
        lblVillageImg = tk.Label(self, image=villageImg)

        villageImgBrand = tk.PhotoImage(file=r"img/village.gif")
        lblVillageImgBrand = tk.Label(self, image=villageImgBrand)
        lblVillageImg.image = villageImg

        lblName = tk.Label(self, text="Naam : " + str(self.controller.dorp.getName()))
        lblName.pack(side="top", fill="x", pady=1)

        lblPopulation = tk.Label(self, text="Bevolking : " + str(self.controller.dorp.getPopulation()))
        lblPopulation.pack(side="top", fill="x", pady=1)

        lblWood = tk.Label(self, text="Hout : " + str(self.controller.dorp.getWood()))
        lblWood.pack(side="top", fill="x", pady=1)

        lblVillageImg.pack(side="top", fill="x", pady=10)

        self.pack()

class ClassSelectionPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        label1 = tk.Label(self, text="How many players ?")
        label1.pack()

        self.playerAmount = tk.Entry(self)
        self.playerAmount.insert(0 , "4")
        self.playerAmount.pack()

        start_button = tk.Button(self, text="Go!", command=self.setPlayers)
        start_button.pack()

        self.pack()

    def setPlayers(self):
        self.controller.startGame(self.playerAmount.get())


class PageTwo(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        page_2_label = tk.Label(self, text="This is page two")
        start_button = tk.Button(self, text="Return to start page",
                                 command=lambda: controller.switch_frame(StartPage))
        page_2_label.pack(side="top", fill="x", pady=10)
        start_button.pack()
        self.pack()

class PageStatus(tk.Frame):
            def __init__(self, master, controller):
                tk.Frame.__init__(self, master)
                self.controller = controller

                page_2_label = tk.Label(self, text="This is page status")
                status_label = tk.Label(self, text="Het dorp is " + VillageEvent.state)

                start_button = tk.Button(self, text="Return to start page",
                                         command=lambda: controller.switch_frame(StartPage))
                page_2_label.pack(side="top", fill="x", pady=10)
                status_label.pack(side="top", fill="x", pady=10)
                start_button.pack()
                self.pack()
