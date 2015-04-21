#: -*- encoding: utf-8 -*-

'''
Report Creator is a tool that allows the user to freely
organise his tests reports and then export it to PDF format.

Application is created with Python using Kivy Framework.
'''

__title__ = 'Report Creator'
__version__ = '0.1.0'
__author__ = 'rafalo1333'

import kivy
kivy.require('1.9.0')

from kivy.utils import platform, get_color_from_hex
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.logger import Logger
from kivy.config import Config

Window.clearcolor = get_color_from_hex('#E0E0E0')

from kivy.app import App

class ReportCreatorApp(App):

    def build(self):
        self.title = '%s %s' % (__title__, __version__)
        if platform in ['linux', 'win', 'macosx']:
            Logger.info('Platform: Active platform is %s' % platform)
            Config.set('graphics', 'fullscreen', 'auto')
            Config.set('kivy', 'desktop', 1)
            Config.set('kivy', 'exit_on_escape', 0)
            #Config.set('input', 'mouse', 'mouse_disable_multitouch')
            return Builder.load_file('desktop/main.kv')
        elif platform in ['android', 'ios']:
            Logger.info('Platform: Active platform is %s' % platform)
            return Builder.load_file('mobile/main.kv')
        else:
            Logger.info('Platform: Active platform is %s' % platform)
            return Builder.load_file('desktop/main.kv')
    
if __name__ == '__main__':
    ReportCreatorApp().run()