import functions, Cards 

def setup():
    global font1, background_img, highlightMenu

    font1 = [24, createFont("Ariel", 24)]
    background_img = loadImage("DeckGenerate1.png")
    highlightMenu = loadImage("MainMenuHighlight.png")
    
    
#Dit geeft de interactieve interface weer
def draw():
    image(background_img, 0, 0)
    
    if functions.isMouseWithinSpace2(30, 30, 280, 90):
        image(highlightMenu, 0, 0)
    
    
    
    
