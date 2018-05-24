#!/usr/bin/env python3

"""
Extend the mpv
"""

import mpv
import os
import sys

DELETEKEY = 'r'         # add current file to list of files to be deleted and go to next
NEXTFILEKEY = 'k'       # keep current file and go to next
ACCEPTKEY = 'enter'     # delete all files selected so far and continue
FULLSCREENTOGGLE = 'f'
DIRNAME = os.path.join(os.path.dirname(__file__), 'files')

def view_files():

    player = mpv.MPV(autofit_larger='100%x95%',     # resize video if it's larger than W%xH% of the screen
                     reset_on_next_file='pause',    # reset pause status on next media in playlist
                     loop_file='inf',               # loop file in case of videos
                     input_default_bindings=True,
                     input_vo_keyboard=True)

    @player.on_key_press(DELETEKEY)
    def delete_file():
        to_delete.append(current_video)
        try:
            player.playlist_next()
        except SystemError:
            print('Playlist finished!')
            player.quit()

    @player.on_key_press(NEXTFILEKEY)
    def next_file():
        try:
            player.playlist_next()
        except SystemError:
            print("Playlist finished")
            # playlist finished
            player.quit()

    @player.on_key_press(ACCEPTKEY)
    def accept():
        print(ACCEPTKEY)
        delete_files(to_delete)

    @player.on_key_press(FULLSCREENTOGGLE)
    def fullscreen_toggle():
        print('fullscreen')
        player.fullscreen = not player.fullscreen

    player.fullscreen = True
    mediafiles = [os.path.join(DIRNAME, file) for file in os.listdir(DIRNAME) if os.path.isfile(os.path.join(DIRNAME, file))]
    player.playlist_append(mediafiles[-1])   # hack: last media is skipped, add it twice to make up for ite
    for video in mediafiles:
        player.playlist_append(video)

    player.playlist_pos = 0
    playlist_len = len(player.playlist)
    while True:
        current_video = player.playlist[player.playlist_pos]['filename']
        print("position: " + str(player.playlist_pos) + "/" +str(playlist_len-1))
        if player.playlist_pos >= playlist_len-1:
            print("reached end of playlist")
            break
        else:
            player.wait_for_playback()

def delete_files(filelist):
    for file in filelist:
        #print(file)
        try:
            os.remove(file)
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    to_delete = []
    view_files()
    print(to_delete)
    delete_files(to_delete)

