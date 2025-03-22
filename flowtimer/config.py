import os
import configparser
from pathlib import Path

CONFIG_PATH = os.path.expanduser("~/.flowtimerrc")

def load_config():
    config = configparser.ConfigParser()
    config.read_dict({
        "settings": {
            "work": "25",
            "break": "5",
            "sound_alert": ""
        }
    })
    
    if Path(CONFIG_PATH).exists():
        config.read(CONFIG_PATH)
    
    return config["settings"]