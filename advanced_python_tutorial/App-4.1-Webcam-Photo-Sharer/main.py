from datetime import datetime

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from filesharer import FileSharer


Builder.load_file(('frontend.kv'))

class CameraScreen(Screen):
    def start(self):
        """
        Starts camera and changes Button text
        """
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        """
        Stops camera and changes Button text
        """
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        """
        Creates a filename withe the current time and captures
        and saves a photo image under that filename
        """
        current_time = datetime.now()
        filepath = f"images/img_{current_time.strftime('%Y%m%d_%H%M%S')}.png"
        self.ids.camera.export_to_png(filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = filepath


class ImageScreen(Screen):
    pass

class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()