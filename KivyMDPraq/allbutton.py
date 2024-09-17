from kivy.lang import Builder
from kivymd.app import MDApp

kv = """
MDScreen:
    md_bg_color: app.theme_cls.surfaceColor
    
    MDButton:
        style: 'elevated'
        pos_hint: {'center_x':.5, 'center_y': .5}
        
        MDButtonIcon:
            icon: 'plus'
        
        MDButtonText:
            text: "Elevated"
    
    # Filled button
    MDButton:
        style: 'filled'
        pos_hint: {'center_x':.5, 'center_y': .4}
        
        MDButtonIcon:
            icon: 'plus'
        
        MDButtonText:
            text: '  Filled  '
    MDButton:
        style: 'tonal'
        pos_hint: {'center_x':.5, 'center_y': .3}
        
        MDButtonIcon:
            icon: 'plus'
        
        MDButtonText:
            text: '  Tonal  '  
    MDButton:
        style: 'outlined'
        pos_hint: {'center_x':.5, 'center_y': .2}
        
        MDButtonIcon:
            icon: 'plus'
        
        MDButtonText:
            text: 'outlined'  
    
    MDButton:
        style: 'text'
        pos_hint: {'center_x':.5, 'center_y': .1}
        
        MDButtonIcon:
            icon: 'plus'
        
        MDButtonText:
            text: '  text  '   
"""

class ElevatedButton(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(kv)
    
ElevatedButton().run()