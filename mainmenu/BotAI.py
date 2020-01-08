import Cards, TutorialBot, CardSelectorFed, CardSelectorMaffia, functions

current_scene = "Decissions"
red_saved_dice_value = 0
blue_saved_dice_value = 0
red_forget_safe_dice_value = 0
blue_forget_safe_dice_value = 0
can_attack_false_turn = 0
can_attack = False
can_reroll = False
bot_deck = []
bot_held_mobster_cards = []
bot_held_trap_cards = []
bot_held_job_cards = []
bot_held_cards = []


def nextPlayerTurn():
    global player, can_attack, turn, action, reroll_amount, redtrap_lifespan, bluetrap_lifespan, current_scene, red_forget_safe_dice_value, red_saved_dice_value, blue_forget_safe_dice_value, blue_saved_dice_value, can_attack_false_turn
    if player == 1:
        current_scene = "Decissions"
        functions.total = 0
        player = 0
        player_graveyard_state.append(len(TutorialBot.player_graveyard))
        if CardSelectorFed.current_card_page == "Red_bot":
            bluetrap_lifespan += 1
        else:
            redtrap_lifespan += 1
        
    else:
        functions.total = 0
        player = 1
        bot_graveyard_state.append(len(TutorialBot.bot_graveyard))
        if CardSelectorFed.current_card_page == "Blue_bot":
            bluetrap_lifespan += 1
        else:
            redtrap_lifespan += 1
    turn += 1    
    can_attack = True
    action = 2
    reroll_amount = 1   
    if turn == red_forget_safe_dice_value:
        red_safe_dice_value = 0
    else:
        redjob_acitvated = True
    if turn == blue_forget_safe_dice_value:
        blue_safe_dice_value = 0
    else:
        bluejob_acitvated = True
    if turn == can_attack_false_turn:
        can_attack = False
    if CardSelectorMaffia.current_card_page == "Blue_bot":
        if len(TutorialBot.player_job_field_cards) ==0:
            redjob_activated = False
        if len(TutorialBot.bot_job_field_cards) ==0:
            bluejob_activated = False
    elif CardSelectorFed.current_card_page == "Red_bot":
        if len(TutorialBot.player_job_field_cards) ==0:
            bluejob_activated = False
        if len(TutorialBot.bot_job_field_cards) ==0:
            redjob_activated = False
    if CardSelectorMaffia.current_card_page == "Blue_bot":
        if len(TutorialBot.player_trap_field_cards) ==0:
            redtrap_lifespan = 0
        if len(TutorialBot.bot_trap_field_cards) ==0:
            bluetrap_lifespan = 0
    elif CardSelectorFed.current_card_page == "Red_bot":
        if len(TutorialBot.player_trap_field_cards) ==0:
            bluetrap_lifespan = 0
        if len(TutorialBot.bot_trap_field_cards) ==0:
            redtrap_lifespan = 0
    for i in TutorialBot.player_mobster_field_cards:
                if i.hp1 == 0 and i.hp2 == 0 and i.hp3 == 0:
                    TutorialBot.player_graveyard.append(i)
                    TutorialBot.player_mobster_field_cards.remove(i)
    for i in TutorialBot.bot_mobster_field_cards:
                if i.hp1 == 0 and i.hp2 == 0 and i.hp3 == 0:
                    TutorialBot.bot_graveyard.append(i)
                    TutorialBot.bot_mobster_field_cards.remove(i)
            
