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
        self.filepath = f"images/img_{current_time.strftime('%Y%m%d_%H%M%S')}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):
    def create_link(self):
        """
        Accesses the photo filepath, uploads it to the web,
        and inserts the link in the label widget
        :return:
        """
        filepath = App.get_running_app().root.ids.camera_screen.filepath
        filesharer = FileSharer(filepath = filepath)
        url = filesharer.share()
        self.ids.link.text = url

class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()