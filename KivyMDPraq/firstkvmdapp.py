from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDButton, MDButtonText


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Orange'
        return (
            MDScreen(
                MDButton(
                    MDButtonText(
                        text = 'Hello Tyson',
                        
                    ),
                    pos_hint={'center_x': .5, 'center_y':.5}
                ),
                MDButton(
                    MDButtonText(
                        text = "Please click Me",
                    ),
                    pos_hint = {'center_x': .5, 'center_y':.4}
                )
            )
        )
            

MainApp().run()