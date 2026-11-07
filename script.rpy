# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# The script of the game goes in this file.

# Declare variables
default map_progress = 0

#Register the keyboard listener
default idkpath = 0
 

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
            $ idkpath = idkpath + 1
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


label openyourmap:

    teaman "HERE TO OPEN YOU MAP PRESS M"

    teaman "GO ON! EXPLORE!"

    $ renpy.pause(hard=True)

    return
        

        



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
    ovengirl "now ,hun😏 tell me who🆔 you are?💜"
    jump thanisthethatthingyousaed

label thanisthethatthingyousaed:
    $ yourname = renpy.input("What is your name?")
    $ yourname = yourname.strip()

    if yourname == "":
        "That is not your name."
        jump thanisthethatthingyousaed



menu isthatyourname:
    "Are you sure?"
    "YES":
        jump isthatthatthatyourname
            
    "NO":
        "you can't just undo your mistakes like that"
        jump contenu
            
            
    "i, i don't know":
        $ idkpath = idkpath + 1
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
    ovengirl "[[NAMEHERE] that's a g💮💮d name💜"
    teaman "NO"
    teaman "NO NO"
    teaman "NO NO NO"
    teaman "IT'S PRONOUNCED [yourname]"
    show ovengirl hppy
    ovengirl "ohhhhh that's muuuch better¡ 🧕(:"
    show ovengirl
    ovengirl "sayyy🐵, how did 🦖you🦆 meet🪽 [yourname] Rev Ivan?"
    show teaman ange
    teaman "I TOLD YOU TO NOT CALL ME THAT IN FRONT OF GUESTS!"
    show ovengirl winking 
    ovengirl "oh💅 sorry🦷 MR🧑‍💼 ThE tEa FaIrY :P"
    show teaman at offscreenleft
    show teaman:
        ease 1.0 xalign 2.0
    teaman "AURRRRR"
    show ovengirl
    ovengirl "don't worry 😷about 🫶him😃"
    ovengirl "tell😃 me more about you🤔"
    show ovengirl unknow
    ovengirl "why are you here"
menu whayareyouhere:

    "i'm doing Work experience (:":
        show ovengirl
        ovengirl "oh"
        ovengirl "work!"
        ovengirl "well i do love a"
        show ovengirl thinking
        ovengirl "urrrrr"
        show ovengirl hppy
        ovengirl "a You in uniform"
        ovengirl "yeah¡"
        show ovengirl
        ovengirl "did you know i work from home"
        ovengirl "i can show you!"
        jump totheovengirlshome 

    "i didn't know how to make tea and now i'm here":
        show ovengirl unknow
        ovengirl "oh"
        show ovengirl
        ovengirl "don't worry!"
        ovengirl "it's teasy"
        ovengirl "tell you what, we can go to my home i can show you how to make it :D"
        jump totheovengirlshome

    "idk":
        $ idkpath = idkpath + 1
        show ovengirl winking
        ovengirl "welllll don't worry"
        show ovengirl hppy
        ovengirl "i'm sure your here for a reason"
        show ovengirl
        ovengirl "come on it's getting late"
        jump totheovengirlshome


label totheovengirlshome:
    scene ovengirlhome
    show ovengirl
    ovengirl "welcome to my house!"
    ovengirl "it's a little small but i think it's nice"
    show ovengirl hppy
    ovengirl "i bet your house is much nicer"
    show ovengirl thinking
    ovengirl "Do you"
    ovengirl "Have a home?"
    if idkpath > 2:
        menu doyouhaveahome: 
            "Do you have a home?"

            "it's outsied of town":
                show ovengirl hppy
                ovengirl "oh how exotic!"
                show ovengirl
                ovengirl "i knew someone who"
                jump phonecallforovengirl

            "it's a long way a way":
                show ovengirl unknow
                ovengirl "wooooooow"
                ovengirl "i know how it fills to be far away from home"
                ovengirl "i lived in"
                jump phonecallforovengirl
                

            "it's uhmm well i arr, well i don't really know":
                show ovengirl thinking
                ovengirl "oh"
                ovengirl "how weird"
                ovengirl "how long have you not re.."
                jump phonecallforovengirl

    
 



    label phonecallforovengirl:
        show ovengirl unknow
        play sound "freesound044209.mp3"
        
        ovengirl ""
        ovengirl "urr i need to get that"
        
        show ovengirl:
            ease 1.0 xalign 2.0
    $ renpy.pause(3.0, hard=True)
    jump ovenhomeratsenne
    
    
    label ovenhomeratsenne:
        unknown "pisss hayyyy"
        unknown "hay youu"
        unknown "Hayyy pisss over here!"
        
        
        menu whatdoyousaytotherat030: 
            "What do you say to the unknown voice?"

            "nothing":
                unknown "pisss hayyyy"
                nknown "hhhhhaaaaaayyyy"
                nknown "pisisiisisiisi"
                nknown "yoou"
                jump whatdoyousaytotherat030


            "hello?":
                show ovengirl unknow
                ovengirl "wooooooow"
                ovengirl "i know how it fills to be far away from home"
                ovengirl "i lived in"
                jump phonecallforovengirl
                

            "Smart Gas Double Oven Slide-in Range with InstaView ProBake 2.0 do you have a roommate?":
                show ovengirl thinking
                ovengirl "oh"
                ovengirl "how weird"
                ovengirl "how long have you not re.."
                jump phonecallforovengirl
        

    
label step2oftherat:
    pass 
    
    


        



    #kill me
    




































































































































    # This ends the game.
    


