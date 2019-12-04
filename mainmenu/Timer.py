
import time, functions

def setup():
    global running, time_left, last_millis, start_timer, time_left_2, \
            last_millis_2, running_2, spatie, timer_start, user_input_1, user_input_2, \
            step_count, typing, four_timer, score_player_1, score_player_2, time_mode_choosen
    background(240)
    rect(100, 200, 100, 200)
    
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
    four_timer = False
    typing = True
    step_count = 0
    spatie = 1
    time_mode_choosen = 0
    
def draw():
    global time_left, last_millis, running, start_timer, time_left_2, last_millis_2, \
            running_2, timer_start, user_input_1, user_input_2, step_count, score_player_1, score_player_2, \
            time_mode_choosen
        
    background(240)
    # Player name fields    
    fill(120, 134, 171)
    rect(500, 300, 325, 100)
    rect(1090, 300, 325, 100)
    # Menu button
    fill(200)
    rect(100, 100, 200, 100)
    functions.drawText3("Main Menu", 200, 160, 0, 0, 0, 30)
    # Score reset button
    fill(200)
    rect(910, 300, 100, 100)
    functions.drawText3("Reset\nScore", 923, 338, 0, 0, 0, 27)
    # Timer modes buttons
    fill(200)
    rect(860, 765, 200, 100) # 4 minutes
    rect(630, 765, 200, 100) # 10 minutes
    rect(1090, 765, 200, 100) # 20 minutes
    functions.drawText3("4 Mins + 15", 885, 830, 0, 0, 0, 30)
    functions.drawText3("10 Mins", 675, 830, 0, 0, 0, 30)
    functions.drawText3("20 Mins", 1135, 830, 0, 0, 0, 30)
    
    # User Input prints
    if step_count == 0:
        functions.drawText3("Please input the \nname of Player 1", 530, 200, 0, 0, 0, 35)
    elif step_count == 1:
        functions.drawText3("Please input the \nname of Player 2", 1120, 200, 0, 0, 0, 35)
    elif step_count == 2 and not timer_start:
        functions.drawText3("Pick a time mode!", 770, 200, 0, 0, 0, 48)

    # Draws the user name/score on the screen.
    functions.drawText3(user_input_1, 530, 365, 0, 0, 0, 48)
    functions.drawText3(score_player_1, 835, 365, 0, 0, 0, 60)
    
    functions.drawText3(user_input_2, 1120, 365, 0, 0, 0, 48)
    functions.drawText3(score_player_2, 1055, 365, 0, 0, 0, 60)
    
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
            
        # Pauze knop!   
        fill(0, 100, 0)
        rect(860, 610, 200, 100) 
        functions.drawText3("Switch!", 910, 670, 0, 0, 0, 30)
        functions.drawText3("'Spacebar'", 910, 690, 0, 0, 0, 20)
        functions.drawText3("Press 'Enter' to pause", 865, 730, 0, 0, 0, 20)
        
            
    # Voor de pauze knop "Enter"       
    elif step_count == 2:
        # Start knop! (Visueel)
        fill(100, 0, 0)
        rect(860, 610, 200, 100) 
        functions.drawText3("Start!", 910, 670, 0, 0, 0, 30)
        functions.drawText3("Press 'Enter' to start", 860, 730, 0, 0, 0, 20)
        
    # Millis worden bijgeteld, ookal staat de timer op pauze.
    last_millis = millis()
    last_millis_2 = millis()

    # Draws the timer value
    if time_mode_choosen >= 1:
        functions.drawText2(functions.convertSeconds(time_left), width*0.37, height/2, 0, 0, 0, 48)
        functions.drawText2(str(functions.showMilliseconds(time_left % 1000)), 810, 560, 0, 0, 0, 20)
        functions.drawText2(functions.convertSeconds(time_left_2), width*0.6, height/2, 0, 0 ,0, 48)
        functions.drawText2(str(functions.showMilliseconds(time_left_2 % 1000)), 1194, 560, 0, 0, 0, 20)
        
