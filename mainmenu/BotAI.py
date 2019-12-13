import Cards, TutorialBot, CardSelectorFed, CardSelectorMaffia

# Cords voor locaties van kaarten
# (517, 0), (602, 390), (547, 689), (83, 511), (82, 777)

def setup():
    
    if CardSelectorMaffia.current_card_page == "Blue-bot":
        pass
    if CardSelectorFed.current_card_page == "Red_bot":
        background_colour_image = "TutorialBotDesignMafia.png"
        image(loadImage(background_colour_image), 0, 0)
    

def draw():
    pass
