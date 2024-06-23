import pygame
import time
import threading
import keyboard
import os

DIR_PATH: str = "musics"
KEY_BINDS: str = """&é"'(-è_çàazertyuioipqsdfghjklmwxcvbn"""

SELECT_MUSIC_MESSAGE: str = "APPUYEZ SUR UNE TOUCHE POUR LANCER LA MUSIQUE CORRESPONDANTE ! \n"
QUIT_MESSAGE: str = "Appuyez sur 'Echap' pour quitter le programme. \n"
PAUSE_MESSAGE: str = "Appuyez sur 'Espace' pour mettre en pause la musique en cours. \n"
STOP_MESSAGE: str = "Appuyez sur 'Entrée' pour arrêter la musique en cours. \n"


def min(a: int, b: int) -> int:
    if a < b:
        return a
    return b

def play_music(mp3_path: str) -> None:

    pygame.mixer.init()
    pygame.mixer.music.load(mp3_path)
    pygame.mixer.music.play()    

if __name__ == "__main__":
        
    dir: list = os.listdir(DIR_PATH)
    music_dict: dict = {}
    music_list_message: str = ""
    on_pause: bool = False

    for i in range(min(len(dir), len(KEY_BINDS))):
        music_dict[KEY_BINDS[i]] = dir[i]
        music_list_message += f"{KEY_BINDS[i]} - {dir[i]}\n"
        
    display_message: str = SELECT_MUSIC_MESSAGE + music_list_message + QUIT_MESSAGE + PAUSE_MESSAGE + STOP_MESSAGE

    print(display_message)
        
    while True:
        
        # checking if the user wants to quit the program
        if (keyboard.is_pressed('esc')):
            print("Fermerture du programme...")
            time.sleep(2)
            break
        
        # checking if the user wants to pause the music
        if (keyboard.is_pressed('space')):
            
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
                print("Musique en pause. \n")
                on_pause = True

            elif on_pause:
                pygame.mixer.music.unpause()
                print("Musique reprise. \n")
                on_pause = False

            else:
                continue

            time.sleep(0.3)
            print(display_message)
        
        # checking if the user wants to stop the music
        if keyboard.is_pressed('enter'):
            if (pygame.mixer.music.get_busy()):
                pygame.mixer.music.stop()
                print("Musique arrêtée.")
                time.sleep(0.3)
                print(display_message)
        
        # checking if the user wants to play a music
        if ([key for key in music_dict.keys() if keyboard.is_pressed(key)] != []):
            
            # getting the key pressed to obtain the music to play
            key: chr = [key for key in music_dict.keys() if keyboard.is_pressed(key)][0]
            value: str = music_dict[key]
            
            # killing the music thread
            music_tread = threading.Thread(target=play_music, args=(DIR_PATH+'/'+value,))

            # starting the music thread
            music_tread.start()
            print(f"Musique {music_dict[key]} lancée !\n")
            
            time.sleep(1)
            print(display_message)