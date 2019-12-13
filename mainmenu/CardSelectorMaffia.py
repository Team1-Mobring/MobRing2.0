import Cards, TutorialBot

current_card_page = ""

def setup():
    background(0)
        
def draw():
    global current_card_page
    
    background(0)
    # checkt welke kaarten wanneer getekend moet worden.
    if len(TutorialBot.player_deck) < 10:
        Cards.DrawMaffiaOriginCards()
    elif len(TutorialBot.player_deck) > 9 and len(TutorialBot.player_deck) < 13:
        current_card_page = "Card_selector_maffia_trap"
        Cards.DrawMaffiaTrapCards()
    if len(TutorialBot.player_deck) > 12 and len(TutorialBot.player_deck) < 19:
        current_card_page = "Card_selector_maffia_job"
        Cards.DrawMaffiaJobCards()
