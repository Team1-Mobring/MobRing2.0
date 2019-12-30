import Cards, TutorialBot

current_card_page = ""

def setup():
    global backgroundimg
    backgroundimg = loadImage("PickCards.png")
    image(backgroundimg, 0, 0)
        
def draw():
    global current_card_page, backgroundimg
    image(backgroundimg, 0, 0)
    # checkt welke kaarten wanneer getekend moet worden.
    if len(TutorialBot.player_deck) < 8:
        Cards.DrawMaffiaOriginCards()
    elif len(TutorialBot.player_deck) > 7 and len(TutorialBot.player_deck) < 11:
        current_card_page = "Card_selector_maffia_trap"
        Cards.DrawMaffiaTrapCards()
    elif len(TutorialBot.player_deck) > 9 and len(TutorialBot.player_deck) < 17:
        current_card_page = "Card_selector_maffia_job"
        Cards.DrawMaffiaJobCards()
    elif len(TutorialBot.player_deck) == 17:
        current_card_page = "Blue_bot"
