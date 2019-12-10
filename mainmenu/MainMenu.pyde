
import TutorialBot, functions, Generator, Timer, Handleiding, CardSelectorFed, CardSelectorMaffia, Cards, Generator2, Generator3

def setup():
    global highlightQuit, highlightTutorial, highlightManual, highlightRandomDeck, highlightTimer, backgroundMenu, current_page, main_menu_load,\
    tutorial_load, generator_load, timer_load, handleiding_load, generator2_load, generator3_load, card_selector_fed_load, card_selector_maffia_load

    fullScreen()
    
    current_page = "Main_Menu"
    main_menu_load = False
    tutorial_load = False
    generator_load = False
    timer_load = False
    handleiding_load = False
    generator2_load = False
    generator3_load = False
    card_selector_fed_load = False
    card_selector_maffia_load = False 
    highlightQuit = loadImage("QuitHighlight.png")
    highlightTutorial = loadImage("TutorialBotHighlight.png")
    highlightManual = loadImage("ManualHighlight.png")
    highlightRandomDeck = loadImage("RandomDeckHighlight.png")
    highlightTimer = loadImage("TimedModeHighlight.png")
    backgroundMenu = loadImage('MainMenuafb.png')
    image(backgroundMenu, 0, 0)

def draw():
    global current_page, tutorial_load, generator_load, timer_load, main_menu_load, handleiding_load, card_selector_fed_load, card_selector_maffia_load, generator2_load, generator3_load

    if current_page == "Main_Menu":
        image(backgroundMenu, 0, 0)
        # Manual highlight
        if ((384 <= mouseX <= 873) and (517 <= mouseY <= 671)):
            image(highlightManual, 0, 0)
        # Tutorial Bot highlight
        if ((1048 <= mouseX <= 1536) and (517 <= mouseY <= 671)):
            image(highlightTutorial, 0, 0)
        # Deck generator highlight
        if ((1048 <= mouseX <= 1536) and (761 <= mouseY <= 915)):
            image(highlightRandomDeck, 0, 0)
        # Timer button highlight
        if ((384 <= mouseX <= 873) and (761 <= mouseY <= 915)):
            image(highlightTimer, 0, 0)
        # Exit button highlight
        if ((1746  <= mouseX <= 1818) and (72 <= mouseY <= 172)):
            image(highlightQuit, 0, 0)  
            
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
            
    if current_page == "Random Deck Generator 2":
        if generator2_load == False:
            Generator2.setup()
            generator2_load = True
        else:
            Generator2.draw()
            
    if current_page == "Random Deck Generator 3":
        if generator3_load == False:
            Generator3.setup()
            generator3_load = True
        else:
            Generator3.draw()
               
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
        
    if current_page == "Card_selector_fed":
        if card_selector_fed_load == False:
            CardSelectorFed.setup()
            card_selector_fed_load = True
        else:
            CardSelectorFed.draw()
    
    if current_page == "Card_selector_maffia":
        if card_selector_maffia_load == False:
            CardSelectorMaffia.setup()
            card_selector_maffia_load = True
        else:
            CardSelectorMaffia.draw()

def keyReleased():    
    if current_page == "Timer" and timer_load == True:
        # Zorgt ervoor dat "Spatie" niet timer 2 start, wanneer je een andere timed mode begint.
        if Timer.timer_reset != Timer.time_mode_choosen and not Timer.timer_start:
            Timer.timer_reset = Timer.time_mode_choosen
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
                if Timer.four_timer and Timer.bonus_mode: 
                    Timer.time_left_2 += 15000
                else:
                    Timer.bonus_mode = True
            else:
                # Oneven getal, gaat de tweede keer af.
                Timer.running_2 = not Timer.running_2
                if Timer.four_timer:
                    Timer.time_left += 15000
            
        #  De "and keyCode != 16" zorgt ervoor dat de unicode voor "Shift" niet  bij user_input wordt opgeteld.
        if Timer.step_count == 0:
            if keyCode == 8:
                Timer.user_input_1 = Timer.user_input_1 [0:-1]
            # De naam mag 10 characters lang zijn.
            elif len(Timer.user_input_1) <= 11 and keyCode != 16:
                Timer.user_input_1 += key
        
        if Timer.step_count == 1:
            if keyCode == 8:
                Timer.user_input_2 = Timer.user_input_2 [0:-1]
            # De naam mag 10 characters lang zijn.
            # Checkt if shift is pressed, then capitalize the key
            elif len(Timer.user_input_2) <= 11 and keyCode != 16:
                if functions.isShiftPressed():
                    Timer.user_input += key.capitalize()
                else:
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
   
