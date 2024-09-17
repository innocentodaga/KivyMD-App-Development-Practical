from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDButtonIcon, MDButtonText
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

kv = """

MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDButton:
        style: "elevated"
        theme_width: "Custom"
        size_hint_x: .5
        height: '56dp'
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        theme_shadow_color: "Custom"
        shadow_color: "green"
        
        MDButtonIcon:
            icon:"plus"
            x : text.x - (self.width + dp(10))
            theme_icon_color: "Custom"
            icon_color: "green"
        MDButtonText
            text:"Button"
            theme_text_color: "Custom"
            text_color: "green"
            id : text
            pos_hint : {"center_x": .5, "center_y": .5}
"""

class Button(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Olive"
    
        return Builder.load_string(kv)

Button().run()