from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDButtonIcon, MDButtonText
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

kv = """

MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDIconButton:
        icon: "heart-outline"
        style: "standard"
        pos_hint: {'center_x':.5, 'center_y': .5}
    
    MDIconButton:
        icon: "heart-outline"
        style: "filled"
        pos_hint: {'center_x':.4, 'center_y': .4}
    MDIconButton:
        icon: "heart-outline"
        style: "tonal"
        pos_hint: {'center_x':.3, 'center_y': .3}
        
    MDIconButton:
        icon: "heart-outline"
        style: "outlined"
        pos_hint: {'center_x':.2, 'center_y': .2}
        
    MDIconButton:
        icon: "pencil-outline"
        style: "standard"
        pos_hint: {'center_x':.1, 'center_y': .1}
            
"""

class Button(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Olive"
    
        return Builder.load_string(kv)

Button().run()