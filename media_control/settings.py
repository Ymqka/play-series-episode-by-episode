import os
from pathlib import Path
import configparser

home = str(Path.home())

config_dir  = os.path.join(home, '.config', 'medcon')
config_path = os.path.join(config_dir, 'config')
db_path     = os.path.join(config_dir, 'watched_db')

conf = configparser.ConfigParser()
conf.read(config_path)



