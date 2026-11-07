
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.clearcolor = (0.04, 0.07, 0.13, 1)

class RemoteApp(App):

    def build(self):
        root = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=12
        )

        title = Label(
            text="LG SMART REMOTE",
            font_size=25,
            size_hint_y=None,
            height=65
        )
        root.add_widget(title)

        self.status = Label(
            text="تلویزیون متصل نیست",
            size_hint_y=None,
            height=40
        )
        root.add_widget(self.status)

        self.ip = TextInput(
            hint_text="IP تلویزیون",
            multiline=False,
            size_hint_y=None,
            height=50
        )
        root.add_widget(self.ip)

        connect = Button(
            text="جستجوی تلویزیون",
            size_hint_y=None,
            height=55
        )
        connect.bind(on_press=self.search_tv)
        root.add_widget(connect)

        buttons = [
            ["▲"],
            ["◀", "OK", "▶"],
            ["▼"],
            ["VOL -", "HOME", "VOL +"],
            ["CH -", "BACK", "CH +"]
        ]

        for line in buttons:
            row = BoxLayout(
                size_hint_y=None,
                height=65,
                spacing=8
            )

            for name in line:
                btn = Button(text=name)
                btn.bind(on_press=self.command)
                row.add_widget(btn)

            root.add_widget(row)

        return root

    def search_tv(self, instance):
        self.status.text = "آماده جستجوی تلویزیون"

    def command(self, instance):
        self.status.text = (
            "فرمان انتخاب شده: " + instance.text
        )

RemoteApp().run()
