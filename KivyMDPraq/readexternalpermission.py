from kivy import platform
from kivy.lang import Builder
from kivy.clock import Clock

from kivymd.app import MDApp


class ReadExternalPerm(MDApp):
    def build(self):
        Builder.load_file('readexternalperm.kv')
    
    # updating the color scheme when the app resumes
    def on_resume(self, *args):
        self.theme_cls.set_colors()
    
    # when sets dynamic color value, the self method will be called.theme_cls.set_colors()
    # which will generate a color sceme from a custom wallpaper if dynamic color is True
    def set_dynamic_color(self, *args) -> None:
        self.theme_cls.dynamic_color = True
        
    def on_start(self) -> None:
        # its fired at the start yf the app and requests the necessary permissions
    
        def callback(permission, results):
            if all([res for res in results]):
                Clock.schedule_once(self.set_dynamic_color)
        if platform == 'android':
            from android.permissions import Permission, request_permissions
            permissions = [Permission.READ_EXTERNAL_STORAGE]
            request_permissions(permissions, callback)
        
ReadExternalPerm().run()