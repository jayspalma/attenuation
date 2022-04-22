from kivy.config import Config

Config.set("graphics", "resizable", False)


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.core.window import Window
import socket


class Attenuation(App):
    def build(self):
        self.title = "Attenuation Control Panel"
        Window.clearcolor = (0.25, 0.5, 0.73, 0.61)
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # # image widget
        self.window.add_widget(Image(source="merge2.png"))

        # label widget
        self.greeting = Label(
            text="What Value of Attenuation would you like (0 - 80)",
            font_size=25,
            color="#00FFCE",
        )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(
            multiline=False,
            padding_y=(20, 20),
            padding_x=(225, 20),
            size_hint=(1, 0.5),
            font_size=25,
        )

        self.window.add_widget(self.user)

        self.button = Button(
            text="SUBMIT",
            font_size=15,
            size_hint=(1, 0.5),
            bold=True,
            background_color="#00FFCE",
            border=(20, 20, 20, 20),
        )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        try:
            int(self.user.text)

            if int(self.user.text) <= 80 and int(self.user.text) >= 0:
                self.greeting.text = "Attenuation Set to " + self.user.text
                attennuation_value = self.user.text

                SERVER_IP = "172.19.73.92"
                PORT = 6969

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((SERVER_IP, PORT))
                s.send(bytes(attennuation_value, "utf-8"))

            else:
                self.greeting.text = (
                    "Value out of range: Please choose only between 0 - 80"
                )
        except:
            self.greeting.text = "Value Error: Please choose only between 0 - 80"


# run Attenuation App Class
if __name__ == "__main__":
    Attenuation().run()
