import os
import colorama
import subprocess

global play
play = False

lobby = True
global tdelay
tdelay = 0

class pipe:
    def __init__(self,x,y,pipe_type,alive):
        self.x = 0
        self.y = 0
        self.pipe_type = 0
        self.alive = True
class bird:
    def __init__(self,x,y,alive):
    



def render():
    global tdelay
    tdelay += 1
    if tdelay == 30:
        tdelay = 0
        apply_gravity()
        move()

def lobby():
    global play
    print("                                             ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print("                                             Welcome to Flappy Bird - TE!")
    print("                                             ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
    print("                                            Made by: DevXstyler - 26.1.2026")
    print("                                                        V0.0.1")
    print("\n                                           [1] Play")
    print("                                           [2] Stats")
    print("                                           [3] Credits")    
    print("                                           [4] Exit")
    usr_choice = input("\n                                         Enter Choice: ")
    usr_choice = int(usr_choice)
    if usr_choice == 1:
        play = True
if lobby:
    os.system("cls")
    lobby()

else:
    None
while True:
    while play:
        render()
    #os.system("cls")
