import Cards, TutorialBot

def setup():
    background(0)
    Cards.DrawFedOriginCards()
    
def draw():
    if len(TutorialBot.player_deck) > 8:
        background(0)
        Cards.DrawFedTrapCards()
    if len(TutorialBot.player_deck) > 11:
        baclground(0)
        Cards.DrawFedJobCards()
    
