import functions, Cards 
#setup
def setup():
    global font
    
    font1 = [24, createFont("Ariel", 24)]
#Dit geeft de interactieve interface weer
def draw():
    background(0)
    
    functions.drawText("Player 1, Press the button down below to generate your deck.", 960, 440)
    
    fill(100, 0, 100)
    rect(910, 600, 100, 100)
    
    functions.drawText2("Generate!", 960, 660, 255, 255, 255, 20)

    
