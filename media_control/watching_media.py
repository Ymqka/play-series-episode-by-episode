import sqlite3
import os
import sys

import media_control.settings as settings

class WatchingMedia:
    def __init__(self):
        self._connection = sqlite3.connect(settings.db_path)
        self._conf = settings.conf

        self._curr = self._connection.cursor()
        self._curr.execute("create table if not exists watched(name TEXT)")

    def play_episode(self, path_to_episode):
        curr = self._curr

        os.system("i3-msg 'workspace 7: VLC'")
        os.system("vlc --fullscreen " + path_to_episode)

        return

    def play_previous_episode(self):
        prev_episode = self.get_previous_episode()
        
        current_series_dir = self._conf.get('app_data', 'CURRENT_SERIES_DIR')

        self.play_episode(os.path.join(current_series_dir,prev_episode))

        return


    def play_next_episode(self):
        curr = self._curr

        current_series_dir = self._conf.get('app_data', 'CURRENT_SERIES_DIR')

        next_episode = self.get_next_episode()

        self.play_episode(os.path.join(current_series_dir,next_episode))

        curr.execute("insert into watched(name) values(?)", [next_episode])
        
        self._connection.commit()

        return next_episode

    def get_previous_episode(self):
        return self._conf.get('app_data', 'PREVIOUS_EPISODE')

    def get_next_episode(self):
        curr = self._curr

        curr.execute("select name from watched")
        watched_episodes = [ item[0] for item in curr.fetchall() ]

        current_series_dir = self._conf.get('app_data', 'CURRENT_SERIES_DIR')

        all_episodes = os.listdir(current_series_dir)

        not_watched = [ item for item in all_episodes if item not in watched_episodes ]
        not_watched.sort()

        if len(not_watched) == 0:
            print("Out of episodes")
            sys.exit(1)

        return not_watched[0]


    def __del__(self):
        self._connection.close()