import threading
from playsound3 import playsound

# Play a sound from a local file
# playsound("sounds/benkirb-notification-sound-3-262896.mp3mp3", block=False) 

# def loop_background():
#     while True:
#         playsound("sounds/sergequadrado-robotic-loop-251861.mp3")

# def sound_background():
#     # Create and start the thread
#     loop_thread = threading.Thread(target=loop_background, name='backgroundMusicThread')
#     loop_thread.daemon = True # Allows the program to exit even if the thread is running
#     loop_thread.start()

def sound_intro():
    playsound("sounds/47313572-intro-sound-2-269294.mp3", block=False)

def sound_start_game():
    playsound("sounds/47313572-soft-startup-sound-269291.mp3", block=False)

def sound_message():
    playsound("sounds/supremetylewiss-message-13716.mp3", block=False) 

def sound_defeated():
    playsound("sounds/grimgravy-call-alert-strain-195737.mp3", block=False) 

def sound_win():
    playsound("sounds/benkirb-notification-sound-3-262896.mp3mp3", block=False) 