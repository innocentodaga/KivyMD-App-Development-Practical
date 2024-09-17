from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.metrics import dp

kv = """
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor
    
    MDNavigationLayout:
        ScreenManager:
            MDScreen:
                MDButton:
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    on_release: nav_drawer.set_state("toggle")
                   
                    MDButtonText:
                        text: "Open Drawer"
        MDNavigationDrawer:
            id: nav_drawer
            radius: 0, dp(10), dp(10), 0
            
            MDNavigationDrawerMenu:
                MDNavigationDrawerLabel:
                    text: "Mail"
                
                MDNavigationDrawerItem:
                    height: dp(45)
                    MDNavigationDrawerItemLeadingIcon:
                        icon: "account"
                    
                    MDNavigationDrawerItemText:
                        text: "Inbox"
                    
                    MDNavigationDrawerItemTrailingText:
                        text: "24"
                
                MDNavigationDrawerDivider:                
                
                MDNavigationDrawerItem:
                    height: dp(45)
                    MDNavigationDrawerItemLeadingIcon:
                        icon: "account"
                    
                    MDNavigationDrawerItemText:
                        text: "Inbox"
                    
                    MDNavigationDrawerItemTrailingText:
                        text: "24"
                
                
                MDNavigationDrawerItem:
                    height: dp(45)
                    MDNavigationDrawerItemLeadingIcon:
                        icon: "account"
                    
                    MDNavigationDrawerItemText:
                        text: "Inbox"
                    
                    MDNavigationDrawerItemTrailingText:
                        text: "24"

"""

class NavigationDrawer(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(kv)

NavigationDrawer().run()
