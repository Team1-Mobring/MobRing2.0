import Timer, BotAI, TutorialBot, Cards

origin_netherlands_active =  False
origin_colombia_active = False
selected_dice = ""
total = 0
x = 0
clairevoyance_counter = 0

def backgroundTint():
    fill(0, 0, 0, 128)
    rect(0, 0, 1920, 1080)
        
def isMouseWithinSpace2(x, y, w, h):
    if x < mouseX < x + w and y < mouseY < y + h:
        return True
    else:
        return False

def fillZero(time):
    if len(str(time)) < 2:
        time = "0" + str(time)
    return time    

def convertSeconds(m):
    s = m / 1000
    minutes = s // 60
    seconds = s % 60
    return str(fillZero(minutes))+":"+str(fillZero(seconds)) 

def showMilliseconds(x):
    if x == 0:
        return "000"
    else:
        return x

def isShiftPressed():
    def keyPressed():
        if keyCode == 16:
            return True
        
def drawText(word, x, y):
    fill(255)
    #textFont(font)
    text(word, x, y)
    textAlign(CENTER)
    
def drawText2(word, x, y, r, g, b, size):
    textAlign(CENTER)
    textSize(size)
    #textFont(font)
    fill(r, g, b)
    text(word, x, y)
    textAlign(CENTER)

def drawText3(word, x, y, r, g, b, size):
    textSize(size)
    #textFont(font)
    fill(r, g, b)
    text(word, x, y)
    textAlign(LEFT)
    
def drawTextTimer1(word, x, y, r, g, b, size):
    font = loadFont("OCRAExtended-100.vlw")
    textFont(font)
    textSize(size)
    fill(r, g, b)
    textAlign(LEFT)
    text(word, x, y)
    
def drawTextTimer2(word, x, y, r, g, b, size):
    font = loadFont("OCRAExtended-100.vlw")
    textFont(font)
    textSize(size)
    fill(r, g, b)
    textAlign(RIGHT)
    text(word, x, y)
    
def drawScore(word, x, y, r, g, b, size):
    font = loadFont("OCRAExtended-100.vlw")
    textFont(font)
    textSize(size)
    fill(r, g, b)
    textAlign(CENTER)
    text(word, x, y)

# Function to attack with dices
def roll():
    global white_dice, red_dice, total
    if BotAI.red_saved_dice_value == 0 and BotAI.blue_saved_dice_value == 0:
        white_dice = int(random(1,6))
    else:
        if BotAI.player == 1 and CardSelectorMaffia.current_card_page == "Blue_bot":
            white_dice = BotAI.red_saved_dice_value
        else:
            white_dice = BotAI.blue_saved_dice_value
        if BotAI.player == 0 and CardSelectorMaffia.current_card_page == "Blue_bot":
            white_dice = BotAI.blue_saved_dice_value
        else:
            white_dice = BotAI.red_saved_dice_value
            
    red_dice = int(random(1,6))
    total = white_dice + red_dice
    fill(87, 99, 211)
    textSize(20)
    # FixDaDice
    text(white_dice, 100, 100)
    text(red_dice, 100, 200)
    
# Function part two of attack reroll(with origin effects)
def reroll():
    global white_dice, red_dice, total
    if origin_netherlands_active == True:
        fill(87, 99, 211)
        textSize(20)
        text(white_dice, 100, 100)
        text(red_dice, 100, 200)
    elif origin_colombia_active == True:
        if selected_dice == "white":
                fill(87, 99, 211)
                textSize(20)
                text(dice.white_dice, 100, 100)
        else:
                fill(87, 99, 211)
                textSize(20)
                text(red_dice, 100, 200)
    else:
        text(red_dice, 100, 200)
        
