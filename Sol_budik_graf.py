from kivy.lang import Builder
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivy import FigureCanvasKivy
##!! vyzaduje matplotlib verziu 3.1.3 !!!

#graf
x = [ 1, 2 ,3 ,4 ,5 ]
y = [ 10,5 ,2,10, 5]
plt.plot(x,y)
plt.ylabel("Y osa")
plt.xlabel("X osa")

class GrafBeta(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        lbl = Label(text="[b]Some FigureCanvasKivy attributes:[/b]\n" + "\n".join(dir(FigureCanvasKivy)[-20:]), markup=True)
        box = self.ids.box
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))

    def save_it(self):
        name = self.ids.namer.text
        if name:
            plt.savefig(name)

class Graf(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        Builder.load_file("grf.kv")
        return GrafBeta()
       # screen = MDScreen()

       # return screen


Graf().run()
