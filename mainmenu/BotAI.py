import Cards, TutorialBot, CardSelectorFed, CardSelectorMaffia

# Cords voor locaties van kaarten
# (517, 0), (602, 390), (547, 689), (83, 511), (82, 777)

def setup():
    global load_board
    background_colour_image = "MainMenuafb2.png"
    image(loadImage(background_colour_image), 0, 0)
def draw():    
    
    # Loads in the correct board for the Bot, playerboard will be the physical board of his choosing
    if CardSelectorMaffia.current_card_page == "Blue_bot":
        image(loadImage("TutorialBotDesignFed.png"), 0, 0)
    if CardSelectorFed.current_card_page == "Red_bot":
        image(loadImage("TutorialBotDesignMafia.png"), 0, 0)
    
    # Scales the cards to the right sizes.
    scale(0.3)
    
    # Show that there are still cards in the Bot_Deck
    if len(TutorialBot.bot_deck) > 0:
        image(loadImage("CardBackBlueSideWays.png"), 325, 2650)
    # Shows that there are cards in the graveyard
    if len(TutorialBot.bot_graveyard) > 0 :
        image(loadImage("CardBackBlueSideWays.png"), 325, 1800)
    
    if len(TutorialBot.bot_graveyard) > 0 :
        x = 1727
        y = -180
        for i in range(len(TutorialBot.bot_held_cards)):
            image(loadImage("CardBackBlue.png"), x, y)
            x = x + 210
    
    if len(TutorialBot.bot_mobster_field_cards) > 0 :
        x = 1913
        y = 2350
        
        for i in range(len(TutorialBot.bot_mobster_field_cards)):
            TutorialBot.bot_mobster_field_cards[i].display(x, y)
            x = x + 890
    
    if len(TutorialBot.bot_trap_field_cards) > 0 :
        image(loadImage("CardBackBlueSideWays.png"), 3260, 1380)
    
    if len(TutorialBot.bot_job_field_cards) > 0 :
        TutorialBot.bot_job_field_cards[0].display(2080, 1380)
