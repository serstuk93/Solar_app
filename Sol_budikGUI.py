from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Solarny_Budik(App):
    def build(self):
        self.window = GridLayout()

        #add widgets to window
        self.window.cols=1
        self.window.size_hint = (0.8,0.9)
        self.window.pos_hint = {"center_x": 0.5 , "center_y": 0.5}
        # obrazok pozadia
        self.greeting = Label(
                        text="Solárny budík",
                        font_size = 18,
                        color= "aed6f1"
                        )
        self.window.add_widget(self.greeting)
        self.window.add_widget(Image(source="sun-rise-1148031.jpg",size_hint = (1, 1)))

        self.textinfo = Label(text="Zadajte svoju adresu (mesto)")

        self.window.add_widget(self.textinfo)
        # pouzivatelsky input
        self.user = TextInput(
                    multiline=False,
                    padding_y = (10,2),
                    size_hint = (1, 0.30)
                    )
        self.window.add_widget(self.user)
        self.button = Button(text="Vypocitaj",
                             color= "aed6f1",
                             size_hint = (1, 0.30),
                             bold= True,
                             background_color = "063d3f",
                             background_normal= ""
                             )
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)



        return self.window

    def callback(self, instance):
        self.greeting.text = "Vypočítavam dáta pre mesto " + self.user.text + "..."







if __name__ == "__main__":
    Solarny_Budik().run()