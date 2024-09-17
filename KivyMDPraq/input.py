from kivy.lang import Builder

from kivymd.app import MDApp

kv = """
MDScreen:
    md_bg_color: app.theme_cls.backgroundColor
    
    MDTextField:
        mode: 'outlined'
        size_hint_x: None
        width: "240dp"
        pos_hint: {"center_x": .5, "center_y": .5}
        
        MDTextFieldLeadingIcon:
            icon: "account"
            theme_icon_color: "Custom"
            icon_color_normal: "lightgreen"

        
        MDTextFieldHintText:
            text: "Outlined"
        
        MDTextFieldHelperText:
            text: "Helper Text"
        
        MDTextFieldTrailingIcon:
            icon: "information"
        
        MDTextFieldMaxLengthText:
            max_text_length: 10
    
"""

class InputTextField(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Olive"
        return Builder.load_string(kv)

InputTextField().run()