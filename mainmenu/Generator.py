import functions, Cards

def setup():
    global font1, background_img, Mafia_Highlight, Fed_Highlight, Help_Highlight, highlightMenu
    font1 = [24, createFont("Ariel", 24)]
    background_img = loadImage("ChooseSide.png")
    Mafia_Highlight = loadImage("MafiaButtonHighlight.png")
    Fed_Highlight = loadImage("FedButtonHighlight.png")
    highlightMenu = loadImage("MainMenuHighlight.png")
    Help_Highlight = loadImage("HelpButtonHighlight.png")

#Dit gedeelte zorgt ervoor dat het scherm wordt weergegeven
def draw(font1):
    image(background_img, 0, 0)
    
    if functions.isMouseWithinSpace2(1070, 470, 370, 200):
        image(Mafia_Highlight, 0, 0)
        
    if functions.isMouseWithinSpace2(510, 470, 360, 200):
        image(Fed_Highlight, 0, 0)
        
    if functions.isMouseWithinSpace2(1700, 920, 170, 115):
        image(Help_Highlight, 0, 0)
        
    if functions.isMouseWithinSpace2(30, 30, 280, 90):
        image(highlightMenu, 0, 0)
    
