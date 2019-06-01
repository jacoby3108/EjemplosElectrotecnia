import tkinter as tk
import Config
from UserInput import userInput
from Menus.MenuModo import MenuModo


class MenuPasaBajos(tk.Frame): # heredamos de tk.Frame, padre de MenuPasaBajos
    def __init__(self, parent, controller):
        # parent representa el Frame principal del programa, tenemos que indicarle
        # cuando MenuInputOutput será dibujado

        # controller lo utilizamos cuando necesitamos que el controlador principal del programa haga algo

        # llamamos al constructor
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self,
            height=1,
            width=50,
            text="Configuración parámetros pasa bajo",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )

        self.title.pack(side=tk.TOP, fill=tk.BOTH)

        self.titleFo = tk.Label(
            self,
            height=1,
            width=50,
            text="Frecuencia de corte (kHz)",
            font=Config.SMALL_FONT,
            background="#ccffd5"
        )

        self.titleFo.pack(side=tk.TOP, fill=tk.BOTH, pady=30)

        self.w2 = tk.Scale(self, from_=0, to=100, resolution = 0.1, orient=tk.HORIZONTAL)
        self.w2.pack(side=tk.TOP, fill=tk.BOTH)

        self.buttonContinuar = tk.Button(
            self,
            height=2,
            width=50,
            text="Continuar",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.continuar
        )

        self.buttonContinuar.pack(side=tk.TOP, fill=tk.BOTH, pady=20)

    def continuar(self):
        # configuramos modos
        userInput["f0"] = self.w2.get() * 1000
        self.controller.showFrame(MenuModo)

    def focus(self):
        pass
