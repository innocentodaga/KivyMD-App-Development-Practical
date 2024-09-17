from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty



# Set the window size for mobile view simulation
Window.size = (320, 580)

# Define all your screen classes
class MainScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class SignupScreen(Screen):
    pass

class ForgotScreen(Screen):
    pass

class MyAppScreen(Screen):
    pass

class MyCard(MDCard):
    text = StringProperty()

class Cafeteria(MDApp):
    def on_start(self):
        MyCard(style = "elevated")
         
    def build(self):
        # Set the theme style
        self.theme_cls.theme_style = "Light"
        screen_manager = ScreenManager()

        # Define the screens to be added with their corresponding KV files
        screens = [
            (MainScreen, "main", "./main.kv"),
            (LoginScreen, "login", "./login.kv"),
            (SignupScreen, "signup", "./signup.kv"),
            (ForgotScreen, "forgot", "./forgot.kv"),
            (MyAppScreen, "myapp", "./myapp.kv"),
        ]

        # Add each screen to the screen manager
        for screen_class, name, kv_file in screens:
            screen = screen_class(name=name)
            # Ensure the KV file is correctly loaded for the screen
            screen.add_widget(Builder.load_file(kv_file))
            screen_manager.add_widget(screen)

        return screen_manager

if __name__ == "__main__":
    # Register custom fonts
    LabelBase.register(name="MPoppins", fn_regular="./fonts/Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins", fn_regular="./fonts/Poppins-SemiBold.ttf")
    Cafeteria().run()
