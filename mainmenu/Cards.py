import TutorialBot

# Base code voor mobster karten
class Mobster():
    def __init__(self, type, name, origin, hp1, hp2, hp3, img):
        self.type = type
        self.name = name
        self.origin = origin
        self.hp1 = hp1
        self.hp2 = hp2
        self.hp3 = hp3
        self.img = img
        
    def display(self, x, y):
        self.x = x
        self.y = y
        rimg = loadImage(self.img)
        image(rimg, x, y)
# Base code voor origin kaarten        
class Origin():
    def __init__(self, type, name, img):
        self.type = type
        self.name = name
        self.img = img
        
    def display(self, x, y):
        self.x = x
        self.y = y
        rimg = loadImage(self.img)
        image(rimg, x, y)
# Base code voor trap en job kaarten      
class TrapJob():
    def __init__(self, type, name, hp1, hp2, effect, img):
        self.type = type
        self.name = name
        self.hp1 = hp1
        self.hp2 = hp2
        self.effect = effect
        self.img = img
        
    def display(self, x, y):
        self.x = x
        self.y = y
        rimg = loadImage(self.img)
        image(rimg, x, y)

test_card = Mobster("testType", "TestName", "TestOrigin", 0, 0, 0, "settingsicon2.png")

#Mobsters
aivd1 = Mobster("Mobster", "AIVD1", "Netherlands", 6, 6, 6, "AIVD1.png")
aivd2 = Mobster("Mobster", "AIVD2", "Netherlands", 7, 9, 6, "AIVD2.png")
aivd3 = Mobster("Mobster", "AIVD3", "Netherlands", 0, 10, 5, "AIVD3.png")
aivd4 = Mobster("Mobster", "AIVD4", "Netherlands", 0, 11, 0, "AIVD4.png")
bratva1 = Mobster("Mobster", "Bratva1", "Russia", 7, 8, 8, "Bratva1.png")
bratva2 = Mobster("Mobster", "Bratva2", "Russia", 0, 9, 9, "Bratva2.png")
bratva3 = Mobster("Mobster", "Bratva3", "Russia", 0, 9, 10, "Bratva3.png")
bratva4 = Mobster("Mobster", "Bratva4", "Russia", 0, 10, 10, "Bratva4.png")
cosaNostra1 = Mobster("Mobster", "CosaNostra1", "Italy", 7, 6, 9, "CosaNostra1.png")
cosaNostra2 = Mobster("Mobster", "CosaNostra2", "Italy", 0, 9, 10, "CosaNostra2.png")
cosaNostra3 = Mobster("Mobster", "CosaNostra3", "Italy", 0, 4, 5, "CosaNostra3.png")
cosaNostra4 = Mobster("Mobster", "CosaNostra4", "Italy", 0, 11, 0, "CosaNostra4.png")
dni1 = Mobster("Mobster", "DNI1", "Colombia", 5, 6, 6, "DNI1.png")
dni2 = Mobster("Mobster", "DNI2", "Colombia", 0, 9, 5, "DNI2.png")
dni3 = Mobster("Mobster", "DNI3", "Colombia", 0, 10, 4, "DNI3.png")
dni4 = Mobster("Mobster", "DNI4", "Colombia", 0, 3, 0, "DNI4.png")
farmer1 = Mobster("Mobster", "Farmer1", "Netherlands", 7, 9, 7, "Farmer1.png")
farmer2 = Mobster("Mobster", "Farmer2", "Netherlands", 6, 6, 6, "Farmer2.png")
farmer3 = Mobster("Mobster", "Farmer3", "Netherlands", 0, 10, 5, "Farmer3.png")
farmer4 = Mobster("Mobster", "Farmer4", "Netherlands", 0, 11, 0, "Farmer4.png")
fsb1 = Mobster("Mobster", "FSB1", "Russia", 7, 8, 8, "FSB1.png")
fsb2 = Mobster("Mobster", "FSB2", "Russia", 0, 9, 9, "FSB2.png")
fsb3 = Mobster("Mobster", "FSB3", "Russia", 0, 9, 10, "FSB3.png")
fsb4 = Mobster("Mobster", "FSB4", "Russia", 0, 10, 10, "FSB4.png")
caliKartel1 = Mobster("Mobster", "CaliKartel1", "Colombia", 5, 6, 6, "KaliKartel1.png")
caliKartel2 = Mobster("Mobster", "CaliKartel2", "Colombia", 0, 9, 5, "KaliKartel2.png")
caliKartel3 = Mobster("Mobster", "CaliKartel3", "Colombia", 0, 4, 10, "KaliKartel3.png")
caliKartel4 = Mobster("Mobster", "CaliKartel4", "Colombia", 0, 3, 0, "KaliKartel4.png")
mss1 = Mobster("Mobster", "MSS1", "China", 8, 8, 8, "MSS1.png")
mss2 = Mobster("Mobster", "MSS2", "China", 5, 6, 7, "MSS2.png")
mss3 = Mobster("Mobster", "MSS3", "China", 0, 9, 4, "MSS3.png")
mss4 = Mobster("Mobster", "MSS4", "China", 0, 3, 0, "MSS4.png")
psia1 = Mobster("Mobster", "PSIA1", "Japan", 8, 6, 7, "PSIA1.png")
psia2 = Mobster("Mobster", "PSIA2", "Japan", 8, 6, 9, "PSIA2.png")
psia3 = Mobster("Mobster", "PSIA3", "Japan", 7, 7, 7, "PSIA3.png")
psia4 = Mobster("Mobster", "PSIA4", "Japan", 0, 3, 0, "PSIA4.png")
sismi1 = Mobster("Mobster", "SISMI1", "Italy", 7, 6, 9, "SISMI1.png")
sismi2 = Mobster("Mobster", "SISMI2", "Italy", 0, 5, 4, "SISMI2.png")
sismi3 = Mobster("Mobster", "SISMI3", "Italy", 0, 10, 9, "SISMI3.png")
sismi4 = Mobster("Mobster", "SISMI4", "Italy", 0, 11, 0, "SISMI4.png")
triad1 = Mobster("Mobster", "Triad1", "China", 8, 8, 8, "Triad1.png")
triad2 = Mobster("Mobster", "Triad2", "China", 5, 6, 7, "Triad2.png")
triad3 = Mobster("Mobster", "Triad3", "China", 0, 9, 4, "Triad3.png")
triad4 = Mobster("Mobster", "Triad4", "China", 0, 3, 0, "Triad4.png")
yakuza1 = Mobster("Mobster", "Yakuza1", "Japan", 6, 8, 7, "Yakuza1.png")
yakuza2 = Mobster("Mobster", "Yakuza2", "Japan", 6, 8, 9, "Yakuza2.png")
yakuza3 = Mobster("Mobster", "Yakuza3", "Japan", 7, 7, 7, "Yakuza3.png")
yakuza4 = Mobster("Mobster", "Yakuza4", "Japan", 0, 3, 0, "Yakuza4.png")

