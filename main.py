from kivy.app import App
from kivy.uix.label import Label

class ScannerApp(App):
    def build(self):
        # A simple placeholder text for our main screen
        return Label(text='Document Scanner Ready')

if __name__ == '__main__':
    ScannerApp().run()
