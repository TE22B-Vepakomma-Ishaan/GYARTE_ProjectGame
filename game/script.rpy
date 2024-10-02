# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Host = Character("Host")
define Yessica = Character("Yessica")

image Yessica default = "Yessica_default@3.png"
image Yessica happy = "Yessica_happy@3.png"
image Yessica pensive = "Yessica_pensive@3.png"


image cafe = "Cafe_templateBG.jpg"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene cafe

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Yessica default

    # These display lines of dialogue.

    Yessica "default"

    show Yessica happy

    Yessica "happy"

    show Yessica pensive

    Yessica "Pensive"

    # This ends the game.

    return
