import tkinter as tk

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


class StartPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        start_label = tk.Label(self, text="This is the start page")
        page_1_button = tk.Button(self, text="Open page Village",
                                  command=lambda: controller.switch_frame(VillagePage))
        page_2_button = tk.Button(self, text="Open page two",
                                  command=lambda: controller.switch_frame(PageTwo))
        start_label.pack(side="top", fill="x", pady=10)
        page_1_button.pack()
        page_2_button.pack()
        self.pack()


class VillagePage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        villageImg = tk.PhotoImage(file=r"img/giphy.gif")

        lblVillageImg = tk.Label(self, image=villageImg)
        lblVillageImg.image = villageImg

        lblName = tk.Label(self, text="Naam")
        lblName.pack(side="top", fill="x", pady=1)
        lblPopulation = tk.Label(self, text="Bevoling")
        lblPopulation.pack(side="top", fill="x", pady=1)
        lblWood = tk.Label(self, text="Hout")
        lblWood.pack(side="top", fill="x", pady=1)

        start_button = tk.Button(self, text="Return to start page",
                                 command=lambda: controller.switch_frame(StartPage))
        lblVillageImg.pack(side="top", fill="x", pady=10)
        start_button.pack()
        self.pack()


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
