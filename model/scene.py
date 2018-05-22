includeIO = False

import tkinter as tk
import os
from model.event import *
from model.village import *
import random
import time
if includeIO:
    from driver.nfcreader import NFC
    from driver.hokjesreader import Resources


class TroubleVillage(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.container = tk.Frame(self)

        self.title('Trouble Village')
        self.geometry('800x480')
        self.attributes('-fullscreen', True)
        self.bind('<Escape>', lambda e: self.destroy())
        #if includeIO:
        #   self.overrideredirect(True)

        self.resizable(width=False, height=True)
        self.container.pack(side="top", expand="1", fill="x")
        self._frame = StartPage(master=self.container, controller=self)

    def switch_frame(self, frame_class):
        new_frame = frame_class(master=self.container, controller=self)
        self._frame.destroy()
        self._frame = new_frame

    def startGame(self, players):
        # starting game here.

        self.dorp = Village("Trouble Village", 10, 100, 50, players)
        self.switch_frame(VillagePage)

        if includeIO:
            os.system('omxplayer img/Soundtrack.mp3 &')
            nfcThread = NFC("nfcThread", self.dorp, self)
            nfcThread.start()
            self.spullen = Resources()

    def endGame(self, result):
        # call this function to refresh the resources.
        if result:
            self.switch_frame(GameWonPage)
        else:
            self.switch_frame(GameOverPage)

    def scoreBoard(self):
        self.switch_frame(ScoreBoardPage)

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


        if ((self.dorp.getPopulation()) <= 0):
            self.endGame(0)
        elif self.dorp.ship1 and self.dorp.ship2 and self.dorp.ship3 and self.dorp.ship4:
            self.endGame(1)
        else:
            self.update()

class StartPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        title_font = "Times 60"
        txtcolor = "White"

        canvas = tk.Canvas(self, width=800, height=480, bg="white")

        #Background --> aanpassen later!
        bgimgStart = tk.PhotoImage(file='img/island.gif')
        canvas.bgimg = bgimgStart
        canvas.create_image(0, 0, image=canvas.bgimg, anchor="nw")

        #Title Trouble village
        title = canvas.create_text(400, 100, fill=txtcolor, font=title_font, text="Trouble village")

        start_label = tk.Label(self, text="Trouble Village")

        #Rectangle button start game
        #canvas.create_rectangle(0,245,800,280, fill="white")
        #Button start game
        page_1_button = tk.Button(self, text="Start Adventure!",
                                  command=lambda: controller.switch_frame(ClassSelectionPage), anchor="w", bg="white", width=14)
        canvas.create_window(345, 250, anchor="nw", window=page_1_button)
        #page_1_button.pack()

        #Rectangle button tutorial
        #canvas.create_rectangle(0,300,800,335, fill="white")
        #Button tutorial
        page_2_button = tk.Button(self, text="Tutorial",
                                  command=lambda: controller.switch_frame(VillageTutorial), anchor="w", bg="white")
        canvas.create_window(375, 305, anchor="nw", window=page_2_button)
        #page_2_button.pack()

        #Rectangle button tutorial
        #canvas.create_rectangle(0,355,800,390, fill="white")
        page_3_button = tk.Button(self, text="Start first game",
                                  command=lambda: controller.switch_frame(Story), anchor="w", bg="white")
        canvas.create_window(355, 360, anchor="nw", window=page_3_button)

        canvas.pack()

        self.pack()

class Story(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        small_font = "Times 12"
        title_font = "Times 32"
        color = "black"

        canvas = tk.Canvas(self, width=800, height=480)
        canvas.pack()

        #Achtergrond
        bgimg = tk.PhotoImage(file='img/island.gif')
        canvas.bgimg = bgimg
        canvas.create_image(0, 0, image=canvas.bgimg, anchor="nw")

        #Rectangle
        canvas.create_rectangle(20,460,780,300, fill="white")

        text = canvas.create_text(290, 320,fill=color,font=small_font, text="   Once upon a time there was a small village far away "
                                                                            "from where we are now.")
        text2 = canvas.create_text(300, 340,fill=color,font=small_font, text="People lived together in peace and harmony. "
                                                                             "They enjoyed living in the village.")
        text3 = canvas.create_text(390, 360,fill=color,font=small_font, text="Even though they had a peacefull living, the village carries a curse. "
                                                                             "A curse that takes place every 100 years.")

        #BackButton
        Next_button = tk.Button(self, text="Next", command=lambda: controller.switch_frame(Story1), anchor='w',
                                width=8)
        Next_button_window = canvas.create_window(650, 420, anchor='nw', window=Next_button)


        self.pack()

class Story1(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        small_font = "Times 12"
        title_font = "Times 32"
        color = "black"

        canvas = tk.Canvas(self, width=800, height=480)
        canvas.pack()

        #Achtergrond
        bgimg = tk.PhotoImage(file='img/vulcano.gif')
        canvas.bgimg = bgimg
        canvas.create_image(0, 0, image=canvas.bgimg, anchor="nw")

        #Rectangle
        canvas.create_rectangle(20,460,780,300, fill="white")

        text1 = canvas.create_text(320, 320,fill=color,font=small_font, text="Every 100 years the 'sleeping mountain' called 'Vurcanu' "
                                                                             "awakes from his beauty sleep.")
        text2 = canvas.create_text(260, 340, fill=color, font=small_font, text="He bursts burning rocks and fire and "
                                                                               "destroys everything he touches.")
        text3 = canvas.create_text(370, 360,fill=color,font=small_font, text="Even though the villagers are strong and smart people,"
                                                                             " they will never be able to defend their small village")
        text4 = canvas.create_text(150, 380,fill=color,font=small_font, text="from the destruction of Vurcanu.")
        text5 = canvas.create_text(200, 400,fill=color,font=small_font, text="The only way to escape the curse of Vurcanu is...")

        #NextButton
        Next_button = tk.Button(self, text="Next", command=lambda: controller.switch_frame(Story2), anchor='w',
                                width=8)
        Next_button_window = canvas.create_window(650, 420, anchor='nw', window=Next_button)


        self.pack()

class Story2(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        small_font = "Times 12"
        title_font = "Times 32"
        color = "black"

        canvas = tk.Canvas(self, width=800, height=480)
        canvas.pack()

        #Achtergrond
        bgimg = tk.PhotoImage(file='img/boat.gif')
        canvas.bgimg = bgimg
        canvas.create_image(0, 0, image=canvas.bgimg, anchor="nw")

        #Rectangle
        canvas.create_rectangle(20,460,780,300, fill="white")

        text1 = canvas.create_text(350, 320,fill=color,font=small_font, text="By making a boat! A boat big enough to carry the whole village"
                                                                             " and leave the village until Vurcano")
        text2 = canvas.create_text(125, 340,fill=color,font=small_font, text="           goes back to his beauty sleep.")
        text3 = canvas.create_text(245, 360,fill=color,font=small_font, text="        Help us survive against the odds of nature and help us build a boat.")
        text4 = canvas.create_text(315, 380,fill=color,font=small_font, text="  Will you guys be the one to save as many villagers "
                                                                             "as possible from this 'trouble village'?")
        text5 = canvas.create_text(155, 400,fill=color,font=small_font, text="       Or will the curse of Vurcano get you?")

        #BackButton
        Next_button = tk.Button(self, text="Start Adventure!", command=lambda: controller.switch_frame(ClassSelectionPage), anchor='w',
                                width=12)
        Next_button_window = canvas.create_window(650, 420, anchor='nw', window=Next_button)


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
        canvas.create_rectangle(0, 480, 50, 430, fill="white")
        canvas.create_rectangle(600, 480, 800, 240, fill="white")

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

        icon_geenkleurship1 = tk.PhotoImage(file='img/geenkleurship1.png')
        canvas.icon_geenkleurship1 = icon_geenkleurship1
        canvas.create_image(615, 400, image=canvas.icon_geenkleurship1, anchor="nw")

        icon_geenkleurship2 = tk.PhotoImage(file='img/geenkleurship2.png')
        canvas.icon_geenkleurship2 = icon_geenkleurship2
        canvas.create_image(705, 400, image=canvas.icon_geenkleurship2, anchor="nw")

        icon_geenkleurship3 = tk.PhotoImage(file='img/geenkleurship3.png')
        canvas.icon_geenkleurship3 = icon_geenkleurship3
        canvas.create_image(614, 248, image=canvas.icon_geenkleurship3, anchor="nw")

        icon_geenkleurship4 = tk.PhotoImage(file='img/geenkleurship4.png')
        canvas.icon_geenkleurship4 = icon_geenkleurship4
        canvas.create_image(704, 243, image=canvas.icon_geenkleurship4, anchor="nw")

        if (dorp.getState() != 0):
            icon_state = tk.PhotoImage(file=dorp.getStateImg())
            canvas.icon_state = icon_state
            canvas.create_image(7, 440, image=canvas.icon_state, anchor="nw")

        if (dorp.well):
            icon_well = tk.PhotoImage(file='img/well.png')
            canvas.icon_well = icon_well
            canvas.create_image(345, 211, image=canvas.icon_well, anchor="nw")

        if (dorp.stockpile):
            icon_stockpile = tk.PhotoImage(file='img/stockpile.png')
            canvas.icon_stockpile = icon_stockpile
            canvas.create_image(110, 164, image=canvas.icon_stockpile, anchor="nw")

        if (dorp.ship1):
            icon_ship1 = tk.PhotoImage(file='img/ship1.png')
            canvas.icon_ship1 = icon_ship1
            canvas.create_image(615, 400, image=canvas.icon_ship1, anchor="nw")

        if (dorp.ship2):
            icon_ship2 = tk.PhotoImage(file='img/ship2.png')
            canvas.icon_ship2 = icon_ship2
            canvas.create_image(705, 400, image=canvas.icon_ship2, anchor="nw")

        if (dorp.ship3):
            icon_ship3 = tk.PhotoImage(file='img/ship3.png')
            canvas.icon_ship3 = icon_ship3
            canvas.create_image(614, 248, image=canvas.icon_ship3, anchor="nw")

        if (dorp.ship4):
            icon_ship4 = tk.PhotoImage(file='img/ship4.png')
            canvas.icon_ship4 = icon_ship4
            canvas.create_image(704, 243, image=canvas.icon_ship4, anchor="nw")

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

class VillageTutorial(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        small_font = "Times 16"
        title_font = "Times 32"
        color = "black"

        canvas = tk.Canvas(self, width=800, height=480)
        canvas.pack()

        #Achtergrond
        bgimg = tk.PhotoImage(file='img/background.png')
        canvas.bgimg = bgimg
        canvas.create_image(0, 0, image=canvas.bgimg, anchor="nw")

        #Rectangle
        canvas.create_rectangle(130,40,670,440, fill="white")

        #Intro
        label = canvas.create_text(400, 150,fill=color,font=small_font, text="\n       Welcome to the Trouble Village tutorial!"
                                   "\n" + "             This tutorial will explain how to:" +
                                   "\n" + "                  Add resources using cards" + "\n" +
                                   "\n" + "\nUpgrade your village by building new constructions" +
                                   "\n" + "\n               And win by repearing the ship!")
        #label_label = canvas.create_text(200, 25, text="bob")
        #self.after(5000, label.destroy)


        #Button back
        Back_button = tk.Button(self, text="Back", command=lambda: controller.switch_frame(StartPage), anchor='w',
                                width=8)
        Back_button_window = canvas.create_window(10, 10, anchor='nw', window=Back_button)

        #Button resources
        Resources_button = tk.Button(self, text="Tutorial resources", command=lambda: controller.switch_frame(TutorialResources),
                                     anchor='w', width=14)
        Resources_button_window = canvas.create_window(340, 150, anchor='nw', window=Resources_button)

        #Button Building constructions
        Building_button = tk.Button(self, text="Tutorial build buildings", command=lambda: controller.switch_frame(TutorialBuilding),
                                     anchor='w', width=20)
        Building_button_window = canvas.create_window(320, 210, anchor='nw', window=Building_button)

        #Button building ship
        Ship_button = tk.Button(self, text="Tutorial build ship", command=lambda: controller.switch_frame(TutorialShip),
                                     anchor='w', width=20)
        Resources_button_window = canvas.create_window(320, 260, anchor='nw', window=Ship_button)

        #Titel
        canvas.create_text(400,20,fill=color,font=title_font,text="Tutorial")

        self.pack()


class TutorialResources(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        small_font = "Times 16"
        title_font = "Times 32"
        color = "black"

        canvas = tk.Canvas(self, width=800, height=480)
        canvas.pack()

        #BackButton
        Back_button = tk.Button(self, text="Back", command=lambda: controller.switch_frame(VillageTutorial), anchor='w',
                                width=8)
        Back_button_window = canvas.create_window(10, 10, anchor='nw', window=Back_button)

        #Achtergrond
        bgimg = tk.PhotoImage(file='img/background.png')
        canvas.bgimg = bgimg
        canvas.create_image(0, 0, image=canvas.bgimg, anchor="nw")

        #Rectangle
        canvas.create_rectangle(130,40,670,440, fill="white")

        label = canvas.create_text(400, 100,fill=color,font=small_font, text="\n" +"          By traveling the land you will collect resources" +"\n"+
                                   "                                     for your village." + "\n"+
                                   "        After every round the players will have to scan"+"\n"+
                                   "        an eventcard to see if the odds are in their favor.")

        icon_water = tk.PhotoImage(file='img/waterdrop.png')
        canvas.icon_water = icon_water
        canvas.create_image(450, 230, image=canvas.icon_water, anchor="nw")

        icon_logs = tk.PhotoImage(file='img/woodd.png')
        canvas.icon_logs = icon_logs
        canvas.create_image(150, 230, image=canvas.icon_logs, anchor="nw")

        #Titel
        canvas.create_text(400,20,fill=color,font=title_font,text="Tutorial resources")

        self.pack()


class TutorialBuilding(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        small_font = "Times 16"
        title_font = "Times 32"
        color = "black"

        canvas = tk.Canvas(self, width=800, height=480)
        canvas.pack()

        #BackButton
        Back_button = tk.Button(self, text="Back", command=lambda: controller.switch_frame(VillageTutorial), anchor='w',
                                width=8)
        Back_button_window = canvas.create_window(10, 10, anchor='nw', window=Back_button)

        #Achtergrond
        bgimg = tk.PhotoImage(file='img/background.png')
        canvas.bgimg = bgimg
        canvas.create_image(0, 0, image=canvas.bgimg, anchor="nw")

        #Rectangle
        canvas.create_rectangle(130,40,670,440, fill="white")

        label = canvas.create_text(400, 100,fill=color,font=small_font, text="\n                To make it easier to collect more resources" + "\n"
                                   + "    the players will be able to build buildings like stockpiles" + "\n" +
                                   "                          or even wells within their village." + "\n"
                                   "\n    The players can scan the building items to build their buildings" +
                                   "\n    Only if they have gathered the resources needed to build them.")

        icon_sp = tk.PhotoImage(file='img/stockpile.png')
        canvas.icon_test = icon_sp
        canvas.create_image(150, 230, image=canvas.icon_test, anchor="nw")

        icon_well = tk.PhotoImage(file='img/well.png')
        canvas.icon_well = icon_well
        canvas.create_image(450, 230, image=canvas.icon_well, anchor="nw")


        #Titel
        canvas.create_text(400,20,fill=color,font=title_font,text="Tutorial building constructions")

        self.pack()

class TutorialShip(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        small_font = "Times 16"
        title_font = "Times 32"
        color = "black"

        canvas = tk.Canvas(self, width=800, height=480)
        canvas.pack()

        #BackButton
        Back_button = tk.Button(self, text="Tutorial", command=lambda: controller.switch_frame(VillageTutorial), anchor='w',
                                width=14)
        Back_button_window = canvas.create_window(10, 10, anchor='nw', window=Back_button)

        #BackNextPage
        ship2_button = tk.Button(self, text="Next page", command=lambda: controller.switch_frame(TutorialShip2), anchor='w',
                                width=14)
        ship2_button_window = canvas.create_window(350, 400, anchor='nw', window=ship2_button)

        #Achtergrond
        bgimg = tk.PhotoImage(file='img/background.png')
        canvas.bgimg = bgimg
        canvas.create_image(0, 0, image=canvas.bgimg, anchor="nw")

        #Rectangle
        canvas.create_rectangle(130,40,670,440, fill="white")

        label = canvas.create_text(400, 150,fill=color,font=small_font, text="To win the game everyone has to work together as a team" +
                                                                        "\n"+   "\n                     to keep the villagers alive and" + "\n" +
                                                                        "\n                    build a ship for them to escape")

        icon_ship1 = tk.PhotoImage(file='img/geenkleurship1.png')
        canvas.icon_ship1 = icon_ship1
        canvas.create_image(470, 360, image=canvas.icon_ship1, anchor="nw")

        icon_ship2 = tk.PhotoImage(file='img/geenkleurship2.png')
        canvas.icon_ship2 = icon_ship2
        canvas.create_image(560, 360, image=canvas.icon_ship2, anchor="nw")

        icon_ship3 = tk.PhotoImage(file='img/geenkleurship3.png')
        canvas.icon_ship3 = icon_ship3
        canvas.create_image(469, 208, image=canvas.icon_ship3, anchor="nw")

        icon_ship4 = tk.PhotoImage(file='img/geenkleurship4.png')
        canvas.icon_ship4 = icon_ship4
        canvas.create_image(559, 203, image=canvas.icon_ship4, anchor="nw")

        #Titel
        canvas.create_text(400,20,fill=color,font=title_font,text="Tutorial building the ship")

        self.pack()


class TutorialShip2(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        small_font = "Times 16"
        title_font = "Times 32"
        color = "black"

        canvas = tk.Canvas(self, width=800, height=480)
        canvas.pack()

        #BackButton
        Back_button = tk.Button(self, text="Tutorial", command=lambda: controller.switch_frame(VillageTutorial), anchor='w',
                                width=14)
        Back_button_window = canvas.create_window(10, 10, anchor='nw', window=Back_button)

        #BackButton
        BackShip_button = tk.Button(self, text="Back", command=lambda: controller.switch_frame(TutorialShip), anchor='w',
                                width=14)
        Back_button_window = canvas.create_window(150, 400, anchor='nw', window=BackShip_button)

        #ButtonNextPage
        ship3_button = tk.Button(self, text="Next page", command=lambda: controller.switch_frame(TutorialShip3), anchor='w',
                                width=14)
        ship2_button_window = canvas.create_window(350, 400, anchor='nw', window=ship3_button)

        #Achtergrond
        bgimg = tk.PhotoImage(file='img/background.png')
        canvas.bgimg = bgimg
        canvas.create_image(0, 0, image=canvas.bgimg, anchor="nw")

        #Rectangle
        canvas.create_rectangle(130,40,670,440, fill="white")

        label = canvas.create_text(400, 150,fill=color,font=small_font, text="        To build the ship the players need to collect resources."+
                                   "\n" +"\n           As a team you will have to upgrade the ship." +
                                   "\n" +"\n        The ship will appear gray on your screen at first.")

        icon_ship1 = tk.PhotoImage(file='img/ship1.png')
        canvas.icon_ship1 = icon_ship1
        canvas.create_image(470, 360, image=canvas.icon_ship1, anchor="nw")

        icon_ship2 = tk.PhotoImage(file='img/geenkleurship2.png')
        canvas.icon_ship2 = icon_ship2
        canvas.create_image(560, 360, image=canvas.icon_ship2, anchor="nw")

        icon_ship3 = tk.PhotoImage(file='img/ship3.png')
        canvas.icon_ship3 = icon_ship3
        canvas.create_image(469, 208, image=canvas.icon_ship3, anchor="nw")

        icon_ship4 = tk.PhotoImage(file='img/geenkleurship4.png')
        canvas.icon_ship4 = icon_ship4
        canvas.create_image(559, 203, image=canvas.icon_ship4, anchor="nw")

        #Titel
        canvas.create_text(400,20,fill=color,font=title_font,text="Tutorial building the ship")

        self.pack()

class TutorialShip3(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        small_font = "Times 16"
        title_font = "Times 32"
        color = "black"

        canvas = tk.Canvas(self, width=800, height=480)
        canvas.pack()

        #BackButton
        Back_button = tk.Button(self, text="Tutorial", command=lambda: controller.switch_frame(VillageTutorial), anchor='w',
                                width=14)
        Back_button_window = canvas.create_window(10, 10, anchor='nw', window=Back_button)

        #BackShipButton
        Back_Ship_button = tk.Button(self, text="Back", command=lambda: controller.switch_frame(TutorialShip2), anchor='w',
                                width=14)
        Back_Ship_button_window = canvas.create_window(150, 400, anchor='nw', window=Back_Ship_button)

        #Achtergrond
        bgimg = tk.PhotoImage(file='img/background.png')
        canvas.bgimg = bgimg
        canvas.create_image(0, 0, image=canvas.bgimg, anchor="nw")

        #Rectangle
        canvas.create_rectangle(130,40,670,440, fill="white")

        label = canvas.create_text(400, 150,fill=color,font=small_font, text="                      The ship will be finished after"+
                                 "\n"+  "\n             all of the ship pieces are added to the ship."+
                                  "\n"+ "\n         After finishing the ship all of the left over villagers"
                                   +"\n"+"\n               will leave the village in safety.")

        icon_ship1 = tk.PhotoImage(file='img/ship1.png')
        canvas.icon_ship1 = icon_ship1
        canvas.create_image(470, 360, image=canvas.icon_ship1, anchor="nw")

        icon_ship2 = tk.PhotoImage(file='img/ship2.png')
        canvas.icon_ship2 = icon_ship2
        canvas.create_image(560, 360, image=canvas.icon_ship2, anchor="nw")

        icon_ship3 = tk.PhotoImage(file='img/ship3.png')
        canvas.icon_ship3 = icon_ship3
        canvas.create_image(469, 208, image=canvas.icon_ship3, anchor="nw")

        icon_ship4 = tk.PhotoImage(file='img/ship4.png')
        canvas.icon_ship4 = icon_ship4
        canvas.create_image(559, 203, image=canvas.icon_ship4, anchor="nw")

        #Titel
        canvas.create_text(400,20,fill=color,font=title_font,text="Tutorial building the ship")

        self.pack()

class GameOverPage(tk.Frame):
    def __init__(self, master, controller):
            tk.Frame.__init__(self, master)
            self.controller = controller

            dorp = self.controller.dorp
            small_font = "Times 20"
            title_font = "Times 40"
            bgcolor = "black"
            txtcolor = "red"

            canvas = tk.Canvas(self, width=800, height=480, bg=bgcolor)


            canvas.create_text(400, 200, fill=txtcolor, font=title_font, text="Game Over!")
          #  canvas.create_text(400, 240, fill=txtcolor, font=small_font, text="Score: " + str(dorp.getPopulation()))

            submit = tk.Button(self, text="Play Again?", command=lambda: controller.switch_frame(StartPage), anchor='w', width=10)
            canvas.create_window(365, 310, anchor='nw', window=submit)
            #TroubleVillage.scoreBoard(self)
            canvas.pack()
            self.pack()


class GameWonPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        dorp = self.controller.dorp
        small_font = "Times 20"
        title_font = "Times 40"
        bgcolor = "black"
        txtcolor = "red"

        canvas = tk.Canvas(self, width=800, height=480, bg=bgcolor)

        canvas.create_text(400, 200, fill=txtcolor, font=title_font, text="You Won!")
        canvas.create_text(400, 240, fill=txtcolor, font=small_font, text="Score: " + str(dorp.getPopulation()))

        submit = tk.Button(self, text="Scoreboard", command=lambda: controller.switch_frame(ScoreBoardPage), anchor='w', width=10)

        canvas.create_window(365, 310, anchor='nw', window=submit)
        canvas.pack()

        file = open('score.txt', 'a')

        file.write("Date: " + time.strftime("%c") + "\t Score:" + str(dorp.getPopulation()) + "\n")

        file.close()

        self.pack()


class ScoreBoardPage(tk.Frame):
    def __init__(self, master, controller):
            tk.Frame.__init__(self, master)
            self.controller = controller

            dorp = self.controller.dorp
            small_font = "Times 10"
            title_font = "Times 40"
            bgcolor = "black"
            txtcolor = "red"
            text = ""
            lineCounter = 0

            canvas = tk.Canvas(self, width=800, height=480, bg=bgcolor)

            file = open('score.txt', 'r')
            for line in file:
                text = text + line + "\n"
                lineCounter +=1

            canvas.create_text(400, 200, fill=txtcolor, font=small_font, text=text)
            submit = tk.Button(self, text="Play Again", command=lambda: controller.switch_frame(StartPage), anchor='w', width=10)
            canvas.create_window(365, 310, anchor='nw', window=submit)
            canvas.pack()

            if lineCounter>10:
                file = open('score.txt, w')

            self.pack()