#origins
origin_China_Red = Origin("Origin", "Origin_China_Red", "OriginChina.png")
origin_China_Blue = Origin("Origin", "Origin_China_Blue", "OriginChinaFED.png")
origin_Japan_Red = Origin("Origin", "Origin_Japan_Red", "OriginJapan.png")
origin_Japan_Blue = Origin("Origin", "Origin_Japan_Blue", "OriginJapanFED.png")
origin_Colombia_Red = Origin("Origin", "Origin_Colombia_Red", "OriginColombia.png")
origin_Colombia_Blue = Origin("Origin", "Origin_Colombia_Blue", "OriginColombiaFED.png")
origin_Italy_Red = Origin("Origin", "Origin_Italy_Red", "OriginItaly.png")
origin_Italy_Blue = Origin("Origin", "Origin_Italy_Blue", "OriginItalyFED.png")
origin_Netherlands_Red = Origin("Origin", "Origin_Netherlands_Red", "OriginNederland.png")
origin_Netherlands_Blue = Origin("Origin", "Origin_Netherlands_Blue", "OriginNederlandFED.png")
origin_Russia_Red = Origin("Origin", "Origin_Russia_Red", "OriginRussia.png")
origin_Russia_Blue = Origin("Origin", "Origin_Russia_Blue", "OriginRussiaFED.png")

