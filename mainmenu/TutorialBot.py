import Cards

# Button cords
main_menu_x = 70
fed_x = 495
maffia_x = 1125
help_x = 1550
box_y = 550
box_width = 300
box_height = 100
box_x = 0

# Player card sets
player_deck =  set()
player_graveyard = set()
player_held_cards = set()
player_mobster_field_cards = set()
player_job_field_cards = set()
player_trap_field_cards = set()
# Bot card sets
bot_deck = set()
bot_graveyard = set()
bot_held_cards = set()
bot_mobster_field_cards = set()
bot_job_field_cards = set()
bot_trap_field_cards = set()


def setup():
    size(1920, 1080)
    background(255)
    Cards.test_card.display()
def draw():
    fill(180)
    main_menu = rect(main_menu_x, box_y, box_width, box_height)
    fed = rect(fed_x, box_y, box_width, box_height)
    maffia = rect(maffia_x, box_y, box_width, box_height)
    help = rect(help_x, box_y, box_width, box_height)
    fill(255)
    textAlign(CENTER)
    main_menu_text  = text("Main menu", main_menu_x + 0.5 * box_width, box_y + 0.5 * box_height)
    fed_text  = text("Federal Agency", fed_x + 0.5 * box_width, box_y + 0.5 * box_height)
    maffia_text  = text("Maffia", maffia_x + 0.5 * box_width, box_y + 0.5 * box_height)
    help_text  = text("Help!", help_x + 0.5 * box_width, box_y + 0.5 * box_height)
    
# box clicker
def isMouseWithinSpace(x, y, w, h):
    if x < mouseX < x + w and y < mouseY < y + h:
        return True
    else:
        return False

# mouseclcik registrater    
def mousePressed():
    global box_width, box_height, box_x, box_y
    if isMouseWithinSpace(main_menu_x, box_y, box_width, box_height):
        background(140,200,180)
        print("click")
    elif isMouseWithinSpace(fed_x, box_y, box_width, box_height):
        background(140,200,180)
        print("click2")
    elif isMouseWithinSpace(maffia_x, box_y, box_width, box_height):
        background(140,200,180)
        print("click3")
    elif isMouseWithinSpace(help_x, box_y, box_width, box_height):
        background(140,200,180)
        print("click4")
    else:
        print("wrong!")
