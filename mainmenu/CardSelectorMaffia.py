import Cards, TutorialBot

current_page = ""

def setup():
    background(0)
        
def draw():
    global current_page
    
    background(0)
    # checkt welke kaarten wanneer getekend moet worden.
    if len(TutorialBot.player_deck) < 10:
        Cards.DrawMaffiaOriginCards()
    if len(TutorialBot.player_deck) < 13:
        current_page = "Card_selector_maffia_trap"
        Cards.DrawMaffiaTrapCards()
    if len(TutorialBot.player_deck) < 19:
        current_page = "Card_selector_maffia_job"
        Cards.DrawMaffiaJobCards()
