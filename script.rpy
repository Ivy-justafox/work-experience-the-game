# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# The script of the game goes in this file.

# Declare variables
default map_progress = 0

#Register the keyboard listener



screen key_listener():
    key "K_m" action If(
        map_open,
        [
            SetVariable("map_open", False),
            Stop("music"),
            If(
                previous_music is not None,
                Play("music", previous_music, loop=True)
            )
        ],
        [
            SetVariable("previous_music", renpy.music.get_playing("music")),
            SetVariable("map_open", True),
            Play("music", "the Drudgery of work.mp3", loop=True)
        ]
    )

    if map_open:
        use MapUI


label map:
    if map_progress == 0:
        
        jump call_mapUI
        

        # Put your map content here.
    else:
        pass

label acookingland:
    scene cooklandea
    show teaman
    
    menu unecessaryfemboy:
        "what":
            teaman "SEE? IT'S EASY"
            jump bcookingland
            
        "where are we?":
            teaman "WE CALL IT"
            teaman "WELL I CALL IT"
            teaman "COCKLANDEA"
            jump bcookingland

        "what happened?":
            teaman "WE USED THE SUPER EASY TO CODED MAP TO GET TO"
            teaman "COCKLANDEA!!"
            jump bcookingland



    

    


#label house1_pressed:
    #scene bg classroom
    #"House 1 was pressed!"
    #jump after_house_choice

define ovengirl = Character("Smart Gas Double Oven Slide-in Range with InstaView ProBake 2.0" )
define man = Character("manager Bob" )
define teaman = Character("the tea fairy")
define evilfade = Dissolve(45.0)


# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.



    "Hay you"

    "yeah you!"

    scene kitchen
    show man
    man "welcome to your new Internship!"


    man "yes yes"
  

    man "i know you MUST excited"
    man "but we have a job to do"

    man  "now, can you make tea?"
    man  "..."
    man  "of course you can!"
    man "so what your gonna do is"
    man  "MAKE"
    man  "ME"
    man  "TEA!"
    man  "."
    man ".."
    man  "..."
    man "you got that?"
    menu canyoumaketea:
        
        "Yes":
            jump youmaketea
            
        "No":
            play sound "sonic-exe-laugh.mp3"
            show man kill
            "DIE!"
            return

            #block of code to run
    label youmaketea:
        show man
        "manager Bob" "great! i'll Leave you to it"
        hide man
        ""
        "how do i "
        ""
        "make tea?"
        scene kitchen evil 
        play sound "god-is-coming.mp3"
        with evilfade
        scene kitchen
        show teaman
        # he only in all caps
        #only
        "the tea fairy" "HAY! HAY! HAY!"
        "the tea fairy" "I'M THE TEA FAIRY!"
        "the tea fairy" "I DON'T KNOW ABOUT YOU BUT I'M FEELING TEEEEARRIFIC"
        show teaman lafing
        "the tea fairy" "HE HE HE HA HE!"
        show teaman
        "the tea fairy" "I HIRED YOU DON'T KNOW HOW TO MAKE TEA!!!"
        "the tea fairy" "NOW WE CAN'T HAVE THAT CAN WE?"
        "the tea fairy" "can we"
        "the tea fairy" "SO THAT'S WHY YOU NEED ME!"
        "the tea fairy" "THE TEA FAIRYYYYYY!!!!!!!!!"
        "the tea fairy" "I'LL HLEP YOU! IT'S EASY"
        "the tea fairy" "OR SHOULD I SAY TEASY?"
        show teaman lafing
        "the tea fairy" "HE HE HE HE HE!"
        "the tea fairy" "HA"
        show teaman 
        teaman "BUT THE ONLY WAY TO MAKE TEA IS TO LEARN HOW TO TRAVERSE THE KITCHEN"
        jump openyourmap

init python:
    config.overlay_screens.append("key_listener")

default map_open = False
default previous_music = None


label openyourmap :
    teaman "HERE TO OPEN YOU MAP PRESS M"
    jump openyourmap
        

        



label bcookingland:
    scene cooklandea
    show teaman
    teaman "YES, SEE IN COOKLANDEA, YOU NEED TO LOOK OUT FOR..."

    show ovengirl at offscreenleft
    show ovengirl:
        ease 2.0 xalign 1.0  # Slide to the right

    show teaman:
        ease 2.0 xalign 0.0 
        
    teaman "oh it's you."
    ovengirl "yass Of Course it's me¡"
    show ovengirl unknow
    ovengirl "🅰️nnd who is this you bought with you¿ 🙏"
    teaman "NO ONE"
    ovengirl "ohhhh don't🔣 say thAt¡ 🈶🈶"
    show ovengirl 
    ovengirl "now ,hun😏 tell me who🆔 your are?💜"
    jump thanisthethatthingyousaed

label thanisthethatthingyousaed:

    $ yourname = renpy.input("What is your name?")
    $ yourname = yourname.strip()


menu isthatyourname:
    "Are you sure?"
    "YES":
        jump isthatthatthatyourname
            
    "NO":
        "you can't just undo your mistakes like that"
        jump contenu
            
            
    "i, i don't know":
        "well don't worry abot that you can change your name within 2-3 weeks"
        jump contenu




label isthatthatthatyourname:

    menu:
        "Are you really sure?"

        "100%%":
            jump contenu

        "Wait, I'm not sure about this":
            "This option is permanent."
            jump contenu



label contenu:
    ovengirl "🙏oOOooOOoO"
    ovengirl "[[NAMEHERE] that's a good name💜"
    teaman "NO"
    teaman "NO NO"
    teaman "NO NO NO"
    teaman "IT'S PRONOUNCED [yourname]"
    ovengirl "ohhhhh that's muuuch better¡ (:"
    




    


    #kill me
    






































































































































    # This ends the game.
    

    
    return
