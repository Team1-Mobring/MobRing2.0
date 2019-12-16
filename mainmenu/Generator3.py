import functions, Cards, random
origins = ['China', 'Japan', 'Italy', 'Russia', 'Netherlands', 'Colombia']
randomOrigin = random.choice(origins)
randomOrigin2 = random.choice(origins)
traps = ['Ambushed', 'Dodge', 'Revive', 'Ricochet', 'Sniped']
randomTrap = random.choice(traps)
randomTrap2 = random.choice(traps)
randomTrap3 = random.choice(traps)
jobs = ['Anti-Hit', 'Clairevoyance', 'Prophecy', 'Reroll', 'Retaliate', 'Reveal', 'Sacrifice', 'Small Hit', 'Stun', 'The odds are against you']
randomJob = random.choice(jobs)
randomJob2 = random.choice(jobs)
randomJob3 = random.choice(jobs)
randomJob4 = random.choice(jobs)
randomJob5 = random.choice(jobs)
randomJob6 = random.choice(jobs)



def setup():
    global background_img, highlightMenu, highlightGen, highlightTut
    font1 = [24, createFont("Ariel", 24)]
    background_img = loadImage("DeckGenerate2.png")
    highlightMenu = loadImage("MainMenuHighlight.png")
    highlightGen = loadImage("GenerateDeckHighlight2.png")
    highlightTut = loadImage("PlayTutorialBotHighlight.png")

#Dit gedeelte zorgt ervoor dat het scherm wordt weergegeven    
def draw():
    image(background_img, 0, 0)
    
    functions.drawScore("Your deck has been Generated!", 960, 200, 255, 255, 255, 40)
    functions.drawScore("Your origins drawn are " + randomOrigin + ' and ' + randomOrigin2, 960, 350, 255, 255, 255, 23)
    functions.drawScore("Your traps drawn are " + randomTrap + ', ' + randomTrap2 + ' and ' + randomTrap3, 960, 400, 255, 255, 255, 23)
    functions.drawScore("Your jobs drawn are " + randomJob + ', ' + randomJob2 + ', ' + randomJob3 + ', ' + randomJob4 + ', ' + randomJob5 + ' and ' + randomJob6, 960, 450, 255, 255, 255, 20)
    
    if functions.isMouseWithinSpace2(30, 30, 280, 90):
        image(highlightMenu, 0, 0)
    if functions.isMouseWithinSpace2(1070, 800, 400, 200):
        image(highlightGen, 0, 0)
    if functions.isMouseWithinSpace2(530, 800, 400, 200):
        image(highlightTut, 0, 0)
    

#
#
# Dit scherm is nog niet af, uiteindelijk wordt hier het random deck gegenereerd en weergegeven.
