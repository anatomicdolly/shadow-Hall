# Write your code here :-)

print("hello young one. \n")
print("welcome to this text adventure. \n")
print("written in python 3, this is .... \n")
print(" THE SHADOW HALL")
print("            by chase")

name = input("let's start with your name ... what is it? \n")

print(" hello " + name)
print("your adventure begins in a dark room,")
print("you can see nothing but faint lines on the floor,")
print("from a dim light cascading through the bars of a cell.")

print("what would you do?")
print(" 1. walk around the cell")
print(" 2. look for torches")
print(" 3. yell for help")
choices = input()
if choices == "1":
    print("it's too dark to see... are you sure?")
    print(" 1. yes")
    print(" 2. no")
    choices = input()
    if choices == "1":
        print(" you tripped and broke your neck..")
        print(" GAME OVER ")
    if choices == "2":
        print("you decide not to explore yet..")
        print("what would you do?")
        print(" 1. look for torches.")
        print(" 2. yell for help")
        choices = input()
        if choices == "1":
            print("you look around your imediate location, you didn't find a torch, but you found a small stone.")
            print("you tap the stone on the ground below you, and it sparks, lighting up a small area around you for a brief moment")
            print(" you may now use 'spark' to get your barrings briefly.")
            print("what would you do now?")
            print(" 1. yell for help")
            print(" 2. spark")
            choices = input()
            if choices == "1":
                print("you shout for someone, anyone, hoping they would answer...")
                print(" 'hello young one...' ")
                print(" CHAPTER 1 COMPLETE ")
                print(" more to come!")
            if choices == "2":
                print("you got your bearings!")
                print("you decide to call for help hoping someone will answer.")
                print(" '...hello child...' ")
                print(" CHAPTER 1 COMPLETE ")
                print(" more to come! ")
        if choices == "2":
            print(" you shout for someone , anyone, hoping they would answer...")
            print("there was no answer...")
            print(" you decide to look around your imediate location, you didn't find any torches, but you found a small stone.")
            print("you tap the stone on the ground below you, and it sparks, lighting up a small area around you for a brief moment.")
            print(" you may now use 'spark' to get your bearings briefly.")
            print(" you decide to yell for help one more time.")
            print(" 'hello young one...' ")
            print(" CHAPTER 1 COMPLETE ")
            print(" more to come!")

if choices == "2":
    print(" you look around your imedtiate location, you didn't find a torch, but you found a small stone.")
    print("you tap the stone on the ground below you, and it sparks, lighting up a small area around you for a brief moment")
    print(" you may now use 'spark' to get your barrings briefly.")
    print(" now what?")
    print(" 1. walk around cell")
    print(" 2. ask for help")
    choices = input()
    if choices == "1":
        print("would you like to use spark?")
        print(" 1. yes")
        print(" 2. no")
        choices = input()
        if choices == "1":
            print("you fumble around thinking you saw something shine back at you.")
            print("you found a small metal nail, it seems to be a newer material than what the rest of the cell is..")
            print("you put the nail in your pocket.")
            print(" you decide to yell for help")
            print(" 'hello young one...' ")
            print(" CHAPTER 1 COMPLETE ")
            print("more to come! ")
    if choices == "2":
        print(" you shout hoping someone will hear your call...")
        print(" '...hello child...' ")
        print(" CHAPTER 1 COMPLETE ")
        print(" more to come! ")

if choices == "3":
    print("you shout hoping someone would hear you.")
    print(" you don't hear a response...")
    print("now what?")
    print(" 1. walk around the cell.")
    print(" 2. look for torches")
    choices = input()
    if choices == "1":
        print(" are you sure?")
        print(" 1. yes")
        print(" 2. no")
        choices = input()
        if choices == "1":
            print(" you fell and broke your neck.")
            print(" GAME OVER ")
        if choices == "2":
            print("you decide not to not explore yet..")
            print(" you decide to look for torches.")
            print(" you didn't find any.")
            print(" but you did find a small stone, tapping it on the ground generates a spark, lighting a small area for a brief moment")
            print("you can now use 'spark' to to get your bearings briefly")
            print(" now what?")
            print(" 1. walk around the cell")
            print(" 2. 'spark' ")
            print(" 3. give up. ")
            choices = input()
            if choices == "1":
                print("you fall and break your neck.")
                print(" GAME OVER ")

            if choices == "2":
                print("you've got your bearings!")
                print(" 1. walk around the cell")
                print(" 2. give up")
                choices = input()
                if choices == "1":
                    print("you find a small metal nail.")
                    print("you put it in your pocket")
                    print(" 1 ask for help")
                    print(" 2. give up")
                    choices = input()
                    if choices == "1":
                        print("you shout hoping someone can hear you")
                        print(" '...hello young one...' ")
                        print(" CHAPTER 1 COMPLETE ")
                        print(" more to come! ")

                    if choices == "2":
                        print(" the shadows took you")
                        print(" never surrender!")
                        print(" GAME OVER ")

            if choices == "3":
                print("the shadows took you.")
                print(" never surrender!")
                print(" GAME OVER ")

    if choices == "2":
        print("you look around your imediate area for torches.")
        print(" you didn't find any.")
        print(" you did find a small stone.")
        print(" when you tap the stone on the ground it creates a spark, lighing the area around you for a brief moment.")
        print(" you can now use 'spark' to get your bearings briefly.")
        print(" now what?")
        print(" 1. walk around the cell.")
        print(" 2. ask for help")
        choices = input()
        if choices == "1":
            print(" would you like to use spark?")
            print(" 1. yes")
            print(" 2. no")
            choices = input()
            if choices == "1":
                print(" you got your bearings!")
                print(" you found a metal nail")
                print(" you put the nail in your pocket.")
                print(" you decide to ask for help.")
                print(" you shout hoping someone will answer your call")
                print(" '....hello child...' ")
                print(" CHAPTER 1 COMPLETE")
                print(" more to come")

            if choices == "2":
                print(" you fell and broke your neck.")
                print(" GAME OVER ")

        if choices == "2":
            print(" you shout hoping someone will hear your call")
            print(" '....hello child...' ")
            print(" CHAPTER 1 COMPLETE ")
            print(" more to come! ")