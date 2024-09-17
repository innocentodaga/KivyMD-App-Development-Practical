from kivy.lang import Builder
import kivymd
from kivymd.app import MDApp


kv = """
MDScreen:
    md_bg_color: app.theme_cls.surfaceColor
    MDExtendedFabButton:
        id: btn
        pos_hint: {"center_x": .5, "center_y": .5}
        MDExtendedFabButtonIcon:
            icon: "pencil-outline"
        MDExtendedFabButtonText:
            text: "Compose"
        
        # on_touch_down:
        #     if not btn.collide_point(*args[1].pos): \
        #     btn.fab_state = "expand" \
        #     if btn.fab_state == "collapse" else "collapse"
                
"""
class EXtendedFabIcon(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = "Orange"
        
        return Builder.load_string(kv)

EXtendedFabIcon().run()