def setup():
    global load_board, player, actions, current_scene, can_attack, can_place_card, redjob_activated, bluejob_activated, \
    end_turn_img, end_turn_img_highlight, turn, reroll_amount, bluetrap_lifespan, redtrap_lifespan, bot_graveyard_state, player_graveyard_state, \
    player_mobster_field_state, bot_mobster_field_state, play_card_img, play_card_img_highlight, attack_img, attack_img_highlight, background_colour_image, \
    red_forget_safe_value, red_saved_dice_value, blue_forget_safe_value, blue_saved_value, can_reroll, reroll_img, reroll_img_highlight, \
    dice_white_1, dice_white_2, dice_white_3, dice_white_4, dice_white_5, dice_white_6, dice_red_1, dice_red_2, dice_red_3, dice_red_4, dice_red_5, dice_red_6, \
    back_img, back_img_highlight, bot_deck, bot_held_mobster_cards, bot_held_trap_cards, bot_held_job_cards, bot_held_cards
    
    dice_white_1 = loadImage("DiceWhite1.png")
    dice_white_2 = loadImage("DiceWhite2.png")
    dice_white_3 = loadImage("DiceWhite3.png")
    dice_white_4 = loadImage("DiceWhite4.png")
    dice_white_5 = loadImage("DiceWhite5.png")
    dice_white_6 = loadImage("DiceWhite6.png")

    dice_red_1 = loadImage("DiceRed1.png")
    dice_red_2 = loadImage("DiceRed2.png")
    dice_red_3 = loadImage("DiceRed3.png")
    dice_red_4 = loadImage("DiceRed4.png")
    dice_red_5 = loadImage("DiceRed5.png")
    dice_red_6 = loadImage("DiceRed6.png")
    
    
    if CardSelectorMaffia.current_card_page == "Blue_bot":
        bot_deck = [Cards.fsb3, Cards.fsb4, Cards.psia1, Cards.psia2, Cards.psia3, Cards.psia4, Cards.anti_Hit_Blue2, Cards.retaliate_Blue1, Cards.reroll_Blue1, Cards.the_Odds_Are_Against_You_Blue1, Cards.revive_Blue1]
        bot_held_mobster_cards = [Cards.fsb3, Cards.fsb4, Cards.psia1, Cards.psia2, Cards.psia3, Cards.psia4]
        bot_held_trap_cards = [Cards.dodge_Blue1, Cards.ricochet_Blue1, Cards.revive_Blue1]
        bot_held_job_cards = [Cards.anti_Hit_Blue1, Cards.anti_Hit_Blue2, Cards.retaliate_Blue1, Cards.reroll_Blue1, Cards.the_Odds_Are_Against_You_Blue1]
        bot_held_cards = [Cards.dodge_Blue1, Cards.ricochet_Blue1, Cards.anti_Hit_Blue1]
        TutorialBot.bot_mobster_field_cards = [Cards.fsb1, Cards.fsb2]
    
    if CardSelectorFed.current_card_page == "Red_bot":
        bot_deck = [Cards.bratva3, Cards.bratva4, Cards.yakuza1, Cards.yakuza2, Cards.yakuza3, Cards.yakuza4, Cards.anti_Hit_Red2, Cards.reroll_Red1, Cards.the_Odds_Are_Against_You_Red1, Cards.revive_Red1]
        bot_held_mobster_cards = [Cards.bratva3, Cards.bratva4, Cards.yakuza1, Cards.yakuza2, Cards.yakuza3, Cards.yakuza4]
        bot_held_trap_cards = [Cards.dodge_Red1, Cards.ricochet_Red1, Cards.revive_Red1]
        bot_held_job_cards = [Cards.anti_Hit_Red1, Cards.anti_Hit_Red2, Cards.retaliate_Red1, Cards.reroll_Red1, Cards.the_Odds_Are_Against_You_Red1]
        bot_held_cards = [Cards.dodge_Red1, Cards.retaliate_Red1, Cards.anti_Hit_Red1]
        TutorialBot.bot_mobster_field_cards = [Cards.bratva1, Cards.bratva2]
        
    can_reroll = False
    back_img = loadImage("BackButton.png")
    back_img_highlight = loadImage("BackButtonHighlight.png")
    reroll_img = loadImage("RerollButton.png")
    attack_img = loadImage("AttackButton.png")
    reroll_img_highlight = loadImage("RerollButtonHighlight.png")
    attack_img_highlight = loadImage("AttackButtonHighlight.png")
    play_card_img = loadImage("PlayCardButton.png")
    play_card_img_highlight = loadImage("PlayCardButtonHighlight.png")
    end_turn_img = loadImage("EndTurnButton.png")
    end_turn_img_highlight = loadImage("EndTurnButtonHighlight.png")
    can_place_card = True
    can_attack = True
    actions = 2
    player = 1
    background_colour_image = loadImage("MainMenuafb2.png")
    redjob_activated = False
    bluejob_activated = False
    turn = 1
    reroll_amount = 1
    bluetrap_lifespan = 0
    redtrap_lifespan = 0
    bot_graveyard_state = []
    player_graveyard_state = []
    bot_mobster_field_state = []
    player_mobster_field_state = []
    
