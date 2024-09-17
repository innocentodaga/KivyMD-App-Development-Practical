from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
from kivymd.uix.screen import MDScreen

Window.size = (320, 580)

class BaseMDNavigationItem(MDNavigationItem):
    icon =  StringProperty()
    text = StringProperty()


class BaseScreen(MDScreen):
    ...

KV = """

<BaseMDNavigationItem>
    MDNavigationItemIcon:
        icon: root.icon
    MDNavigationItemLabel:
        text: root.text

<BaseScreen>
    MDLabel:
        text: root.name
        halign: "center"

MDBoxLayout:
    orientation: "vertical"
    md_bg_color: self.theme_cls.backgroundColor
    
    
    MDNavigationLayout:
        MDTopAppBar:
            type: "small"
            size_hint_x: .9
            size_hint_y: None
            max_height: dp(20)
            pos_hint: {"center_y": .95}
            
            MDTopAppBarLeadingButtonContainer:
                MDActionTopAppBarButton:
                    icon: "menu"
                    on_release: nav_drawer.set_state("toggle")
                    
            MDTopAppBarTitle:
                text: "Cafeteria"
                pos_hint: {"center_x": .5}
                
            MDTopAppBarTrailingButtonContainer:
            MDActionTopAppBarButton:
                icon: "account-circle-outline"
                
        MDScreenManager:
            id: screen_manager
            
            BaseScreen:
                name: "Home"
            BaseScreen:
                name: "Orders"
            BaseScreen:
                name: "Favorites"
            BaseScreen:
                name: "Profile"

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
                
    MDNavigationBar:
        on_switch_tabs: app.on_switch_tabs(*args)
        
        BaseMDNavigationItem
            icon: "home"
            text: "Home"
            active: True
        BaseMDNavigationItem
            icon: "toolbox"
            text: "Orders" 
        BaseMDNavigationItem
            icon: "cart-heart"
            text: "Favorites"  
        BaseMDNavigationItem
            icon: "account-circle"
            text: "Profile" 

"""
class BottomNavigation(MDApp):
    def on_switch_tabs(
        self,
        bar: MDNavigationBar,
        item: MDNavigationItem,
        item_icon: str,
        item_text: str,
    ):
        self.root.ids.screen_manager.current = item_text
    
    def build(self):
        return Builder.load_string(KV)

BottomNavigation().run()

