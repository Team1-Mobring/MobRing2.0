import Cards, TutorialBot, CardSelectorFed, CardSelectorMaffia, functions

# Cords voor locaties van kaarten
# (517, 0), (602, 390), (547, 689), (83, 511), (82, 777)

def setup():
    global load_board, player, actions, current_scene, can_attack, can_place_card, redjob_activated, bluejob_activated, end_turn_img, turn, reroll_amount, bluetrap_lifespan, redtrap_lifespan, bot_graveyard_state, player_graveyard_state
    
    end_turn_img = loadImage("EndTurnButton.png")
    end_turn_img_highlight = loadImage("EndTurnButtonHighlight.png")
    can_place_card = True
    current_scene = "Decissions"
    can_attack = True
    actions = 2
    player = 1
    background_colour_image = "MainMenuafb2.png"
    image(loadImage(background_colour_image), 0, 0)
    redjob_activated = False
    bluejob_activated = False
    turn = 1
    reroll_amount = 1
    bluetrap_lifespan = 0
    redtrap_lifespan = 0
    bot_graveyard_state = []
    player_graveyard_state = []
    
def draw():    
    global player, actions, current_scene, can_attack, can_place_cards, redjob_activated, bluejob_activated, end_turn_img, turn, reroll_amount, bluetrap_lifespan, redtrap_lifespan, bot_graveyard_state, player_graveyard_state
    
    # Loads in the correct board for the Bot, playerboard will be the physical board of his choosing
    if CardSelectorMaffia.current_card_page == "Blue_bot":
        image(loadImage("TutorialBotDesignFed.png"), 0, 0)
        
        # Red trap effect checker
        if len(TutorialBot.bot_trap_field_cards) > 1:
            # Loads in the correct effects of the card
            # Blue trap effect checker
            if len(TutorialBot.bot_trap_field_cards) > 1:
        
                # if ambushed is played by the bot, the players job card will be placed in the bots hand 
                if TutorialBot.bot_trap_field_cards[0] == Cards.ambushed_Blue1 or TutorialBot.bot_trap_field_cards[0] == Cards.ambushed_Blue2:
                    if (TutorialBot.player_job_field_cards) == 1:
                        TutorialBot.bot_deck.append(TutorialBot.player_trap_field_cards[0])
                        bluetrap_lifespan = 2
                    if bluetrap_lifespan == 2:
                        TutorialBot.bot_held_job_cards.append(TutorialBot.player_trap_field_cards[0])
                        TutorialBot.player_job_field_cards.pop()
                
                # If dodge is played when a one cost action is used that does damage, this will be negated    
                if TutorialBot.bot_trap_field_cards[0] == Cards.dodge_Blue1 or TutorialBot.bot_trap_field_cards[0] == Cards.dodge_Blue2:
                    if player == 1 and roll > 0:
                        funtions.roll.total = 0
                        bluetrap_lifespan = 2
                    if bluetrap_lifespan == 2:
                        TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                        TutorialBot.player_trap_field_cards.pop()
                
                # If a mobster card goes into the graveyard it goes back into the field with all lives recovered
                if TutorialBot.bot_trap_field_cards[0] == Cards.revive_Blue1 or TutorialBot.bot_trap_field_cards[0] == Cards.revive_Blue2:
                    n = len(bot_graveyard_state) + redtrap-lifespan
                    if len(TutorialBot.bot_graveyard) > bot_graveyard_state[n]:
                        TutorialBot.bot_mobster_field_cards.append(TutorialBot.bot_graveyard[-1])    
                        bluetrap_lifespan = 2
                    if bluetrap_lifespan == 2:
                        TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                        TutorialBot.player_trap_field_cards.pop()
                # 
                if TutorialBot.bot_trap_field_cards[0] == Cards.ricochet_Blue1 or TutorialBot.bot_trap_field_cards[0] == Cards.ricochet_Blue2:
                    
                    bluetrap_lifespan = 2
                    if bluetrap_lifespan == 2:
                        TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                        TutorialBot.player_trap_field_cards.pop()
                    
                #
                if TutorialBot.bot_trap_field_cards[0] == Cards.sniped_Blue1 or TutorialBot.bot_trap_field_cards[0] == Cards.sniped_Blue2:
                    
                    bluetrap_lifespan = 2
                    if bluetrap_lifespan == 2:
                        TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                        TutorialBot.player_trap_field_cards.pop()
        
        
    # Loads in the correct board for the Bot, playerboard will be the physical board of his choosing    
    if CardSelectorFed.current_card_page == "Red_bot":
        image(loadImage("TutorialBotDesignMafia.png"), 0, 0)
        # Loads in the correct effects of the card
        # Red trap effect checker
        if len(tutorial.botplayer_trap_field_cards) > 1:
            
            # If ambushed is played by the bot, the players job card will be placed in the bots hand
            if TutorialBot.bot_trap_field_cards[0] == Cards.ambushed_Red1 or TutorialBot.bot_trap_field_cards[0] == Cards.ambushed_Red2:
                if (TutorialBot.player_job_field_cards) == 1:
                    TutorialBot.bot_deck.append(TutorialBot.player_trap_field_cards[0])
                    redtrap_lifespan = 2
                if redtrap_lifespan == 2:
                        TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                        TutorialBot.player_trap_field_cards.pop()
                                
            # If dodge is played when a one cost action is used that does damage, this will be negated     
            if TutorialBot.bot_trap_field_cards[0] == Cards.dodge_Red1 or TutorialBot.bot_trap_field_cards[0] == Cards.dodge_Red2:
                if player == 1 and roll > 0:
                    funtions.roll.total = 0
                    redtrap_lifespan = 2
                if redtrap_lifespan == 2:
                    TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                    TutorialBot.player_trap_field_cards.pop() 
                    
            # If a mobster card goes into the graveyard it goes back into the field with all lives recovered
            if TutorialBot.bot_trap_field_cards[0] == Cards.revive_Red1 or TutorialBot.bot_trap_field_cards[0] == Cards.revive_Red2:
                n = len(bot_graveyard_state) + redtrap-lifespan
                if len(TutorialBot.bot_graveyard) > bot_graveyard_state[n]:
                    TutorialBot.bot_mobster_field_cards.append(TutorialBot.bot_graveyard[-1])         
                    redtrap_lifespan = 2
                if redtrap_lifespan == 2:
                        TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                        TutorialBot.player_trap_field_cards.pop()
                        
            # If this card is played and the enemy attacks, attack the enemy with the same amount or +1/-1 damage
            if TutorialBot.bot_trap_field_cards[0] == Cards.ricochet_Red1 or TutorialBot.bot_trap_field_cards[0] == Cards.ricochet_Red2:
                if player == 1 and functions.roll.total > 0:
                    
                    redtrap_lifespan = 2
                if redtrap_lifespan == 2:
                        TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                        TutorialBot.player_trap_field_cards.pop()
                        
            #
            if TutorialBot.bot_trap_field_cards[0] == Cards.sniped_Red1 or TutorialBot.bot_trap_field_cards[0] == Cards.sniped_Red2:
                
                redtrap_lifespan = 2
                if redtrap_lifespan == 2:
                        TutorialBot.bot_graveyard.append(TutorialBot.bot_trap_field_cards[0])
                        TutorialBot.player_trap_field_cards.pop()
    
        
    
    # Scales the cards to the right sizes.
    scale(0.3)
    
    # Show that there are still cards in the Bot_Deck
    if len(TutorialBot.bot_deck) > 0:
        image(loadImage("CardBackBlueSideWays.png"), 325, 2650)
        
    # Shows that there are cards in the graveyard
    if len(TutorialBot.bot_graveyard) > 0 :
        image(loadImage("CardBackBlueSideWays.png"), 325, 1800)
        
    # Shows that there are cards in the bot his hands
    if len(TutorialBot.bot_held_cards) > 0 :
        x = 1727
        y = -180
        for i in range(len(TutorialBot.bot_held_cards)):
            image(loadImage("CardBackBlue.png"), x, y)
            x = x + 210
            
    # Shows the mobster card(s) in the field
    if len(TutorialBot.bot_mobster_field_cards) > 0 :
        x = 1913
        y = 2350
        for i in range(len(TutorialBot.bot_mobster_field_cards)):
            TutorialBot.bot_mobster_field_cards[i].display(x, y)
            x = x + 890
            
    # Shows the trap card on the field
    if len(TutorialBot.bot_trap_field_cards) > 0 :
        image(loadImage("CardBackBlueSideWays.png"), 3260, 1380)
        
    # Shows the job card on the field
    if len(TutorialBot.bot_job_field_cards) > 0 :
        TutorialBot.bot_job_field_cards[0].display(2080, 1380)
        
    def nextPlayerTurn():
        global player, can_attack, turn, action, reroll_amount, redtrap_lifespan, bluetrap_lifespan
        if player == 1:
            player = 0
            player_graveyard_state.append(len(TutorialBot.player_graveyard))
            if CardSelectorFed.current_card_page == "Red_bot":
                bluetrap_lifespan += 1
            else:
                redtrap_lifespan += 1
        else:
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
    
    # Red job effect checker
    # Reveals two cards of the players choosing
    if len(TutorialBot.player_job_field_cards) > 0:
        if TutorialBot.player_job_field_cards[0] == Cards.clairevoyance_Red1 or TutorialBot.player_job_field_cards[0] == Cards.clairevoyance_Red2:
            if redjob_activated == False:
                
                redjob_activated = True
            if redjob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()

    if len(TutorialBot.bot_job_field_cards) > 0:
        # -2 damage
        if TutorialBot.bot_job_field_cards[0] == Cards.anti_Hit_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.anti_Hit_Red2:
            if redjob_activated == False:
                functions.roll.total = functions.roll.total -2
                redjob_activated = True
            if redjob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()

        # Saves one of the dice values for next turn
        if TutorialBot.bot_job_field_cards[0] == Cards.prophecy_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.prophecy_Red2:
            if redjob_activated == False:
                
                redjob_activated = True
            if redjob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
            
        # Can reroll twice
        if TutorialBot.bot_job_field_cards[0] == Cards.reroll_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.reroll_Red2:
            if redjob_activated == False:
                reroll_amount = 2
                redjob_activated = True
            if redjob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        
        # Take one card back and  reset its health
        if TutorialBot.bot_job_field_cards[0] == Cards.retaliate_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.retaliate_Red2:
            pass
            
        # Reveals the trap card of the enemy
        if TutorialBot.bot_job_field_cards[0] == Cards.reveal_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.reveal_Red2:
            pass
            
        # Kill one of your non damaged mobsters to kill one mobster of the enemy
        if TutorialBot.bot_job_field_cards[0] == Cards.sacrifice_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.sacrifice_Red2:
            pass
            
        # Adds +2 bonus damage
        if TutorialBot.bot_job_field_cards[0] == Cards.small_Hit_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.small_Hit_Red2:
            pass
            
        # The enemy can not attack
        if TutorialBot.bot_job_field_cards[0] == Cards.stun_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.stun_Red2:
            pass
            
        # Move one of your ring containers to the oppponent
        if TutorialBot.bot_job_field_cards[0] == Cards.the_Odds_Are_Against_You_Red1 or TutorialBot.bot_job_field_cards[0] == Cards.the_Odds_Are_Against_You_Red2:
            pass
    
    # Blue job effect checker
    # Reveals two cards of the players choosing
    if len(TutorialBot.player_job_field_cards) > 0:
        if TutorialBot.player_job_field_cards[0] == Cards.clairevoyance_Blue1 or TutorialBot.player_job_field_cards[0] == Cards.clairevoyance_Blue2:
            if bluejob_activated == False:
                
                redjob_activated = True
            if bluejob_activated == True:
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
                
    if len(TutorialBot.bot_job_field_cards) > 0:
        # -2 damage
        if TutorialBot.bot_job_field_cards[0] == Cards.anti_Hit_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.anti_Hit_Blue2:
            if bluejob_activated == False:
                functions.roll.total = functions.roll.total -2
                redjob_activated = True
            if bluejob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
                                
        # Saves one of the dice values for next turn
        if TutorialBot.bot_job_field_cards[0] == Cards.prophecy_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.prophecy_Blue2:
            pass
        
        # Can reroll twice
        if TutorialBot.bot_job_field_cards[0] == Cards.reroll_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.reroll_Blue2:
            if bluejob_activated == False:
                reroll_amount = 2
                redjob_activated = True
            if bluejob_activated == True:
                TutorialBot.bot_graveyard.append(TutorialBot.bot_job_field_cards[0])
                TutorialBot.bot_job_field_cards.pop()
        
        # Take one card back and  reset its health
        if TutorialBot.bot_job_field_cards[0] == Cards.retaliate_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.retaliate_Blue2:
            pass
            
        # Reveals the trap card of the enemy
        if TutorialBot.bot_job_field_cards[0] == Cards.reveal_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.reveal_Blue2:
            pass
            
        # Kill one of your non damaged mobsters to kill one mobster of the enemy
        if TutorialBot.bot_job_field_cards[0] == Cards.sacrifice_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.sacrifice_Blue2:
            pass
            
        # Adds +2 bonus damage
        if TutorialBot.bot_job_field_cards[0] == Cards.small_Hit_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.small_Hit_Blue2:
            pass
        
        # The enemy can not attack
        if TutorialBot.bot_job_field_cards[0] == Cards.stun_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.stun_Blue2:
            pass
            
        # Move one of your ring containers to the oppponent
        if TutorialBot.bot_job_field_cards[0] == Cards.the_Odds_Are_Against_You_Blue1 or TutorialBot.bot_job_field_cards[0] == Cards.the_Odds_Are_Against_You_Blue2:
            pass
            
    # Checks player turn, if it is not the players turn than executes bot discission maker    
    if player == 1:
        if current_scene == "Decissions":
            if turn > 2 and can_attack == True:
                pass
            if can_place_card == True:
                pass
            image(end_turn_img, 0, 0)
    else:
        # Checks if the bot can get a card
        if len(TutorialBot.bot_deck) > 0:
            num = random(o, len(TutorialBot.bot_deck) - 1)
            TutorialBot.bot_held_cards.append(TutorialBot.bot_deck[num])
            del TutorialBot.bot_deck[num]
            
        # play Mobstercard check
        if len(TutorialBot.bot_mobster_field_cards) < 3 and len(TutorialBot.bot_held_cards) > 0 and random(0,1) == 1:
            num = random(o, len(TutorialBot.bot_held_mobster_cards) - 1)
            pass
            
        # Play Trapcard check
        if len(TutorialBot.bot_trap_field_cards) < 1 and random(0,1) == 1:
            num = random(o, len(TutorialBot.bot_held_trap_cards) - 1)
            pass
            
        # Play Jobcard check
        if len(TutorialBot.bot_job_field_cards) < 1 and random(0,1) == 1:
            num = random(o, len(TutorialBot.bot_held_job_cards) - 1)
            pass
            
        # Attack check
        if turn > 2 and len(TutorialBot.player_mobster_field_cards) > 0 and can_attack == True and random(0,1) == 1:
            # if attack check is True than attacks
            functions.roll()
            # checks if the rolled total is the same as the hp of a card
            if functions.roll.total == TutorialBot.player_mobster_field_cards[0](hp1) or functions.roll.total == TutorialBot.player_mobster_field_cards[0](hp2) or functions.roll.total == TutorialBot.player_mobster_field_cards[0](hp3):
                pass
            elif len(TutorialBot.player_mobster_field_cards) >= 1 and (functions.roll.total == TutorialBot.player_mobster_field_cards[1](hp1) or functions.roll.total == TutorialBot.player_mobster_field_cards[1](hp2) or functions.roll.total == TutorialBot.player_mobster_field_cards[2](hp3)):
                pass
            elif len(TutorialBot.player_mobster_field_cards) == 2 and (functions.roll.total == TutorialBot.player_mobster_field_cards[2](hp1) or functions.roll.total == TutorialBot.player_mobster_field_cards[2](hp2) or functions.roll.total == TutorialBot.player_mobster_field_cards[2](hp3)):
                pass
            else:
                if reroll_amount > 0:
                    functions.reroll()
                    if functions.roll.total == TutorialBot.player_mobster_field_cards[0](hp1) or functions.roll.total == TutorialBot.player_mobster_field_cards[0](hp2) or functions.roll.total == TutorialBot.player_mobster_field_cards[0](hp3):
                        reroll_amount = 0
                        pass
                    elif len(TutorialBot.player_mobster_field_cards) >= 1 and (functions.roll.total == TutorialBot.player_mobster_field_cards[1](hp1) or functions.roll.total == TutorialBot.player_mobster_field_cards[1](hp2) or functions.roll.total == TutorialBot.player_mobster_field_cards[1](hp3)):
                        reroll_amount = 0
                        pass
                    elif len(TutorialBot.player_mobster_field_cards) == 2 and (functions.roll.total == TutorialBot.player_mobster_field_cards[2](hp1) or functions.roll.total == TutorialBot.player_mobster_field_cards[2](hp2) or functions.roll.total == TutorialBot.player_mobster_field_cards[2](hp3)):
                        reroll_amount = 0
                        pass
                    else:
                        reroll_amount = 0
                        
            can_attack = False
        else:
            nextPlayerTurn()
