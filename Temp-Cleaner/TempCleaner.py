import os
import pathlib
import time

# store colors
def COLOR(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"



# make a list that stores every path
Paths = []
UsrInput = None
global ActionOnBoot #Make global
ActionOnBoot = "Run-And-Close" #Run and Close or Run and Show Menu

#functions
def Only_Y_and_N():
    UsrInput = None
    print(COLOR(255,0,0,'Please only type "y" or "n"'))
    time.sleep(0.5)
def No_Input_Detected():
    UsrInput = None
    print(COLOR(255,0,0,"No input detected, please try again"))
    time.sleep(0.5)
# main
print(COLOR(255,0,0,"-- Welcome to TempCleaner --"))
time.sleep(0.01)
print(COLOR(245,0,10,"TempCleaner is a simple programm"))
time.sleep(0.01)
print(COLOR(235,0,20,"Written in Python that"))
time.sleep(0.01)
print(COLOR(225,0,30,"Cleans temporary files on every boot!"))
time.sleep(0.01)
print(COLOR(215,0,40,"To Start you first have to define"))
time.sleep(0.01)
print(COLOR(205,0,50,"A folder that includes your temporary files"))
time.sleep(0.01)
print(COLOR(195,0,60,"you want to clean."))
time.sleep(0.01)
print(COLOR(185,0,70,"Do you want to do that?"))

while True:
    time.sleep(0.01)
    print(COLOR(175,0,80,"Select a Path to be cleared? [Y/N]"), end=" ")
    UsrInput = input().lower()
    if UsrInput and UsrInput == "y":
        UsrInput = None #reset UsrInput for next use
        break #if User inputed y, jump to line 39 (and break the loop)
    elif UsrInput == "":
        print("No input, please try again")
    elif UsrInput == "n":
        UsrInput = None
        break #if User inputed n, jump to line 39 (and break the loop)
    elif UsrInput != "n" or UsrInput != "y" and UsrInput != "":
        print('Please only type "y" or "n"')
    else:
        print("unknown error, please try again")
time.sleep(0.01)
print(COLOR(255,0,0,"WARNING: every file in the path you input will be Deleted!"))


while True:
    time.sleep(0.01)
    print(COLOR(155,0,100,"Are you sure you want to continue? [Y/N]"), end=" ")
    UsrInput = input().lower()
    if UsrInput and UsrInput == "y":
        UsrInput = None
        break #if User inputed y, jump to line 68 (and break the loop)
    elif UsrInput == "":
        No_Input_Detected()
    elif UsrInput == "n":
        UsrInput = None
        break #if User inputed n, jump to line 68 (and break the loop)
    elif UsrInput != "n" or UsrInput != "y" and UsrInput != "":
        Only_Y_and_N()
    else:
        print(COLOR(255,0,0,"Unknown Error, please try again"))

def Menu():
    global ActionOnBoot  #Make global to be able to change it in the settings
    time.sleep(0.01)
    os.system('cls' if os.name == 'nt' else 'clear') #Clear terminal (cross platform)
    print(COLOR(145,0,110,"-- TempCleaner Menu --"))
    time.sleep(0.01)
    print(COLOR(135,0,120,"1) Add Path"))
    time.sleep(0.01)
    print(COLOR(125,0,130,"2) Delete Path"))
    time.sleep(0.01)
    print(COLOR(115,0,140,"3) List Paths"))
    time.sleep(0.01)
    print(COLOR(105,0,150,"4) Settings"))
    time.sleep(0.01)

    print(COLOR(95,0,160,"Please select an option: "), end=" ")
    UsrInput = input().lower()
    while True:
        if UsrInput and UsrInput == "1":
            UsrInput = None
            while True:
                print(COLOR(85,0,170,"Please input a Path: "), end=" ")
                UsrInput = input()
                if os.path.exists(UsrInput) and os.path.isdir(UsrInput):
                    Paths.append(UsrInput)
                    print(COLOR(75,0,180,"Path added!"))
                    UsrInput = None
                    break
                elif UsrInput == "":
                    No_Input_Detected()
                elif not os.path.exists(UsrInput):
                    print(COLOR(255,0,0,"Path does not exist, please try again or type 'Cancel' to go back"))
                elif not os.path.isdir(UsrInput):
                    print(COLOR(255,0,0,"This is not a directory, please try again or type 'Cancel' to go back"))
                elif UsrInput and UsrInput.lower() == "cancel":
                    UsrInput = None
                    break
                else:
                    print(COLOR(255,0,0,"Unknown Error, please try again"))
            break
        elif UsrInput and UsrInput == "2":
            UsrInput = None
            while True:
                print(COLOR(65,0,190,"Please input the Path you want to delete: "), end=" ")
                UsrInput = input()
                if UsrInput in Paths:
                    Paths.remove(UsrInput)
                    print(COLOR(55,0,200,"Path removed!"))
                    UsrInput = None
                    break
                elif UsrInput == "":
                    No_Input_Detected()
                elif UsrInput not in Paths:
                    print(COLOR(255,0,0,"Path not in list, please try again or type 'Cancel' to go back"))
                elif UsrInput and UsrInput.lower() == "cancel":
                    UsrInput = None
                    break
                else:
                    print(COLOR(255,0,0,"Unknown Error, please try again"))
            break
        elif UsrInput and UsrInput == "3":
            UsrInput = None
            if len(Paths) == 0:
                print(COLOR(45,0,210,"No paths defined yet!"))
            else:
                print(COLOR(35,0,220,"Defined Paths:"))
                for p in Paths:
                    print(COLOR(25,0,230,p))
            break
        elif UsrInput and UsrInput == "4":
            UsrInput = None
            print(COLOR(15,0,240,"-- Avaiable Settings --"))
            print(COLOR(5,0,250,"1) Action On Boot"))
            print(COLOR(0,0,255,"2) Recycle or Delete"))
            print(COLOR(0,0,255,"3) Auto or Manual"))
            print(COLOR(0,0,255,"4) Every X boots"))
            print(COLOR(0,0,255,"5) Back to Menu"))
            while True:
                print(COLOR(0,0,255,"Please select an option: "), end=" ")
                UsrInput = input().lower()
                if UsrInput and UsrInput == "1":
                    UsrInput = None
                    print(COLOR(0,0,255,"Default Action ="), end=" ")
                    print(COLOR(0,255,0,ActionOnBoot))
                    print(COLOR(0,0,255,"Change to Run and show menu? [Y/N]" if ActionOnBoot != "Run-And-Show-Menu" else "Change to Run and Close [Y/N]"), end=" ")
                    UsrInput = input().lower()
                    if UsrInput and UsrInput == "y":
                        print(COLOR(0,0,255,"Action changed to Run and show menu!" if ActionOnBoot != "Run-And-Show-Menu" else "Action changed to Run and close!"))
                        ActionOnBoot = "Run-And-Show-Menu"
                        time.sleep(0.5)
                    elif UsrInput and UsrInput == "n":
                        time.sleep(0.5)
                        if ActionOnBoot == "Run-And-Close":
                            print(COLOR(0,0,255,"Action remains Run and close!"))
                        else:
                            print(COLOR(0,0,255,"Action changed to Run and close!" if ActionOnBoot != "Run-And-Close" else "Action changed to Run and show menu!"))
                        ActionOnBoot = "Run-And-Close"
                    elif UsrInput == "":
                        No_Input_Detected()
                    else:
                        Only_Y_and_N()
                    time.sleep(0.5)
                    Menu()
                    break
                elif UsrInput and UsrInput == "2":
                    UsrInput = None
                    print(COLOR(0,0,255,"Not implemented yet!"))
                    Menu()
                    break
                elif UsrInput and UsrInput == "3":
                    UsrInput = None
                    print(COLOR(0,0,255,"Not implemented yet!"))
                    Menu()
                    break                    
                elif UsrInput and UsrInput == "4":
                    UsrInput = None
                    print(COLOR(0,0,255,"Not implemented yet!"))
                    Menu()
                    break
                elif UsrInput and UsrInput == "5":
                    UsrInput = None
                    Menu()
                    break
                elif UsrInput == "":
                    UsrInput = None #to be sure it's set to None
                    No_Input_Detected()
                    Menu()
                    break
                elif UsrInput != "1" or UsrInput != "2" or UsrInput != "3" or UsrInput != "4" or UsrInput != "5" and UsrInput != "":
                    print(COLOR(255,0,0,'please only type "1", "2", "3", "4" or "5"'))
                    UsrInput = None
                    Menu()
                    break
                else:
                    print(COLOR(255,0,0,"Unknown Error, please try again"))
                    Menu()
                    break
        else:
            print(COLOR(255,0,0,'please only type "1", "2", "3" or "4"'))
            time.sleep(0.5)
            UsrInput = None
            Menu()
            break
while True:
    input(COLOR(0,0,255,("Press 'Enter' To Continue..")))
    time.sleep(0.8)
    Menu()