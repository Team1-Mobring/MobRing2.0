import Cards, TutorialBot, CardSelectorFed, CardSelectorMaffia

# Cords voor locaties van kaarten
# (517, 0), (602, 390), (547, 689), (83, 511), (82, 777)

def setup():
    background_colour_image = "MainMenuafb2.png"
    image(loadImage(background_colour_image), 0, 0)    

def draw():
    if CardSelectorMaffia.current_card_page == "Blue_bot":
        image(loadImage("TutorialBotDesignFed.png"), 0, 0)
    if CardSelectorFed.current_card_page == "Red_bot":
        image(loadImage("TutorialBotDesignMafia.png"), 0, 0)