#Jobs
anti_Hit_Red1 = TrapJob("Job","Anti_Hit_Red", 1, 0, "-2 dmg", "JobAnti-Hit.png")
anti_Hit_Red2 = TrapJob("Job","Anti_Hit_Red", 1, 0, "-2 dmg", "JobAnti-Hit.png")
anti_Hit_Blue1 = TrapJob("Job","Anti_Hit_Blue", 1, 0, "-2 dmg", "JobAnti-HitFED.png")
anti_Hit_Blue2 = TrapJob("Job","Anti_Hit_Blue", 1, 0, "-2 dmg", "JobAnti-HitFED.png")
clairevoyance_Red1 = TrapJob("Job","Clairevoyance_Red", 1, 0, "Reveal 2 cards", "JobClairevoyance.png")
clairevoyance_Red2 = TrapJob("Job","Clairevoyance_Red", 1, 0, "Reveal 2 cards", "JobClairevoyance.png")
clairevoyance_Blue1 = TrapJob("Job","Clairevoyance_Blue", 1, 0, "Reveal 2 cards", "JobClairevoyanceFED.png")
clairevoyance_Blue2 = TrapJob("Job","Clairevoyance_Blue", 1, 0, "Reveal 2 cards", "JobClairevoyanceFED.png")
prophecy_Red1 = TrapJob("Job","Prophecy_Red", 1, 0, "Save 1 rolled dice value", "JobProphecy.png")
prophecy_Red2 = TrapJob("Job","Prophecy_Red", 1, 0, "Save 1 rolled dice value", "JobProphecy.png")
prophecy_Blue1 = TrapJob("Job","Prophecy_Blue", 1, 0, "Save 1 rolled dice value", "JobProphecyFED.png")
prophecy_Blue2 = TrapJob("Job","Prophecy_Blue", 1, 0, "Save 1 rolled dice value", "JobProphecyFED.png")
reroll_Red1 = TrapJob("Job","Reroll_Red", 1, 0, "can reroll a second time", "JobReroll.png")
reroll_Red2 = TrapJob("Job","Reroll_Red", 1, 0, "can reroll a second time", "JobReroll.png")
reroll_Blue1 = TrapJob("Job","Reroll_Blue", 1, 0, "can reroll a second time", "JobRerollFED.png")
reroll_Blue2 = TrapJob("Job","Reroll_Blue", 1, 0, "can reroll a second time", "JobRerollFED.png")
retaliate_Red1=  TrapJob("Job","Retaliate_Red", 1, 0, "Take back a card and fully heal it", "JobRetaliate.png")
retaliate_Red2 = TrapJob("Job","Retaliate_Red", 1, 0, "Take back a card and fully heal it", "JobRetaliate.png")
retaliate_Blue1 = TrapJob("Job","Retaliate_Blue", 1, 0, "Take back a card and fully heal it", "JobRetaliateFED.png")
retaliate_Blue2 = TrapJob("Job","Retaliate_Blue", 1, 0, "Take back a card and fully heal it", "JobRetaliateFED.png")
reveal_Red1 = TrapJob("Job","Reveal_Red", 1, 0, "Reveal the enemy trap", "JobReveal.png")
reveal_Red2 = TrapJob("Job","Reveal_Red", 1, 0, "Reveal the enemy trap", "JobReveal.png")
reveal_Blue1 = TrapJob("Job","Reveal_Blue", 1, 0, "Reveal the enemy trap", "JobRevealFED.png")
reveal_Blue2 = TrapJob("Job","Reveal_Blue", 1, 0, "Reveal the enemy trap", "JobRevealFED.png")
sacrifice_Red1 = TrapJob("Job","Sacrifice_Red", 1, 0, "Sacrifice a non damaged Mobster to kill an enemy Mobster", "JobSacrifice.png")
sacrifice_Red2 = TrapJob("Job","Sacrifice_Red", 1, 0, "Sacrifice a non damaged Mobster to kill an enemy Mobster", "JobSacrifice.png")
sacrifice_Blue1 = TrapJob("Job","Sacrifice_Blue", 1, 0, "Sacrifice a non damaged Mobster to kill an enemy Mobster", "JobSacrificeFED.png")
sacrifice_Blue2 = TrapJob("Job","Sacrifice_Blue", 1, 0, "Sacrifice a non damaged Mobster to kill an enemy Mobster", "JobSacrificeFED.png")
small_Hit_Red1 = TrapJob("Job","Small_Hit_Red", 1, 0, "+2 dmg", "JobSmallHit.png")
small_Hit_Red2 = TrapJob("Job","Small_Hit_Red", 1, 0, "+2 dmg", "JobASmallHit.png")
small_Hit_Blue1 = TrapJob("Job","Small_Hit_Blue", 1, 0, "+2 dmg", "JobSmallHitFED.png")
small_Hit_Blue2 = TrapJob("Job","Small_Hit_Blue", 1, 0, "+2 dmg", "JobSmallHitFED.png")
stun_Red1 = TrapJob("Job","Stun_Red", 1, 0, "Your enemy can't attack with their dice next turn", "JobStun.png")
stun_Red2 = TrapJob("Job","Stun_Red", 1, 0, "Your enemy can't attack with their dice next turn", "JobStun.png")
stun_Blue1 = TrapJob("Job","Stun_Blue", 1, 0, "Your enemy can't attack with their dice next turn", "JobStunFED.png")
stun_Blue2 = TrapJob("Job","Stun_Blue", 1, 0, "Your enemy can't attack with their dice next turn", "JobStunFED.png")
the_Odds_Are_Against_You_Red1 = TrapJob("Job","The_Odds_Are_Against_You_Red", 1, 0, "Move one of your ringcontainers to your enemy", "JobTheoddsareagainstyou.png")
the_Odds_Are_Against_You_Red2 = TrapJob("Job","The_Odds_Are_Against_You_Red", 1, 0, "Move one of your ringcontainers to your enemy", "JobTheoddsareagainstyou.png")
the_Odds_Are_Against_You_Blue1 = TrapJob("Job","The_Odds_Are_Against_You_Blue", 1, 0, "Move one of your ringcontainers to your enemy", "JobTheoddsareagainstyouFED.png")
the_Odds_Are_Against_You_Blue2 = TrapJob("Job","The_Odds_Are_Against_You_Blue", 1, 0, "Move one of your ringcontainers to your enemy", "JobTheoddsareagainstyouFED.png")

