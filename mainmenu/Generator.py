
import functions

def setup():
    global font1
    
    font1 = [24, createFont("Ariel", 24)]


def draw(font1):
    background(0)
    
    functions.drawText("Player 1, Are you Mafia or Federal Agencies?", 960, 440)
    
    fill(0, 0, 255)
    rect(1160, 640, 100, 100)
    
    fill(255, 0, 0)
    rect(660, 640, 100, 100)
    
    functions.drawText("Mafia", 710, 685)
    functions.drawText("FA", 1210, 685)
