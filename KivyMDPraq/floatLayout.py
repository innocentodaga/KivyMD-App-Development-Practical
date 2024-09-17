from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder

KV = """
MDFloatLayout:
    radius: [25,0,0,0]
    md_bg_color: app.theme_cls.primaryColor
    
    MDGridLayout:
        adaptive_height: True
        md_bg_color: app.theme_cls.primaryColor
"""

class MyFloatApp(MDFloatLayout):
    pass

class MyApp(MDApp):
    def build(self):
        Builder.load_string(KV)
        return MyFloatApp()
    
MyApp().run()