from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

class ThemeSame(MDApp):
    def build(self):
        self.theme_cls.theme_switch_style_animation = True
        self.theme_cls.theme_switch_style_animation_duration = .8
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        
        return(
            MDScreen(
                MDCard(
                    MDLabel(
                        id = 'label',
                        text="Theme Style - {}".format(
                            self.theme_cls.theme_style),
                        halign = "center",
                        valign = "center",
                        bold = True,
                        font_style = "Display",
                        role = "small",
                    ),
                    MDButton(
                        MDButtonText(
                            text = "Set Theme",
                        ),
                        on_release= self.switch_theme_style,
                        pos_hint= {"center_x": .5}
                    ),
                    id="card",
                    orientation = "vertical",
                    padding = (0, 0, 0,'36dp'),
                    size_hint = (.5, .5),
                    pos_hint = {'center_x': .5, 'center_y':.5},
                    style = "elevated",
                    
                )
            )
        )

    def on_start(self):
        def on_start(*args):
            self.root.md_bg_color = self.theme_cls.backgroundColor
        Clock.schedule_once(on_start)
    def switch_theme_style(self, *args):
        self.theme_cls.primary_palette = (
        "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
        )
        self.theme_cls.theme_style = (
        "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )
        self.root.get_ids().label.text = (
        "Theme style - {}".format(self.theme_cls.theme_style)
        )
ThemeSame().run()
