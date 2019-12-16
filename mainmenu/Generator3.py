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
    font1 = [24, createFont("Ariel", 24)]

#Dit gedeelte zorgt ervoor dat het scherm wordt weergegeven    
def draw():
    
    functions.drawText("Your deck has been Generated!", 960, 200)
    functions.drawText("Your origins drawn are " + randomOrigin + ' and ' + randomOrigin2, 960, 250)
    functions.drawText("Your traps drawn are " + randomTrap + ', ' + randomTrap2 + ' and ' + randomTrap3, 960, 300)
    functions.drawText("Your jobs drawn are " + randomJob + ', ' + randomJob2 + ', ' + randomJob3 + ', ' + randomJob4 + ', ' + randomJob5 + ' and ' + randomJob6, 960, 350)
    
    

#
#
# Dit scherm is nog niet af, uiteindelijk wordt hier het random deck gegenereerd en weergegeven.
