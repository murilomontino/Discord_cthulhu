from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '240')

class Gerenciador(ScreenManager):
    pass

class DiscordAppBot(App):
    pass

DiscordAppBot().run()

