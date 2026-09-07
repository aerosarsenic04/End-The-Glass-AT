# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define an = Character("castiael", color="#ffffff")
define m = Character("moros", color="#ffffff")


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
        an "now"
        $ angel_trigger = True
        $ renpy.quit()

    if name.lower() == "judgement":
        an "..."
        an "..."
        an "im sorry"
        an "i haven't paid for my sins"
        an "i don't deserve this blessing"
        an "this... this gift."
        an "the lord has been merciful"
        an "the lord has been merciful"
        an "the lord has been merciful"
        an "the lord has been merciful"
        an "i have not been merciful"
        an "judgement is here to condemn me"
        an "i must pay for my sins"
        an "the lord has been"
        an "merciful"
        $ angel_trigger = True
        $ renpy.quit()

    # This ends the game.

    return
