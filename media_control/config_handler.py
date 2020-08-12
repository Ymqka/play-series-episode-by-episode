import sqlite3
import configparser
import os

import media_control.settings as settings

class ConfigHandler:
    def __init__(self):
        self._path_to_conf = settings.config_path
        self._conf = configparser.ConfigParser()

        self._conf.read(self._path_to_conf)

    def write(self):
        conf_handler = open(self._path_to_conf, 'w')

        self._conf.write(conf_handler)

        with open(self._path_to_conf, 'w') as config_file:
            self._conf.write(config_file)

        return

    def show(self):
        conf = self._conf

        for section in conf.sections():
            for(key, val) in conf.items(section):
                print(key + '=' + val)

        return

    def update_previous_episode(self, latest_episode):
        conf = self._conf

        conf.set('app_data', 'PREVIOUS_EPISODE', latest_episode)

        return

    def update_series_dir(self, path_to_dir):
        conf = self._conf

        if path_to_dir == '.':
            path_to_dir = ''


        path_to_series_dir = os.path.join(os.getcwd(),path_to_dir)

        conf.set('app_data', 'INITED', 'TRUE')
        conf.set('app_data', 'CURRENT_SERIES_DIR', path_to_series_dir)

        return

    def check_if_inited(self):
        if self._conf.get('app_data', 'INITED') == 'FALSE':
            print('APP NOT INITED, EXITING\nto init app type "medcon --set {path_to_series_dir}"')
            sys.exit(1)
