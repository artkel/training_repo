import webbrowser
from datetime import datetime

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
from filesharer import FileSharer


Builder.load_file(('frontend.kv'))

class CameraScreen(Screen):
    def start(self):
        """
        Starts camera and changes Button text
        """
        self.ids.camera.opacity = 1
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        """
        Stops camera and changes Button text
        """
        self.ids.camera.opacity = 0
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
    link_message = "Create a link first"
    def create_link(self):
        """
        Accesses the photo filepath, uploads it to the web,
        and inserts the link in the label widget
        """
        filepath = App.get_running_app().root.ids.camera_screen.filepath
        filesharer = FileSharer(filepath = filepath)
        self.url = filesharer.share()
        self.ids.link.text = self.url

    def copy_link(self):
        """
        Copy link to the clipboard available for pasting
        """
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_message

    def open_link(self):
        """
        Open link with default browser
        """
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_message

class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()