#Traps
ambushed_Red1 = TrapJob("Trap", "Ambushed_Red", 1, 1, "When the enemy plays a job, it will be placed in your hand", "TrapAmbushed.png")
ambushed_Red2 = TrapJob("Trap", "Ambushed_Red", 1, 1, "When the enemy plays a job, it will be placed in your hand", "TrapAmbushed.png")
ambushed_Blue1 = TrapJob("Trap", "Ambushed_Blue", 1, 1, "When the enemy plays a job, it will be placed in your hand", "TrapAmbushedFED.png")
ambushed_Blue2 = TrapJob("Trap", "Ambushed_Blue", 1, 1, "When the enemy plays a job, it will be placed in your hand", "TrapAmbushedFED.png")
dodge_Red1 = TrapJob("Trap", "Dodge_Red", 1, 1, "Your mobster is immune to every 1 cost action when it takes damage", "TrapDodge.png")
dodge_Red2 = TrapJob("Trap", "Dodge_Red", 1, 1, "Your mobster is immune to every 1 cost action when it takes damage", "TrapDodge.png")
dodge_Blue1 = TrapJob("Trap", "Dodge_Blue", 1, 1, "Your mobster is immune to every 1 cost action when it takes damage", "TrapDodgeFED.png")
dodge_Blue2 = TrapJob("Trap", "Dodge_Blue", 1, 1, "Your mobster is immune to every 1 cost action when it takes damage", "TrapDodgeFED.png")
revive_Red1 = TrapJob("Trap", "Revive_Red", 1, 1, "When a mobster dies, revive it", "TrapRevive.png")
revive_Red2 = TrapJob("Trap", "Revive_Red", 1, 1, "When a mobster dies, revive it", "TrapRevive.png")
revive_Blue1 = TrapJob("Trap", "Revive_Blue", 1, 1, "When a mobster dies, revive it", "TrapReviveFED.png")
revive_Blue2 = TrapJob("Trap", "Revive_Blue", 1, 1, "When a mobster dies, revive it", "TrapReviveFED.png")
ricochet_Red1 = TrapJob("Trap", "Ricochet_Red", 1, 1, "When you are attacked, you can attack with the same value or +1 bonus/-1 damage", "TrapRicochet.png")
ricochet_Red2 = TrapJob("Trap", "Ricochet_Red", 1, 1, "When you are attacked, you can attack with the same value or +1 bonus/-1 damage", "TrapRicochet.png")
ricochet_Blue1 = TrapJob("Trap", "Ricochet_Blue", 1, 1, "When you are attacked, you can attack with the same value or +1 bonus/-1 damage", "TrapRicochetFED.png")
ricochet_Blue2 = TrapJob("Trap", "Ricochet_Blue", 1, 1, "When you are attacked, you can attack with the same value or +1 bonus/-1 damage", "TrapRicochetFED.png")
sniped_Red1 = TrapJob("Trap", "Sniped_Red", 1, 1, "When the enemy plays a Mobster, damage one of his hp", "TrapSniped.png")
sniped_Red2 = TrapJob("Trap", "Sniped_Red", 1, 1, "When the enemy plays a Mobster, damage one of his hp", "TrapSniped.png")
sniped_Blue1 = TrapJob("Trap", "Sniped_Blue", 1, 1, "When the enemy plays a Mobster, damage one of his hp", "TrapSnipedFED.png")
sniped_Blue2 = TrapJob("Trap", "Sniped_Blue", 1, 1, "When the enemy plays a Mobster, damage one of his hp", "TrapSnipedFED.png")

