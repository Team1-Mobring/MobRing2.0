
import time, functions

def setup():
    global running, time_left, last_millis, start_timer, time_left_2, \
            last_millis_2, running_2, spatie, timer_start, user_input_1, user_input_2, \
            step_count, typing, timer_10, score_player_1, score_player_2, time_mode_choosen, \
            mainmenu2_img, background_img, pauzeknop_img, playerinput1_img, playerinput2_img, \
            entername1_img, entername2_img, highlight10, highlight15, highlight20, highlightMenu, highlightReset, \
            highlightPauze, highlightStart, highlightSpatie, pickmode_img, pickmode, timer_reset, bonus_mode
    
    background_img = loadImage("TimerDesign.png")
    mainmenu2_img = loadImage("MainMenu2.png")
    pauzeknop_img = loadImage("PauzeKnop.png")
    playerinput1_img = loadImage("PlayerInput1.png")
    playerinput2_img = loadImage("PlayerInput2.png")
    entername1_img = loadImage("EnterName1.png")
    entername2_img = loadImage("EnterName2.png")
    pickmode_img = loadImage("PickModePointer.png")
    
    highlight10 = loadImage("Timer10sHighlight.png")
    highlight15 = loadImage("Timer15sHighlight.png")
    highlight20 = loadImage("Timer20sHighlight.png")
    
    highlightMenu = loadImage("MainMenuHighlight.png")
    highlightReset = loadImage("ResetScoreHighlight.png")
    highlightPauze = loadImage("PauzeHighlight.png")
    highlightStart = loadImage("StartHighlight.png")
    highlightSpatie = loadImage("SpatieHighlight.png")
    
    last_millis = millis()    
    last_millis_2 = millis()
    user_input_1 = ''
    user_input_2 = ''  
    score_player_1 = 0    
    score_player_2 = 0        
    time_left = 0 
    time_left_2 = time_left        
    added_time = 0
    running = False
    running_2 = False   
    timer_start = False                 
    timer_10 = False
    timer_15 = False
    timer_20 = False
    typing = True
    step_count = 0
    spatie = 1
    time_mode_choosen = 0
    pickmode = False
    bonus_mode = False
    timer_reset = 0
    
def draw():
    global time_left, last_millis, running, start_timer, time_left_2, last_millis_2, \
            running_2, timer_start, user_input_1, user_input_2, step_count, score_player_1, score_player_2, \
            time_mode_choosen

    image(background_img, 0, 0)  

    #Step count, highlight player input.
    if step_count == 0:
        image(playerinput1_img, -458.8, -157.5)
        image(entername1_img, 0, 0)
    elif step_count == 1:
        image(playerinput2_img, 0, 0)
        image(entername2_img, 0, 0)
    elif step_count == 2 and not pickmode:
        image(pickmode_img, 0, 0)
        
    #__ All button highlights __
    # "5 Min" button
    if functions.isMouseWithinSpace2(499, 65, 228, 122) and step_count == 2:
        image(highlight10, 0, 0)
    # "10 Min" button
    if functions.isMouseWithinSpace2(845, 65, 228, 122) and step_count == 2:
        image(highlight15, 0, 0)
    # "20 Min" button
    if functions.isMouseWithinSpace2(1175, 65, 228, 122) and step_count == 2:
        image(highlight20, 0, 0)
    # "Main Menu" button
    if functions.isMouseWithinSpace2(36, 35, 270, 90):
        image(highlightMenu, 0, 0)
    # "Reset Score" button
    if functions.isMouseWithinSpace2(813, 380, 268, 87):
        image(highlightReset, 0, 0)        
        
    # Draws the user name/score on the screen.
    functions.drawScore(user_input_1, 555, 440, 0, 0, 0, 60)
    functions.drawScore(score_player_1, 266, 445, 0, 0, 0, 60)
    functions.drawScore(user_input_2, 1337, 440, 0, 0, 0, 60)
    functions.drawScore(score_player_2, 1624, 445, 0, 0, 0, 60)
    
    # Timer code
    if timer_start:
        if running:
            time_left = (time_left - (millis() - last_millis))
        else:
            pass    
        if running_2:
            time_left_2 = (time_left_2 - (millis() - last_millis_2))
        else:
            pass    
        # Timer stopt zodra die onder 1 seconden komt.
        if time_left < 25:
            timer_start = False
            if running:
                score_player_2 += 1
        if time_left_2 < 25:
            timer_start = False
            if running_2:
                score_player_1 += 1
        # Pauze knop!   Hier moet "Pauze" komen in het rood
        image(pauzeknop_img, 0, 0)
    # Voor de pauze knop "Enter"       
    elif step_count == 2:
        pass
        # Start knop! (Visueel) Hier moet "Start" komen in het groen

    # Millis worden bijgeteld, ookal staat de timer op pauze. (Want millis telt door vanaf aanroepen van die functie)
    last_millis = millis()
    last_millis_2 = millis()

    # Draws the timer value
    if time_mode_choosen >= 1:
        if running:
            functions.drawTextTimer2(functions.convertSeconds(time_left), 798, 660, 52, 189, 235, 150)
            functions.drawText2(str(functions.showMilliseconds(time_left % 1000)), 750, 697, 52, 189, 235, 40)
            
        if running_2:           
            functions.drawTextTimer1(functions.convertSeconds(time_left_2), 1096, 660, 52, 189, 235, 150)       
            functions.drawText2(str(functions.showMilliseconds(time_left_2 % 1000)), 1142, 697, 52, 189, 235, 40)

        if not running:
            functions.drawTextTimer2(functions.convertSeconds(time_left), 798, 660, 0, 0, 0, 98)
            functions.drawText2(str(functions.showMilliseconds(time_left % 1000)), 770, 680, 0, 0, 0, 20)
            
        if not running_2:
            functions.drawTextTimer1(functions.convertSeconds(time_left_2), 1096, 660, 0, 0 ,0, 98) 
            functions.drawText2(str(functions.showMilliseconds(time_left_2 % 1000)), 1120, 680, 0, 0, 0, 20)
