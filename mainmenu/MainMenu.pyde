import TutorialBot, functions, Generator, Timer, Handleiding

handleidingY = 360
tutorialY = 420
randomDeckGeneratorY = 480
timedGameplayY = 540
x = 200
w = 200
h = 50
timer_reset = 0

current_page = "Main_Menu"
main_menu_load = False
tutorial_load = False
generator_load = False
timer_load = False
handleiding_load = False

def setup():
    global f
    fullScreen()
    
    f = createFont('arial',32)
    img3 = loadImage('MainMenuafb.png')
    image(img3, 0, 0, 1920, 1200)
    fill(0, 0, 255)
    textFont(f,150)
    text('MOB', 150, 450)    
    
    fill(2500, 0, 0)
    text('RING', 1500, 450)
    stroke(255)
    textFont(f, 28)
    
    # knop handleiding
    fill(255,)
    rect(500, 900, w, h)
    fill(0,)
    textFont(f, 25)    
    text("Manual Course", 510, 935)      
    
    # knop tutorial
    fill(255, 255, 255)
    rect(750, 900, w, h)
    fill(0)
    text("Tutorial", 760, 935)
        
    #Random deck generator
    fill(255, 255, 255)
    rect(1000, 900, w, h)
    fill(0)
    text("Random deck", 1010, 935)
        
    #Timed gameplay 
    fill(255, 255, 255)
    rect(1250, 900, w, h)
    fill(0)
    text("Timed Gameplay", 1255, 935)
    fill(0 ,100)

def draw():
    global current_page, tutorial_load, generator_load, timer_load, main_menu_load, handleiding_load

    if current_page == "Main_Menu":
        if main_menu_load == False:
            setup()
            main_menu_load = True
        else:
            img2 = loadImage('icons8-settings-100.png')
            image(img2, 1850, 1000, 50, 50)
            
    if current_page == "Tutorial_Bot":
        if tutorial_load == False:
            TutorialBot.setup()
            tutorial_load = True
        else:
            TutorialBot.draw()

    if current_page == "Random Deck Generator":
        if generator_load == False:
            Generator.setup()
            generator_load = True
        else:
            Generator.draw(f)
            
    if current_page == "Timer":
        if timer_load == False:
            Timer.setup()
            timer_load = True
        else:
            Timer.draw()
            
    if current_page == "Handleiding":
        if handleiding_load == False:
            Handleiding.setup()
            handleiding_load = True
        else:
            Handleiding.draw()
        
# Timer.py keys registratie
def keyReleased():
    global timer_code, timer_reset
    
    if current_page == "Timer" and timer_load == True:
        # Zorgt ervoor dat "Spatie" niet timer 2 start, wanneer je een andere timed mode begint.
        if timer_reset != Timer.time_mode_choosen and not Timer.timer_start:
            timer_reset = Timer.time_mode_choosen
            Timer.running_2 = False
        
        # De "Spatie" functie van Timer.py, start en pauzeert timer1/timer2.
        if keyCode == 32 and Timer.timer_start == True:
            Timer.spatie = Timer.spatie + 1

            if Timer.running:
                Timer.running = not Timer.running
            
            if Timer.running_2:
                Timer.running_2 = not Timer.running_2
            #De volgende if functie is om de volgorde aan te geven.
            if Timer.spatie % 2 == 0:
                # Even getal, gaat de eerste keer af.
                Timer.running = not Timer.running
                #Als de 4 minute timer aan staat komt er X seconden bij.
                if Timer.four_timer: 
                    Timer.time_left_2 += 15000
            else:
                # Oneven getal, gaat de tweede keer af.
                Timer.running_2 = not Timer.running_2
                if Timer.four_timer:
                    Timer.time_left += 15000
            
        if Timer.step_count == 0:
            if keyCode == 8:
                Timer.user_input_1 = Timer.user_input_1 [0:-1]
            # De naam mag 10 characters lang zijn.
            elif len(Timer.user_input_1) <= 10:
                Timer.user_input_1 += key
        
        if Timer.step_count == 1:
            if keyCode == 8:
                Timer.user_input_2 = Timer.user_input_2 [0:-1]
            # De naam mag 10 characters lang zijn.
            elif len(Timer.user_input_2) <= 10:
                Timer.user_input_2 += key
            
        # "Enter" functie in de timer /is tijdelijk.
        if keyCode == 10 and Timer.step_count == 2 and Timer.time_left > 25 and Timer.time_left_2 > 25:
            Timer.timer_start = not Timer.timer_start
      
        # "Enter" functie tijdens het typen
        if keyCode == 10 and Timer.typing == True and Timer.step_count < 2:
            Timer.step_count += 1

    # TO exit the program!.
    if keyCode == 27:
        key == " "
                    