#lists Trap cards blue
traps_Blue = [ambushed_Blue1, ambushed_Blue2, dodge_Blue1, dodge_Blue2, revive_Blue1, revive_Blue2, ricochet_Blue1, ricochet_Blue2, sniped_Blue1, sniped_Blue2]

#lists Trap cards red
traps_Red = [ambushed_Red1, ambushed_Red2, dodge_Red1, dodge_Red2, revive_Red1, revive_Red2, ricochet_Red1, ricochet_Red2, sniped_Red1, sniped_Red2]

#lists Job cards blue
jobs_Blue = [anti_Hit_Blue1, anti_Hit_Blue2, clairevoyance_Blue1, clairevoyance_Blue2, prophecy_Blue1, prophecy_Blue2, reroll_Blue1, reroll_Blue2, retaliate_Blue1, retaliate_Blue2, reveal_Blue1, reveal_Blue2, sacrifice_Blue1, sacrifice_Blue2, small_Hit_Blue1, small_Hit_Blue2, stun_Blue1, stun_Blue2, the_Odds_Are_Against_You_Blue1, the_Odds_Are_Against_You_Blue2]

#lists Job cards red
jobs_Red = [anti_Hit_Red1, anti_Hit_Red2, clairevoyance_Red1, clairevoyance_Red2, prophecy_Red1, prophecy_Red2, reroll_Red1, reroll_Red2, retaliate_Red1, retaliate_Red2, reveal_Red1, reveal_Red2, sacrifice_Red1, sacrifice_Red2, small_Hit_Red1, small_Hit_Red2, stun_Red1, stun_Red2, the_Odds_Are_Against_You_Red1, the_Odds_Are_Against_You_Red2]

# Lists mobsters in blue origins
empty = ""
china_Blue = [origin_China_Blue, mss1, mss2, mss3, mss4]
japan_Blue = [origin_Japan_Blue, psia1, psia2, psia3, psia4]
netherlands_Blue = [origin_Netherlands_Blue, aivd1, aivd2, aivd3, aivd4]
colombia_Blue = [origin_Colombia_Blue, dni1, dni2, dni3, dni4]
italy_Blue = [origin_Italy_Blue, sismi1, sismi2, sismi3, sismi4]
russia_Blue = [origin_Russia_Blue, fsb1, fsb2, fsb3, fsb4]

# Lists mobsters in red origins
china_Red = [origin_China_Red, triad1, triad2, triad3, triad4]
japan_Red = [origin_Japan_Red, yakuza1, yakuza2, yakuza3, yakuza4]
netherlands_Red = [origin_Netherlands_Red, farmer1, farmer2, farmer3, farmer4]
colombia_Red = [origin_Colombia_Red, caliKartel1, caliKartel2, caliKartel3, caliKartel4]
italy_Red = [origin_Italy_Red, cosaNostra1, cosaNostra2, cosaNostra3, cosaNostra4]
russia_Red = [origin_Russia_Red, bratva1, bratva2, bratva3, bratva4]

