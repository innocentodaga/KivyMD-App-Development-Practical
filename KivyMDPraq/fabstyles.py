from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDFabButton

KV = '''
MDScreen:
    md_bg_color: app.theme_cls.surfaceColor
    MDBoxLayout:
        id: box
        adaptive_size: True
        spacing: "32dp"
        pos_hint: {"center_x": .5, "center_y": .5}
'''
class Example(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)
    def on_start(self):
        styles = {
            "standard": "surface",
            "small": "secondary",
            "large": "tertiary",
        }
        for style in styles.keys():
            self.root.ids.box.add_widget(
                MDFabButton(
                    style=style, icon="pencil-outline", color_map=styles[style]
                )
        )
Example().run()