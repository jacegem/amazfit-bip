import webbrowser

from PyQt5.QtWidgets import QPushButton, QSizePolicy


class DonateButton(QPushButton):
    def __init__(self, dollar):
        title = '${}'.format(dollar)
        super().__init__(title)
        super().setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        super().clicked.connect(lambda: self.open_donate(dollar))

    def open_donate(self, dollar):
        webbrowser.open('https://paypal.me/payw/{}'.format(dollar))


class FullButton(QPushButton):
    def __init__(self, title):
        super().__init__(title)
        super().setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
