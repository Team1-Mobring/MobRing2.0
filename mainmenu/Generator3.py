import functions, Cards, random
origins = ['China', 'Japan', 'Italy', 'Russia', 'Netherlands', 'Colombia']
traps = ['Ambushed', 'Dodge', 'Revive', 'Ricochet', 'Sniped']
jobs = ['Anti-Hit', 'Clairevoyance', 'Prophecy', 'Reroll', 'Retaliate', 'Reveal', 'Sacrifice', 'Small Hit', 'Stun', 'The odds are against you']
rdg_step_count = True
def setup():
    global background_img, highlightMenu, highlightGen, highlightTut, randomJob, randomJob2, randomJob3, randomJob4, randomJob5, randomJob6, randomTrap, randomTrap2, randomTrap3, randomOrigin, randomOrigin2
    font1 = [24, createFont("Ariel", 24)]
    background_img = loadImage("DeckGenerate2.png")
    highlightMenu = loadImage("MainMenuHighlight.png")
    highlightGen = loadImage("GenerateDeckHighlight2.png")
    highlightTut = loadImage("PlayTutorialBotHighlight.png")
    randomJob = random.choice(jobs)
    randomJob2 = random.choice(jobs)
    randomJob3 = random.choice(jobs)
    randomJob4 = random.choice(jobs)
    randomJob5 = random.choice(jobs)
    randomJob6 = random.choice(jobs)
    randomTrap = random.choice(traps)
    randomTrap2 = random.choice(traps)
    randomTrap3 = random.choice(traps)
    randomOrigin2 = random.choice(origins)
    randomOrigin = random.choice(origins)

#Dit gedeelte zorgt ervoor dat het scherm wordt weergegeven    
        

def draw():
    global rdg_step_count, randomJob, randomJob2, randomJob3, randomJob4, randomJob5, randomJob6, randomTrap, randomTrap2, randomTrap3, randomOrigin, randomOrigin2
    image(background_img, 0, 0)
    if rdg_step_count == True:
        randomJob = random.choice(jobs)
        randomJob2 = random.choice(jobs)
        randomJob3 = random.choice(jobs)
        randomJob4 = random.choice(jobs)
        randomJob5 = random.choice(jobs)
        randomJob6 = random.choice(jobs)
        randomTrap = random.choice(traps)
        randomTrap2 = random.choice(traps)
        randomTrap3 = random.choice(traps)
        randomOrigin = random.choice(origins)
        randomOrigin2 = random.choice(origins)
        while randomOrigin == randomOrigin2:
            randomOrigin = random.choice(origins)
            randomOrigin2 = random.choice(origins)
        while randomTrap == randomTrap2:
            randomTrap = random.choice(traps)
            randomTrap2 = random.choice(traps)
        while randomJob == randomJob2:
            randomJob = random.choice(jobs)
            randomJob2 = random.choice(jobs)
        while randomJob3 == randomJob4:
            randomJob3 = random.choice(jobs)
            randomJob4 = random.choice(jobs)
        while randomJob5 == randomJob6:
            randomJob5 = random.choice(jobs)
            randomJob6 = random.choice(jobs)
        rdg_step_count = False
        


    functions.drawScore("Your deck has been Generated!", 960, 300, 255, 255, 255, 40)
    functions.drawScore("Your origins drawn are \n" + randomOrigin + '\n' + randomOrigin2, 570, 400, 255, 255, 255, 23)
    functions.drawScore("Your traps drawn are \n" + randomTrap + '\n' + randomTrap2 + '\n' + randomTrap3, 960, 400, 255, 255, 255, 23)
    functions.drawScore("Your jobs drawn are \n" + randomJob + '\n' + randomJob2 + '\n' + randomJob3 + '\n' + randomJob4 + '\n' + randomJob5 + '\n' + randomJob6, 1330, 400, 255, 255, 255, 20)
    functions.drawScore
    
    if functions.isMouseWithinSpace2(30, 30, 280, 90):
        image(highlightMenu, 0, 0)
    if functions.isMouseWithinSpace2(1070, 800, 400, 200):
        image(highlightGen, 0, 0)
    if functions.isMouseWithinSpace2(530, 800, 400, 200):
        image(highlightTut, 0, 0)
        

    
