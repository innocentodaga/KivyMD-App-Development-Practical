from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.utils.set_bars_colors import set_bars_colors
KV = '''
MDBoxLayout:
    orientation: "vertical"
    
    MDTopAppBar:
        title: "MDTopAppBar"
    MDBottomNavigation:
        panel_color: app.theme_cls.surfaceColor
        text_color_active: .2, .2, .2, 1
        text_color_normal: .9, .9, .9, 1
        use_text: False
        MDBottomNavigationItem:
            icon: 'gmail'
        MDBottomNavigationItem:
            icon: 'twitter'
        MDBottomNavigationItem:
            icon: 'youtube'
'''
class Test(MDApp):
    def build(self):
        self.set_bars_colors()
        return Builder.load_string(KV)
    def set_bars_colors(self):
        set_bars_colors(
            self.theme_cls.primary_color, # status bar color
            self.theme_cls.primary_color, # navigation bar color
            "Light", # icons color of status bar
        )
Test().run()