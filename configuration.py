import mineclone as mc

def askConfigValues():
    print("Mineclone " + mc.version + "configuration")
    print("")
    print("Would you like to use default values?")
    yesorno = input("y or n")

    if yesorno.casefold():
        print("Using default values")
    else:
        print("Using custom values")