def mousePressed():
    global box_width, box_height, box_x, box_y, current_page, main_menu_load, tutorial_load, timer_load, handleiding_load, card_selector_maffia_load, card_selector_fed_load
    def isMouseWithinSpace(x, y, w, h):
        if x < mouseX < x + w and y < mouseY < y + h:
            return True
        else:
            return False
    print(mouseX, mouseY)
      
    if current_page == "Handleiding":
        if isMouseWithinSpace(0, 0, 1920, 1080):
            Handleiding.text1()
            current_page = "Handleiding 1"
        
    if current_page == "Handleding 1":
        if isMouseWithinSpace(0, 0, 1920, 1080):
            Handleiding.text2()
            current_page = "Handleiding 2"
        
    if current_page == "Handleding 2":
        if isMouseWithinSpace(0, 0, 1920, 1080):
            Handleiding.text3()
            current_page = "Handleiding 3"
    
    if current_page == "Handleding 3":
        if isMouseWithinSpace(0, 0, 1920, 1080):
            Handleiding.text4()
            current_page = "Handleiding 4"
    
    # Voegt origin + mobster kaarten toe aan de player_deck
    if current_page == "Card_selector_fed":
        if isMouseWithinSpace(0, 0, 205, 310):
            Cards.DeckAdderFed(Cards.fed_origins[0])
        if isMouseWithinSpace(210, 0, 205, 310):
            Cards.DeckAdderFed(Cards.fed_origins[1])
        if isMouseWithinSpace(420, 0, 205, 310):
            Cards.DeckAdderFed(Cards.fed_origins[2])
        if isMouseWithinSpace(630, 0, 205, 310):
            Cards.DeckAdderFed(Cards.fed_origins[3])
        if isMouseWithinSpace(840, 0, 205, 310):
            Cards.DeckAdderFed(Cards.fed_origins[4])
        if len(Cards.fed_origins) == 6 and isMouseWithinSpace(1050, 0, 205, 310):
            Cards.DeckAdderFed(Cards.fed_origins[5])
            
     # Voegt origin + mobster kaarten toe aan de player_deck       
    if current_page == "Card_selector_maffia":
        if isMouseWithinSpace(0, 0, 205, 310):
            Cards.DeckAdderMaffia(Cards.maffia_origins[0])
        if isMouseWithinSpace(210, 0, 205, 310):
            Cards.DeckAdderMaffia(Cards.maffia_origins[1])
        if isMouseWithinSpace(420, 0, 205, 310):
            Cards.DeckAdderMaffia(Cards.maffia_origins[2])
        if isMouseWithinSpace(630, 0, 205, 310):
            Cards.DeckAdderMaffia(Cards.maffia_origins[3])
        if isMouseWithinSpace(840, 0, 205, 310):
            Cards.DeckAdderMaffia(Cards.maffia_origins[4])
        if len(Cards.maffia_origins) == 6 and isMouseWithinSpace(1050, 0, 205, 310):
            Cards.DeckAdderMaffia(Cards.maffia_origins[5])
    
    # Voegt trap kaarten toe aan de player_deck
    if CardSelectorFed.current_page == "Card_selector_fed_trap":
        if isMouseWithinSpace(0, 0, 205, 310):
            Cards.DeckAdderFed(Cards.traps_Blue[0])
        if isMouseWithinSpace(210, 0, 205, 310):
            Cards.DeckAdderFed(Cards.traps_Blue[1])
        if isMouseWithinSpace(420, 0, 205, 310):
            Cards.DeckAdderFed(Cards.traps_Blue[2])
        if isMouseWithinSpace(630, 0, 205, 310):
            Cards.DeckAdderFed(Cards.traps_Blue[3])
        if isMouseWithinSpace(840, 0, 205, 310):
            Cards.DeckAdderFed(Cards.traps_Blue[4])
        if isMouseWithinSpace(0, 325, 205, 310):
            Cards.DeckAdderFed(Cards.traps_Blue[5])
        if isMouseWithinSpace(0, 325, 205, 310):
            Cards.DeckAdderFed(Cards.traps_Blue[6])
        if isMouseWithinSpace(0, 325, 205, 310):
            Cards.DeckAdderFed(Cards.traps_Blue[7])
        if isMouseWithinSpace(0, 325, 205, 310):
            Cards.DeckAdderFed(Cards.traps_Blue[8])
        if len(Cards.traps_Blue) == 10 and isMouseWithinSpace(0, 325, 205, 310):
            Cards.DeckAdderFed(Cards.traps_Blue[9])

            
     # Voegt  trap kaarten toe aan de player_deck       
    if CardSelectorMaffia.current_page == "Card_selector_maffia_trap":
        if isMouseWithinSpace(0, 0, 205, 310):
            Cards.DeckAdderMaffia(Cards.traps_Red[0])
        if isMouseWithinSpace(210, 0, 205, 310):
            Cards.DeckAdderMaffia(Cards.traps_Red[1])
        if isMouseWithinSpace(420, 0, 205, 310):
            Cards.DeckAdderMaffia(Cards.traps_Red[2])
        if isMouseWithinSpace(630, 0, 205, 310):
            Cards.DeckAdderMaffia(Cards.traps_Red[3])
        if isMouseWithinSpace(840, 0, 205, 310):
            Cards.DeckAdderMaffia(traps_Red[4])
        if isMouseWithinSpace(0, 325, 205, 310):
            Cards.DeckAdderMaffia(Cards.traps_Red[5])
        if isMouseWithinSpace(210, 325, 205, 310):
            Cards.DeckAdderMaffia(Cards.traps_Red[6])
        if isMouseWithinSpace(420, 325, 205, 310):
            Cards.DeckAdderMaffia(Cards.traps_Red[7])
        if isMouseWithinSpace(630, 325, 205, 310):
            Cards.DeckAdderMaffia(Cards.traps_Red[8])
        if len(Cards.Traps_Red) == 10 and isMouseWithinSpace(840, 325, 205, 310):
            Cards.DeckAdderMaffia(Cards.traps_Red[9])

    # Voegt trap kaarten toe aan de player_deck
    if CardSelectorFed.current_page == "Card_selector_fed_trap":
        if isMouseWithinSpace(0, 0, 205, 310):
            Cards.DeckAdderFed(Cards.jobs_Blue[0])
        if isMouseWithinSpace(210, 0, 205, 310):
            Cards.DeckAdderFed(Cards.jobs_Blue[1])
        if isMouseWithinSpace(420, 0, 205, 310):
            Cards.DeckAdderFed(Cards.traps_Blue[2])
        if isMouseWithinSpace(630, 0, 205, 310):
            Cards.DeckAdderFed(Cards.jobs_Blue[3])
        if isMouseWithinSpace(840, 0, 205, 310):
            Cards.DeckAdderFed(Cards.jobs_Blue[4])
        if isMouseWithinSpace(0, 325, 205, 310):
            Cards.DeckAdderFed(Cards.jobs_Blue[5])
        if isMouseWithinSpace(210, 325, 205, 310):
            Cards.DeckAdderFed(Cards.jobs_Blue[6])
        if isMouseWithinSpace(420, 325, 205, 310):
            Cards.DeckAdderFed(Cards.jobs_Blue[7])
        if isMouseWithinSpace(630, 325, 205, 310):
            Cards.DeckAdderFed(Cards.jobs_Blue[8])
        if len(Cards.traps_Blue) == 10 and isMouseWithinSpace(840, 325, 205, 310):
            Cards.DeckAdderFed(Cards.jobs_Blue[9])
        if isMouseWithinSpace(0, 650, 205, 310):
            Cards.DeckAdderFed(Cards.jobs_Blue[10])
        if isMouseWithinSpace(210, 650, 205, 310):
            Cards.DeckAdderFed(Cards.jobs_Blue[11])
        if isMouseWithinSpace(420, 650, 205, 310):
            Cards.DeckAdderFed(Cards.jobs_Blue[12])
        if isMouseWithinSpace(630, 650, 205, 310):
            Cards.DeckAdderFed(Cards.jobs_Blue[13])
        if len(Cards.traps_Blue) == 15 and isMouseWithinSpace(840, 650, 205, 310):
            Cards.DeckAdderFed(Cards.jobs_Blue[14])
        if len(Cards.traps_Blue) == 16 and isMouseWithinSpace(0, 975, 205, 310):
            Cards.DeckAdderFed(Cards.jobs_Blue[15])
        if len(Cards.traps_Blue) == 17 and isMouseWithinSpace(210, 975, 205, 310):
            Cards.DeckAdderFed(Cards.jobs_Blue[16])
        if len(Cards.traps_Blue) == 18 and isMouseWithinSpace(420, 975, 205, 310):
            Cards.DeckAdderFed(Cards.jobs_Blue[17])
        if len(Cards.traps_Blue) == 19 and isMouseWithinSpace(630, 975, 205, 310):
            Cards.DeckAdderFed(Cards.jobs_Blue[18])
        if len(Cards.traps_Blue) == 20 and isMouseWithinSpace(840, 975, 205, 310):
            Cards.DeckAdderFed(Cards.job_Blue[19])
        
    if current_page == "Tutorial_Bot" and tutorial_load == True:    
        # box clicker
        if isMouseWithinSpace(70, 550, 300, 100):
            current_page = "Main_Menu"
            main_menu_load = False
            tutorial_load = False
        elif isMouseWithinSpace(TutorialBot.fed_x, TutorialBot.box_y, TutorialBot.box_width, TutorialBot.box_height):
            current_page = "Card_selector_fed"
            main_menu_load = False
            tutorial_load = False
            card_selector_fed_load = False
            print("click2")
        elif isMouseWithinSpace(TutorialBot.maffia_x, TutorialBot.box_y, TutorialBot.box_width, TutorialBot.box_height):
            current_page = "Card_selector_maffia"
            main_menu_load = False
            tutorial_load = False
            card_selector_maffia_load = False
            print("click3")
        elif isMouseWithinSpace(TutorialBot.help_x, TutorialBot.box_y, TutorialBot.box_width, TutorialBot.box_height):
            current_page = "Handleiding"
            main_menu_load = False
            tutorial_load = False
            handleiding_load = False
            print("click4")
        else:
            print("wrong!")

    if current_page == "Timer" and timer_load == True:     
        # Home menu button
        if isMouseWithinSpace(36, 35, 270, 90):
            current_page = "Main_Menu"
            main_menu_load = False
            timer_load = False
        
        # 10 minute timer button
        if isMouseWithinSpace(845, 65, 228, 122) and Timer.step_count == 2:
            Timer.time_left = 300000
            Timer.time_left_2 = 300000
            Timer.timer_start = False
            Timer.four_timer = False
            Timer.time_mode_choosen = 1
            Timer.pickmode = True
            Timer.bonus_mode = False
        
        # 20 minute timer button
        if isMouseWithinSpace(1175, 65, 228, 122) and Timer.step_count == 2:
            Timer.time_left = 600000
            Timer.time_left_2 = 600000
            Timer.timer_start = False
            Timer.four_timer = False
            Timer.time_mode_choosen = 2
            Timer.pickmode = True
            Timer.bonus_mode = False
            
        # 5 minute timer button
        if isMouseWithinSpace(499, 65, 228, 122) and Timer.step_count == 2:
            Timer.time_left = 150000
            Timer.time_left_2 = 150000
            Timer.timer_start = False
            Timer.four_timer = True   
            Timer.time_mode_choosen = 3 
            Timer.pickmode = True
            Timer.bonus_mode = False
            
        # Reset score button
        if isMouseWithinSpace(813, 380, 268, 87) and Timer.step_count == 2:
            Timer.score_player_1 = 0
            Timer.score_player_2 = 0 
            
    if current_page == "Main_Menu" and main_menu_load == True:
            #mouse    
        if ((384 <= mouseX <= 873) and (517 <= mouseY <= 671)):
            current_page = "Handleiding"
        if ((1048 <= mouseX <= 1536) and (517 <= mouseY <= 671)):
            #rect(x, tutorialY, w, h) and fill(0, 100)
            current_page = "Tutorial_Bot"  #Current page veranderd.
        if ((1048 <= mouseX <= 1536) and (761 <= mouseY <= 915)):
            #rect(x, randomDeckGeneratorY, w, h) and fill(0, 100)
            current_page = "Random Deck Generator"
        if ((384 <= mouseX <= 873) and (761 <= mouseY <= 915)):
            #rect(x, timedGameplayY, w, h) and fill(0, 100)
            current_page = "Timer"
        if isMouseWithinSpace(1746, 72, 100, 100):
            exit()            

# Interactieve knoppen voor Random Deck        
    if current_page == "Random Deck Generator" and generator_load == True:
        if ((1160 < mouseX < 1260) and (640 <= mouseY <= 740)):
            current_page = "Random Deck Generator 2"
        if ((660 < mouseX < 760) and (640 <= mouseY <= 740)):
            current_page = "Random Deck Generator 2"
            
    if current_page == "Random Deck Generator 2" and generator2_load == True:
        if ((910 < mouseX < 1010) and (600 <= mouseY <= 700)):
            current_page = "Random Deck Generator 3"            
