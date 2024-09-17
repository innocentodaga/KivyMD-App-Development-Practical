from kivy.lang import Builder
from kivymd.app import MDApp

KV = """
MDScreen: 
    md_bg_color: self.theme_cls.backgroundColor
    
    MDLinearProgressIndicator:
        size_hint_x: .5
        value: 50
        pos_hint: {"center_x": .5, "center_y": .5}
    
    MDCircularProgressIndicator:
        size_hint: None, None
        size: "30dp", "30dp"
        pos_hint: {'center_x': .5, 'center_y': .6}

    MDCircularProgressIndicator:
        size_hint: None, None
        size: "30dp", "30dp"
        pos_hint: {'center_x': .5, 'center_y': .7}
        determinate: True
        on_determinate_complete: print(args)
    
    
"""


class ProgressIndicator(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

ProgressIndicator().run()