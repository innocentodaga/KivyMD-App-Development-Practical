from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.metrics import sp
from kivymd.app import MDApp


KV = """
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor
    
    MDLabel:
        text: "MDLabel"
        halign: "center"
        font_style: "nasalization"
"""

class AddCustomFont(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        
        LabelBase.register(
            name="nasalization",
            fn_regular="./fonts/Poppins-Regular.ttf",
        )
        
        self.theme_cls.font_styles["nasalization"] = {
            "large":{
                "line_height": 1.64,
                "font-name": "nasalization",
                "font-size": sp(57),
            },
            "medium":{
                "line_height": 1.52,
                "font-name": "nasalization",
                "font-size": sp(45),
            },
            "small":{
                "line_height": 1.44,
                "font-name": "nasalization",
                "font-size": sp(36),
            }
        }
        
        return Builder.load_string(KV)
AddCustomFont().run()