import Cards, functions, CardSelectorMaffia, CardSelectorFed

# Button cords
main_menu_x = 35
main_menu_y = 35
fed_x = 510
fed_y = 470
maffia_x = 1070
maffia_y = 470
help_x = 1700
help_y = 920
box_width = 300
box_height = 100
box_x = 0

# Player card sets
player_deck = []
player_graveyard = []
player_mobster_field_cards = []
player_job_field_cards = []
player_trap_field_cards = []
# Bot card sets
bot_deck = []
bot_held_cards = []
if CardSelectorMaffia.current_card_page == "Blue_bot":
    bot_deck = [Cards.fsb3, Cards.fsb4, Cards.psia1, Cards.psia2, Cards.psia3, Cards.psia4, Cards.anit_Hit_Blue2, Cards.retaliate_Blue1, Cards.reroll_Blue1, Cards.the_Odds_Are_Against_You_Blue1, Cards.revive_Blue1]
    bot_held_mobster_cards = [Cards.fsb1, Cards.fsb2, Cards.fsb3, Cards.fsb4, Cards.psia1, Cards.psia2, Cards.psia3, Cards.psia4]
    bot_held_trap_cards = [Cards.dodge_Blue1, Cards.ricochet_Blue1, Cards.revive_Blue1]
    bot_held_job_cards = [Cards.anit_Hit_Blue1, Cards.anit_Hit_Blue2, Cards.retaliate_Blue1, Cards.reroll_Blue1, Cards.the_Odds_Are_Against_You_Blue1]
    bot_held_cards = [Cards.fsb1, Cards.fsb2, Cards.dodge_Blue1, Cards.ricochet_Blue1, Cards.anit_Hit_Blue1]
if CardSelectorFed.current_card_page == "Red_bot":
    bot_deck = [Cards.bratva3, Cards.bratva4, Cards.yakuza1, Cards.yakuza2, Cards.yakuza3, Cards.yakuza4, Cards.anti_Hit_Red2, Cards.reroll_Red1, Cards.the_Odds_Are_Against_You_Red1, Cards.revive_Red1]
    bot_held_mobster_cards = [Cards.bratva1, Cards.bratva2, Cards.bratva3, Cards.bratva4, Cards.yakuza1, Cards.yakuza2, Cards.yakuza3, Cards.yakuza4]
    bot_held_trap_cards = [Cards.dodge_Red1, Cards.ricochet_Red1, Cards.revive_Red1]
    bot_held_job_cards = [Cards.anti_Hit_Red1, Cards.anti_Hit_Red2, Cards.retaliate_Red1, Cards.reroll_Red1, Cards.the_Odds_Are_Against_You_Red1]
    bot_held_cards = [Cards.bratva1, Cards.bratva2, Cards.dodge_Red1, Cards.retaliate_Red1, Cards.anti_Hit_Red1]
bot_graveyard = []
bot_mobster_field_cards = [Cards.bratva1]
bot_job_field_cards = []
bot_trap_field_cards = []


tutbotbackground = loadImage("ChooseSide.png")
Maffia_Highlight = loadImage("MafiaButtonHighlight.png")
Fed_Highlight = loadImage("FedButtonHighlight.png")
highlightMenu = loadImage("MainMenuHighlight.png")
Help_Highlight = loadImage("HelpButtonHighlight.png")


def setup():
    global tutbotbackground, Maffia_Highlight, Fed_Highlight, highlightMenu, Help_Highlight
    
    tutbotbackground = loadImage("ChooseSide.png")
    Maffia_Highlight = loadImage("MafiaButtonHighlight.png")
    Fed_Highlight = loadImage("FedButtonHighlight.png")
    highlightMenu = loadImage("MainMenuHighlight.png")
    Help_Highlight = loadImage("HelpButtonHighlight.png")
def draw():
    
    image(tutbotbackground, 0, 0)
    
    if functions.isMouseWithinSpace2(maffia_x, maffia_y, 360, 195):
        image(Maffia_Highlight, 0, 0)
        
    if functions.isMouseWithinSpace2(fed_x, fed_y, 360, 195):
        image(Fed_Highlight, 0, 0)
        
    if functions.isMouseWithinSpace2(help_x, help_y, 170, 115):
        image(Help_Highlight, 0, 0)
        
    if functions.isMouseWithinSpace2(main_menu_x, main_menu_y, 265, 90):
        image(highlightMenu, 0, 0)
