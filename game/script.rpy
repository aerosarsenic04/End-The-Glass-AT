# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define an = Character("castiael", color="#ffffff")
define m = Character("moros", color="#ffffff")
define y = Character("[name]", color="#a4c6c0")
default persistent.content_warning = False


# The game starts here. 

label start:

    $ angel_trigger = False

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    if persistent.content_warning:
        jump game_start

    "Before beginning, please ensure you understand the content warnings for this game."
    "This game contains themes of suicidal ideation, depression, religious imagery, blood and self-harm."
    "Would you like to see the detailed list of warnings? (spoilers)"

    menu:
        "yes":
            jump cwdetailed
        "no":
            jump contin


label cwdetailed:

    "Game contains depiction of self mutilation via wing amputation, extreme nihilism, heavily existential themes, implied suicide (1/3 endings)."
    "Please understand that the main character struggles heavily with mental illness."
    "This game does not have a happy ending"

    jump contin


label contin:

    $ persistent.content_warning = True

    "Would you like to play?"

    menu:
        "yes":
            jump game_start
        "no":
            $ renpy.quit()

#SECTION - Game actually starts here; name input
label game_start:
    # These display lines of dialogue.
    "you wake."
    an "hello. you must be..."
    $ name = renpy.input("what is your name?", length=50)
    $ name = name.strip()
    if name == "":
        $name = "{REDACTED}"

    if not name:
        $name = "{REDACTED}"

    if name.lower() == "angel":
        an "..."
        an "..."
        an "you should leave"
        an '{font=fonts/Esteban.ttf}{color=#c40404}now{/color}{/font}'
        $ angel_trigger = True
        $ renpy.quit()

    if name.lower() == "judgement":
        an "..."
        an "..."
        an "im sorry"
        an "i haven't paid for my sins"
        an "i don't deserve this blessing"
        an "this... this gift."
        an "{font=fonts/Esteban.ttf}the lord has been merciful{/font}"
        an "{font=fonts/Esteban.ttf}the lord has been merciful{/font}"
        an "{font=fonts/Esteban.ttf}the lord has been merciful{/font}"
        an "{font=fonts/Esteban.ttf}the lord has been merciful{/font}"
        an "i have not been merciful"
        an "judgement is here to condemn me"
        an "i must pay for my sins"
        an "the lord has been"
        an "merciful"
        $ angel_trigger = True
        $ renpy.quit()

    y "... Where am I? What is this?"
    y "I don't remember falling asleep here."
    an "oh... my apologies for the inconvenience."
    an "This is... a house?"
    "You look around... This is definitely YOUR home"
    y "you... who are you? why are you in my home!?"
    "You get up"
    an "I am Castiael! I am an angel sent to watch over you."
    an "Your hardships have not been unseen"
    y "I..."
    "You pause... this person sounds crazy, but there's an unexplicable ease in their voice."
    "They do seem inexplicably angelic... but you could be imagining that."

#TODO - Option to uhhhh make sure cas is an angel.
# Their eyes are bright

    y "I still think you might be mistaken; I don't... believe."
    an "Belief is not required for me to safeguard you... you humans have this concept of guardian angels, and I suppose I can assume that role."

#TODO - OPT to yes or no angel... you get stuck with cas anyways
    y "I don't need a guardian angel."

    an "Please teach me well."




label Find_wings:
    "You wake... paranoid."
    "There is an inexplicable terror in your chest."
    "You can't help but feel that if you go to sleep again, you might not wake."
    "You breathe deeply and get out of bed."
    "This is not anything you've felt before..."


    "You enter the bathroom"
    an "[name]"
    an "aren't my wings beautiful?"
    an "please"
    an "they're beautiful right?"
    "You can hear your own breath."
    "What... what are you even supposed to do?"
    "The bathroom is covered in blood"
    "Your shears are in Castiael's steady hand"
    "His back is a bloodied, hacked mess. The blood soaked towel-like lumps seem to be what remains of his wings on the cold tiled floor."
    y "Castiael..."
    y "What are you..."
    "You almost utter an 'are you okay?' but it dies on your lips. There is nothing you can say that will change anything..."
    an "it's okay, [name]"
    an "the lord will grant me freedom"
    an "i won't hurt anymore"
    "He's lying, you can see through it now. The angel has tears rolling down his blood-stained face, his previous composure is shattered."
    y "Castiael, put the shears down."
    an "i..."
    an "okay, [name]"
    "The shears clatter onto the tile, splattering blood on the tiles near your feet"
    "You can see Castiael start to tremble."
    y "It's... It's fine, Castiael. Everything is fine. Just... Come on, we need to stop the bleeding."
    
    # This ends the game.

    return