def cardEffectActivator():
    global clairevoyance_counter
    # Checks if there is a trap card on the bots side of the field
    if len(TutorialBot.bot_trap_field_cards) > 1:
        # Blue ambushed is played by the bot, the players job card will be placed in the bots hand 
        if TutorialBot.bot_trap_field_cards[0] == Cards.ambushed_Blue1 or TutorialBot.bot_trap_field_cards[0] == Cards.ambushed_Blue2:
            if (TutorialBot.player_job_field_cards) == 1:
                TutorialBot.bot_hand_held_cards.append(TutorialBot.player_trap_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
                bluetrap_lifespan = 2
            if bluetrap_lifespan == 2:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        # If blue dodge is played by the bot, when a one cost action is used that does damage, this will be negated    
        if TutorialBot.bot_trap_field_cards[0] == Cards.dodge_Blue1 or TutorialBot.bot_trap_field_cards[0] == Cards.dodge_Blue2:
            if player == 1 and roll > 0:
                funtions.roll.total = 0
                bluetrap_lifespan = 2
            if bluetrap_lifespan == 2:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                TutorialBot.bot_trap_field_cards.pop()
        # If blue revive is played by the bot, when a bots mobster card goes into the graveyard it goes back into the field with all lives recovered
        if TutorialBot.bot_trap_field_cards[0] == Cards.revive_Blue1 or TutorialBot.bot_trap_field_cards[0] == Cards.revive_Blue2:
            n = len(bot_graveyard_state) + redtrap-lifespan - 1
            if len(TutorialBot.bot_graveyard) > bot_graveyard_state[n]:
                TutorialBot.bot_mobster_field_cards.append(TutorialBot.bot_graveyard[-1])    
                bluetrap_lifespan = 2
            if bluetrap_lifespan == 2:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                TutorialBot.bot_trap_field_cards.pop()
        # If blue ricochet is played by the bot, when the player attacks the bot can attack with +1/-1 or the same amount of damage
        if TutorialBot.bot_trap_field_cards[0] == Cards.ricochet_Blue1 or TutorialBot.bot_trap_field_cards[0] == Cards.ricochet_Blue2:
            if player == 1 and functions.total > 0:
                x = 300
                y = 400
                for i in TutorialBot.bot_mobster_field_cards:
                    if i.hp1 == functions.total -1 or i.hp1 == functions.total or i.hp1 == functions.total + 1:
                        i.display(x, y)
                        x += 210
                    elif i.hp2 == functions.total -1 or i.hp2 == functions.total or i.hp2 == functions.total + 1:
                        i.display(x, y)
                        x += 210
                    elif i.hp3 == functions.total -1 or i.hp3 == functions.total or i.hp3 == functions.total + 1:
                        i.display(x, y)
                        x += 210
                bluetrap_lifespan = 2
            if bluetrap_lifespan == 2:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                TutorialBot.bot_trap_field_cards.pop()
        # If blue sniped is played by the bot, when the player plays a mobstercard the mobster card loses one hp
        if TutorialBot.bot_trap_field_cards[0] == Cards.sniped_Blue1 or TutorialBot.bot_trap_field_cards[0] == Cards.sniped_Blue2:
            n = len(bot_mobster_field_state) + redtrap_lifespan - 1
            if len(player_mobster_field_state) < player_mobster_field_state[n]:
                current_scene = "Sniped"
                scale(0.7)
                TutorialBot.player_mobster_field_cards[-1].display(300, 400)
                if TutorialBot.player_mobster_field_cards[-1].hp1 > 0:
                    TutorialBot.player_mobster_field_cards[-1].hp1 = 0
                elif TutorialBot.player_mobster_field_cards[-1].hp2 > 0:
                    TutorialBot.player_mobster_field_cards[-1].hp2 = 0
                else:
                    TutorialBot.player_mobster_field_cards[-1].hp3 = 0
                bluetrap_lifespan = 2
            if bluetrap_lifespan == 2:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                TutorialBot.bot_trap_field_cards.pop()
                current_scene = ""
        # If red ambushed is played by the bot, when the player plays a job card this card will be placed in the bots hand
        if TutorialBot.bot_trap_field_cards[0] == Cards.ambushed_Red1 or TutorialBot.bot_trap_field_cards[0] == Cards.ambushed_Red2:
            if (TutorialBot.player_job_field_cards) == 1:
                TutorialBot.bot_hand_held_cards.append(TutorialBot.player_trap_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
                redtrap_lifespan = 2
            if redtrap_lifespan == 2:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                TutorialBot.bot_trap_field_cards.pop()                
        # If red dodge is played by the bot, when a one cost action is used that does damage, this will be negated     
        if TutorialBot.bot_trap_field_cards[0] == Cards.dodge_Red1 or TutorialBot.bot_trap_field_cards[0] == Cards.dodge_Red2:
            if player == 1 and roll > 0:
                funtions.roll.total = 0
                redtrap_lifespan = 2
            if redtrap_lifespan == 2:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                TutorialBot.bot_trap_field_cards.pop() 
        # If red revive is played by the bot, when a mobster card goes into the graveyard it goes back into the field with all lives recovered
        if TutorialBot.bot_trap_field_cards[0] == Cards.revive_Red1 or TutorialBot.bot_trap_field_cards[0] == Cards.revive_Red2:
            n = len(bot_graveyard_state) + redtrap_lifespan - 1
            if len(TutorialBot.bot_graveyard) > bot_graveyard_state[n]:
                TutorialBot.bot_mobster_field_cards.append(TutorialBot.bot_graveyard[-1])         
                redtrap_lifespan = 2
            if redtrap_lifespan == 2:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                TutorialBot.bot_trap_field_cards.pop()    
        # If red ricochet is played by the bot, when the player attacks the bot can attack with +1/-1 or the same amount of damage
        if TutorialBot.bot_trap_field_cards[0] == Cards.ricochet_Red1 or TutorialBot.bot_trap_field_cards[0] == Cards.ricochet_Red2:
            if player == 1 and functions.total > 0:
                x = 300
                y = 400
                for i in TutorialBot.bot_mobster_field_cards:
                    if i.hp1 == functions.total -1 or i.hp1 == functions.total or i.hp1 == functions.total + 1:
                        i.display(x, y)
                        x += 210
                    elif i.hp2 == functions.total -1 or i.hp2 == functions.total or i.hp2 == functions.total + 1:
                        i.display(x, y)
                        x += 210
                    elif i.hp3 == functions.total -1 or i.hp3 == functions.total or i.hp3 == functions.total + 1:
                        i.display(x, y)
                        x += 210
                redtrap_lifespan = 2
            if redtrap_lifespan == 2:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                TutorialBot.bot_trap_field_cards.pop()
        # If red sniped is playedby the bot, when the enemy plays a mobster the mobster will take 1 damage
        if TutorialBot.bot_trap_field_cards[0] == Cards.sniped_Red1 or TutorialBot.bot_trap_field_cards[0] == Cards.sniped_Red2:
            n = len(player_mobster_field_state) + redtrap_lifespan - 1
            if len(player_mobster_field_state) < player_mobster_field_state[n]:
                current_scene = "Sniped"
                scale(0.7)
                TutorialBot.player_mobster_field_cards[-1].display(300, 400)
                if TutorialBot.player_mobster_field_cards[-1].hp1 > 0:
                    TutorialBot.player_mobster_field_cards[-1].hp1 = 0
                elif TutorialBot.player_mobster_field_cards[-1].hp2 > 0:
                    TutorialBot.player_mobster_field_cards[-1].hp2 = 0
                else:
                    TutorialBot.player_mobster_field_cards[-1].hp3 = 0
                redtrap_lifespan = 2
            if redtrap_lifespan == 2:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                TutorialBot.bot_trap_field_cards.pop()
                current_scene = ""
    
    # Checks if there is a trap card on the players side of the field
    if len(TutorialBot.player_trap_field_cards) > 1:
        # If blue ambushed is played by the player, the bots job card will be placed in the bots hand 
        if TutorialBot.player_trap_field_cards[0] == Cards.ambushed_Blue1 or TutorialBot.player_trap_field_cards[0] == Cards.ambushed_Blue2:
            if (TutorialBot.bot_job_field_cards) == 1:
                TutorialBot.player_hand_held_cards.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
                bluetrap_lifespan = 2
            if bluetrap_lifespan == 2:
                TutorialBot.player_graveyard.append(TutorialBot.player_trap_field_cards[0])
                TutorialBot.bot_trap_field_cards.pop()
        # If blue dodge is played by the player, when a one cost action is used that does damage, this will be negated    
        if TutorialBot.player_trap_field_cards[0] == Cards.dodge_Blue1 or TutorialBot.player_trap_field_cards[0] == Cards.dodge_Blue2:
            if player == 1 and roll > 0:
                funtions.roll.total = 0
                bluetrap_lifespan = 2
            if bluetrap_lifespan == 2:
                TutorialBot.player_graveyard.append(TutorialBot.player_trap_field_cards[0])
                TutorialBot.player_trap_field_cards.pop()
        # If blue revive is played by the player, when a players mobster card goes into the graveyard it goes back into the field with all lives recovered
        if TutorialBot.player_trap_field_cards[0] == Cards.revive_Blue1 or TutorialBot.player_trap_field_cards[0] == Cards.revive_Blue2:
            n = len(player_graveyard_state) + redtrap-lifespan - 1
            if len(TutorialBot.player_graveyard) > player_graveyard_state[n]:
                TutorialBot.player_mobster_field_cards.append(TutorialBot.player_graveyard[-1])    
                bluetrap_lifespan = 2
            if bluetrap_lifespan == 2:
                TutorialBot.player_graveyard.append(TutorialBot.player_trap_field_cards[0])
                TutorialBot.player_trap_field_cards.pop()
        # If blue ricochet is played by the player, when the bot attacks the bot can attack with +1/-1 or the same amount of damage
        if TutorialBot.player_trap_field_cards[0] == Cards.ricochet_Blue1 or TutorialBot.player_trap_field_cards[0] == Cards.ricochet_Blue2:
            if player == 0 and functions.total > 0:
                x = 300
                y = 400
                for i in TutorialBot.bot_mobster_field_cards:
                    if i.hp1 == functions.total -1 or i.hp1 == functions.total or i.hp1 == functions.total + 1:
                        i.display(x, y)
                        x += 210
                    elif i.hp2 == functions.total -1 or i.hp2 == functions.total or i.hp2 == functions.total + 1:
                        i.display(x, y)
                        x += 210
                    elif i.hp3 == functions.total -1 or i.hp3 == functions.total or i.hp3 == functions.total + 1:
                        i.display(x, y)
                        x += 210
                bluetrap_lifespan = 2
            if bluetrap_lifespan == 2:
                TutorialBot.player_graveyard.append(TutorialBot.player_trap_field_cards[0])
                TutorialBot.player_trap_field_cards.pop()
        # If blue sniped is played by the player, when the bot plays a mobstercard the mobster card loses one hp
        if TutorialBot.player_trap_field_cards[0] == Cards.sniped_Blue1 or TutorialBot.player_trap_field_cards[0] == Cards.sniped_Blue2:
            n = len(bot_mobster_field_state) + redtrap_lifespan - 1
            if len(player_mobster_field_state) < player_mobster_field_state[n]:
                current_scene = "Sniped"
                scale(0.7)
                TutorialBot.bot_mobster_field_cards[-1].display(300, 400)
                bluetrap_lifespan = 2
            if current_scene == "" and bluetrap_lifespan == 2:
                TutorialBot.player_graveyard.append(TutorialBot.player_trap_field_cards[0])
                TutorialBot.player_trap_field_cards.pop()
                
        # If red ambushed is played by the player, when the bot plays a job card this card will be placed in the players hand
        if TutorialBot.player_trap_field_cards[0] == Cards.ambushed_Red1 or TutorialBot.player_trap_field_cards[0] == Cards.ambushed_Red2:
            if (TutorialBot.bot_job_field_cards) == 1:
                TutorialBot.player_hand_held_cards.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
                redtrap_lifespan = 2
            if redtrap_lifespan == 2:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                TutorialBot.bot_trap_field_cards.pop()
                                
        # If red dodge is played by the player, when a one cost action is used that does damage, this will be negated     
        if TutorialBot.player_trap_field_cards[0] == Cards.dodge_Red1 or TutorialBot.player_trap_field_cards[0] == Cards.dodge_Red2:
            if player == 0 and roll > 0:
                funtions.roll.total = 0
                redtrap_lifespan = 2
            if redtrap_lifespan == 2:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                TutorialBot.player_trap_field_cards.pop() 
                    
        # If red revive is played by the player, when a mobster card goes into the graveyard it goes back into the field with all lives recovered
        if TutorialBot.player_trap_field_cards[0] == Cards.revive_Red1 or TutorialBot.player_trap_field_cards[0] == Cards.revive_Red2:
            n = len(player_graveyard_state) + redtrap_lifespan - 1
            if len(TutorialBot.player_graveyard) > player_graveyard_state[n]:
                TutorialBot.player_mobster_field_cards.append(TutorialBot.player_graveyard[-1])         
                redtrap_lifespan = 2
            if redtrap_lifespan == 2:
                TutorialBot.player_graveyard.append(TutorialBot.player_trap_field_cards[0])
                TutorialBot.player_trap_field_cards.pop()
                        
        # If red ricochet is played by the player, when the bot attacks the player can attack with +1/-1 or the same amount of damage
        if TutorialBot.player_trap_field_cards[0] == Cards.ricochet_Red1 or TutorialBot.player_trap_field_cards[0] == Cards.ricochet_Red2:
            if player == 0 and functions.total > 0:
                x = 300
                y = 400
                for i in TutorialBot.bot_mobster_field_cards:
                    if i.hp1 == functions.total -1 or i.hp1 == functions.total or i.hp1 == functions.total + 1:
                        i.display(x, y)
                        x += 210
                    elif i.hp2 == functions.total -1 or i.hp2 == functions.total or i.hp2 == functions.total + 1:
                        i.display(x, y)
                        x += 210
                    elif i.hp3 == functions.total -1 or i.hp3 == functions.total or i.hp3 == functions.total + 1:
                        i.display(x, y)
                        x += 210
                redtrap_lifespan = 2
            if redtrap_lifespan == 2:
                TutorialBot.player_graveyard.append(TutorialBot.player_trap_field_cards[0])
                TutorialBot.player_trap_field_cards.pop()
                        
        # If red sniped is played by the player, when the bot plays a mobster the mobster will take 1 damage
        if TutorialBot.player_trap_field_cards[0] == Cards.sniped_Red1 or TutorialBot.player_trap_field_cards[0] == Cards.sniped_Red2:
            n = len(bot_mobster_field_state) + redtrap_lifespan - 1
            if len(bot_mobster_field_state) > bot_mobster_field_state[n]:
                current_scene = "Sniped"
                scale(0.7)
                TutorialBot.bot_mobster_field_cards[-1].display(300, 400)
                redtrap_lifespan = 2
            if current_scene == "" and redtrap_lifespan == 2:
                TutorialBot.player_graveyard.append(TutorialBot.player_trap_field_cards[0])
                TutorialBot.player_trap_field_cards.pop()
                current_scene = "Game" 
    
    
    
    
    # Checks if there is a job card on the bots side of the field
    if len(TutorialBot.bot_job_field_cards) > 0:
        # If red anti hit is played by the bot, total damage will be -2
        if TutorialBot.bot_job_field_cards[0] == Cards.anti_Hit_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.anti_Hit_Red2:
            if redjob_activated == False:
                functions.roll.total = functions.roll.total -2
                redjob_activated = True
            if redjob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        # If red prophecy is played by the bot, safes one dice value for the next turn
        if TutorialBot.bot_job_field_cards[0] == Cards.prophecy_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.prophecy_Red2:
            if redjob_activated == False:
                current_scene = "Safe Dice"
                red_forget_safe_dice_value = turn + 3
                red_saved_dice_value = white_dice
                redjob_activated = True                          
            if turn == forget_safe_dice_value:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
                red_forget_safe_dice_value = 0
        # If red reroll is played by the bot, the bot can reroll one extra time
        if TutorialBot.bot_job_field_cards[0] == Cards.reroll_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.reroll_Red2:
            if redjob_activated == False:
                reroll_amount = 2
                redjob_activated = True
            if redjob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        # if red retaliate is played by the bot, the bot takes one card back into its hand and fully restores it
        if TutorialBot.bot_job_field_cards[0] == Cards.retaliate_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.retaliate_Red2:
            if redjob_activated == False:
                scale(2)
                x = 100
                y = 100
                for i in range(len(TutorialBot.bot_mobster_field_cards)):
                    TutorialBot.bot_mobster_field_cards[i].display(x, y)
                    x = x + 400
                num = random(0, len(TutorialBot.bot_mobster_field_cards))
                TutorialBot.bot_held_cards.append(TutorialBot.bot_mobster_field_cards[num])
                TutorialBot.bot_held_mobster_cards.append(TutorialBot.bot_mobster_field_cards[num])
                TutorialBot.bot_mobster_field_cards.pop(num)
                redjob_activated = True
            if redjob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_mobster_field_cards[num])
                TutorialBot.bot_job_field_cards.pop()
        # If red sacrifice is played by the bot, send one of your none damaged cards to the graveyard and kill one of the players mobster cards
        if TutorialBot.bot_job_field_cards[0] == Cards.sacrifice_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.sacrifice_Red2:
            if TutorialBot.bot_mobster_field_cards[0].hp1 > 0 and TutorialBot.bot_mobster_field_cards[0].hp2 > 0 and TutorialBot.bot_mobster_field_cards[0].hp3 > 0:
                if redjob_activated == False:
                    scale(2)
                    num = random(0, len(TutorialBot.player_mobster_field_cards) - 1)
                    Tutorialbot.player_graveyard.append(TutorialBot.player_mobster_field_Cards[num])
                    TutorialBot.player_mobster_field_Cards.pop(num)
                    redjob_activated = True
                if redjob_activated == True:
                    TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                    TutorialBot.bot_job_field_cards.pop()
            if TutorialBot.bot_mobster_field_cards[1].hp1 > 0 and TutorialBot.bot_mobster_field_cards[1].hp2 > 0 and TutorialBot.bot_mobster_field_cards[1].hp3 > 0:
                if redjob_activated == False:
                    scale(2)
                    num = random(0, len(TutorialBot.player_mobster_field_cards) - 1)
                    Tutorialbot.player_graveyard.append(TutorialBot.player_mobster_field_Cards[num])
                    TutorialBot.player_mobster_field_Cards.pop(num)
                    redjob_activated = True
                if redjob_activated == True:
                    TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                    TutorialBot.bot_job_field_cards.pop()                
            if TutorialBot.bot_mobster_field_cards[2].hp1 > 0 and TutorialBot.bot_mobster_field_cards[2].hp2 > 0 and TutorialBot.bot_mobster_field_cards[2].hp3 > 0:
                if redjob_activated == False:
                    scale(2)
                    num = random(0, len(TutorialBot.player_mobster_field_cards) - 1)
                    Tutorialbot.player_graveyard.append(TutorialBot.player_mobster_field_Cards[num])
                    TutorialBot.player_mobster_field_Cards.pop(num)
                    redjob_activated = True
                if redjob_activated == True:
                    TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                    TutorialBot.bot_job_field_cards.pop()
        # If red small hit is played by the bot, total damage will be +2
        if TutorialBot.bot_job_field_cards[0] == Cards.small_Hit_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.small_Hit_Red2:
            if redjob_activated == False:
                functions.total += 2
                redjob_activated = True
            if redjob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        # If Red stun is played by the bot, the player can not attack
        if TutorialBot.bot_job_field_cards[0] == Cards.stun_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.stun_Red2:
            if redjob_activated == False:
                can_attack_false_turn = turn + 1
                redjob_activated =  True
            if redjob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        # If red the odds are against you is played by the bot, the moves one of his ringcontainers to you
        if TutorialBot.bot_job_field_cards[0] == Cards.the_Odds_Are_Against_You_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.the_Odds_Are_Against_You_Red2:
            if redjob_activated == False:
                scale(2)
                x = 300
                y = 400
                for i in TutorialBot.bot_mobster_field_cards:
                    if i.hp1 == 0 or i.hp2 == 0 or i.hp3 == 0:
                        i.display(x, y)
                        x += 130
                redjob_activated = True
            if redjob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        # If blue anti hit is played by the bot, total damage is -2
        if TutorialBot.bot_job_field_cards[0] == Cards.anti_Hit_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.anti_Hit_Blue2:
            if bluejob_activated == False:
                functions.roll.total = functions.roll.total -2
                bluejob_activated = True
            if bluejob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        # If blue prophecy is played by the bot, it safes one of the dices value for next turn
        if TutorialBot.bot_job_field_cards[0] == Cards.prophecy_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.prophecy_Blue2:
            if bluejob_activated == False:
                current_scene = "Safe Dice"
                blue_forget_safe_dice_value = turn + 3
                blue_saved_dice_value = white_dice
                bluejob_activated = True                          
            if turn == forget_safe_dice_value:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
                blue_forget_safe_dice_value = 0
        # If blue reroll is played by the bot, Can reroll twice
        if TutorialBot.bot_job_field_cards[0] == Cards.reroll_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.reroll_Blue2:
            if bluejob_activated == False:
                reroll_amount = 2
                redjob_activated = True
            if bluejob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        # If blue retaliate is played by the bot, Take one card back and  reset its health
        if TutorialBot.bot_job_field_cards[0] == Cards.retaliate_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.retaliate_Blue2:
            if bluejob_activated == False:
                scale(2)
                x = 100
                y = 100
                for i in range(len(TutorialBot.bot_mobster_field_cards)):
                    TutorialBot.bot_mobster_field_cards[i].display(x, y)
                    x = x + 400
                num = random(0, len(TutorialBot.bot_mobster_field_cards))
                TutorialBot.bot_held_cards.append(TutorialBot.bot_mobster_field_cards[num])
                TutorialBot.bot_held_mobster_cards.append(TutorialBot.bot_mobster_field_cards[num])
                TutorialBot.bot_mobster_field_cards.pop(num)
                bluejob_activated = True
            if bluejob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_mobster_field_cards[num])
                TutorialBot.bot_job_field_cards.pop()
        # If blue sacrifice is played by the bot, kill one of your non damaged mobsters to kill one mobster of the enemy
        if TutorialBot.bot_job_field_cards[0] == Cards.sacrifice_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.sacrifice_Blue2:
            if TutorialBot.bot_mobster_field_cards[0].hp1 > 0 and TutorialBot.bot_mobster_field_cards[0].hp2 > 0 and TutorialBot.bot_mobster_field_cards[0].hp3 > 0:
                if bluejob_activated == False:
                    scale(2)
                    num = random(0, len(TutorialBot.player_mobster_field_cards) - 1)
                    Tutorialbot.player_graveyard.append(TutorialBot.player_mobster_field_Cards[num])
                    TutorialBot.player_mobster_field_Cards.pop(num)
                    bluejob_activated = True
                if bluejob_activated == True:
                    TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                    TutorialBot.bot_job_field_cards.pop()
            if TutorialBot.bot_mobster_field_cards[1].hp1 > 0 and TutorialBot.bot_mobster_field_cards[1].hp2 > 0 and TutorialBot.bot_mobster_field_cards[1].hp3 > 0:
                if bluejob_activated == False:
                    scale(2)
                    num = random(0, len(TutorialBot.player_mobster_field_cards) - 1)
                    Tutorialbot.player_graveyard.append(TutorialBot.player_mobster_field_Cards[num])
                    TutorialBot.player_mobster_field_Cards.pop(num)
                    bluejob_activated = True
                if bluejob_activated == True:
                    TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                    TutorialBot.bot_job_field_cards.pop()                
            if TutorialBot.bot_mobster_field_cards[2].hp1 > 0 and TutorialBot.bot_mobster_field_cards[2].hp2 > 0 and TutorialBot.bot_mobster_field_cards[2].hp3 > 0:
                if bluejob_activated == False:
                    scale(2)
                    num = random(0, len(TutorialBot.player_mobster_field_cards) - 1)
                    Tutorialbot.player_graveyard.append(TutorialBot.player_mobster_field_Cards[num])
                    TutorialBot.player_mobster_field_Cards.pop(num)
                    bluejob_activated = True
                if bluejob_activated == True:
                    TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                    TutorialBot.bot_job_field_cards.pop()
        # If blue small hit is played by the bot, add +2 bonus damage to total damage
        if TutorialBot.bot_job_field_cards[0] == Cards.small_Hit_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.small_Hit_Blue2:
            if bluejob_activated == False:
                functions.total += 2
                bluejob_activated = True
            if bluejob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        # If blue stun is played by the bot, the player can not attack
        if TutorialBot.bot_job_field_cards[0] == Cards.stun_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.stun_Blue2:
            if bluejob_activated == False:
                can_attack_false_turn = turn + 1
                bluejob_activated =  True
            if bluejob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        # If blue the odds are against you is played by the bot, the bot moves one of its ring containers to the player
        if TutorialBot.bot_job_field_cards[0] == Cards.the_Odds_Are_Against_You_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.the_Odds_Are_Against_You_Blue2:
            if bluejob_activated == False:
                scale(2)
                x = 300
                y = 400
                for i in TutorialBot.bot_mobster_field_cards:
                    if i.hp1 == 0 or i.hp2 == 0 or i.hp3 == 0:
                        i.display(x, y)
                        x += 130
                bluejob_activated = True
            if bluejob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        
    # Checks if there is a job card on the players side of the field
    if len(TutorialBot.player_job_field_cards) > 0:
        # If red clairevoyance is played by the player, reveals two cards of the players choosing
        if TutorialBot.player_job_field_cards[0] == Cards.clairevoyance_Red1 or TutorialBot.player_job_field_cards[0] == Cards.clairevoyance_Red2:
            if BotAI.redjob_activated == False:
                clairevoyance_counter = 0
                BotAI.current_scene = "Clairevoyance"
            if clairevoyance_counter == 2:
                BotAI.redjob_activated = True
            if BotAI.redjob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
                BotAI.current_scene = "Decissions"
        # If red reveal is played by the player, reveals the trap card of the enemy
        if TutorialBot.player_job_field_cards[0] == Cards.reveal_Red1 or TutorialBot.player_job_field_cards[0] == Cards.reveal_Red2:
            if redjob_activated == False:
                if len(TutorialBot.bot_trap_field_cards) > 1:
                    scale(2)
                    tutorialBot.bot_trap_field_cards[0].display(300, 400)
                redjob_activated = True
            if redjob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        # If blue clairevoyance is played by the player, reveals two cards of the players choosing
        if TutorialBot.player_job_field_cards[0] == Cards.clairevoyance_Blue1 or TutorialBot.player_job_field_cards[0] == Cards.clairevoyance_Blue2:
            if bluejob_activated == False:
                clairevoyance_counter = 0
                BotAI.current_scene = "Clairevoyance"
            if clairevoyance_counter == 2:
                bluejob_activated = True
                clairevoyance_counter = 0
            if bluejob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        # If blue reveal is played by the player, reveals the trap card of the enemy
        if TutorialBot.player_job_field_cards[0] == Cards.reveal_Blue1 or TutorialBot.player_job_field_cards[0] == Cards.reveal_Blue2:
            if bluejob_activated == False:
                if len(TutorialBot.bot_trap_field_cards) > 1:
                    scale(2)
                    tutorialBot.bot_trap_field_cards[0].display(300, 400)
                bluejob_activated = True
            if bluejob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        # If red stun is played by the player, the bot can not attack
        if TutorialBot.player_job_field_cards[0] == Cards.stun_Red1 or TutorialBot.player_job_field_cards[0] == Cards.stun_Red2:
            if redjob_activated == False:
                can_attack_false_turn = turn + 1
                redjob_activated =  True
            if redjob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        # If blue stun is played by the player, the bot can not attack
        if TutorialBot.player_job_field_cards[0] == Cards.stun_Blue1 or TutorialBot.player_job_field_cards[0] == Cards.stun_Blue2:
            if bluejob_activated == False:
                can_attack_false_turn = turn + 1
                bluejob_activated =  True
            if bluejob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        #If red the odds are against you is played by the player, Move one of the players ring containers to the bot
        if TutorialBot.player_job_field_cards[0] == Cards.the_Odds_Are_Against_You_Red1 or TutorialBot.player_job_field_cards[0] == Cards.the_Odds_Are_Against_You_Red2:
            if redjob_activated == False:
                scale(2)
                x = 300
                y = 400
                for i in TutorialBot.bot_mobster_field_cards:
                    if i.hp1 == 0 or i.hp2 == 0 or i.hp3 == 0:
                        i.display(x, y)
                        x += 130
                redjob_activated = True
            if redjob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        #If blue the odds are against you is played by the player, Move one of the players ring containers to the bot
        if TutorialBot.player_job_field_cards[0] == Cards.the_Odds_Are_Against_You_Blue1 or TutorialBot.player_job_field_cards[0] == Cards.the_Odds_Are_Against_You_Blue2:
            if bluejob_activated == False:
                scale(2)
                x = 300
                y = 400
                for i in TutorialBot.bot_mobster_field_cards:
                    if i.hp1 == 0 or i.hp2 == 0 or i.hp3 == 0:
                        i.display(x, y)
                        x += 130
                bluejob_activated = True
            if bluejob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
         # If blue anti hit is played by the player, total damage is -2
        if TutorialBot.player_job_field_cards[0] == Cards.anti_Hit_Blue1 or TutorialBot.player_job_field_cards[0] == Cards.anti_Hit_Blue2:
            if bluejob_activated == False:
                functions.roll.total = functions.roll.total -2
                bluejob_activated = True
            if bluejob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        # If red anti hit is played by the player, total damage is -2
        if TutorialBot.player_job_field_cards[0] == Cards.anti_Hit_Blue1 or TutorialBot.player_job_field_cards[0] == Cards.anti_Hit_Blue2:
            if redjob_activated == False:
                functions.roll.total = functions.roll.total -2
                redjob_activated = True
            if redjob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        # If red reroll is played by the player, the player can reroll one extra time
        if TutorialBot.player_job_field_cards[0] == Cards.reroll_Red1 or TutorialBot.player_job_field_cards[0] == Cards.reroll_Red2:
            if redjob_activated == False:
                reroll_amount = 2
                redjob_activated = True
            if redjob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        # If blue reroll is played by the player, the player can reroll one extra time
        if TutorialBot.player_job_field_cards[0] == Cards.reroll_Red1 or TutorialBot.player_job_field_cards[0] == Cards.reroll_Red2:
            if bluejob_activated == False:
                reroll_amount = 2
                bluejob_activated = True
            if bluejob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        # If blue small hit is played by the player, add +2 bonus damage to total damage
        if TutorialBot.player_job_field_cards[0] == Cards.small_Hit_Blue1 or TutorialBot.player_job_field_cards[0] == Cards.small_Hit_Blue2:
            if bluejob_activated == False:
                functions.total += 2
                bluejob_activated = True
            if bluejob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        # If red small hit is played by the player, add +2 bonus damage to total damage
        if TutorialBot.player_job_field_cards[0] == Cards.small_Hit_Red1 or TutorialBot.player_job_field_cards[0] == Cards.small_Hit_Red2:
            if redjob_activated == False:
                functions.total += 2
                redjob_activated = True
            if redjob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        # If red prophecy is played by the player, safes one dice value for the next turn
        if TutorialBot.player_job_field_cards[0] == Cards.prophecy_Red1 or TutorialBot.player_job_field_cards[0] == Cards.prophecy_Red2:
            if redjob_activated == False:
                current_scene = "Safe Dice"
                red_forget_safe_dice_value = turn + 3
                redjob_activated = True                          
            if turn == forget_safe_dice_value:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
                red_forget_safe_dice_value = 0
        # If blue prophecy is played by the player, safes one dice value for the next turn
        if TutorialBot.player_job_field_cards[0] == Cards.prophecy_Blue1 or TutorialBot.player_job_field_cards[0] == Cards.prophecy_Blue2:
            if bluejob_activated == False:
                current_scene = "Safe Dice"
                blue_forget_safe_dice_value = turn + 3
                bluejob_activated = True                          
            if turn == forget_safe_dice_value:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
                red_forget_safe_dice_value = 0
        # If blue sacrifice is played by the player, kill one of your non damaged mobsters to kill one mobster of the enemy
        if TutorialBot.player_job_field_cards[0] == Cards.sacrifice_Blue1 or TutorialBot.player_job_field_cards[0] == Cards.sacrifice_Blue2:
            x = 300
            y = 400
            for i in range(len(TutorialBot.player_mobster_field_cards)):
                if TutorialBot.player_mobster_field_cards[i].hp1 > 0 and TutorialBot.player_mobster_field_cards[i].hp2 > 0 and TutorialBot.player_mobster_field_cards[i].hp3 > 0:
                    BotAI.current_scene = "Sacrifice"
                    if BotAI.current_scene == "Sacrifice" and BotAI.bluejob_activated == False:
                        scale(2)
                        TutorialBot.player_mobster_field_cards[i].display(x, y)
                        x += 130
                    if BotAI.bluejob_activated == True:
                        TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                        TutorialBot.player_job_field_cards.pop()
                        BotAI.current_scene = "Decissions"
        # If red sacrifice is played by the player, kill one of your non damaged mobsters to kill one mobster of the enemy
        if TutorialBot.player_job_field_cards[0] == Cards.sacrifice_Red1 or TutorialBot.player_job_field_cards[0] == Cards.sacrifice_Red2:
            x = 300
            y = 400
            for i in range(len(TutorialBot.player_mobster_field_cards)):
                if TutorialBot.player_mobster_field_cards[i].hp1 > 0 and TutorialBot.player_mobster_field_cards[i].hp2 > 0 and TutorialBot.player_mobster_field_cards[i].hp3 > 0:
                    BotAI.current_scene = "Sacrifice"
                    if BotAI.current_scene == "Sacrifice" and BotAI.redjob_activated == False:
                        scale(2)
                        TutorialBot.player_mobster_field_cards[i].display(x, y)
                        x += 130
                    if BotAI.redjob_activated == True:
                        TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                        TutorialBot.player_job_field_cards.pop()
                        BotAI.current_scene = "Decissions"
        
        
        
        
        
