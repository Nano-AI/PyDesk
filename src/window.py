import platform
import threading
from datetime import datetime
from typing import Dict

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from src.GetWeather import *

SettingsPath = "./config/settings.json"


def get_time() -> str:
    with open(SettingsPath) as timeF:
        data = json.load(timeF)
        return datetime.now().strftime(data['time-settings']['format'])


def get_platform() -> str:
    return platform.system()


def get_date() -> Dict[str, int]:
    with open(SettingsPath) as dateF:
        data = json.load(dateF)
        return {
            "day": int(datetime.today().strftime('%d')),
            "month": int(datetime.today().strftime('%m')),
            "year": int(datetime.today().strftime('%Y')),
            "custom-date": str(datetime.today().strftime(data['date-settings']['format']))
        }


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        weather_setup()

        self.time = QLabel(self)
        self.date = QLabel(self)
        self.today_weather = QLabel(self)

        self.add_styles()
        self.current_date = get_date()

        self.date.setFont(QFont("Arial, Helvetica, sans-serif", 34))
        self.time.setFont(QFont("Arial, Helvetica, sans-serif", 20))
        self.today_weather.setFont(QFont("Arial, Helvetica, sans-serif", 18))

        # print(self.current_date['custom-date'])
        self.date.setText(str(self.current_date['custom-date']))
        self.today_weather.setText(get_weather())
        self.today_weather.adjustSize()

        self.make_window_full_undecorated()

        self.time.setText(get_time())

        self.show()
        self.update_time()

    def update_time(self):
        threading.Timer(1.0, lambda: self.update_time()).start()
        self.time.setText(get_time())
        date = get_date()
        self.time.adjustSize()
        if date['day'] >= self.current_date['day'] or date['month'] >= self.current_date['month'] or date['year'] >= \
                self.current_date['year']:
            self.current_date = date
            self.date.setText(self.current_date['custom-date'])
            self.date.adjustSize()
        del date

    def make_window_full_undecorated(self):
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)
        with open(SettingsPath) as fullScreenInfo:
            data = json.load(fullScreenInfo)
            self.setStyleSheet(
                f"border-image: url({data['background-url']}) 0 0 0 0 stretch stretch;"
                # "background-color: black;"
            )
            self.time.setStyleSheet(
                f"color: rgb({data['time-settings']['color']}); background: transparent; border-image: none"
            )
            self.date.setStyleSheet(
                f"color: rgb({data['date-settings']['color']}); background: transparent; border-image: none"
            )
            self.today_weather.setStyleSheet(
                f"color: rgb({data['date-settings']['color']}); background: transparent; border-image: none"
            )

    def add_styles(self):
        self.date.move(25, 25)
        self.time.move(25, 75)
        self.today_weather.move(1000, 25)
