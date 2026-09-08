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

    # This ends the game.

    return
