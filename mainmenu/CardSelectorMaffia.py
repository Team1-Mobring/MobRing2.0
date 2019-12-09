import Cards, TutorialBot

def setup():
    background(0)
    Cards.DrawMaffiaOriginCards()
    
def draw():
    if len(TutorialBot.player_deck) > 8:
        Cards.DrawMaffiaTrapCards()
    if len(TutorialBot.player_deck) > 11:
        Cards.DrawMaffiaJobCards()
