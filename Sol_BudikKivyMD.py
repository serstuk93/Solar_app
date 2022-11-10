# kivy needs xsel or xclip installed in linux via apt get install


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
from location_drawer import MapLocator
from kivy.uix.screenmanager import (
    ScreenManager,
    Screen,
    WipeTransition,
    FadeTransition,
    SlideTransition,
    CardTransition,
    SwapTransition,
    FallOutTransition,
    RiseInTransition,
)

# check libraries usage in KV file, they can be used when marked unused there

Window.minimum_height = 850
Window.minimum_width = 750


# Declare all screens
class MenuScreen(Screen):
    pass


class PlotScreen(Screen):
    pass


class AboutScreen(Screen):
    pass


class GitScreen(Screen):
    pass


class Sol_Calc(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.resres = None
        self.new_map = None
        self.t1 = "t1.png"
        self.imt1 = Image(source="t1.png")

    def build(self):
        # Create the screen manager
        # ddd = Builder.load_string("Sol_Calc.kv")
        ddd = Builder.load_file("Sol_Calc.kv")

        self.title = "Solar Calculator"
        self.icon = "icon.png"
        self.selecteddate = ""
        sm = ScreenManager(transition=WipeTransition())
        sm.add_widget(MenuScreen(name="screen_1"))
        sm.add_widget(PlotScreen(name="screen_2"))
        sm.add_widget(AboutScreen(name="screen_3"))
        sm.add_widget(GitScreen(name="screen_4"))
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        # return Builder.load_string(KV)

        def my_callback(dt):  # function for actual time counting
            if self.root.get_screen("screen_1").ids.time_val.text != "":
                datetime_object = datetime.strptime(
                    self.root.get_screen("screen_1").ids.time_val.text,
                    "%d/%m/%Y %H:%M:%S",
                )
                d = timedelta(seconds=1)
                datetime_object = datetime_object + d
                datetime_object = datetime_object.strftime("%d/%m/%Y %H:%M:%S")
                self.root.get_screen("screen_1").ids.time_val.text = str(
                    datetime_object
                )

        Clock.schedule_interval(my_callback, 1)  # refresh time every second

        return sm

    def callback_return_home(self):
        # self.theme_cls.theme_style_switch_animation_duration = 0.8
        # self.theme_cls.icon_color =[ 0, 0, 0, 0]
        self.root.current = "screen_1"

    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )

    def on_save(self, instance, value, date_range):
        #  self.chosendate = value,
        # print(instance, value, date_range)
        self.selecteddate = value
        self.date_val =  str(self.selecteddate.strftime("%d/%m/%Y"))
        self.root.get_screen("screen_1").ids.date_val.text = self.date_val
        # return self.build()

    def on_cancel(self, instance, value):
        """Events called when the "CANCEL" dialog box button is clicked."""

    def calendars(self):
        return self.show_date_picker()

    def show_date_picker(self):
        #    Builder.load_string(KV)

        self.date_dialog = MDDatePicker(
            #  primary_color=self.theme_cls.primary_color,
            #  accent_color="darkred",
            #  primary_color="brown",
            #    accent_color="darkred",
            #    selector_color="red",
            #    text_toolbar_color="lightgrey",
            #   text_color="orange",
            #   text_current_color="white",
            #   text_button_color="lightgrey",
            #  input_field_background_color_normal="coral",
            #  input_field_background_color_focus="red",
        )
        self.date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        self.date_dialog.open()

    # print(self.theme_cls.)
    # return Builder.load_string(KV)
    # print("save",self.on_save)

    def reset(self):  # function for reset button
        self.root.get_screen("screen_1").ids.input_field_1.text = ""
        self.root.get_screen("screen_1").ids.time_val.text = ""
        self.root.get_screen("screen_1").ids.input_field_1.helper_text = "City"
        self.root.get_screen("screen_1").ids.time_val.text = ""
        self.root.get_screen("screen_1").ids.time_val_label.text = ""
        self.root.get_screen("screen_1").ids.location_val_label.text = ""
        self.root.get_screen("screen_1").ids.date_val.text = ""
     

        # podrobne vysl hodnoty
        self.root.get_screen("screen_1").ids.location_val.text = ""
        self.root.get_screen("screen_1").ids.sunrise_val.text = ""
        self.root.get_screen("screen_1").ids.sunset_val.text = ""
        self.root.get_screen("screen_1").ids.noon_val.text = ""
        self.root.get_screen("screen_1").ids.lat_val.text = ""
        self.root.get_screen("screen_1").ids.long_val.text = ""
        self.root.get_screen("screen_1").ids.tz_val.text = ""
        

        self.resres = None
        self.default_map()
        self.imt1.reload()
        self.drw = None

    def flip(self):  # flip handler
        self.reset()
        """
        self.label.text = ""
        self.input.text = ""
        self.selecteddate = ""
        """

    def input_value(self):
        self.value = self.root.get_screen("screen_1").ids.input_field_1.text
        print("What you typed is: ", self.value)
        return self.value

    def convert_R(self, args=0):  # function for convert button
        if self.selecteddate:
            self.seldat = self.selecteddate
        else:
            self.seldat = ""
            self.selecteddate = ""
        try:
            val = str(self.input_value()).title()
            self.root.get_screen("screen_1").ids.input_field_1.text = val
            if len(val) > 3:
                # CalcSol.UTCcl(self, val, self.seldat)
                if CalcSol.UTCcl(self, val, self.seldat) != None:
                    self.reset()
                    self.root.get_screen(
                        "screen_1"
                    ).ids.input_field_1.helper_text = "Location does not exist"
                    return self.convert_R
                self.resres = CalcSol.calculations(self, val)

                if self.resres == None:
                    self.reset()
                    self.root.get_screen(
                        "screen_1"
                    ).ids.input_field_1.helper_text = "Wrong adress"
                    return self.convert_R
               # else:
                    # print("passed")
            else:
                self.reset()
                self.root.get_screen(
                    "screen_1"
                ).ids.input_field_1.helper_text = "Wrong value"
                return self.convert_R
        except ValueError:
            self.root.get_screen("screen_1").ids.time_val.text = ""
            self.root.get_screen(
                "screen_1"
            ).ids.input_field_1.helper_text = "Wrong value"
            self.root.get_screen("screen_1").ids.input_field_1.text = ""
            return self.convert_R

        self.drw = self.map_draw()  # generate map
        self.imt1.reload()  # reload map img when changed

        if self.drw != None:  # widget with map reloading
            self.root.get_screen("screen_1").ids.mapimg.source = "t1.png"
            self.root.get_screen("screen_1").ids.mapimg.reload()
            """
            self.screen.add_widget(
                Image(
                    source="t1.png",
                    nocache=True,
                    allow_stretch=True,
                    keep_ratio=True,
                    # height = 220, width = 220,
                    # allow_stretch: True,
                    # size_hint_y: 0, # Tells the layout to ignore the size_hint in y dir
                    size_hint=(0.8, 0.25),
                    # size_hint_min=(200, 200),
                    # size=(100, 100),
                    # pos=(200, 200),
                    pos_hint={"center_x": 0.5, "y": 0.01},
                )
            )
            """
            self.drw = None

     #   self.root.get_screen("screen_1").ids.input_field_1.helper_text = "Current time"
        self.root.get_screen("screen_1").ids.time_val_label.text = "Time and Date of Location"
        self.root.get_screen("screen_1").ids.time_val.text = self.resres[20]
        self.root.get_screen("screen_1").ids.location_val_label.text = "Selected Location"
       # self.date_val =  str(self.selecteddate.strftime("%d/%m/%Y"))
        
            #print(date_val)
        #  dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
        self.root.get_screen("screen_1").ids.date_val.text = self.resres[-1][:10]



        # podrobne vysl hodnoty
        self.root.get_screen("screen_1").ids.location_val.text = self.resres[0]
        self.root.get_screen("screen_1").ids.sunrise_val.text = self.resres[17]
        self.root.get_screen("screen_1").ids.sunset_val.text = self.resres[18]
        self.root.get_screen("screen_1").ids.noon_val.text = self.resres[16]
        self.root.get_screen("screen_1").ids.lat_val.text = self.resres[1][0:5] + "°"
        self.root.get_screen("screen_1").ids.long_val.text = self.resres[2][0:5] + "°"
        self.root.get_screen("screen_1").ids.tz_val.text = self.caz

    def default_map(
        self,
    ):  # show default map image when app is builded without pinned location
        self.root.get_screen("screen_1").ids.mapimg.source = "w1.jpg"

    def map_draw(self):  # generate new map with pin in it as selected location
        if self.resres != None:
            #print(f"resres {self.resres[1]}")
            self.map_generator = MapLocator(self.resres[1], self.resres[2])
            img_loc = self.map_generator.img_map_generator()
            """
            self.screen.add_widget(
                Image(
                    source="t1.png",
                    nocache=True,
                    allow_stretch=True,
                    keep_ratio=True,
                    size_hint=(0.8, 0.25),
                    pos_hint={"center_x": 0.5, "y": 0.01},
                )
            )
            """
            return img_loc


Sol_Calc().run()


# TODO add button for language change, change variable in sol_budik location = geolocator.geocode
# TODO fix primary secondary fonts
# TODO memory leak fix
# TODO add time selector not just date
# TODO cape town location adjust
# TODO reykjavik location adjust 