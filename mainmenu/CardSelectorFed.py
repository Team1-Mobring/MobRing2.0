import Cards, TutorialBot

current_card_page = ""

def setup():
    background(0)
    
    
def draw():
    global current_card_page
    background(0)
    # checkt welke kaarten wanneer getekend moet worden.
    if len(TutorialBot.player_deck) < 10:
        Cards.DrawFedOriginCards()
    elif len(TutorialBot.player_deck) > 9 and len(TutorialBot.player_deck) < 13:
        current_card_page = "Card_selector_fed_trap"
        Cards.DrawFedTrapCards()
        print(Cards.fed_origins)
        print(TutorialBot.player_deck)
    elif len(TutorialBot.player_deck)> 12  and len(TutorialBot.player_deck) < 19:
        current_card_page = "Card_selector_fed_job"
        Cards.DrawFedJobCards()
        print(TutorialBot.player_deck)
