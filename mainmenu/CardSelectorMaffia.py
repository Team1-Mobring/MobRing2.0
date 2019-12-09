import Cards, TutorialBot

def setup():
    background(0)
        
def draw():
    background(0)
    # checkt welke kaarten wanneer getekend moet worden.
    if len(TutorialBot.player_deck) < 10:
        Cards.DrawMaffiaOriginCards()
    if len(TutorialBot.player_deck) > 9:
        Cards.DrawMaffiaTrapCards()
    if len(TutorialBot.player_deck) > 12:
        Cards.DrawMaffiaJobCards()
