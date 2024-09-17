from kivy.lang import Builder
from kivymd.app import MDApp

KV ="""
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor
    
    MDBoxLayout:
        radius: "15dp"
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: .4, .8
        md_bg_color: (1,.2, .2, .3)
        
        FitImage:
            source: "image1.jpg"
            size_hint_y: .35
            pos_hint: {"top": 1}
            radius: "15dp", "15dp", 0, 0 
"""

class CardWithImage(MDApp):
    def build(self):
        return Builder.load_string(KV)

CardWithImage().run()
