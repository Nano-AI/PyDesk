import platform
from datetime import datetime
from typing import Dict
import json

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
