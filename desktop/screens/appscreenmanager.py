from kivy.uix.screenmanager import ScreenManager

class AppScreenManager(ScreenManager):

    '''
    Application's main Screen Manager, that is returned as the root widget.
    It contains all the screens app uses and allows to switch between them.
    '''

    def switch_to_screen(self, screen):
        self.current = screen