def draw():    
    global player, actions, current_scene, can_attack, can_place_cards, redjob_activated, bluejob_activated, end_turn_img, turn, reroll_amount, \
    bluetrap_lifespan, redtrap_lifespan, bot_graveyard_state, player_graveyard_state, player_mobster_field_state, bot_mobster_field_state, end_turn_img_highlight, \
    play_card_img, play_card_img_highlight, attack_img, attack_img_highlight, background_colour_image, \
    dice_white_1, dice_white_2, dice_white_3, dice_white_4, dice_white_5, dice_white_6, dice_red_1, dice_red_2, dice_red_3, dice_red_4, dice_red_5, dice_red_6, \
    back_img, back_img_highlight, bot_deck, bot_held_mobster_cards, bot_held_trap_cards, bot_held_job_cards, bot_held_cards
    
    # Draws the background
    image(background_colour_image, 0, 0)
    
    # Loads in the correct board for the Bot, playerboard will be the physical board of his choosing
    if CardSelectorMaffia.current_card_page == "Blue_bot":
        image(loadImage("TutorialBotDesignFed.png"), 0, 0)
        
        if current_scene == "Attack" or current_scene =="Reroll" or current_scene =="Reroll2" or current_scene == "Safe Dice":
            if functions.white_dice == 1:
                image(dice_white_1, 0, 0)
            elif functions.white_dice == 2:
                image(dice_white_2, 0, 0)
            elif functions.white_dice == 3:
                image(dice_white_3, 0, 0)
            elif functions.white_dice == 4:
                image(dice_white_4, 0, 0)
            elif functions.white_dice == 5:
                image(dice_white_5, 0, 0)
            elif functions.white_dice == 6:
                image(dice_white_6, 0, 0)
    
            if functions.red_dice == 1:
                image(dice_red_1, 0, 0)
            elif functions.red_dice == 2:
                image(dice_red_2, 0, 0)
            elif functions.red_dice == 3:
                image(dice_red_3, 0, 0)
            elif functions.red_dice == 4:
                image(dice_red_4, 0, 0)
            elif functions.red_dice == 5:
                image(dice_red_5, 0, 0)
            elif functions.red_dice == 6:
                image(dice_red_6, 0, 0)
                
        # Scales the cards to the right sizes.
        scale(0.3)
        
        # Show that there are still cards in the Bot_Deck
        if len(bot_deck) > 0:
            image(loadImage("CardBackBlueSideWays.png"), 325, 2650)
            
        # Shows that there are cards in the graveyard
        if len(TutorialBot.bot_graveyard) > 0 :
            image(loadImage("CardBackBlueSideWays.png"), 325, 1800)
            
        # Shows that there are cards in the bot his hands
        if len(bot_held_cards) > 0 :
            x = 1727
            y = -180
            for i in range(len(bot_held_cards)):
                image(loadImage("CardBackBlue.png"), x, y)
                x = x + 210
        # Shows the trap card on the field
        if len(TutorialBot.bot_trap_field_cards) > 0 :
            image(loadImage("CardBackBlueSideWays.png"), 3260, 1380)
            
        # Shows the job card on the field
        if len(TutorialBot.bot_job_field_cards) > 0 :
            image(loadImage("CardBackBlueSideWays.png"),2080, 1380)
        
        
        
    # Loads in the correct board for the Bot, playerboard will be the physical board of his choosing    
    if CardSelectorFed.current_card_page == "Red_bot":
        image(loadImage("TutorialBotDesignMafia.png"), 0, 0)        
        
        if current_scene == "Attack" or current_scene =="Reroll" or current_scene =="Reroll2" or current_scene == "Safe Dice":
            if functions.white_dice == 1:
                image(dice_white_1, 0, 0)
            elif functions.white_dice == 2:
                image(dice_white_2, 0, 0)
            elif functions.white_dice == 3:
                image(dice_white_3, 0, 0)
            elif functions.white_dice == 4:
                image(dice_white_4, 0, 0)
            elif functions.white_dice == 5:
                image(dice_white_5, 0, 0)
            elif functions.white_dice == 6:
                image(dice_white_6, 0, 0)
    
            if functions.red_dice == 1:
                image(dice_red_1, 0, 0)
            elif functions.red_dice == 2:
                image(dice_red_2, 0, 0)
            elif functions.red_dice == 3:
                image(dice_red_3, 0, 0)
            elif functions.red_dice == 4:
                image(dice_red_4, 0, 0)
            elif functions.red_dice == 5:
                image(dice_red_5, 0, 0)
            elif functions.red_dice == 6:
                image(dice_red_6, 0, 0)           
            
        # Scales the cards to the right sizes.
        scale(0.3)
        
        # Show that there are still cards in the Bot_Deck
        if len(bot_deck) > 0:
            image(loadImage("CardBackRedSideWays.png"), 325, 2650)
            
        # Shows that there are cards in the graveyard
        if len(TutorialBot.bot_graveyard) > 0 :
            image(loadImage("CardBackRedSideWays.png"), 325, 1800)
            
        # Shows that there are cards in the bot his hands
        if len(bot_held_cards) > 0 :
            x = 1727
            y = -180
            for i in range(len(bot_held_cards)):
                image(loadImage("CardBackRed.png"), x, y)
                x = x + 210
        # Shows the trap card on the field
        if len(TutorialBot.bot_trap_field_cards) > 0 :
            image(loadImage("CardBackRedSideWays.png"), 3260, 1380)
            
        # Shows the job card on the field
        if len(TutorialBot.bot_job_field_cards) > 0 :
            image(loadImage("CardBackRedSideWays.png"),2080, 1380)
                
    # Shows the mobster card(s) in the field
    if len(TutorialBot.bot_mobster_field_cards) > 0 :
        x = 1913
        y = 2350
        for i in range(len(TutorialBot.bot_mobster_field_cards)):
            TutorialBot.bot_mobster_field_cards[i].display(x, y)
            x = x + 890
            
    
    
    # Activates card effects
    functions.cardEffectActivator()
    # Checks player turn, if it is not the players turn than executes bot discission maker 
    if player == 1:
        if current_scene == "Decissions":
            scale(3.333333333)
            functions.backgroundTint()
            if turn > 2 and can_attack == True:
                image(attack_img, 0, 0)
                if functions.isMouseWithinSpace2(552, 976, 238, 100):
                    image(attack_img_highlight, 0, 0)
            if can_place_card == True:
                image(play_card_img, 0, 0)
                if functions.isMouseWithinSpace2(829, 973, 238, 100):
                    image(play_card_img_highlight, 0, 0)
            image(end_turn_img, 0, 0)
            if functions.isMouseWithinSpace2(1114, 969, 238, 100):
                image(end_turn_img_highlight, 0, 0)
                
        if current_scene == "Attack":
            scale(3.333333333)
            functions.backgroundTint()
            image(back_img, 0, 0)
            if functions.isMouseWithinSpace2(10, 980, 95, 1070):
                image(back_img_highlight, 0, 0)
            if can_reroll == True:
                image(reroll_img, 0, 0)
                if functions.isMouseWithinSpace2(552, 976, 238, 100):
                    image(reroll_img_highlight, 0, 0)
            scale(0.6)
            x = 100
            y = 450
            for i in range(len(TutorialBot.bot_mobster_field_cards)):
                if functions.total == TutorialBot.bot_mobster_field_cards[i].hp1 or functions.total == TutorialBot.bot_mobster_field_cards[i].hp2 or functions.total == TutorialBot.bot_mobster_field_cards[i].hp3:
                    TutorialBot.bot_mobster_field_cards[i].display(x, y)
                x += 700
            
        if current_scene == "Reroll":
            scale(3.333333333)
            functions.backgroundTint()
            image(back_img, 0, 0)
            if functions.isMouseWithinSpace2(10, 980, 95, 1070):
                image(back_img_highlight, 0, 0)
            if can_reroll == True:
                image(reroll_img, 0, 0)
                if functions.isMouseWithinSpace2(552, 976, 238, 100):
                    image(reroll_img_highlight, 0, 0)
            scale(0.6)
            x = 100
            y = 450
            for i in range(len(TutorialBot.bot_mobster_field_cards)):
                if functions.total == TutorialBot.bot_mobster_field_cards[i].hp1 or functions.total == TutorialBot.bot_mobster_field_cards[i].hp2 or functions.total == TutorialBot.bot_mobster_field_cards[i].hp3:
                    TutorialBot.bot_mobster_field_cards[i].display(x, y)
                x += 700
        
        if current_scene == "Reroll2":
            scale(3.333333333)
            functions.backgroundTint()
            image(back_img, 0, 0)
            if functions.isMouseWithinSpace2(10, 980, 95, 1070):
                image(back_img_highlight, 0, 0)
            if can_reroll == True:
                image(reroll_img, 0, 0)
                if functions.isMouseWithinSpace2(552, 976, 238, 100):
                    image(reroll_img_highlight, 0, 0)
            scale(0.6)
            x = 100
            y = 450
            for i in range(len(TutorialBot.bot_mobster_field_cards)):
                if functions.total == TutorialBot.bot_mobster_field_cards[i].hp1 or functions.total == TutorialBot.bot_mobster_field_cards[i].hp2 or functions.total == TutorialBot.bot_mobster_field_cards[i].hp3:
                    TutorialBot.bot_mobster_field_cards[i].display(x, y)
                x += 700
        
        if current_scene == "Play card":
            scale(3.333333)
            image(back_img, 0, 0)
            if functions.isMouseWithinSpace2(10, 980, 95, 1070):
                image(back_img_highlight, 0, 0)
            scale(0.3)
            x = 100
            y = 450
            for i in range(len(TutorialBot.player_deck)):
                if i == 9:
                    x = 100
                    y = 1550
                TutorialBot.player_deck[i].display(x, y)
                x += 700 
            
        if current_scene == "Safe Dice":
            scale(3.333333333)
            functions.backgroundTint()
        
        if current_scene == "Select_deathcard":
            scale(3.33333)
            functions.backgroundTint()
            x = 500
            y = 666
            scale(0.6)
            for i in range(len(TutorialBot.bot_mobster_field_cards)):
                TutorialBot.bot_mobster_field_cards[i].display(x, y)
                x += 700
        
        if current_scene == "TOAAY":
            scale(3.33333)
            functions.backgroundTint()
            x = 500
            y = 666
            scale(0.6)
            for i in TutorialBot.player_mobster_field_cards:
                if i.hp1 == 0 or i.hp2 == 0 or i.hp3 == 0:
                    i.display(x, y)
                    x += 700
        
        if current_scene == "Sacrifice":
            scale(3.33333)
            functions.backgroundTint()
            x = 500
            y = 666
            scale(0.6)
            for i in TutorialBot.player_mobster_field_cards:
                if i.hp1 > 0 or i.hp2 > 0 or i.hp3 > 0:
                    i.display(x,y)
                    x += 700
                    
        if current_scene == "Retaliate":
            scale(3.33333)
            functions.backgroundTint()
            x = 500
            y = 666
            scale(0.6)
            for i in range(len(TutorialBot.player_mobster_field_cards)):
                TutorialBot.player_mobster_field_cards[i].display(x, y)
                x += 700
    else:
        # Checks if the bot can get a card
        if len(bot_deck) > 0:
            num = int(random(0, len(bot_deck) - 1))
            bot_held_cards.append(bot_deck[num])
            bot_deck.pop(num)
            
        # play Mobstercard check
        if len(TutorialBot.bot_mobster_field_cards) < 3 and len(bot_held_mobster_cards) > 0 and len(bot_held_cards) > 0 and int(random(0,10)) <5:
            num = int(random(0, len(bot_held_mobster_cards) - 1))
            if bot_held_mobster_cards[num] in bot_held_cards:
                TutorialBot.bot_mobster_field_cards.append(bot_held_mobster_cards[num])
                bot_held_cards.remove(bot_held_mobster_cards[num])
                bot_held_mobster_cards.pop(num)
            
        # Play Trapcard check
        if len(TutorialBot.bot_trap_field_cards) < 1 and len(bot_held_trap_cards) > 0 and len(bot_held_cards) > 0 and random(0,10) < 5:
            num = int(random(0, len(bot_held_trap_cards) - 1))
            if bot_held_trap_cards[num] in bot_held_cards:
                TutorialBot.bot_trap_field_cards.append(bot_held_trap_cards[num])
                bot_held_cards.remove(bot_held_trap_cards[num])
                bot_held_trap_cards.pop(num)
            
        # Play Jobcard check
        if len(TutorialBot.bot_job_field_cards) < 1 and len(bot_held_job_cards) > 0 and len(bot_held_cards) > 0 and random(0,10) < 5:
            num = int(random(0, len(bot_held_job_cards) - 1))
            if bot_held_job_cards[num] in bot_held_cards:
                TutorialBot.bot_job_field_cards.append(bot_held_job_cards[num])
                bot_held_cards.remove(bot_held_job_cards[num])
                bot_held_job_cards.pop(num)
            
        # Attack check
        if turn > 2 and len(TutorialBot.player_mobster_field_cards) > 0 and can_attack == True and int(random(0,1)) == 1:
            # if attack check is True than attacks
            functions.roll()
            # checks if the rolled total is the same as the hp of a card
            if functions.total == TutorialBot.player_mobster_field_cards[0].hp1 or functions.total == TutorialBot.player_mobster_field_cards[0].hp2 or functions.total == TutorialBot.player_mobster_field_cards[0].hp3:
                if functions.total == TutorialBot.player_mobster_field_cards[0].hp1:
                    TutorialBot.player_mobster_field_cards[0].hp1 = 0
                elif functions.total == TutorialBot.player_mobster_field_cards[0].hp2:
                    TutorialBot.player_mobster_field_cards[0].hp2 = 0
                elif functions.total == TutorialBot.player_mobster_field_cards[0].hp3:
                    TutorialBot.player_mobster_field_cards[0].hp3 = 0
                nextPlayerTurn()
            elif len(TutorialBot.player_mobster_field_cards) >= 1 and (functions.total == TutorialBot.player_mobster_field_cards[1].hp1 or functions.total == TutorialBot.player_mobster_field_cards[1].hp2 or functions.total == TutorialBot.player_mobster_field_cards[2].hp3):
                if functions.total == TutorialBot.player_mobster_field_cards[0].hp1:
                    TutorialBot.player_mobster_field_cards[1].hp1 = 0
                elif functions.total == TutorialBot.player_mobster_field_cards[0].hp2:
                    TutorialBot.player_mobster_field_cards[1].hp2 = 0
                elif functions.total == TutorialBot.player_mobster_field_cards[0].hp3:
                    TutorialBot.player_mobster_field_cards[1].hp3 = 0
                nextPlayerTurn()
            elif len(TutorialBot.player_mobster_field_cards) == 2 and (functions.total == TutorialBot.player_mobster_field_cards[2].hp1 or functions.total == TutorialBot.player_mobster_field_cards[2].hp2 or functions.total == TutorialBot.player_mobster_field_cards[2].hp3):
                if functions.total == TutorialBot.player_mobster_field_cards[0].hp1:
                    TutorialBot.player_mobster_field_cards[2].hp1 = 0
                elif functions.total == TutorialBot.player_mobster_field_cards[0].hp2:
                    TutorialBot.player_mobster_field_cards[2].hp2 = 0
                elif functions.total == TutorialBot.player_mobster_field_cards[0].hp3:
                    TutorialBot.player_mobster_field_cards[2].hp3 = 0
                nextPlayerTurn()
            else:
                if reroll_amount > 0:
                    functions.reroll()
                    if functions.total == TutorialBot.player_mobster_field_cards[0].hp1 or functions.total == TutorialBot.player_mobster_field_cards[0].hp2 or functions.total == TutorialBot.player_mobster_field_cards[0].hp3:
                        reroll_amount = 0
                        if functions.total == TutorialBot.player_mobster_field_cards[0].hp1:
                            TutorialBot.player_mobster_field_cards[0].hp1 = 0
                        elif functions.total == TutorialBot.player_mobster_field_cards[0].hp2:
                            TutorialBot.player_mobster_field_cards[0].hp2 = 0
                        elif functions.total == TutorialBot.player_mobster_field_cards[0].hp3:
                            TutorialBot.player_mobster_field_cards[0].hp3 = 0
                        nextPlayerTurn()
                    elif len(TutorialBot.player_mobster_field_cards) >= 1 and (functions.total == TutorialBot.player_mobster_field_cards[1].hp1 or functions.total == TutorialBot.player_mobster_field_cards[1].hp2 or functions.total == TutorialBot.player_mobster_field_cards[1].hp3):
                        reroll_amount = 0
                        if functions.total == TutorialBot.player_mobster_field_cards[0].hp1:
                            TutorialBot.player_mobster_field_cards[1].hp1 = 0
                        elif functions.total == TutorialBot.player_mobster_field_cards[0].hp2:
                            TutorialBot.player_mobster_field_cards[1].hp2 = 0
                        elif functions.total == TutorialBot.player_mobster_field_cards[0].hp3:
                            TutorialBot.player_mobster_field_cards[1].hp3 = 0
                        nextPlayerTurn()
                    elif len(TutorialBot.player_mobster_field_cards) == 2 and (functions.total == TutorialBot.player_mobster_field_cards[2].hp1 or functions.total == TutorialBot.player_mobster_field_cards[2].hp2 or functions.total == TutorialBot.player_mobster_field_cards[2].hp3):
                        reroll_amount = 0
                        if functions.total == TutorialBot.player_mobster_field_cards[0].hp1:
                            TutorialBot.player_mobster_field_cards[2].hp1 = 0
                        elif functions.total == TutorialBot.player_mobster_field_cards[0].hp2:
                            TutorialBot.player_mobster_field_cards[2].hp2 = 0
                        elif functions.total == TutorialBot.player_mobster_field_cards[0].hp3:
                            TutorialBot.player_mobster_field_cards[2].hp3 = 0
                        nextPlayerTurn()
                    else:
                        reroll_amount = 0
            can_attack = False
            nextPlayerTurn()
        else:
            nextPlayerTurn()
