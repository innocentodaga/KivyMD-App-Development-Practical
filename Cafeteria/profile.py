from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDIconButton
from kivy.core.window import Window
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout

Window.size = (320, 600)


class ProfileCard(MDFloatLayout, CommonElevationBehavior):
    pass

class Profile(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        Builder.load_file('profile.kv')
        

if __name__ == '__main__':
    LabelBase.register(name="MPoppins", fn_regular="./fonts/Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins", fn_regular="./fonts/Poppins-SemiBold.ttf")
    Profile().run()