import Cards, TutorialBot, functions

current_card_page = ""

def setup():
    global backgroundimg
    backgroundimg = loadImage("PickCards.png")
    image(backgroundimg, 0, 0)
    
def draw():
    global current_card_page, backgroundimg
    image(backgroundimg, 0 , 0)
    # checkt welke kaarten wanneer getekend moet worden.
    if len(TutorialBot.player_deck) < 8:
        Cards.DrawFedOriginCards()
    elif len(TutorialBot.player_deck) > 7 and len(TutorialBot.player_deck) < 11:
        current_card_page = "Card_selector_fed_trap"
        Cards.DrawFedTrapCards()
    elif len(TutorialBot.player_deck) > 9 and len(TutorialBot.player_deck) < 17:
        current_card_page = "Card_selector_fed_job"
        Cards.DrawFedJobCards()
    elif len(TutorialBot.player_deck) == 17:
        current_card_page = "Red_bot"
    scale(3.33333333)
    if functions.isMouseWithinSpace2(TutorialBot.help_x, TutorialBot.help_y, 170, 115):
        image(TutorialBot.Help_Highlight, 0, 0)
        
    if functions.isMouseWithinSpace2(TutorialBot.main_menu_x, TutorialBot.main_menu_y, 265, 90):
        image(TutorialBot.highlightMenu, 0, 0)
