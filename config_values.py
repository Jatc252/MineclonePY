"""
Mineclone - config_values.py
v0.0.2 beta 1

Brought to you by Jatc251
https://jatc251.com

GitHub: https://github.com/Jatc252/Mineclone
"""

import mineclone

# User inputted variables in their string form to be integerised
global tpsString
global flySpeedString
global gravityString
global playerHeightString
global walkSpeedString
global worldSizeString
global jumpHeightString

# Variables to be filled with the integerised versions of their string counterparts
global tpsInt
global flySpeedInt
global gravityInt
global playerHeightInt
global walkSpeedInt
global worldSizeInt
global jumpHeightInt

def askConfigValues():
    print("Mineclone " + mineclone.version + "configuration")
    print("")
    print("Would you like to use default values?")
    yesorno = input("y or n")

    if yesorno.casefold():
        print("Using default values")
    else:
        print("Using custom values")
        customValues()


def customValues():
    print("Please set your chosen values. Input 'd' for default values")
    print(" ")

    while True:
        try:
            tpsString = input("TPS? ")
            if tpsString.casefold() == 'd':
                tpsString = 120
            tpsInt = int(tpsString)
            break
        except ValueError:
            print(tpsString + " is not a valid number.")
    print("TPS is now: ", tpsInt)
    print(" ")

    while True:
        try:
            walkSpeedString = input("Walk Speed? ")
            if walkSpeedString.casefold() == 'd':
                walkSpeedString = 5
            walkSpeedInt = int(walkSpeedString)
            break
        except ValueError:
            print(walkSpeedString + " is not a valid number.")
    print("Walk Speed is now: ", walkSpeedInt)
    print(" ")

    while True:
        try:
            flySpeedString = input("Fly Speed? ")
            if flySpeedString.casefold() == 'd':
                flySpeedString = 15
            flySpeedInt = int(flySpeedString)
            break
        except ValueError:
            print(flySpeedString + " is not a valid number.")
    print("Fly Speed is now: ", flySpeedInt)
    print(" ")

    while True:
        try:
            gravityString = input("Gravity? ")
            if gravityString.casefold() == 'd':
                gravityString = 20
            gravityInt = int(gravityString)
            break
        except ValueError:
            print(gravityString + " is not a valid number.")
    print("Gravity is now: ", gravityInt)
    print(" ")

    while True:
        try:
            playerHeightString = input(
                "Player Height? ")
            if playerHeightString.casefold() == 'd':
                playerHeightString = 2
            playerHeightInt = int(playerHeightString)
            break
        except ValueError:
            print(playerHeightString + " is not a valid number.")
    print("Player Height is now: ", playerHeightInt)
    print(" ")

    while True:
        try:
            worldSizeString = input("World Size? ")
            if worldSizeString.casefold() == 'd':
                worldSizeString = 80
            worldSizeInt = int(worldSizeString)
            break
        except ValueError:
            print(worldSizeString + " is not a valid number.")
    print("World Size is now: ", worldSizeInt)
    print(" ")

    while True:
        try:
            jumpHeightString = input("Jump height? ")
            if jumpHeightString.casefold() == 'd':
                jumpHeightString = 1
            else:
                jumpHeightInt = int(jumpHeightString)
            break
        except ValueError:
            print(jumpHeightString + " is not a valid number.")
    print("Jump Height is now: ", jumpHeightInt)
    print(" ")


def printConfig():
    print("Configuration: ")
    print("TPS: ", tpsInt)
    print("World Size: ", worldSizeInt)
    print("Gravity: ", gravityInt)
    print("Fly Speed: ", flySpeedInt)
    print("Walk Speed: ", walkSpeedInt)
    print("Jump Height is", jumpHeightInt)
    print("Player Height is", playerHeightInt)
