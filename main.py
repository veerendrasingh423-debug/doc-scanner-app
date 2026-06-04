from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button

class ScannerApp(App):
    def build(self):
        # Create a vertical layout
        layout = BoxLayout(orientation='vertical')
        
        # Add the live camera preview
        self.camera = Camera(play=True, resolution=(640, 480))
        layout.add_widget(self.camera)
        
        # Add a big button at the bottom to snap the photo
        self.capture_btn = Button(text="Capture Document", size_hint=(1, 0.2))
        layout.add_widget(self.capture_btn)
        
        return layout

if __name__ == '__main__':
    ScannerApp().run()
