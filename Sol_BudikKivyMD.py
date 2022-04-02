from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from Sol_budik import CalcSol,UTCcalc
from kivy.core.window import Window
Window.minimum_height = 500
Window.minimum_width = 500


class Solarny_Budik(MDApp,CalcSol):


    def flip(self):
        self.result_calc.text = ""
        self.label.text = ""
        self.input.text= ""
        self.vys1.text = ""
        self.vys2.text = ""
        self.vys3.text = ""
        self.vys4.text = ""
        self.vys5.text = ""
        self.vys6.text = ""
        self.vys7.text = ""

    def convert_R(self,args=0):
        try:
            val = str(self.input.text)
            if len(val)>3:
                resres = CalcSol.calculations(self, val)
                if resres == None:
                    self.label.text = "Nezadal si správnu adresu"
                    #self.label.text = location
                    return self.convert_R
                else:
                    print("ahoj")
            else:
                self.result_calc.text = ""
                self.label.text = "Nesprávna hodnota"
                self.input.text = ""
                return self.convert_R
        except ValueError:
            self.result_calc.text = ""
            self.label.text = "Nesprávna hodnota"
            self.input.text = ""
            return self.convert_R





        self.result_calc.text = resres[20]
        self.label.text = "Dnešný dátum je "

        #podrobne vysl hodnoty
        self.vys1.text = resres[0]
        self.vys2.text = resres[17]
        self.vys3.text = resres[18]
        self.vys4.text = resres[16]
        self.vys5.text = resres[1][0:2] + "°"
        self.vys6.text = resres[2][0:2] + "°"
        self.vys7.text = str(self.tzzzz) + ""

    def build(self):
        screen = MDScreen()

        #top toolbar
        self.theme_cls.theme_style = "Dark"  # "Light"
        self.toolbar = MDToolbar(title="Solárny budík")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [
            ["rotate-3d-variant", lambda x:self.flip()]]


        screen.add_widget(self.toolbar)

        #logo
        screen.add_widget(Image(source="sun-rise-1148031.jpg",allow_stretch= True, keep_ratio = False,
                                #height = 220, width = 220,
                               # pos=(100, 500),
                               # allow_stretch: True,
                                #size_hint_y: 0, # Tells the layout to ignore the size_hint in y dir

                               # size_hint=(1, 0.4),
                                size_hint_min=(500,500),
                                size=(500,1010),
                                pos_hint= {"center_x":0.5, "center_y":0.4 }
        ))
        self.input = MDTextField(
            text="",
            hint_text =  "Zadaj svoju adresu ( mesto ) ",

            halign="center",

            size_hint= (0.8,1),
            pos_hint={"center_x": 0.5, "center_y": 0.80},
            font_size = 22
        )
        screen.add_widget(self.input)
        #label primanrny aj sekundarny
        self.label=MDLabel(

            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.75},
            theme_text_color = "Secondary",

        )
        self.result_calc=MDLabel(

            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.70},
            theme_text_color = "Primary",
            font_style = "H5"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.result_calc)
        #button convert
        screen.add_widget(MDFillRoundFlatButton(
            text="Vypočítaj",
            font_size = 17,
            pos_hint =  {"center_x": 0.5 , "center_y":0.65},
            on_press = self.convert_R
        ))
        # podrobnosti vysledky
        self.vys1 = MDLabel(

            halign="left",
            size_hint_min= (150,200),
            pos_hint={"center_x":  0.9, "center_y": 0.6},
            theme_text_color="Secondary",

        )
        screen.add_widget(self.vys1)
        self.vys2 = MDLabel(

            halign="center",
            pos_hint={"center_x": 0.45, "center_y": 0.55},
            theme_text_color="Secondary",

        )
        screen.add_widget(self.vys2)
        self.vys3 = MDLabel(

            halign="center",
            pos_hint={"center_x": 0.45, "center_y": 0.5},
            theme_text_color="Secondary",

        )
        screen.add_widget(self.vys3)
        self.vys4 = MDLabel(

            halign="center",
            pos_hint={"center_x": 0.45, "center_y": 0.45},
            theme_text_color="Secondary",

        )
        screen.add_widget(self.vys4)
        self.vys5 = MDLabel(

            halign="center",
            pos_hint={"center_x": 0.45, "center_y": 0.4},
            theme_text_color="Secondary",

        )
        screen.add_widget(self.vys5)
        self.vys6 = MDLabel(

            halign="center",
            pos_hint={"center_x": 0.45, "center_y": 0.35},
            theme_text_color="Secondary",

        )
        screen.add_widget(self.vys6)

        self.vys7 = MDLabel(

            halign="center",
            pos_hint={"center_x": 0.45, "center_y": 0.3},
            theme_text_color="Secondary",

        )
        screen.add_widget(self.vys7)

        self.inf1 = MDLabel(
            text="Tvoja zadaná poloha",
            halign="left",
            pos_hint={"center_x": 0.6, "center_y": 0.60},
            theme_text_color="Secondary",

        )
        screen.add_widget(self.inf1)
        self.inf2 = MDLabel(
            text="Čas východu slnka",
            halign="left",
            pos_hint={"center_x": 0.6, "center_y": 0.55},
            theme_text_color="Secondary",

        )
        screen.add_widget(self.inf2)
        self.inf3 = MDLabel(
            text="Čas západu slnka",

            halign="left",
            pos_hint={"center_x": 0.6, "center_y": 0.5},
            theme_text_color="Secondary",

        )
        screen.add_widget(self.inf3)
        self.inf4 = MDLabel(
            text="Poludnie",

            halign="left",
            pos_hint={"center_x": 0.6, "center_y": 0.45},
            theme_text_color="Secondary",

        )
        screen.add_widget(self.inf4)
        self.inf5 = MDLabel(
            text="Zemepisná šírka",

            halign="left",
            pos_hint={"center_x": 0.6, "center_y": 0.4},
            theme_text_color="Secondary",

        )
        screen.add_widget(self.inf5)
        self.inf6 = MDLabel(
            text="Zemepisná výška",

            halign="left",
            pos_hint={"center_x": 0.6, "center_y": 0.35},
            theme_text_color="Secondary",

        )
        screen.add_widget(self.inf6)
        self.inf7 = MDLabel(
            text="Časové pásmo",

            halign="left",
            pos_hint={"center_x": 0.6, "center_y": 0.3},
            theme_text_color="Secondary",

        )
        screen.add_widget(self.inf7)














        return screen



if __name__ == "__main__":
    Solarny_Budik().run()