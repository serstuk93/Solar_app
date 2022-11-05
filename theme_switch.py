from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivymd.uix.button import MDFloatingActionButton
from kivy.core.window import Window

Window.minimum_height = 800
Window.minimum_width = 400


"""
                Button:
                    text:'Hello'
                    size:(100, 50)
                    pos_hint: {"center_x": 1, "center_y": .5}
                Button:
                    text:'WORLD'
                    size_hint:(None, None)
                Button:
                    text:'HAAello'
                    size_hint:(.1, 0.3)
                    pos_hint: {"center_x": .5, "center_y": .5}
                    """

"""
        MDBoxLayout:
            id: box
            spacing: "10dp"
            adaptive_size: True
            orientation: 'horizontal'

            MDRaisedButton:
                text: "Set theme"
                on_release: app.switch_theme_style()
                pos_hint: {"center_x": .5, "center_y": 0}
            MDRaisedButton:
                text: "BBBBB"
                on_release: app.switch_theme_style()
                pos_hint: {"center_x": .5, "center_y": 1}
            """
KV = '''
<TooltipMDIconButton@MDIconButton+MDTooltip>



MDBoxLayout:
    height: self.minimum_height

    MDNavigationRail:   # navigation
        MDNavigationRailItem:
            text: "Calculator"
            icon: "sun-clock"

        MDNavigationRailItem:
            text: "Plot"
            icon: "file-table"

        MDNavigationRailItem:
            text: "About"
            icon: "creative-commons"

        MDNavigationRailItem:
            text: "Git"
            icon: "git"
    MDScreen:    # screen
    
        MDCard:
            focus_behavior: True
            ripple_behavior: True
            orientation: "horizontal"
            padding: 10, 0, 0 , "5dp"
            size_hint: .9, .1
            spacing:20
            pos_hint: {"center_x": .5, "center_y": 0.94}
            elevation: 4
            shadow_radius: 6
            shadow_offset: 0, 2

            MDLabel:
               # size_hint: .1, 0.1
                size: self.size
                
             #  pos_hint: {"left": 0.1, "top": 1}
                halign: "left"
                valign: "center"   
                text: "Theme style - {}".format(app.theme_cls.theme_style)
                bold: True
                font_style: "H5"
            MDRaisedButton:
                text: "Set theme"
                on_release: app.switch_theme_style()
                pos_hint: {"center_x": .5, "center_y": 0.5}
            TooltipMDIconButton:                     # reset button
                icon: "restart"
                tooltip_text: "Clear input"
                pos_hint: {"center_x": .5, "center_y": .5}




        MDBoxLayout:
            spacing: 20
          #  padding: 0, 0, 0 , "20dp"
            orientation: "horizontal"
            pos_hint: {"x": .05, "top": 0.87}
            adaptive_height: True
            md_bg_color: "red"  # app.theme_cls.primary_color
         #   canvas:
         #       Color:
         #           rgba: app.theme_cls.primary_color
          #      Rectangle:
         #           pos: self.pos
          #          size: self.size

            MDLabel:
                md_bg_color: "blue" 
                text: "Sol Calc - {}".format(app.theme_cls.theme_style)
                width: 250
                size_hint : (None, 0.3)
               # pos_hint: {"center_x": 0.1, "top": 1}
                halign: "center"
                valign: "center"
                bold: True
                font_style: "H5"

            MDRaisedButton:
                text: "Set theme"
                on_release: app.switch_theme_style()
             #   pos_hint: {"right": .5, "top": 1}




        MDCard:
            md_bg_color: "green"  # app.theme_cls.primary_color
            focus_behavior: True
            ripple_behavior: True
            orientation: "vertical"
            padding: 20, 20, 0 , "36dp"
            size_hint: .9, .25
            pos_hint: {"center_x": 0.5, "center_y": 0.7}
            elevation: 4
            shadow_radius: 6
            shadow_offset: 0, 2
        
            MDLabel:
                text: "Calculations"
                size_hint: .5, 0.1
                size: self.size
                pos_hint: {"center_x": 0.5, "top": 0.1}
                halign: "center"
                valign: "center"
                bold: True
                font_style: "H5"
            MDBoxLayout:
                padding : 5
                adaptive_width: True
                size_hint_y : 0.2
                spacing: "20dp"
                pos_hint: {"left": 0, "top": 0.5}
                adaptive_height: True
                md_bg_color: "red"  # app.theme_cls.primary_color
                height: self.minimum_height
                MDRectangleFlatButton:
                    text: "Set theme"
                    on_release: app.switch_theme_style()
                    pos_hint: {"left": .5, "top": 1}
                MDRectangleFlatButton:
                    text: "Set theme"
                    on_release: app.switch_theme_style()
                    pos_hint: {"right": .5, "top": 1}
            MDBoxLayout:
                padding : 5
                adaptive_width: True
                size_hint_y : 0.2
                spacing: "20dp"
                pos_hint: {"left": 0.5, "top": 0.5}
                adaptive_height: True
                md_bg_color: "blue"  # app.theme_cls.primary_color
                height: self.minimum_height
                MDRectangleFlatButton:
                    text: "Set theme"
                    on_release: app.switch_theme_style()
                    pos_hint: {"left": .5, "top": 1}
                MDRectangleFlatButton:
                    text: "Set theme"
                    on_release: app.switch_theme_style()
                    pos_hint: {"right": .5, "top": 1}




        MDBoxLayout:
            height: self.minimum_height
            pos_hint: {"top": 0.6, "x":0.05}
            orientation: "vertical"
            spacing: 20
            padding: 20, 20, 0 , "36dp"
            size : (100,10)
            size_hint_y : 0.3
            md_bg_color: "red"  # app.theme_cls.primary_color
            MDBoxLayout:
                orientation: "horizontal"
                MDLabel:
                    text: "Selected Location"
                MDLabel:
                    text: "AAAAAAAAAAA"
            MDBoxLayout:
                orientation: "horizontal"
                MDLabel:
                    text: "Sunrise time"
                MDLabel:
                    text: "AAAAAAAAAAA"
            MDBoxLayout:
                orientation: "horizontal"
            
                MDLabel:
                    text: "Sunset time"
                MDLabel:
                    text: "AAAAAAAAAAA"
            MDBoxLayout:
                orientation: "horizontal"
                MDLabel:
                    text: "Noon"
                MDLabel:
                    text: "AAAAAAAAAAA"
            MDBoxLayout:
                orientation: "horizontal"
                MDLabel:
                    text: "Geographical Latitude"
                MDLabel:
                    text: "AAAAAAAAAAA"
            MDBoxLayout:
                orientation: "horizontal"
                MDLabel:
                    text: "Terrestrial Longitude"
                MDLabel:
                    text: "AAAAAAAAAAA"
            MDBoxLayout:
                orientation: "horizontal"
                MDLabel:
                    text: "Timezone"
                MDLabel:
                    text: "AAAAAAAAAAA"
        


        MDCard:
        #    md_bg_color: app.theme_cls.primary_color
            focus_behavior: True
            ripple_behavior: True
            size_hint: .9, .3
            pos_hint: {"center_x": .5, "center_y": 0.16}
            elevation: 4
            shadow_radius: 6
            shadow_offset: 0, 2
            size_hint_max_x:450
            size_hint_max_y:240
            size_hint_min_y:150

            Image:
                source:"w1.jpg"
                nocache:True
                allow_stretch:True
                keep_ratio:True
                size_hint:(1, 1)
                pos_hint:{"center_x": 0.5, "top": 1}
            



'''

"""

        MDCard:
            orientation: "vertical"
            padding: 0, 0, 0 , "36dp"
            size_hint: .9, .2
            pos_hint: {"center_x": .5, "center_y": .5}
            elevation: 4
            shadow_radius: 6
            shadow_offset: 0, 2
        MDBoxLayout:
           
            adaptive_height: True
            md_bg_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.minimum_height

            canvas:
                Color:
                    rgba: app.theme_cls.primary_color
                Rectangle:
                    pos: self.pos
                    size: self.size
                    """



class SolarCalculator(MDApp):
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )
    """
    def on_start(self):
        data = {
            "standard": {"md_bg_color": "#fefbff", "text_color": "#6851a5"},
            "small": {"md_bg_color": "#e9dff7", "text_color": "#211c29"},
            "large": {"md_bg_color": "#f8d7e3", "text_color": "#311021"},
            "sd": {"md_bg_color": "#f8d7e3", "text_color": "#311021"},
        }
        for type_button in data.keys():
            self.root.ids.box.add_widget(
                MDRectangleFlatButton(
                    text= "MDRectangleFlatButton",
                    theme_text_color= "Custom",
                    text_color= "white",
                    line_color= "red",
                )
            )"""


SolarCalculator().run()

