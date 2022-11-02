# kivy needs xsel or xclip installed in linux via apt get install




from kivy import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'minimum_width', '500')
Config.set('graphics', 'minimum_height', '800')

import io
from kivy.core.image import Image as CoreImage
from PIL import Image, ImageOps


from datetime import datetime, timedelta
from operator import index
from kivy.clock import Clock

from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.pickers import MDDatePicker
from Sol_budik import CalcSol
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from location_drawer import MapLocator

Window.minimum_height = 800
Window.minimum_width =500

KV = """
MDFloatLayout:

    MDTopAppBar:
        title: "MDDatePicker"
        pos_hint: {"top": 1}
        elevation: 10

    MDRaisedButton:
        text: "Open date picker"
        pos_hint: {'center_x': .5, 'center_y': .5}
        size_hint_y : 0.5
        on_release: app.show_date_picker()
"""
# zatial nefungujuci slider
KV2 = """
Screen

    MDSlider:
        min: 0
        max: 24
        value: 12
"""


class Solar_Calc(MDApp, CalcSol):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.resres = None
        self.new_map = None
        self.t1 = "t1.jpg"
        self.imt1 = Image(source = 't1.jpg')

        

    def reset(self):
        self.result_calc.text = ""
        self.vys1.text = ""
        self.vys2.text = ""
        self.vys3.text = ""
        self.vys4.text = ""
        self.vys5.text = ""
        self.vys6.text = ""
        self.vys7.text = ""
        self.resres = None
        self.default_map()
        self.imt1.reload()

    def flip(self):
        self.reset()
        self.label.text = ""
        self.input.text = ""
        self.selecteddate = ""

    def convert_R(self, args=0):
        if self.selecteddate:
            self.seldat = self.selecteddate
        else:
            self.seldat = ""
            self.selecteddate = ""
        try:
            val = str(self.input.text).capitalize()
            self.input.text = self.input.text.capitalize()
            if len(val) > 3:
                # CalcSol.UTCcl(self, val, self.seldat)
                if CalcSol.UTCcl(self, val, self.seldat) != None:
                    self.reset()
                    self.label.text = "Location does not exist"
                    return self.convert_R
                self.resres = CalcSol.calculations(self, val)

                if self.resres == None:
                    self.reset()
                    self.label.text = "Wrong adress"
                    return self.convert_R
                else:
                    print("passed")
            else:
                self.reset()
                self.label.text = "Wrong value"
                return self.convert_R
        except ValueError:
            self.result_calc.text = ""
            self.label.text = "Wrong value"
            self.input.text = ""
            return self.convert_R

        self.drw = self.map_draw()
        self.imt1.reload()
        if self.drw != None:
            print("BBBB")
            
            self.screen.add_widget(
            Image(

                source="t1.jpg",
                nocache = True,
                allow_stretch=True,
                keep_ratio=True,
                # height = 220, width = 220,
                
                # allow_stretch: True,
                # size_hint_y: 0, # Tells the layout to ignore the size_hint in y dir
                size_hint=(0.8, 0.25),
                # size_hint_min=(200, 200),
                # size=(100, 100),
                #pos=(200, 200),
                pos_hint={"center_x":.5, "y": 0.01},
                ))
            
            self.drw= None 
        self.label.text = "Current time"
        self.result_calc.text = self.resres[20]

        # Clock.schedule_once(my_callback, 5)

        # podrobne vysl hodnoty
        self.vys1.text = self.resres[0]
        self.vys2.text = self.resres[17]
        self.vys3.text = self.resres[18]
        self.vys4.text = self.resres[16]
        self.vys5.text = self.resres[1][0:5] + "°"
        self.vys6.text = self.resres[2][0:5] + "°"
        self.vys7.text = self.caz

        

    def build(self):
        self.theme_cls.primary_palette = "Gray"  # "Purple", "Red"
        self.screen = MDScreen()
        # screen.size_hint_max_x =500
    
        Builder.load_string(KV2)
        # top toolbar
        self.selecteddate = ""
        self.theme_cls.theme_style = "Light"  # "Light"
        self.toolbar = MDTopAppBar(title="Solar Calculator")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [["rotate-3d-variant", lambda x: self.flip()]]
        self.screen.add_widget(self.toolbar)

        # logo
        self.screen.add_widget(
            Image(
                source="background.png",
                allow_stretch=True,
                keep_ratio=False,
                # height = 220, width = 220,
                # pos=(100, 500),
                # allow_stretch: True,
                # size_hint_y: 0, # Tells the layout to ignore the size_hint in y dir
                # size_hint=(1, 0.4),
                #size_hint_min=(500, 500),
                #size=(500, 1010),
                pos_hint={"center_x": 0.5, "center_y": 0.405},
            )
        )
        self.input = MDTextField(
            text="",
            hint_text="Location",
            halign="center",
            size_hint=(0.8, 0.4),
            pos_hint={"center_x": 0.5, "center_y": 0.85},
            font_size=22,
        )
        self.screen.add_widget(self.input)
        # label primanrny aj sekundarny
        self.label = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.8},
            theme_text_color="Secondary",
        )
        self.result_calc = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.75},
            theme_text_color="Primary",
            font_style="H5",
        )
        self.screen.add_widget(self.label)
        self.screen.add_widget(self.result_calc)
        # button convert
        self.screen.add_widget(
            MDFillRoundFlatButton(
                text="Calculate",
                halign="left",
                font_size=17,
                pos_hint={ "center_x": 0.2, "center_y": 0.7},
                on_press=self.convert_R,
                theme_text_color="Secondary",
        ))
        self.screen.add_widget(
            MDFillRoundFlatButton(
                text="Select date",
                font_size=17,
                pos_hint={"center_x": 0.79, "center_y": 0.7},
                on_press=self.calendars,
            )
        )
        # podrobnosti vysledky
        self.vys1 = MDLabel(
            halign="center",
            size_hint_min=(100, 200),
            size_hint_x = 0.5,
            pos_hint={"center_x": 0.75, "center_y": 0.6},
            theme_text_color="Secondary",
        )
        self.screen.add_widget(self.vys1)
        self.vys2 = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.75, "center_y": 0.55},
            theme_text_color="Secondary",
        )
        self.screen.add_widget(self.vys2)
        self.vys3 = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.75, "center_y": 0.5},
            theme_text_color="Secondary",
        )
        self.screen.add_widget(self.vys3)
        self.vys4 = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.75, "center_y": 0.45},
            theme_text_color="Secondary",
        )
        self.screen.add_widget(self.vys4)
        self.vys5 = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.75, "center_y": 0.4},
            theme_text_color="Secondary",
        )
        self.screen.add_widget(self.vys5)
        self.vys6 = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.75, "center_y": 0.35},
            theme_text_color="Secondary",
        )
        self.screen.add_widget(self.vys6)

        self.vys7 = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.75, "center_y": 0.3},
            theme_text_color="Secondary",
        )
        self.screen.add_widget(self.vys7)

        self.inf1 = MDLabel(
            text="Selected Location",
            halign="left",
            pos_hint={"center_x": 0.6, "center_y": 0.6},
            theme_text_color="Secondary",
        )
        self.screen.add_widget(self.inf1)
        self.inf2 = MDLabel(
            text="Sunrise time",
            halign="left",
            pos_hint={"center_x": 0.6, "center_y": 0.55},
            theme_text_color="Secondary",
        )
        self.screen.add_widget(self.inf2)
        self.inf3 = MDLabel(
            text="Sunset time",
            halign="left",
            pos_hint={"center_x": 0.6, "center_y": 0.5},
            theme_text_color="Secondary",
        )
        self.screen.add_widget(self.inf3)
        self.inf4 = MDLabel(
            text="Noon",
            halign="left",
            pos_hint={"center_x": 0.6, "center_y": 0.45},
            theme_text_color="Secondary",
        )
        self.screen.add_widget(self.inf4)
        self.inf5 = MDLabel(
            text="Geographical Latitude",
            halign="left",
            pos_hint={"center_x": 0.6, "center_y": 0.4},
            theme_text_color="Secondary",
        )
        self.screen.add_widget(self.inf5)
        self.inf6 = MDLabel(
            text="Terrestrial Longitude",
            halign="left",
            pos_hint={"center_x": 0.6, "center_y": 0.35},
            theme_text_color="Primary",
        )
        self.screen.add_widget(self.inf6)
        self.inf7 = MDLabel(
            text="Timezone",
            halign="left",
            pos_hint={"center_x": 0.6, "center_y": 0.3},
            theme_text_color="Secondary",
        )
        self.screen.add_widget(self.inf7)

        self.default_map()

            


        def my_callback(dt):
            if self.result_calc.text != "":
                datetime_object = datetime.strptime(
                    self.result_calc.text, "%d/%m/%Y %H:%M:%S"
                )
                d = timedelta(seconds=1)
                datetime_object = datetime_object + d
                datetime_object = datetime_object.strftime("%d/%m/%Y %H:%M:%S")
                self.result_calc.text = str(datetime_object)


        Clock.schedule_interval(my_callback, 1)

        return self.screen

    def default_map(self):
        self.screen.add_widget(
            Image(
                source="w1.jpg",
                allow_stretch=True,
                keep_ratio=True,
                # height = 220, width = 220,
                
                # allow_stretch: True,
                # size_hint_y: 0, # Tells the layout to ignore the size_hint in y dir
                size_hint=(0.8, 0.25),
                # size_hint_min=(200, 200),
                # size=(100, 100),
                #pos=(200, 200),
                pos_hint={"center_x":.5, "y": 0.01},
                ))


    def map_draw(self):
        print("AAAAAAAAA")
        
        if self.resres != None:
            print(f"resres {self.resres[1]}")
            self.map_generator = MapLocator(self.resres[1],self.resres[2])
            img_loc = self.map_generator.img_map_generator()


            

            """
            print("A",img_loc)
            view = Image.open(io.BytesIO(img_loc))
            print(view)
            # x = Image.open(img_loc)

            #view.show()
            #im = CoreImage(view, ext="png")
            # print("B",im)

            from kivy.uix.image import Image as VIM, CoreImage

            f=open("t1.jpg",'rb')

            binary_data= f.read() #image opened in binary mode

            data = io.BytesIO(binary_data)
            img=CoreImage(data, ext="png").texture

            new_img= VIM()
            new_img.texture= img
            print(new_img)
            self.screen.add_widget(new_img
                )

            """
            self.screen.add_widget(
                Image(
                    source='t1.jpg',
                    nocache = True,
                    allow_stretch=True,
                    keep_ratio=True,
                    size_hint=(0.8, 0.25),
                    pos_hint={"center_x":.5, "y": 0.01 },
                    ))
            
            return img_loc


    def on_save(self, instance, value, date_range):
        #  self.chosendate = value,
        # print(instance, value, date_range)
        # print(value)
        self.selecteddate = value
        # return self.build()

    def on_cancel(self, instance, value):
        """Events called when the "CANCEL" dialog box button is clicked."""

    def calendars(self, kv):

        return self.show_date_picker()

    def show_date_picker(self):
        Builder.load_string(KV)
        self.date_dialog = MDDatePicker()
        self.date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        self.date_dialog.open()
        # print("save",self.on_save)


if __name__ == "__main__":
    Solar_Calc().run()
