import os
from pathlib import Path

import media_control.settings as settings

def init():
    home = str(Path.home())

    if Path(settings.config_path).is_file():
        return
    
    Path(settings.config_dir).mkdir(parents=True, exist_ok=True)
    Path(settings.config_path).touch()

    conf = settings.conf

    if not conf.has_section('app_data'):
        conf.add_section('app_data')
        conf.set('app_data', 'INITED', 'FALSE')
        conf.set('app_data', 'BEFORE_HAND_COMMAND', '')
        conf.set('app_data', 'VIDEO_PLAY_COMMAND', 'vlc ')
        conf.set('app_data', 'PREVIOUS_EPISODE', '')
        conf.set('app_data', 'CURRENT_SERIES_DIR', '')
        with open(settings.config_path, 'w') as config_file:
            conf.write(config_file)
