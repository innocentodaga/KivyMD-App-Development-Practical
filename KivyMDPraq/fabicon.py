import kivymd
from kivymd.app import MDApp
from kivymd.uix.button import MDFabButton
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

kv= """
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor
    
    MDFabButton:
        icon: "pencil-outline"
        style: "standard"
        pos_hint: {'center_x': .5, 'center_y':.5}
"""


class FabIcon(MDApp):
    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Olive"
        
        return Builder.load_string(kv)

FabIcon().run()