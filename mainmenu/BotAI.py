import Cards, TutorialBot, CardSelectorFed, CardSelectorMaffia, functions

current_scene = "Decissions"
red_saved_dice_value = 0
blue_saved_dice_value = 0
red_forget_safe_dice_value = 0
blue_forget_safe_dice_value = 0
can_attack_false_turn = 0
can_attack = False
can_reroll = False
# Cords voor locaties van kaarten
# (517, 0), (602, 390), (547, 689), (83, 511), (82, 777)

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
    
def setup():
    global load_board, player, actions, current_scene, can_attack, can_place_card, redjob_activated, bluejob_activated, end_turn_img, end_turn_img_highlight, turn, reroll_amount, bluetrap_lifespan, redtrap_lifespan, bot_graveyard_state, player_graveyard_state, player_mobster_field_state, bot_mobster_field_state, play_card_img, play_card_img_highlight, attack_img, attack_img_highlight, background_colour_image, red_forget_safe_value, red_saved_dice_value, blue_forget_safe_value, blue_saved_value, can_reroll, reroll_img, reroll_img_highlight
    
    can_reroll = False
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
    global player, actions, current_scene, can_attack, can_place_cards, redjob_activated, bluejob_activated, end_turn_img, turn, reroll_amount, bluetrap_lifespan, redtrap_lifespan, bot_graveyard_state, player_graveyard_state, player_mobster_field_state, bot_mobster_field_state, end_turn_img_highlight, play_card_img, play_card_img_highlight, attack_img, attack_img_highlight, background_colour_image
    
    # Draws the background
    image(background_colour_image, 0, 0)
    
    # Loads in the correct board for the Bot, playerboard will be the physical board of his choosing
    if CardSelectorMaffia.current_card_page == "Blue_bot":
        image(loadImage("TutorialBotDesignFed.png"), 0, 0)

    # Loads in the correct board for the Bot, playerboard will be the physical board of his choosing    
    if CardSelectorFed.current_card_page == "Red_bot":
        image(loadImage("TutorialBotDesignMafia.png"), 0, 0)        
    
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
            if can_reroll == True:
                image(reroll_img, 0, 0)
                if functions.isMouseWithinSpace2(552, 976, 238, 100):
                    image(reroll_img_highlight, 0, 0)
            if can_place_card == True:
                image(play_card_img, 0, 0)
                if functions.isMouseWithinSpace2(829, 973, 238, 100):
                    image(play_card_img_highlight, 0, 0)
            image(end_turn_img, 0, 0)
            if functions.isMouseWithinSpace2(1114, 969, 238, 100):
                image(end_turn_img_highlight, 0, 0)
        

    else:
        # Checks if the bot can get a card
        if len(TutorialBot.bot_deck) > 0:
            num = int(random(0, len(TutorialBot.bot_deck) - 1))
            TutorialBot.bot_held_cards.append(TutorialBot.bot_deck[num])
            TutorialBot.bot_deck.pop(num)
            
        # play Mobstercard check
        if len(TutorialBot.bot_mobster_field_cards) < 3 and len(TutorialBot.bot_held_cards) > 0 and int(random(0,1)) == 1:
            num = int(random(o, len(TutorialBot.bot_held_mobster_cards) - 1))
            pass
            
        # Play Trapcard check
        if len(TutorialBot.bot_trap_field_cards) < 1 and random(0,1) == 1:
            num = int(random(o, len(TutorialBot.bot_held_trap_cards) - 1))
            pass
            
        # Play Jobcard check
        if len(TutorialBot.bot_job_field_cards) < 1 and random(0,1) == 1:
            num = int(random(o, len(TutorialBot.bot_held_job_cards) - 1))
            pass
            
        # Attack check
        if turn > 2 and len(TutorialBot.player_mobster_field_cards) > 0 and can_attack == True and int(random(0,1)) == 1:
            # if attack check is True than attacks
            functions.roll()
            # checks if the rolled total is the same as the hp of a card
            if functions.total == TutorialBot.player_mobster_field_cards[0].hp1 or functions.total == TutorialBot.player_mobster_field_cards[0].hp2 or functions.total == TutorialBot.player_mobster_field_cards[0].hp3:
                if functions.total == TutorialBot.player_mobster_field_cards[0](hp1):
                    TutorialBot.player_mobster_field_cards[0].hp1 = 0
                elif functions.total == TutorialBot.player_mobster_field_cards[0](hp2):
                    TutorialBot.player_mobster_field_cards[0].hp2 = 0
                elif functions.total == TutorialBot.player_mobster_field_cards[0](hp3):
                    TutorialBot.player_mobster_field_cards[0].hp3 = 0
            elif len(TutorialBot.player_mobster_field_cards) >= 1 and (functions.total == TutorialBot.player_mobster_field_cards[1].hp1 or functions.total == TutorialBot.player_mobster_field_cards[1].hp2 or functions.total == TutorialBot.player_mobster_field_cards[2].hp3):
                if functions.total == TutorialBot.player_mobster_field_cards[0].hp1:
                    TutorialBot.player_mobster_field_cards[1].hp1 = 0
                elif functions.total == TutorialBot.player_mobster_field_cards[0].hp2:
                    TutorialBot.player_mobster_field_cards[1].hp2 = 0
                elif functions.total == TutorialBot.player_mobster_field_cards[0].hp3:
                    TutorialBot.player_mobster_field_cards[1].hp3 = 0
            elif len(TutorialBot.player_mobster_field_cards) == 2 and (functions.total == TutorialBot.player_mobster_field_cards[2].hp1 or functions.total == TutorialBot.player_mobster_field_cards[2].hp2 or functions.total == TutorialBot.player_mobster_field_cards[2].hp3):
                if functions.total == TutorialBot.player_mobster_field_cards[0].hp1:
                    TutorialBot.player_mobster_field_cards[2].hp1 = 0
                elif functions.total == TutorialBot.player_mobster_field_cards[0].hp2:
                    TutorialBot.player_mobster_field_cards[2].hp2 = 0
                elif functions.total == TutorialBot.player_mobster_field_cards[0].hp3:
                    TutorialBot.player_mobster_field_cards[2].hp3 = 0
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
                    elif len(TutorialBot.player_mobster_field_cards) >= 1 and (functions.total == TutorialBot.player_mobster_field_cards[1].hp1 or functions.total == TutorialBot.player_mobster_field_cards[1].hp2 or functions.total == TutorialBot.player_mobster_field_cards[1].hp3):
                        reroll_amount = 0
                        if functions.total == TutorialBot.player_mobster_field_cards[0].hp1:
                            TutorialBot.player_mobster_field_cards[1].hp1 = 0
                        elif functions.total == TutorialBot.player_mobster_field_cards[0].hp2:
                            TutorialBot.player_mobster_field_cards[1].hp2 = 0
                        elif functions.total == TutorialBot.player_mobster_field_cards[0].hp3:
                            TutorialBot.player_mobster_field_cards[1].hp3 = 0
                    elif len(TutorialBot.player_mobster_field_cards) == 2 and (functions.total == TutorialBot.player_mobster_field_cards[2].hp1 or functions.total == TutorialBot.player_mobster_field_cards[2].hp2 or functions.total == TutorialBot.player_mobster_field_cards[2].hp3):
                        reroll_amount = 0
                        if functions.total == TutorialBot.player_mobster_field_cards[0].hp1:
                            TutorialBot.player_mobster_field_cards[2].hp1 = 0
                        elif functions.total == TutorialBot.player_mobster_field_cards[0].hp2:
                            TutorialBot.player_mobster_field_cards[2].hp2 = 0
                        elif functions.total == TutorialBot.player_mobster_field_cards[0].hp3:
                            TutorialBot.player_mobster_field_cards[2].hp3 = 0
                    else:
                        reroll_amount = 0
                        
            can_attack = False
        else:
            nextPlayerTurn()
