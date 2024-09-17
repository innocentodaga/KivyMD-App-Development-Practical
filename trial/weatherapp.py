from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView

class Weather(BoxLayout):
    pass

class MyRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super(MyRecycleView, self).__init__(**kwargs)
        self.data = [{'text': "Palo Alto, MX"}, {'text': "Palo Alto, US"}]

class WeatherApp(App):
    def build(self):
        return Weather()

if __name__ == '__main__':
    WeatherApp().run()
