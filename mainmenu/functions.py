import Timer, BotAI, TutorialBot, Cards, CardSelectorMaffia, CardSelectorFed

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
        white_dice = int(random(1,7))
    else:
        if BotAI.player == 1 and CardSelectorMaffia.current_card_page == "Blue_bot":
            white_dice = BotAI.red_saved_dice_value
        else:
            white_dice = BotAI.blue_saved_dice_value
        if BotAI.player == 0 and CardSelectorMaffia.current_card_page == "Blue_bot":
            white_dice = BotAI.blue_saved_dice_value
        else:
            white_dice = BotAI.red_saved_dice_value
            
    red_dice = int(random(1,7))
    total = white_dice + red_dice
    #fill(87, 99, 211)
    #textSize(20)
    #text(white_dice, 100, 100)
    #text(red_dice, 100, 200)
    
# Function part two of attack reroll(with origin effects)
def reroll():
    global white_dice, red_dice, total
    red_dice = int(random(1,7))
    total = white_dice + red_dice
    BotAI.reroll_amount -=1
    if BotAI.reroll_amount == 0:
        BotAI.can_reroll = False
        
def cardEffectActivator():
    global clairevoyance_counter, total
    # Checks if there is a trap card on the bots side of the field
    if len(TutorialBot.bot_trap_field_cards) > 1:
        # Blue ambushed is played by the bot, the players job card will be placed in the bots hand 
        if TutorialBot.bot_trap_field_cards[0] == Cards.ambushed_Blue1 or TutorialBot.bot_trap_field_cards[0] == Cards.ambushed_Blue2:
            BotAI.actions -= 1
            if (TutorialBot.player_job_field_cards) == 1:
                BotAI.bot_held_cards.append(TutorialBot.player_trap_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
                bluetrap_lifespan = 2
            if bluetrap_lifespan == 2:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
                BotAI.action
        # If blue dodge is played by the bot, when a one cost action is used that does damage, this will be negated    
        if TutorialBot.bot_trap_field_cards[0] == Cards.dodge_Blue1 or TutorialBot.bot_trap_field_cards[0] == Cards.dodge_Blue2:
            BotAI.actions -= 1
            if player == 1 and roll > 0:
                funtions.roll.total = 0
                bluetrap_lifespan = 2
            if bluetrap_lifespan == 2:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                TutorialBot.bot_trap_field_cards.pop()
        # If blue revive is played by the bot, when a bots mobster card goes into the graveyard it goes back into the field with all lives recovered
        if TutorialBot.bot_trap_field_cards[0] == Cards.revive_Blue1 or TutorialBot.bot_trap_field_cards[0] == Cards.revive_Blue2:
            BotAI.actions -= 1
            n = len(bot_graveyard_state) + redtrap-lifespan - 1
            if len(TutorialBot.bot_graveyard) > bot_graveyard_state[n]:
                TutorialBot.bot_mobster_field_cards.append(TutorialBot.bot_graveyard[-1])    
                bluetrap_lifespan = 2
            if bluetrap_lifespan == 2:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                TutorialBot.bot_trap_field_cards.pop()
        # If blue ricochet is played by the bot, when the player attacks the bot can attack with +1/-1 or the same amount of damage
        if TutorialBot.bot_trap_field_cards[0] == Cards.ricochet_Blue1 or TutorialBot.bot_trap_field_cards[0] == Cards.ricochet_Blue2:
            BotAI.actions -= 1
            if player == 1 and total > 0:
                x = 300
                y = 400
                for i in TutorialBot.bot_mobster_field_cards:
                    if i.hp1 == total -1 or i.hp1 == total or i.hp1 == total + 1:
                        i.display(x, y)
                        x += 210
                    elif i.hp2 == total -1 or i.hp2 == total or i.hp2 == total + 1:
                        i.display(x, y)
                        x += 210
                    elif i.hp3 == total -1 or i.hp3 == total or i.hp3 == total + 1:
                        i.display(x, y)
                        x += 210
                bluetrap_lifespan = 2
            if bluetrap_lifespan == 2:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                TutorialBot.bot_trap_field_cards.pop()
        # If blue sniped is played by the bot, when the player plays a mobstercard the mobster card loses one hp
        if TutorialBot.bot_trap_field_cards[0] == Cards.sniped_Blue1 or TutorialBot.bot_trap_field_cards[0] == Cards.sniped_Blue2:
            BotAI.actions -= 1
            n = len(bot_mobster_field_state) + redtrap_lifespan - 1
            if len(player_mobster_field_state) < player_mobster_field_state[n]:
                BotAI.current_scene = "Sniped"
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
                BotAI.current_scene = ""
        # If red ambushed is played by the bot, when the player plays a job card this card will be placed in the bots hand
        if TutorialBot.bot_trap_field_cards[0] == Cards.ambushed_Red1 or TutorialBot.bot_trap_field_cards[0] == Cards.ambushed_Red2:
            BotAI.actions -= 1
            if (TutorialBot.player_job_field_cards) == 1:
                BotAI.bot_held_cards.append(TutorialBot.player_trap_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
                redtrap_lifespan = 2
            if redtrap_lifespan == 2:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                TutorialBot.bot_trap_field_cards.pop()                
        # If red dodge is played by the bot, when a one cost action is used that does damage, this will be negated     
        if TutorialBot.bot_trap_field_cards[0] == Cards.dodge_Red1 or TutorialBot.bot_trap_field_cards[0] == Cards.dodge_Red2:
            BotAI.actions -= 1
            if player == 1 and roll > 0:
                funtions.roll.total = 0
                redtrap_lifespan = 2
            if redtrap_lifespan == 2:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                TutorialBot.bot_trap_field_cards.pop() 
        # If red revive is played by the bot, when a mobster card goes into the graveyard it goes back into the field with all lives recovered
        if TutorialBot.bot_trap_field_cards[0] == Cards.revive_Red1 or TutorialBot.bot_trap_field_cards[0] == Cards.revive_Red2:
            BotAI.actions -= 1
            n = len(bot_graveyard_state) + redtrap_lifespan - 1
            if len(TutorialBot.bot_graveyard) > bot_graveyard_state[n]:
                TutorialBot.bot_mobster_field_cards.append(TutorialBot.bot_graveyard[-1])         
                redtrap_lifespan = 2
            if redtrap_lifespan == 2:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                TutorialBot.bot_trap_field_cards.pop()    
        # If red ricochet is played by the bot, when the player attacks the bot can attack with +1/-1 or the same amount of damage
        if TutorialBot.bot_trap_field_cards[0] == Cards.ricochet_Red1 or TutorialBot.bot_trap_field_cards[0] == Cards.ricochet_Red2:
            BotAI.actions -= 1
            if player == 1 and total > 0:
                x = 300
                y = 400
                for i in TutorialBot.bot_mobster_field_cards:
                    if i.hp1 == total -1 or i.hp1 == total or i.hp1 == total + 1:
                        i.display(x, y)
                        x += 210
                    elif i.hp2 == total -1 or i.hp2 == total or i.hp2 == total + 1:
                        i.display(x, y)
                        x += 210
                    elif i.hp3 == total -1 or i.hp3 == total or i.hp3 == total + 1:
                        i.display(x, y)
                        x += 210
                redtrap_lifespan = 2
            if redtrap_lifespan == 2:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                TutorialBot.bot_trap_field_cards.pop()
        # If red sniped is playedby the bot, when the enemy plays a mobster the mobster will take 1 damage
        if TutorialBot.bot_trap_field_cards[0] == Cards.sniped_Red1 or TutorialBot.bot_trap_field_cards[0] == Cards.sniped_Red2:
            BotAI.actions -= 1
            n = len(player_mobster_field_state) + redtrap_lifespan - 1
            if len(player_mobster_field_state) < player_mobster_field_state[n]:
                BotAI.current_scene = "Sniped"
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
                BotAI.current_scene = ""
    
    # Checks if there is a trap card on the players side of the field
    if len(TutorialBot.player_trap_field_cards) > 1:
        # If blue ambushed is played by the player, the bots job card will be placed in the bots hand 
        if TutorialBot.player_trap_field_cards[0] == Cards.ambushed_Blue1 or TutorialBot.player_trap_field_cards[0] == Cards.ambushed_Blue2:
            BotAI.actions -= 1
            if (TutorialBot.bot_job_field_cards) == 1:
                TutorialBot.player_hand_held_cards.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
                bluetrap_lifespan = 2
            if bluetrap_lifespan == 2:
                TutorialBot.player_graveyard.append(TutorialBot.player_trap_field_cards[0])
                TutorialBot.bot_trap_field_cards.pop()
        # If blue dodge is played by the player, when a one cost action is used that does damage, this will be negated    
        if TutorialBot.player_trap_field_cards[0] == Cards.dodge_Blue1 or TutorialBot.player_trap_field_cards[0] == Cards.dodge_Blue2:
            BotAI.actions -= 1
            if player == 1 and roll > 0:
                funtions.roll.total = 0
                bluetrap_lifespan = 2
            if bluetrap_lifespan == 2:
                TutorialBot.player_graveyard.append(TutorialBot.player_trap_field_cards[0])
                TutorialBot.player_trap_field_cards.pop()
        # If blue revive is played by the player, when a players mobster card goes into the graveyard it goes back into the field with all lives recovered
        if TutorialBot.player_trap_field_cards[0] == Cards.revive_Blue1 or TutorialBot.player_trap_field_cards[0] == Cards.revive_Blue2:
            BotAI.actions -= 1
            n = len(player_graveyard_state) + redtrap-lifespan - 1
            if len(TutorialBot.player_graveyard) > player_graveyard_state[n]:
                TutorialBot.player_mobster_field_cards.append(TutorialBot.player_graveyard[-1])    
                bluetrap_lifespan = 2
            if bluetrap_lifespan == 2:
                TutorialBot.player_graveyard.append(TutorialBot.player_trap_field_cards[0])
                TutorialBot.player_trap_field_cards.pop()
        # If blue ricochet is played by the player, when the bot attacks the bot can attack with +1/-1 or the same amount of damage
        if TutorialBot.player_trap_field_cards[0] == Cards.ricochet_Blue1 or TutorialBot.player_trap_field_cards[0] == Cards.ricochet_Blue2:
            BotAI.actions -= 1
            if player == 0 and total > 0:
                x = 300
                y = 400
                for i in TutorialBot.bot_mobster_field_cards:
                    if i.hp1 == total -1 or i.hp1 == total or i.hp1 == total + 1:
                        i.display(x, y)
                        x += 210
                    elif i.hp2 == total -1 or i.hp2 == total or i.hp2 == total + 1:
                        i.display(x, y)
                        x += 210
                    elif i.hp3 == total -1 or i.hp3 == total or i.hp3 == total + 1:
                        i.display(x, y)
                        x += 210
                bluetrap_lifespan = 2
            if bluetrap_lifespan == 2:
                TutorialBot.player_graveyard.append(TutorialBot.player_trap_field_cards[0])
                TutorialBot.player_trap_field_cards.pop()
        # If blue sniped is played by the player, when the bot plays a mobstercard the mobster card loses one hp
        if TutorialBot.player_trap_field_cards[0] == Cards.sniped_Blue1 or TutorialBot.player_trap_field_cards[0] == Cards.sniped_Blue2:
            BotAI.actions -= 1
            n = len(bot_mobster_field_state) + redtrap_lifespan - 1
            if len(player_mobster_field_state) < player_mobster_field_state[n]:
                BotAI.current_scene = "Sniped"
                scale(0.7)
                TutorialBot.bot_mobster_field_cards[-1].display(300, 400)
                bluetrap_lifespan = 2
            if BotAI.current_scene == "" and bluetrap_lifespan == 2:
                TutorialBot.player_graveyard.append(TutorialBot.player_trap_field_cards[0])
                TutorialBot.player_trap_field_cards.pop()
                
        # If red ambushed is played by the player, when the bot plays a job card this card will be placed in the players hand
        if TutorialBot.player_trap_field_cards[0] == Cards.ambushed_Red1 or TutorialBot.player_trap_field_cards[0] == Cards.ambushed_Red2:
            BotAI.actions -= 1
            if (TutorialBot.bot_job_field_cards) == 1:
                TutorialBot.player_hand_held_cards.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
                redtrap_lifespan = 2
            if redtrap_lifespan == 2:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                TutorialBot.bot_trap_field_cards.pop()
                                
        # If red dodge is played by the player, when a one cost action is used that does damage, this will be negated     
        if TutorialBot.player_trap_field_cards[0] == Cards.dodge_Red1 or TutorialBot.player_trap_field_cards[0] == Cards.dodge_Red2:
            BotAI.actions -= 1
            if player == 0 and roll > 0:
                funtions.roll.total = 0
                redtrap_lifespan = 2
            if redtrap_lifespan == 2:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                TutorialBot.player_trap_field_cards.pop() 
                    
        # If red revive is played by the player, when a mobster card goes into the graveyard it goes back into the field with all lives recovered
        if TutorialBot.player_trap_field_cards[0] == Cards.revive_Red1 or TutorialBot.player_trap_field_cards[0] == Cards.revive_Red2:
            BotAI.actions -= 1
            n = len(player_graveyard_state) + redtrap_lifespan - 1
            if len(TutorialBot.player_graveyard) > player_graveyard_state[n]:
                TutorialBot.player_mobster_field_cards.append(TutorialBot.player_graveyard[-1])         
                redtrap_lifespan = 2
            if redtrap_lifespan == 2:
                TutorialBot.player_graveyard.append(TutorialBot.player_trap_field_cards[0])
                TutorialBot.player_trap_field_cards.pop()
                        
        # If red ricochet is played by the player, when the bot attacks the player can attack with +1/-1 or the same amount of damage
        if TutorialBot.player_trap_field_cards[0] == Cards.ricochet_Red1 or TutorialBot.player_trap_field_cards[0] == Cards.ricochet_Red2:
            BotAI.actions -= 1
            if player == 0 and total > 0:
                x = 300
                y = 400
                for i in TutorialBot.bot_mobster_field_cards:
                    if i.hp1 == total -1 or i.hp1 == total or i.hp1 == total + 1:
                        i.display(x, y)
                        x += 210
                    elif i.hp2 == total -1 or i.hp2 == total or i.hp2 == total + 1:
                        i.display(x, y)
                        x += 210
                    elif i.hp3 == total -1 or i.hp3 == total or i.hp3 == total + 1:
                        i.display(x, y)
                        x += 210
                redtrap_lifespan = 2
            if redtrap_lifespan == 2:
                TutorialBot.player_graveyard.append(TutorialBot.player_trap_field_cards[0])
                TutorialBot.player_trap_field_cards.pop()
                        
        # If red sniped is played by the player, when the bot plays a mobster the mobster will take 1 damage
        if TutorialBot.player_trap_field_cards[0] == Cards.sniped_Red1 or TutorialBot.player_trap_field_cards[0] == Cards.sniped_Red2:
            BotAI.actions -= 1
            n = len(bot_mobster_field_state) + redtrap_lifespan - 1
            if len(bot_mobster_field_state) > bot_mobster_field_state[n]:
                BotAI.current_scene = "Sniped"
                scale(0.7)
                TutorialBot.bot_mobster_field_cards[-1].display(300, 400)
                redtrap_lifespan = 2
            if BotAI.current_scene == "" and redtrap_lifespan == 2:
                TutorialBot.player_graveyard.append(TutorialBot.player_trap_field_cards[0])
                TutorialBot.player_trap_field_cards.pop()
                BotAI.current_scene = "Game" 
    
    
    
    
    # Checks if there is a job card on the bots side of the field
    if len(TutorialBot.bot_job_field_cards) > 0:
        # If red anti hit is played by the bot, total damage will be -2
        if TutorialBot.bot_job_field_cards[0] == Cards.anti_Hit_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.anti_Hit_Red2:
            if BotAI.redjob_activated == False:
                BotAI.actions -= 1
                total = total -2
                BotAI.redjob_activated = True
            if BotAI.redjob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        # If red prophecy is played by the bot, safes one dice value for the next turn
        elif TutorialBot.bot_job_field_cards[0] == Cards.prophecy_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.prophecy_Red2:
            if BotAI.redjob_activated == False:
                BotAI.actions -= 1
                roll()
                BotAI.current_scene = "Safe Dice"
                BotAI.red_forget_safe_dice_value = BotAI.turn + 3
                BotAI.red_saved_dice_value = white_dice
                BotAI.redjob_activated = True                          
            if BotAI.turn == BotAI.red_forget_safe_dice_value:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
                BotAI.red_forget_safe_dice_value = 0
        # If red reroll is played by the bot, the bot can reroll one extra time
        elif TutorialBot.bot_job_field_cards[0] == Cards.reroll_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.reroll_Red2:
            if BotAI.redjob_activated == False:
                BotAI.actions -= 1
                BotAI.reroll_amount += 1
                BotAI.redjob_activated = True
            if BotAI.redjob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        # if red retaliate is played by the bot, the bot takes one card back into its hand and fully restores it
        elif TutorialBot.bot_job_field_cards[0] == Cards.retaliate_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.retaliate_Red2:
            if BotAI.redjob_activated == False:
                BotAI.actions -= 2
                scale(2)
                x = 100
                y = 100
                for i in range(len(TutorialBot.bot_mobster_field_cards)):
                    TutorialBot.bot_mobster_field_cards[i].display(x, y)
                    x = x + 400
                num = int(random(0, len(TutorialBot.bot_mobster_field_cards)))
                BotAI.bot_held_cards.append(TutorialBot.bot_mobster_field_cards[num])
                BotAI.bot_held_mobster_cards.append(TutorialBot.bot_mobster_field_cards[num])
                TutorialBot.bot_mobster_field_cards.pop(num)
                BotAI.redjob_activated = True
            if BotAI.redjob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        # If red sacrifice is played by the bot, send one of your none damaged cards to the graveyard and kill one of the players mobster cards
        elif TutorialBot.bot_job_field_cards[0] == Cards.sacrifice_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.sacrifice_Red2:
            if TutorialBot.bot_mobster_field_cards[0].hp1 > 0 and TutorialBot.bot_mobster_field_cards[0].hp2 > 0 and TutorialBot.bot_mobster_field_cards[0].hp3 > 0:
                if BotAI.redjob_activated == False:
                    BotAI.actions -= 2
                    scale(2)
                    num = int(random(0, len(TutorialBot.player_mobster_field_cards) - 1))
                    Tutorialbot.player_graveyard.append(TutorialBot.player_mobster_field_Cards[num])
                    TutorialBot.player_mobster_field_Cards.pop(num)
                    BotAI.redjob_activated = True
                if BotAI.redjob_activated == True:
                    TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                    TutorialBot.bot_job_field_cards.pop()
            if TutorialBot.bot_mobster_field_cards[1].hp1 > 0 and TutorialBot.bot_mobster_field_cards[1].hp2 > 0 and TutorialBot.bot_mobster_field_cards[1].hp3 > 0:
                if BotAI.redjob_activated == False:
                    BotAI.actions -= 2
                    scale(2)
                    num = int(random(0, len(TutorialBot.player_mobster_field_cards) - 1))
                    Tutorialbot.player_graveyard.append(TutorialBot.player_mobster_field_Cards[num])
                    TutorialBot.player_mobster_field_Cards.pop(num)
                    BotAI.redjob_activated = True
                if BotAI.redjob_activated == True:
                    TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                    TutorialBot.bot_job_field_cards.pop()                
            if TutorialBot.bot_mobster_field_cards[2].hp1 > 0 and TutorialBot.bot_mobster_field_cards[2].hp2 > 0 and TutorialBot.bot_mobster_field_cards[2].hp3 > 0:
                if BotAI.redjob_activated == False:
                    BotAI.actions -= 2
                    scale(2)
                    num = int(random(0, len(TutorialBot.player_mobster_field_cards) - 1))
                    Tutorialbot.player_graveyard.append(TutorialBot.player_mobster_field_Cards[num])
                    TutorialBot.player_mobster_field_Cards.pop(num)
                    BotAI.redjob_activated = True
                if BotAI.redjob_activated == True:
                    TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                    TutorialBot.bot_job_field_cards.pop()
        # If red small hit is played by the bot, total damage will be +2
        elif TutorialBot.bot_job_field_cards[0] == Cards.small_Hit_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.small_Hit_Red2:
            if BotAI.redjob_activated == False:
                BotAI.actions -= 1
                total += 2
                BotAI.redjob_activated = True
            if BotAI.redjob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        # If Red stun is played by the bot, the player can not attack
        elif TutorialBot.bot_job_field_cards[0] == Cards.stun_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.stun_Red2:
            if BotAI.redjob_activated == False:
                BotAI.actions -= 1
                can_attack_false_turn = turn + 1
                BotAI.redjob_activated =  True
            if BotAI.redjob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        # If red the odds are against you is played by the bot, the moves one of his ringcontainers to you
        elif TutorialBot.bot_job_field_cards[0] == Cards.the_Odds_Are_Against_You_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.the_Odds_Are_Against_You_Red2:
            if BotAI.redjob_activated == False:
                BotAI.actions -= 2
                scale(2)
                x = 300
                y = 400
                for i in TutorialBot.bot_mobster_field_cards:
                    if i.hp1 == 0 or i.hp2 == 0 or i.hp3 == 0:
                        i.display(x, y)
                        x += 130
                BotAI.redjob_activated = True
            if BotAI.redjob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        # If blue anti hit is played by the bot, total damage is -2
        elif TutorialBot.bot_job_field_cards[0] == Cards.anti_Hit_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.anti_Hit_Blue2:
            if BotAI.bluejob_activated == False:
                BotAI.actions -= 1
                total = total -2
                BotAI.bluejob_activated = True
            if BotAI.bluejob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        # If blue prophecy is played by the bot, it safes one of the dices value for next turn
        elif TutorialBot.bot_job_field_cards[0] == Cards.prophecy_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.prophecy_Blue2:
            if BotAI.bluejob_activated == False:
                BotAI.actions -= 1
                roll()
                BotAI.current_scene = "Safe Dice"
                BotAI.blue_forget_safe_dice_value = BotAI.turn + 3
                BotAI.blue_saved_dice_value = white_dice
                BotAI.bluejob_activated = True                          
            if BotAI.turn == BotAI.blue_forget_safe_dice_value:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
                BotAI.blue_forget_safe_dice_value = 0
        # If blue reroll is played by the bot, Can reroll twice
        elif TutorialBot.bot_job_field_cards[0] == Cards.reroll_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.reroll_Blue2:
            if BotAI.bluejob_activated == False:
                BotAI.actions -= 1
                BotAI.reroll_amount += 1
                BotAI.redjob_activated = True
            if BotAI.bluejob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        # If blue retaliate is played by the bot, Take one card back and  reset its health
        elif TutorialBot.bot_job_field_cards[0] == Cards.retaliate_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.retaliate_Blue2:
            if BotAI.bluejob_activated == False:
                BotAI.actions -= 2
                scale(2)
                x = 100
                y = 100
                for i in range(len(TutorialBot.bot_mobster_field_cards)):
                    TutorialBot.bot_mobster_field_cards[i].display(x, y)
                    x = x + 400
                num = int(random(0, len(TutorialBot.bot_mobster_field_cards)))
                BotAI.bot_held_cards.append(TutorialBot.bot_mobster_field_cards[num])
                BotAI.bot_held_mobster_cards.append(TutorialBot.bot_mobster_field_cards[num])
                TutorialBot.bot_mobster_field_cards.pop(num)
                BotAI.bluejob_activated = True
            if BotAI.bluejob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        # If blue sacrifice is played by the bot, kill one of your non damaged mobsters to kill one mobster of the enemy
        elif TutorialBot.bot_job_field_cards[0] == Cards.sacrifice_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.sacrifice_Blue2:
            if TutorialBot.bot_mobster_field_cards[0].hp1 > 0 and TutorialBot.bot_mobster_field_cards[0].hp2 > 0 and TutorialBot.bot_mobster_field_cards[0].hp3 > 0:
                if BotAI.bluejob_activated == False:
                    BotAI.actions -= 2
                    scale(2)
                    num = int(random(0, len(TutorialBot.player_mobster_field_cards) - 1))
                    Tutorialbot.player_graveyard.append(TutorialBot.player_mobster_field_Cards[num])
                    TutorialBot.player_mobster_field_Cards.pop(num)
                    BotAI.bluejob_activated = True
                if BotAI.bluejob_activated == True:
                    TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                    TutorialBot.bot_job_field_cards.pop()
            if TutorialBot.bot_mobster_field_cards[1].hp1 > 0 and TutorialBot.bot_mobster_field_cards[1].hp2 > 0 and TutorialBot.bot_mobster_field_cards[1].hp3 > 0:
                if BotAI.bluejob_activated == False:
                    BotAI.actions -= 2
                    scale(2)
                    num = int(random(0, len(TutorialBot.player_mobster_field_cards) - 1))
                    Tutorialbot.player_graveyard.append(TutorialBot.player_mobster_field_Cards[num])
                    TutorialBot.player_mobster_field_Cards.pop(num)
                    BotAI.bluejob_activated = True
                if BotAI.bluejob_activated == True:
                    TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                    TutorialBot.bot_job_field_cards.pop()                
            if TutorialBot.bot_mobster_field_cards[2].hp1 > 0 and TutorialBot.bot_mobster_field_cards[2].hp2 > 0 and TutorialBot.bot_mobster_field_cards[2].hp3 > 0:
                if BotAI.bluejob_activated == False:
                    BotAI.actions -= 2
                    scale(2)
                    num = int(random(0, len(TutorialBot.player_mobster_field_cards) - 1))
                    Tutorialbot.player_graveyard.append(TutorialBot.player_mobster_field_Cards[num])
                    TutorialBot.player_mobster_field_Cards.pop(num)
                    BotAI.bluejob_activated = True
                if BotAI.bluejob_activated == True:
                    TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                    TutorialBot.bot_job_field_cards.pop()
        # If blue small hit is played by the bot, add +2 bonus damage to total damage
        elif TutorialBot.bot_job_field_cards[0] == Cards.small_Hit_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.small_Hit_Blue2:
            if BotAI.bluejob_activated == False:
                BotAI.actions -= 1
                total += 2
                BotAI.bluejob_activated = True
            if BotAI.bluejob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        # If blue stun is played by the bot, the player can not attack
        elif TutorialBot.bot_job_field_cards[0] == Cards.stun_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.stun_Blue2:
            if BotAI.bluejob_activated == False:
                BotAI.actions -= 1
                can_attack_false_turn = turn + 1
                BotAI.bluejob_activated =  True
            if BotAI.bluejob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        # If blue the odds are against you is played by the bot, the bot moves one of its ring containers to the player
        elif TutorialBot.bot_job_field_cards[0] == Cards.the_Odds_Are_Against_You_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.the_Odds_Are_Against_You_Blue2:
            if BotAI.bluejob_activated == False:
                BotAI.actions -= 2
                scale(2)
                x = 300
                y = 400
                for i in TutorialBot.bot_mobster_field_cards:
                    if i.hp1 == 0 or i.hp2 == 0 or i.hp3 == 0:
                        i.display(x, y)
                        x += 130
                BotAI.bluejob_activated = True
            if BotAI.bluejob_activated == True:
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
                BotAI.actions -= 1
                BotAI.redjob_activated = True
            if BotAI.redjob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
                BotAI.current_scene = "Decissions"
        # If red reveal is played by the player, reveals the trap card of the enemy
        elif TutorialBot.player_job_field_cards[0] == Cards.reveal_Red1 or TutorialBot.player_job_field_cards[0] == Cards.reveal_Red2:
            if BotAI.redjob_activated == False:
                BotAI.actions -= 1
                if len(TutorialBot.bot_trap_field_cards) > 1:
                    scale(2)
                    tutorialBot.bot_trap_field_cards[0].display(300, 400)
                BotAI.redjob_activated = True
            if BotAI.redjob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        # If blue clairevoyance is played by the player, reveals two cards of the players choosing
        elif TutorialBot.player_job_field_cards[0] == Cards.clairevoyance_Blue1 or TutorialBot.player_job_field_cards[0] == Cards.clairevoyance_Blue2:
            if BotAI.bluejob_activated == False:
                clairevoyance_counter = 0
                BotAI.current_scene = "Clairevoyance"
            if clairevoyance_counter == 2:
                BotAI.actions -= 1
                BotAI.bluejob_activated = True
                clairevoyance_counter = 0
            if BotAI.bluejob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        # If blue reveal is played by the player, reveals the trap card of the enemy
        elif TutorialBot.player_job_field_cards[0] == Cards.reveal_Blue1 or TutorialBot.player_job_field_cards[0] == Cards.reveal_Blue2:
            if BotAI.bluejob_activated == False:
                BotAI.actions -= 1
                if len(TutorialBot.bot_trap_field_cards) > 1:
                    scale(2)
                    tutorialBot.bot_trap_field_cards[0].display(300, 400)
                BotAI.bluejob_activated = True
            if BotAI.bluejob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        # If red stun is played by the player, the bot can not attack
        elif TutorialBot.player_job_field_cards[0] == Cards.stun_Red1 or TutorialBot.player_job_field_cards[0] == Cards.stun_Red2:
            if BotAI.redjob_activated == False:
                BotAI.actions -= 1
                can_attack_false_turn = turn + 1
                BotAI.redjob_activated =  True
            if BotAI.redjob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        # If blue stun is played by the player, the bot can not attack
        elif TutorialBot.player_job_field_cards[0] == Cards.stun_Blue1 or TutorialBot.player_job_field_cards[0] == Cards.stun_Blue2:
            if BotAI.bluejob_activated == False:
                BotAI.actions -= 1
                can_attack_false_turn = turn + 1
                BotAI.bluejob_activated =  True
            if BotAI.bluejob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        # If red the odds are against you is played by the player, Move one of the players ring containers to the bot
        elif TutorialBot.player_job_field_cards[0] == Cards.the_Odds_Are_Against_You_Red1 or TutorialBot.player_job_field_cards[0] == Cards.the_Odds_Are_Against_You_Red2:
            if BotAI.redjob_activated == False:
                BotAI.actions -= 2
                BotAI.current_scene = "TOAAY"
                BotAI.redjob_activated = True
            if BotAI.redjob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        #If blue the odds are against you is played by the player, Move one of the players ring containers to the bot
        elif TutorialBot.player_job_field_cards[0] == Cards.the_Odds_Are_Against_You_Blue1 or TutorialBot.player_job_field_cards[0] == Cards.the_Odds_Are_Against_You_Blue2:
            if BotAI.bluejob_activated == False:
                BotAI.actions -= 2
                BotAI.current_scene = "TOAAY"
                scale(2)
                x = 300
                y = 400
                for i in TutorialBot.bot_mobster_field_cards:
                    if i.hp1 == 0 or i.hp2 == 0 or i.hp3 == 0:
                        i.display(x, y)
                        x += 130
                BotAI.bluejob_activated = True
            if BotAI.bluejob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        # If blue anti hit is played by the player, total damage is -2
        elif TutorialBot.player_job_field_cards[0] == Cards.anti_Hit_Blue1 or TutorialBot.player_job_field_cards[0] == Cards.anti_Hit_Blue2:
            if BotAI.bluejob_activated == False:
                BotAI.actions -= 1
                total = total -2
                BotAI.bluejob_activated = True
            if BotAI.bluejob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        # If red anti hit is played by the player, total damage is -2
        elif TutorialBot.player_job_field_cards[0] == Cards.anti_Hit_Blue1 or TutorialBot.player_job_field_cards[0] == Cards.anti_Hit_Blue2:
            if BotAI.redjob_activated == False:
                BotAI.actions -= 1
                total = total -2
                BotAI.redjob_activated = True
            if BotAI.redjob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        # If red reroll is played by the player, the player can reroll one extra time
        elif TutorialBot.player_job_field_cards[0] == Cards.reroll_Red1 or TutorialBot.player_job_field_cards[0] == Cards.reroll_Red2:
            if BotAI.redjob_activated == False:
                BotAI.actions -= 1
                BotAI.reroll_amount += 1
                BotAI.redjob_activated = True
            if BotAI.redjob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        # If blue reroll is played by the player, the player can reroll one extra time
        elif TutorialBot.player_job_field_cards[0] == Cards.reroll_Blue1 or TutorialBot.player_job_field_cards[0] == Cards.reroll_Blue2:
            if BotAI.bluejob_activated == False:
                BotAI.actions -= 1
                BotAI.reroll_amount += 1
                BotAI.bluejob_activated = True
            if BotAI.bluejob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        # If blue small hit is played by the player, add +2 bonus damage to total damage
        elif TutorialBot.player_job_field_cards[0] == Cards.small_Hit_Blue1 or TutorialBot.player_job_field_cards[0] == Cards.small_Hit_Blue2:
            if BotAI.bluejob_activated == False:
                BotAI.actions -= 1
                total += 2
                BotAI.bluejob_activated = True
            if BotAI.bluejob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        # If red small hit is played by the player, add +2 bonus damage to total damage
        elif TutorialBot.player_job_field_cards[0] == Cards.small_Hit_Red1 or TutorialBot.player_job_field_cards[0] == Cards.small_Hit_Red2:
            if BotAI.redjob_activated == False:
                BotAI.actions -= 1
                total += 2
                BotAI.redjob_activated = True
            if BotAI.redjob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
        # If red prophecy is played by the player, safes one dice value for the next turn
        elif TutorialBot.player_job_field_cards[0] == Cards.prophecy_Red1 or TutorialBot.player_job_field_cards[0] == Cards.prophecy_Red2:
            if BotAI.redjob_activated == False:
                BotAI.actions -= 1
                roll()
                BotAI.current_scene = "Safe Dice"
                BotAI.red_forget_safe_dice_value = BotAI.turn + 3
                BotAI.redjob_activated = True                          
            if BotAI.turn == BotAI.red_forget_safe_dice_value:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
                BotAI.red_forget_safe_dice_value = 0
        # If blue prophecy is played by the player, safes one dice value for the next turn
        elif TutorialBot.player_job_field_cards[0] == Cards.prophecy_Blue1 or TutorialBot.player_job_field_cards[0] == Cards.prophecy_Blue2:
            if BotAI.bluejob_activated == False:
                BotAI.actions -= 1
                roll()
                BotAI.current_scene = "Safe Dice"
                BotAI.blue_forget_safe_dice_value = BotAI.turn + 3
                BotAI.bluejob_activated = True                          
            if BotAI.turn == BotAI.blue_forget_safe_dice_value:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
                BotAI.blue_forget_safe_dice_value = 0
        # If blue sacrifice is played by the player, kill one of your non damaged mobsters to kill one mobster of the enemy
        elif TutorialBot.player_job_field_cards[0] == Cards.sacrifice_Blue1 or TutorialBot.player_job_field_cards[0] == Cards.sacrifice_Blue2:
            BotAI.actions -= 2
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
        elif TutorialBot.player_job_field_cards[0] == Cards.sacrifice_Red1 or TutorialBot.player_job_field_cards[0] == Cards.sacrifice_Red2:
            BotAI.actions -= 2
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
        # if red retaliate is played by the player, the player takes one card back into its hand and fully restores it
        elif TutorialBot.player_job_field_cards[0] == Cards.retaliate_Red1 or TutorialBot.player_job_field_cards[0] == Cards.retaliate_Red2:
            BotAI.actions -= 2
            if BotAI.redjob_activated == False:
                BotAI.current_scene = "Retaliate"
            if BotAI.redjob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
                BotAI.current_scene = "Decissions"
        # if blue retaliate is played by the player, the player takes one card back into its hand and fully restores it
        elif TutorialBot.player_job_field_cards[0] == Cards.retaliate_Red1 or TutorialBot.player_job_field_cards[0] == Cards.retaliate_Red2:
            BotAI.actions -= 2
            if BotAI.bluejob_activated == False:
                BotAI.current_scene = "Retaliate"
            if BotAI.bluejob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
                BotAI.current_scene = "Decissions"
        
def hpResetter(x):
    if x == Cards.aivd1:
        if x.hp1 == 0:
            x.hp1 = Cards.aivd1Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.aivd1Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.aivd1Hp.hp3
    if x == Cards.aivd2:
        if x.hp1 == 0:
            x.hp1 = Cards.aivd2Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.aivd2Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.aivd2Hp.hp3
    if x == Cards.aivd3:
        if x.hp1 == 0:
            x.hp1 = Cards.aivd3Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.aivd3Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.aivd3Hp.hp3
    if x == Cards.aivd4:
        if x.hp1 == 0:
            x.hp1 = Cards.aivd4Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.aivd4Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.aivd4Hp.hp3
    if x == Cards.bratva1:
        if x.hp1 == 0:
            x.hp1 = Cards.bratva1Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.bratva1Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.bratva1Hp.hp3
    if x == Cards.bratva2:
        if x.hp1 == 0:
            x.hp1 = Cards.bratva2Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.bratva2Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.bratva2Hp.hp3
    if x == Cards.bratva3:
        if x.hp1 == 0:
            x.hp1 = Cards.bratva3Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.bratva3Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.bratva3Hp.hp3
    if x == Cards.bratva4:
        if x.hp1 == 0:
            x.hp1 = Cards.bratva4Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.bratva4Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.bratva4Hp.hp3
    if x == Cards.cosaNostra1:
        if x.hp1 == 0:
            x.hp1 = Cards.cosaNostra1Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.cosaNostra1Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.cosaNostra1Hp.hp3
    if x == Cards.cosaNostra2:
        if x.hp1 == 0:
            x.hp1 = Cards.cosaNostra2Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.cosaNostra2Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.cosaNostra2Hp.hp3
    if x == Cards.cosaNostra3:
        if x.hp1 == 0:
            x.hp1 = Cards.cosaNostra3Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.cosaNostra3Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.cosaNostra3Hp.hp3
    if x == Cards.cosaNostra4:
        if x.hp1 == 0:
            x.hp1 = Cards.cosaNostra4Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.cosaNostra4Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.cosaNostra4Hp.hp3
    if x == Cards.dni1:
        if x.hp1 == 0:
            x.hp1 = Cards.dni1Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.dni1Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.dni1Hp.hp3
    if x == Cards.dni2:
        if x.hp1 == 0:
            x.hp1 = Cards.dni2Hp.hp1
        x.hp2 = Cards.dni2Hp.hp2
        x.hp3 = Cards.dni2Hp.hp3
    if x == Cards.dni3:
        if x.hp1 == 0:
            x.hp1 = Cards.dni3Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.dni3Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.dni3Hp.hp3
    if x == Cards.dni4:
        if x.hp1 == 0:
            x.hp1 = Cards.dni4Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.dni4Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.dni4Hp.hp3
    if x == Cards.farmer1:
        if x.hp1 == 0:
            x.hp1 = Cards.farmer1Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.farmer1Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.farmer1Hp.hp3
    if x == Cards.farmer2:
        if x.hp1 == 0:
            x.hp1 = Cards.farmer2Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.farmer2Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.farmer2Hp.hp3
    if x == Cards.farmer3:
        if x.hp1 == 0:
            x.hp1 = Cards.farmer3Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.farmer3Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.farmer3Hp.hp3
    if x == Cards.farmer4:
        if x.hp1 == 0:
            x.hp1 = Cards.farmer4Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.farmer4Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.farmer4Hp.hp3
    if x == Cards.fsb1:
        if x.hp1 == 0:
            x.hp1 = Cards.fsb1Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.fsb1Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.fsb1Hp.hp3
    if x == Cards.fsb2:
        if x.hp1 == 0:
            x.hp1 = Cards.fsb2Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.fsb2Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.fsb2Hp.hp3
    if x == Cards.fsb3:
        if x.hp1 == 0:
            x.hp1 = Cards.fsb3Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.fsb3Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.fsb3Hp.hp3
    if x == Cards.fsb4:
        if x.hp1 == 0:
            x.hp1 = Cards.fsb4Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.fsb4Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.fsb4Hp.hp3
    if x == Cards.caliKartel1:
        if x.hp1 == 0:
            x.hp1 = Cards.caliKartel1Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.caliKartel1Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.caliKartel1Hp.hp3
    if x == Cards.caliKartel2:
        if x.hp1 == 0:
            x.hp1 = Cards.caliKartel2Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.caliKartel2Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.caliKartel2Hp.hp3
    if x == Cards.caliKartel3:
        if x.hp1 == 0:
            x.hp1 = Cards.caliKartel3Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.caliKartel3Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.caliKartel3Hp.hp3
    if x == Cards.caliKartel4:
        if x.hp1 == 0:
            x.hp1 = Cards.caliKartel4Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.caliKartel4Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.caliKartel4Hp.hp3
    if x == Cards.mss1:
        if x.hp1 == 0:
            x.hp1 = Cards.mss1Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.mss1Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.mss1Hp.hp3
    if x == Cards.mss2:
        if x.hp1 == 0:
            x.hp1 = Cards.mss2Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.mss2Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.mss2Hp.hp3
    if x == Cards.mss3:
        if x.hp1 == 0:
            x.hp1 = Cards.mss3Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.mss3Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.mss3Hp.hp3
    if x == Cards.mss4:
        if x.hp1 == 0:
            x.hp1 = Cards.mss4Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.mss4Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.mss4Hp.hp3
    if x == Cards.psia1:
        if x.hp1 == 0:
            x.hp1 = Cards.psia1Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.psia1Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.psia1Hp.hp3
    if x == Cards.psia2:
        if x.hp1 == 0:
            x.hp1 = Cards.psia2Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.psia2Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.psia2Hp.hp3
    if x == Cards.psia3:
        if x.hp1 == 0:
            x.hp1 = Cards.psia3Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.psia3Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.psia3Hp.hp3
    if x == Cards.psia4:
        if x.hp1 == 0:
            x.hp1 = Cards.psia4Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.psia4Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.psia4Hp.hp3
    if x == Cards.sismi1:
        if x.hp1 == 0:
            x.hp1 = Cards.sismi1Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.sismi1Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.sismi1Hp.hp3
    if x == Cards.sismi2:
        if x.hp1 == 0:
            x.hp1 = Cards.sismi2Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.sismi2Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.sismi2Hp.hp3
    if x == Cards.sismi3:
        if x.hp1 == 0:
            x.hp1 = Cards.sismi3Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.sismi3Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.sismi3Hp.hp3
    if x == Cards.sismi4:
        if x.hp1 == 0:
            x.hp1 = Cards.sismi4Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.sismi4Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.sismi4Hp.hp3
    if x == Cards.triad1:
        if x.hp1 == 0:
            x.hp1 = Cards.triad1Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.triad1Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.triad1Hp.hp3
    if x == Cards.triad2:
        if x.hp1 == 0:
            x.hp1 = Cards.triad2Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.triad2Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.triad2Hp.hp3
    if x == Cards.triad3:
        if x.hp1 == 0:
            x.hp1 = Cards.triad3Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.triad3Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.triad3Hp.hp3
    if x == Cards.triad4:
        if x.hp1 == 0:
            x.hp1 = Cards.triad4Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.triad4Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.triad4Hp.hp3
    if x == Cards.yakuza1:
        if x.hp1 == 0:
            x.hp1 = Cards.yakuza1Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.yakuza1Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.yakuza1Hp.hp3
    if x == Cards.yakuza2:
        if x.hp1 == 0:
            x.hp1 = Cards.yakuza2Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.yakuza2Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.yakuza2Hp.hp3
    if x == Cards.yakuza3:
        if x.hp1 == 0:
            x.hp1 = Cards.yakuza3Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.yakuza3Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.yakuza3Hp.hp3
    if x == Cards.yakuza4:
        if x.hp1 == 0:
            x.hp1 = Cards.yakuza4Hp.hp1
        elif x.hp2 == 0:
            x.hp2 = Cards.yakuza4Hp.hp2
        elif x.hp3 == 0:
            x.hp3 = Cards.yakuza4Hp.hp3
