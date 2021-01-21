"""
Mineclone - old_config.py
v0.0.2 beta 1

Brought to you by Jatc251
https://jatc251.com

GitHub: https://github.com/Jatc252/Mineclone

This file is currently housing the old configuration code for mineclone.py

# Variables for the chosen values the user chooses
global tpsInput
global flySpeedInput
global gravityInput
global playerHeightInput
global walkSpeedInput
global worldSizeInput
global jumpHeightInput

# Integer version of the chosen values (for the code)
global int_flySpeed
global int_gravity
global int_jumpHeight
global int_playerHeight
global int_tps
global int_walkSpeed
global int_worldSize


# Asks user for configuration values for the world
def askForVariables():
    defaultYesNo = input("Would you like to use the default game configuration? (y/n) ")
    if defaultYesNo.casefold() == 'y':
        print("Using the default world configuration...")
    elif defaultYesNo == 'n':
        print("Please set your chosen values. Input 'd' for default values")
        print(" ")

        while True:
            try:
                tpsInput = input("TPS? ")
                if tpsInput.casefold() == 'd':
                    tpsInput = 120
                int_tps = int(tpsInput)
                break
            except ValueError:
                print(tpsInput + " is not a valid number.")
        print("TPS is now: ", int_tps)
        print(" ")

        while True:
            try:
                walkSpeedInput = input("Walk Speed? ")
                if walkSpeedInput.casefold() == 'd':
                    walkSpeedInput = 5
                int_walkSpeed = int(walkSpeedInput)
                break
            except ValueError:
                print(walkSpeedInput + " is not a valid number.")
        print("Walk Speed is now: ", int_walkSpeed)
        print(" ")

        while True:
            try:
                flySpeedInput = input("Fly Speed? ")
                if flySpeedInput.casefold() == 'd':
                    flySpeedInput = 15
                int_flySpeed = int(flySpeedInput)
                break
            except ValueError:
                print(flySpeedInput + " is not a valid number.")
        print("Fly Speed is now: ", int_flySpeed)
        print(" ")

        while True:
            try:
                gravityInput = input("Gravity? ")
                if gravityInput.casefold() == 'd':
                    gravityInput = 20
                int_gravity = int(gravityInput)
                break
            except ValueError:
                print(gravityInput + " is not a valid number.")
        print("Gravity is now: ", int_gravity)
        print(" ")

        while True:
            try:
                playerHeightInput = input(
                    "Player Height? ")
                if playerHeightInput.casefold() == 'd':
                    playerHeightInput = 2
                int_playerHeight = int(playerHeightInput)
                break
            except ValueError:
                print(playerHeightInput + " is not a valid number.")
        print("Player Height is now: ", int_playerHeight)
        print(" ")

        while True:
            try:
                worldSizeInput = input("World Size? ")
                if worldSizeInput.casefold() == 'd':
                    worldSizeInput = 80
                int_worldSize = int(worldSizeInput)
                break
            except ValueError:
                print(worldSizeInput + " is not a valid number.")
        print("World Size is now: ", int_worldSize)
        print(" ")

        while True:
            try:
                jumpHeightInput = input("Jump height? ")
                if jumpHeightInput.casefold() == 'd':
                    jumpHeightInput = 1
                else:
                    int_jumpHeight = int(jumpHeightInput)
                break
            except ValueError:
                print(jumpHeightInput + " is not a valid number.")
        print("Jump Height is now: ", int_jumpHeight)
        print(" ")

    else:
        askForVariables()


# Tells the user what the configuration variables are set to
def printConfig():
    print("Configuration: ")
    print("TPS: ", int_tps)
    print("World Size: ", int_worldSize)
    print("Gravity: ", int_gravity)
    print("Fly Speed: ", int_flySpeed)
    print("Walk Speed: ", int_walkSpeed)
    print("Jump Height is", int_jumpHeight)
    print("Player Height is", int_playerHeight)


askForVariables()
printConfig()


# comment out above functions till i get around to writing new one
int_tps = int(input("tps"))
int_worldSize = int(input("world size"))
int_gravity = int(input ("gravoity"))
int_flySpeed = int(input("fly spedd"))
int_walkSpeed = int(input("walk speld"))
int_jumpHeight = int(input("jump heioght"))
int_playerHeight = int(input("player height"))
"""