# mouseclcik registrater    
def mousePressed():
    global box_width, box_height, box_x, box_y, current_page, main_menu_load, tutorial_load, \
    timer_load
    def isMouseWithinSpace(x, y, w, h):
        if x < mouseX < x + w and y < mouseY < y + h:
            return True
        else:
            return False
        
    if current_page == "Tutorial_Bot" and tutorial_load == True:
        # box clicker
        
        if isMouseWithinSpace(70, 550, 300, 100):
            current_page = "Main_Menu"
            main_menu_load = False
            tutorial_load = False
        elif isMouseWithinSpace(TutorialBot.fed_x, TutorialBot.box_y, TutorialBot.box_width, TutorialBot.box_height):
            background(140,200,180)
            print("click2")
        elif isMouseWithinSpace(TutorialBot.maffia_x, TutorialBot.box_y, TutorialBot.box_width, TutorialBot.box_height):
            background(140,200,180)
            print("click3")
        elif isMouseWithinSpace(TutorialBot.help_x, TutorialBot.box_y, TutorialBot.box_width, TutorialBot.box_height):
            background(140,200,180)
            print("click4")
        else:
            print("wrong!")

    if current_page == "Timer" and timer_load == True:     
        # Home menu button
        if isMouseWithinSpace(100, 100, 200, 100):
            current_page = "Main_Menu"
            main_menu_load = False
            timer_load = False
        
        # 10 minute timer button
        if isMouseWithinSpace(630, 765, 200, 100) and Timer.step_count == 2:
            Timer.time_left = 300000
            Timer.time_left_2 = 300000
            Timer.timer_start = False
            Timer.four_timer = False
            Timer.time_mode_choosen = 1
    
        
        # 20 minute timer button
        if isMouseWithinSpace(1090, 765, 200, 100) and Timer.step_count == 2:
            Timer.time_left = 6000
            Timer.time_left_2 = 6000
            Timer.timer_start = False
            Timer.four_timer = False
            Timer.time_mode_choosen = 2
            
        # 4 minute timer button
        if isMouseWithinSpace(860, 765, 200, 100) and Timer.step_count == 2:
            Timer.time_left = 120000
            Timer.time_left_2 = 120000
            Timer.timer_start = False
            Timer.four_timer = True   
            Timer.time_mode_choosen = 3 
            
        # Reset score button
        if isMouseWithinSpace(910, 300, 100, 100) and Timer.step_count == 2:
            Timer.score_player_1 = 0
            Timer.score_player_2 = 0        
            
    if current_page == "Main_Menu" and main_menu_load == True:
            #mouse    
        if ((500 < mouseX < 700) and (900 <= mouseY <= 950)):
            rect(x, handleidingY, w, h) and fill(0, 100)
            current_page = "Handleiding"
            
        if ((750 < mouseX < 950) and (900 <= mouseY <= 950)):
            rect(x, tutorialY, w, h) and fill(0, 100)
            current_page = "Tutorial_Bot"  #Current page veranderd.
      
        
        if ((1000 < mouseX < 1200) and (900 <= mouseY <= 950)):
            rect(x, randomDeckGeneratorY, w, h) and fill(0, 100)
            current_page = "Random Deck Generator"
            
        if ((1250 < mouseX < 1450) and (900 <= mouseY <= 950)):
            rect(x, timedGameplayY, w, h) and fill(0, 100)
            current_page = "Timer"
