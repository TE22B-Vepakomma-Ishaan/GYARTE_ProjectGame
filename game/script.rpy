# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character("[playerName]")


define host = Character("Host")
define yessica = Character("Yessica")
define e = Character("Evernight")
define t = Character("Trissy")

image e = "evernight.png"
image t = "trissy@2.png"

image yessica default = "Yessica_default@3.png"
image yessica happy = "Yessica_happy@3.png"
image yessica pensive = "Yessica_pensive@3.png"

image host = "merlin.png"

image cafe = "cafe_background.jpg"
image cafe2 = "cafe_bg2.jpg"

label start:


    scene cafe

    show merlin at left

    host "Hi, welcome to Café [[name]'s Speed Dating Event! Please state your name to register!"

    # python:
    #     playerName = renpy.input("Please input name:", length=12)
    #     playerName = playerName.strip()

    
    # player "my name is [playerName]"

    # host "Welcome, [playerName]! Please wait inside, the event will begin shortly."

    hide merlin

    hide cafe with dissolve

    scene cafe2

    show yessica default at right

    show trissy

    show evernight at left

    e "hi"
    
    menu pick_Date:
        "who should i pick?"

        "Evernight":
            jump evernight_date
        "Trissy":
            jump trissy_date
        "Yessica":
            jump yessica_date
    

    return
