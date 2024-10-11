# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



define config.menu_include_disabled = False
define brittaniCheck = True
define yessicaCheck = True
define shalommCheck = True
define metAll = False




define player = Character("[playerName]")



define host = Character("Host")
define yessica = Character("Yessica")
define brittani = Character("Brittani")
define shalomm = Character("Shalomm")





image yessica = "Yessica_default@3.png"
image yessica happy = "Yessica_happy@3.png"
image yessica pensive = "Yessica_pensive@3.png"

image brittani = "Brittani@3.png"

image shalomm = "Shalomm@3.png"




image host = "merlin.png"

image cafe = "cafe_background.jpg"
image cafe2 = "cafe_bg2.jpg"

label start:


    scene cafe

    show merlin at right

    # host "Hi, welcome to Café [[name]'s Speed Dating Event! Please state your name to register!"

    

    # python:
    #     playerName = renpy.input("Please input name:", length=12)
    #     playerName = playerName.strip()

    
    # player "my name is [playerName]"



    hide merlin

    hide cafe with dissolve

    scene cafe2


    


       

    show yessica at right

    show shalomm

    show brittani at left

     
    label DateF_Options:
    
        python: 
                if ((yessicaCheck == False) and (shalommCheck == False) and(brittaniCheck== False)):
                    metAll = True
        menu DateF_selector:

            "who should i pick?"

            "brittani" if brittaniCheck:
                jump brittani_date
            "shalomm" if shalommCheck:
                jump shalomm_date
            "Yessica" if yessicaCheck:
                jump yessica_date
            "Proceed" if metAll:
                jump Second_DateF



                        
    

    return
