from kivy.lang import Builder
from kivymd.app import MDApp

KV = """
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor
    
    MDCard:
        orientation: 'vertical'
        padding: 0, 0, 0, '36dp'
        size_hint: .5, .5
        style: 'elevated'
        pos_hint: {'center_x': .5, 'center_y': .5}
        
        MDLabel:
            text: "Theme style - {}".format(app.theme_cls.theme_style)
            halign: 'center'
            valign: 'center'
            bold: True
            font_style: 'Display'
            role: 'small'
        MDButton:
            on_release: app.switch_theme_style()
            pos_hint: {"center_x":.5}
            
            MDButtonText:
                text: 'Set theme'
            
"""
class ThemeSwitch(MDApp):
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

ThemeSwitch().run()