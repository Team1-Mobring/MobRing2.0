import Cards, TutorialBot

current_page = ""

def setup():
    background(0)
    
    
def draw():
    global current_page
    background(0)
    # checkt welke kaarten wanneer getekend moet worden.
    if len(TutorialBot.player_deck) < 10:
        Cards.DrawFedOriginCards()
    elif len(TutorialBot.player_deck) > 9:
        current_page = "Card_selector_fed_trap"
        Cards.DrawFedTrapCards()
    elif len(TutorialBot.player_deck) > 12:
        current_page = "Card_selector_fed_job"
        Cards.DrawFedJobCards()
    
