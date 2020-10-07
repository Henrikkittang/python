import random
import os
import pygame
pygame.init()

"""Play mode"""
# SPACE - pause
# r - play song / restart
# s - shuffle current list
# right arrow - next song
# left arrow - previous song
# q - quit to select mode

"""Select mode"""
# up arrow - last list
# down arrow - next list
# e - select list

wn = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Music player")

song_paths = os.listdir("songs")
audio = pygame.mixer.music


def select_win():
    global select_list, songs
    wn.fill((0, 0, 0))

    # Draws the paths on the screen
    for idx, path in enumerate(song_paths):
        if idx == path_index:
            text = font.render(path, 1, (255, 255, 0))
        else:
            text = font.render(path, 1, (255, 255, 255))
        wn.blit(text, (100, idx*25 + 120))

    # check if a path has been selected
    # if so then make a new list of songs and draw the main window
    if path_selected != None:
        songs = os.listdir("songs/" + path_selected)
        for idx, song in enumerate(songs):
            songs[idx] = "songs/" + path_selected + "/" + song
        select_list = False

    pygame.display.update()


def main_win():
    wn.fill((0, 0, 0))

    idx_text = font.render("Number: " + str(song_idx + 1) + "/" + str(len(songs)), 1, (255, 255, 255))
    wn.blit(idx_text, (100, 120))

    cur_song = songs[song_idx].split("/")
    cur_song_text = font.render("Title: " + str(cur_song[2]), 1, (255, 255, 255))
    cur_list_text = font.render("List: " + str(cur_song[1]), 1, (255, 255, 255))

    wn.blit(cur_song_text, (100, 150))
    wn.blit(cur_list_text, (100, 180))

    pygame.display.update()


path_selected = None
path_index = 0
select_list = True
songs = []
font = pygame.font.SysFont("comicsans", 30, True)
song_idx = -1
isPlay = True
run = True
while run:
    pygame.time.delay(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Pauses
    if keys[pygame.K_SPACE]:
        if isPlay == True:
            audio.pause()
            isPlay = False
        else:
            audio.unpause()
            isPlay = True

    # Restarts or starts playing selected song
    if keys[pygame.K_r]:
        audio.load(songs[song_idx])
        pygame.mixer.music.play(1)

    # Shuffles the list
    if keys[pygame.K_s]:
        random.shuffle(songs)
        audio.load(songs[song_idx])
        pygame.mixer.music.play(1)

    # Selects next song
    if (keys[pygame.K_RIGHT] and song_idx < len(songs) - 1) or (audio.get_busy() != 1 and select_list == False):
        song_idx += 1
        audio.load(songs[song_idx])
        pygame.mixer.music.play(1)
    # Selects previous song
    elif keys[pygame.K_LEFT] and song_idx > 0 and select_list == False:
        song_idx -= 1
        audio.load(songs[song_idx])
        pygame.mixer.music.play(1)

    # Skips 5 seconds forward
    if keys[pygame.K_d]:
        cur_pos = audio.get_pos()
        new_pos = (cur_pos / 1000) + 5
        audio.set_pos(new_pos)
    # Skips 5 seconds backwards
    elif keys[pygame.K_a] and audio.get_pos() > 5000:
        cur_pos = audio.get_pos()
        new_pos = (cur_pos / 1000) - 5
        audio.set_pos(new_pos)

    # Quits the current list and draws the select window
    if keys[pygame.K_q]:
        select_list = True
        songs.clear()
        path_selected = None
        audio.stop()
        song_idx = -1

    # Selects next path
    if keys[pygame.K_UP] and path_index > 0:
        path_index -= 1
    # selects previous path
    elif keys[pygame.K_DOWN] and path_index < len(song_paths) - 1:
        path_index += 1
    # Selects the current path
    elif keys[pygame.K_e]:
        path_selected = song_paths[path_index]

    if select_list == True:
        select_win()
    else:
        main_win()