# Lists origins to select voor card selector
fed_origins = [china_Blue, japan_Blue, netherlands_Blue, colombia_Blue, italy_Blue, russia_Blue]
maffia_origins = [china_Red, japan_Red, netherlands_Red, colombia_Red, italy_Red, russia_Red]

# Draw blue origin cards
def DrawFedOriginCards():
    x = 0
    y = 0
    scale(0.3)
    def GetOrigin(i):
        return fed_origins[i]
    for i in range(len(fed_origins)):
        k = GetOrigin(i)
        k[0].display(x, y)
        x = x + 700

# Draw red origin cards
def DrawMaffiaOriginCards():
    x = 0
    y = 0
    scale(0.3)
    def GetOrigin(i):
        return maffia_origins[i]
    for i in range(len(maffia_origins)):
        k = GetOrigin(i)
        k[0].display(x, y)
        x = x + 700

# Draw blue trap cards
def DrawFedTrapCards():
    x = 0
    y = 0
    scale(0.3)
    def GetTrap(i):
        return traps_Blue[i]
    for i in range(len(traps_Blue)):
        if i == 5:
            x = 0
            y = 1100
        traps_Blue[i].display(x, y)
        x = x + 700
        
# Draw red trap cards
def DrawMaffiaTrapCards():
    x = 0
    y = 0
    scale(0.3)
    def GetTrap(i):
        return traps_Red[i]
    for i in range(len(taps_Red)):
        if i == 5:
            x = 0
            y = 1100
        traps_Red[i].display(x, y)
        x = x + 700
        
# Draw blue job cards
def DrawFedJobCards():
    x = 0
    y = 0
    scale(0.3)
    def GetJob(i):
        return jobs_Blue[i]
    for i in range(len(jobs_Blue)):
        if i == 9:
            x = 0
            y = 1100
        if i == 18:
            x = 0
            y = 2200
        jobs_Blue[i].display(x, y)
        x = x + 700

# Draw red job cards
def DrawMaffiaJobCards():
    x = 0
    y = 0
    scale(0.3)
    def GetJob(i):
        return jobs_Red[i]
    for i in range(len(jobs_Red)):
        if i == 9:
            x = 0
            y = 1100
        if i == 18:
            x = 0
            y = 2200
        jobs_Red[i].display(x, y)
        x = x + 700

# Adding fed cards to deck
def DeckAdderFed(c):
    if c == jobs_Blue[0] or c == jobs_Blue[1] or c == jobs_Blue[2] or c == jobs_Blue[3] or c == jobs_Blue[4] or c == jobs_Blue[5] or c == jobs_Blue[6] or c == jobs_Blue[7] or c == jobs_Blue[8] or c == jobs_Blue[9] or c == jobs_Blue[10] or c == jobs_Blue[11] or c == jobs_Blue[12] or c == jobs_Blue[13] or c == jobs_Blue[14] or c == jobs_Blue[15] or c == jobs_Blue[16] or c == jobs_Blue[17] or c == jobs_Blue[18] or c == jobs_Blue[19]:
        TutorialBot.player_deck.append(c)
        jobs_Blue.remove(c)
    elif c <= traps_Blue[0] or c == traps_Blue[1] or c == traps_Blue[2] or c == traps_Blue[3] or c == traps_Blue[4] or c == traps_Blue[5] or c == traps_Blue[6] or c == traps_Blue[7] or c == traps_Blue[8] or c == traps_Blue[9]:
        TutorialBot.player_deck.append(c)
        traps_Blue.remove(c)
    elif c == fed_origins[0] or fed_origins[1] or fed_origins[2] or fed_origins[3] or fed_origins[4]:
        for i in range(len(c)):
            TutorialBot.player_deck.append(i)
        fed_origins.remove(c)
    
    
# Adding maffia cards to deck
def DeckAdderMaffia(c):
    TutorialBot.player_deck.append(c)
    maffia_origins.remove(c)
    
