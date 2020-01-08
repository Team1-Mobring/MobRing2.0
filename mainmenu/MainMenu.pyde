import TutorialBot, functions, Generator, Timer, Handleiding, CardSelectorFed, CardSelectorMaffia, Cards, Generator2, Generator3, BotAI

def setup():
    global highlightQuit, highlightTutorial, highlightManual, highlightRandomDeck, highlightTimer, backgroundMenu, current_page, main_menu_load,\
    tutorial_load, generator_load, timer_load, handleiding_load, generator2_load, generator3_load, card_selector_fed_load, card_selector_maffia_load,\
    botai_load, clairevoyance_counter

    fullScreen()
    
    clairevoyance_counter = 0
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
    botai_load = False
    highlightQuit = loadImage("QuitHighlight.png")
    highlightTutorial = loadImage("TutorialBotHighlight.png")
    highlightManual = loadImage("ManualHighlight.png")
    highlightRandomDeck = loadImage("RandomDeckHighlight.png")
    highlightTimer = loadImage("TimedModeHighlight.png")
    backgroundMenu = loadImage('MainMenuafb.png')
    image(backgroundMenu, 0, 0)

def draw():
    global current_page, tutorial_load, generator_load, timer_load, main_menu_load, handleiding_load, card_selector_fed_load, card_selector_maffia_load, generator2_load, generator3_load, botai_load

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
    
    # Almina Code
    
    # if current_page == "Handleiding 1":
    #     Handleiding.text1()
    
    # if current_page == "Handleiding 2":
    #     Handleiding.text2()
    
    # if current_page == "Handleiding 3":
    #     Handleiding.text3()
    
    # if current_page == "Handleiding 4":
    #     Handleiding.text4()
    
    # if current_page == "Handleiding 5":
    #     Handleiding.text5()
    
    # if current_page == "Handleiding 6":
    #     Handleiding.text6()
    
    # if current_page == "Handleiding 7":
    #     Handleiding.text7()
    
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
    
    if CardSelectorMaffia.current_card_page == "Blue_bot":
        current_page = "Bot"
    
    if  CardSelectorFed.current_card_page == "Red_bot":
        current_page = "Bot"

    if current_page == "Bot":
        if botai_load == False:
            BotAI.setup()
            botai_load = True
        else:
            BotAI.draw()
    if BotAI.current_scene == "Clairevoyance" or BotAI.current_scene == "Sacrifice" or BotAI.current_scene == "Select_deathcard" or BotAI.current_scene == "Play card":
            scale(3.3333333)
            functions.backgroundTint()
            
    if BotAI.current_scene == "Play card":
        scale(0.3)
        x = 100
        y = 450
        for i in range(len(TutorialBot.player_deck)):
            if i == 9:
                x = 100
                y = 1550
            TutorialBot.player_deck[i].display(x, y)
            x += 700   
    

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
                if Timer.timer_10 and Timer.bonus_mode: 
                    Timer.time_left_2 += 10000
                else:
                    Timer.bonus_mode = True
                    
                if Timer.timer_15 and Timer.bonus_mode_2: 
                    Timer.time_left_2 += 15000
                else:
                    Timer.bonus_mode_2 = True
                    
                if Timer.timer_20 and Timer.bonus_mode_3: 
                    Timer.time_left_2 += 20000
                else:
                    Timer.bonus_mode_3 = True
                    
            else:
                # Oneven getal, gaat de tweede keer af.
                Timer.running_2 = not Timer.running_2
                if Timer.timer_10:
                    Timer.time_left += 10000
                    
                if Timer.timer_15:
                    Timer.time_left += 15000
    
                if Timer.timer_20:
                    Timer.time_left += 20000
            
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
    global box_width, box_height, box_x, box_y, current_page, main_menu_load, tutorial_load, timer_load, handleiding_load, card_selector_maffia_load, card_selector_fed_load, clairevoyance_counter
    def isMouseWithinSpace(x, y, w, h):
        if x < mouseX < x + w and y < mouseY < y + h:
            return True
        else:
            return False
    print(mouseX, mouseY)
      
    if current_page == "Handleiding":
        if isMouseWithinSpace(1185, 855, 85, 80) and Handleiding.handleiding_page < 7:
            Handleiding.handleiding_page += 1
        
        if isMouseWithinSpace(633, 854, 85, 80) and Handleiding.handleiding_page > 1:
            Handleiding.handleiding_page -= 1
            
        if isMouseWithinSpace(TutorialBot.main_menu_x, TutorialBot.main_menu_y, 265, 195):
            current_page = "Main_Menu"
            main_menu_load = False
            handleiding_load = False
            
        if isMouseWithinSpace(515, 125, 150, 50):
            Handleiding.handleiding_page = 8
            
        if isMouseWithinSpace(705, 125, 150, 50):
            Handleiding.handleiding_page = 9
            
        if isMouseWithinSpace(900, 125, 150, 50):
            Handleiding.handleiding_page = 10
        
        if isMouseWithinSpace(1095, 125, 150, 50):
            Handleiding.handleiding_page = 11
            
        if isMouseWithinSpace(1285, 125, 150, 50):
            Handleiding.handleiding_page = 12
        
    # if current_page == "Handleiding 1":
    #     if isMouseWithinSpace(1185, 855, 85, 80):
    #         current_page = "Handleiding 2"
        
    # if current_page == "Handleiding 2":
    #     if isMouseWithinSpace(1185, 855, 85, 80):
    #         current_page = "Handleiding 3"
    
    # if current_page == "Handleiding 3":
    #     if isMouseWithinSpace(1185, 855, 85, 80):
    #         current_page = "Handleiding 4"
            
    # if current_page == "Handleiding 4":
    #     if isMouseWithinSpace(1185, 855, 85, 80):
    #         current_page = "Handleiding 5"
            
    # if current_page == "Handleiding 5":
    #     if isMouseWithinSpace(1185, 855, 85, 80):
    #         current_page = "Handleiding 6"
        
    # if current_page == "Handleiding 6":
    #     if isMouseWithinSpace(1185, 855, 85, 80):
    #         print("click")
    #         current_page = "Handleiding 7"
    
    # Voegt origin + mobster kaarten toe aan de player_deck
    if current_page == "Card_selector_fed" and CardSelectorFed.current_card_page == "":
        if isMouseWithinSpace(TutorialBot.main_menu_x, TutorialBot.main_menu_y, 265, 195):
            current_page = "Main_Menu"
            main_menu_load = False
            tutorial_load = False
        if isMouseWithinSpace(33, 134, 205, 310):
            Cards.DeckAdderFedOrigins(Cards.fed_origins[0])
        if isMouseWithinSpace(243, 134, 205, 310):
            Cards.DeckAdderFedOrigins(Cards.fed_origins[1])
        if isMouseWithinSpace(453, 134, 205, 310):
            Cards.DeckAdderFedOrigins(Cards.fed_origins[2])
        if isMouseWithinSpace(663, 134, 205, 310):
            Cards.DeckAdderFedOrigins(Cards.fed_origins[3])
        if isMouseWithinSpace(873, 134, 205, 310):
            Cards.DeckAdderFedOrigins(Cards.fed_origins[4])
        if len(Cards.fed_origins) == 6 and isMouseWithinSpace(1083, 134, 205, 310):
            Cards.DeckAdderFedOrigins(Cards.fed_origins[5])
        if isMouseWithinSpace(TutorialBot.help_x, TutorialBot.help_y, 170, 115):
            current_page = "Handleiding"
            main_menu_load = False
            tutorial_load = False
            handleiding_load = False
            
     # Voegt origin + mobster kaarten toe aan de player_deck       
    if current_page == "Card_selector_maffia" and CardSelectorMaffia.current_card_page == "":
        if isMouseWithinSpace(TutorialBot.main_menu_x, TutorialBot.main_menu_y, 265, 195):
            current_page = "Main_Menu"
            main_menu_load = False
            tutorial_load = False
        if isMouseWithinSpace(33, 134, 205, 310):
            Cards.DeckAdderMaffiaOrigins(Cards.maffia_origins[0])
        if isMouseWithinSpace(243, 134, 205, 310):
            Cards.DeckAdderMaffiaOrigins(Cards.maffia_origins[1])
        if isMouseWithinSpace(453, 134, 205, 310):
            Cards.DeckAdderMaffiaOrigins(Cards.maffia_origins[2])
        if isMouseWithinSpace(663, 134, 205, 310):
            Cards.DeckAdderMaffiaOrigins(Cards.maffia_origins[3])
        if isMouseWithinSpace(873, 134, 205, 310):
            Cards.DeckAdderMaffiaOrigins(Cards.maffia_origins[4])
        if len(Cards.maffia_origins) == 6 and isMouseWithinSpace(1083, 134, 205, 310):
            Cards.DeckAdderMaffiaOrigins(Cards.maffia_origins[5])
        if isMouseWithinSpace(TutorialBot.help_x, TutorialBot.help_y, 170, 115):
            current_page = "Handleiding"
            main_menu_load = False
            tutorial_load = False
            handleiding_load = False
    
    # Voegt trap kaarten toe aan de player_deck
    if CardSelectorFed.current_card_page == "Card_selector_fed_trap":
        if isMouseWithinSpace(TutorialBot.main_menu_x, TutorialBot.main_menu_y, 265, 195):
            current_page = "Main_Menu"
            main_menu_load = False
            tutorial_load = False
        if isMouseWithinSpace(33, 134, 205, 310):
            Cards.DeckAdderFedTraps(Cards.traps_Blue[0])
        if isMouseWithinSpace(243, 134, 205, 310):
            Cards.DeckAdderFedTraps(Cards.traps_Blue[1])
        if isMouseWithinSpace(453, 134, 205, 310):
            Cards.DeckAdderFedTraps(Cards.traps_Blue[2])
        if isMouseWithinSpace(663, 134, 205, 310):
            Cards.DeckAdderFedTraps(Cards.traps_Blue[3])
        if isMouseWithinSpace(873, 134, 205, 310):
            Cards.DeckAdderFedTraps(Cards.traps_Blue[4])
        if isMouseWithinSpace(33, 459, 205, 310):
            Cards.DeckAdderFedTraps(Cards.traps_Blue[5])
        if isMouseWithinSpace(243, 459, 205, 310):
            Cards.DeckAdderFedTraps(Cards.traps_Blue[6])
        if isMouseWithinSpace(453, 459, 205, 310):
            Cards.DeckAdderFedTraps(Cards.traps_Blue[7])
        if len(Cards.traps_Blue) >= 9 and isMouseWithinSpace(663, 459, 205, 310):
            Cards.DeckAdderFedTraps(Cards.traps_Blue[8])
        if len(Cards.traps_Blue) == 10 and isMouseWithinSpace(870, 459, 205, 310):
            Cards.DeckAdderFedTraps(Cards.traps_Blue[9])
        if isMouseWithinSpace(TutorialBot.help_x, TutorialBot.help_y, 170, 115):
            current_page = "Handleiding"
            main_menu_load = False
            tutorial_load = False
            handleiding_load = False

     # Voegt  trap kaarten toe aan de player_deck       
    if CardSelectorMaffia.current_card_page == "Card_selector_maffia_trap":
        if isMouseWithinSpace(TutorialBot.main_menu_x, TutorialBot.main_menu_y, 265, 195):
            current_page = "Main_Menu"
            main_menu_load = False
            tutorial_load = False
        if isMouseWithinSpace(33, 134, 205, 310):
            Cards.DeckAdderMaffiaTraps(Cards.traps_Red[0])
        if isMouseWithinSpace(243, 134, 205, 310):
            Cards.DeckAdderMaffiaTraps(Cards.traps_Red[1])
        if isMouseWithinSpace(453, 134, 205, 310):
            Cards.DeckAdderMaffiaTraps(Cards.traps_Red[2])
        if isMouseWithinSpace(663, 134, 205, 310):
            Cards.DeckAdderMaffiaTraps(Cards.traps_Red[3])
        if isMouseWithinSpace(873, 134, 205, 310):
            Cards.DeckAdderMaffiaTraps(Cards.traps_Red[4])
        if isMouseWithinSpace(33, 459, 205, 310):
            Cards.DeckAdderMaffiaTraps(Cards.traps_Red[5])
        if isMouseWithinSpace(243, 459, 205, 310):
            Cards.DeckAdderMaffiaTraps(Cards.traps_Red[6])
        if isMouseWithinSpace(453, 459, 205, 310):
            Cards.DeckAdderMaffiaTraps(Cards.traps_Red[7])
        if len(Cards.traps_Red) >= 9 and isMouseWithinSpace(663, 459, 205, 310):
            Cards.DeckAdderMaffiaTraps(Cards.traps_Red[8])
        if len(Cards.traps_Red) == 10 and isMouseWithinSpace(873, 459, 205, 310):
            Cards.DeckAdderMaffiaTraps(Cards.traps_Red[9])
        if isMouseWithinSpace(TutorialBot.help_x, TutorialBot.help_y, 170, 115):
            current_page = "Handleiding"
            main_menu_load = False
            tutorial_load = False
            handleiding_load = False

    # Voegt job kaarten toe aan de player_deck
    if CardSelectorFed.current_card_page == "Card_selector_fed_job":
        if isMouseWithinSpace(TutorialBot.main_menu_x, TutorialBot.main_menu_y, 265, 195):
            current_page = "Main_Menu"
            main_menu_load = False
            tutorial_load = False
        if isMouseWithinSpace(33, 134, 205, 310):
            Cards.DeckAdderFedJobs(Cards.jobs_Blue[0])
        if isMouseWithinSpace(243, 134, 205, 310):
            Cards.DeckAdderFedJobs(Cards.jobs_Blue[1])
        if isMouseWithinSpace(453, 134, 205, 310):
            Cards.DeckAdderFedJobs(Cards.jobs_Blue[2])
        if isMouseWithinSpace(663, 134, 205, 310):
            Cards.DeckAdderFedJobs(Cards.jobs_Blue[3])
        if isMouseWithinSpace(873, 134, 205, 310):
            Cards.DeckAdderFedJobs(Cards.jobs_Blue[4])
        if isMouseWithinSpace(1083, 134, 205, 310):
            Cards.DeckAdderFedJobs(Cards.jobs_Blue[5])
        if isMouseWithinSpace(1293, 134, 205, 310):
            Cards.DeckAdderFedJobs(Cards.jobs_Blue[6])
        if isMouseWithinSpace(1503, 134, 205, 310):
            Cards.DeckAdderFedJobs(Cards.jobs_Blue[7])
        if isMouseWithinSpace(1713, 134, 205, 310):
            Cards.DeckAdderFedJobs(Cards.jobs_Blue[8])
        if isMouseWithinSpace(33, 459, 205, 310):
            Cards.DeckAdderFedJobs(Cards.jobs_Blue[9])
        if isMouseWithinSpace(243, 459, 205, 310):
            Cards.DeckAdderFedJobs(Cards.jobs_Blue[10])
        if isMouseWithinSpace(453, 459, 205, 310):
            Cards.DeckAdderFedJobs(Cards.jobs_Blue[11])
        if isMouseWithinSpace(663, 459, 205, 310):
            Cards.DeckAdderFedJobs(Cards.jobs_Blue[12])
        if isMouseWithinSpace(873, 459, 205, 310):
            Cards.DeckAdderFedJobs(Cards.jobs_Blue[13])
        if isMouseWithinSpace(1083, 459, 205, 310):
            Cards.DeckAdderFedJobs(Cards.jobs_Blue[14])
        if len(Cards.jobs_Blue) >= 16 and isMouseWithinSpace(1293, 459, 205, 310):
            Cards.DeckAdderFedJobs(Cards.jobs_Blue[15])
        if len(Cards.jobs_Blue) >= 17 and isMouseWithinSpace(1503, 459, 205, 310):
            Cards.DeckAdderFedJobs(Cards.jobs_Blue[16])
        if len(Cards.jobs_Blue) >= 18 and isMouseWithinSpace(1713, 459, 205, 310):
            Cards.DeckAdderFedJobs(Cards.jobs_Blue[17])
        if len(Cards.jobs_Blue) >= 19 and isMouseWithinSpace(33, 784, 205, 310):
            Cards.DeckAdderFedJobs(Cards.jobs_Blue[18])
        if len(Cards.jobs_Blue) == 20 and isMouseWithinSpace(243, 784, 205, 310):
            Cards.DeckAdderFedJobs(Cards.jobs_Blue[19])
        if isMouseWithinSpace(TutorialBot.help_x, TutorialBot.help_y, 170, 115):
            current_page = "Handleiding"
            main_menu_load = False
            tutorial_load = False
            handleiding_load = False
        
        # Voegt job kaarten toe aan de player_deck
    if CardSelectorMaffia.current_card_page == "Card_selector_maffia_job":
        if isMouseWithinSpace(TutorialBot.main_menu_x, TutorialBot.main_menu_y, 265, 195):
            current_page = "Main_Menu"
            main_menu_load = False
            tutorial_load = False
        if isMouseWithinSpace(33, 134, 205, 310):
            Cards.DeckAdderMaffiaJobs(Cards.jobs_Red[0])
        if isMouseWithinSpace(243, 134, 205, 310):
            Cards.DeckAdderMaffiaJobs(Cards.jobs_Red[1])
        if isMouseWithinSpace(453, 134, 205, 310):
            Cards.DeckAdderMaffiaJobs(Cards.jobs_Red[2])
        if isMouseWithinSpace(663, 134, 205, 310):
            Cards.DeckAdderMaffiaJobs(Cards.jobs_Red[3])
        if isMouseWithinSpace(873, 134, 205, 310):
            Cards.DeckAdderMaffiaJobs(Cards.jobs_Red[4])
        if isMouseWithinSpace(1083, 134, 205, 310):
            Cards.DeckAdderMaffiaJobs(Cards.jobs_Red[5])
        if isMouseWithinSpace(1293, 134, 205, 310):
            Cards.DeckAdderMaffiaJobs(Cards.jobs_Red[6])
        if isMouseWithinSpace(1503, 134, 205, 310):
            Cards.DeckAdderMaffiaJobs(Cards.jobs_Red[7])
        if isMouseWithinSpace(1713, 134, 205, 310):
            Cards.DeckAdderMaffiaJobs(Cards.jobs_Red[8])
        if isMouseWithinSpace(33, 459, 205, 310):
            Cards.DeckAdderMaffiaJobs(Cards.jobs_Red[9])
        if isMouseWithinSpace(243, 459, 205, 310):
            Cards.DeckAdderMaffiaJobs(Cards.jobs_Red[10])
        if isMouseWithinSpace(453, 459, 205, 310):
            Cards.DeckAdderMaffiaJobs(Cards.jobs_Red[11])
        if isMouseWithinSpace(663, 459, 205, 310):
            Cards.DeckAdderMaffiaJobs(Cards.jobs_Red[12])
        if isMouseWithinSpace(873, 459, 205, 310):
            Cards.DeckAdderMaffiaJobs(Cards.jobs_Red[13])
        if len(Cards.jobs_Red) >= 15 and isMouseWithinSpace(1083, 459, 205, 310):
            Cards.DeckAdderMaffiaJobs(Cards.jobs_Red[14])
        if len(Cards.jobs_Red) >= 16 and isMouseWithinSpace(1293, 459, 205, 310):
            Cards.DeckAdderMaffiaJobs(Cards.jobs_Red[15])
        if len(Cards.jobs_Red) >= 17 and isMouseWithinSpace(1503, 459, 205, 310):
            Cards.DeckAdderMaffiaJobs(Cards.jobs_Red[16])
        if len(Cards.jobs_Red) >= 18 and isMouseWithinSpace(1713, 459, 205, 310):
            Cards.DeckAdderMaffiaJobs(Cards.jobs_Red[17])
        if len(Cards.jobs_Red) >= 19 and isMouseWithinSpace(33, 784, 205, 310):
            Cards.DeckAdderMaffiaJobs(Cards.jobs_Red[18])
        if len(Cards.jobs_Red) == 20 and isMouseWithinSpace(243, 784, 205, 310):
            Cards.DeckAdderMaffiaJobs(Cards.jobs_Red[19])
        if isMouseWithinSpace(TutorialBot.help_x, TutorialBot.help_y, 170, 115):
            current_page = "Handleiding"
            main_menu_load = False
            tutorial_load = False
            handleiding_load = False
    
    if BotAI.current_scene == "Reroll2":
        if isMouseWithinSpace(10, 980, 95, 1070):
            BotAI.current_scene = "Decissions"
        if BotAI.can_reroll == True and isMouseWithinSpace(552, 976, 238, 100):
            BotAI.current_scene = "Reroll2"
            functions.reroll()
        x = 60
        y = 270
        for i in range(len(TutorialBot.bot_mobster_field_cards)):
            if TutorialBot.bot_mobster_field_cards[i].hp1 == functions.total or TutorialBot.bot_mobster_field_cards[i].hp2 == functions.total or TutorialBot.bot_mobster_field_cards[i].hp3 == functions.total:
                if isMouseWithinSpace(x, y, 400, 600):
                    if TutorialBot.bot_mobster_field_cards[i].hp1 == functions.total:
                        TutorialBot.bot_mobster_field_cards[i].hp1 = 0
                    elif TutorialBot.bot_mobster_field_cards[i].hp2 == functions.total:
                        TutorialBot.bot_mobster_field_cards[i].hp2 = 0
                    elif TutorialBot.bot_mobster_field_cards[i].hp3 == functions.total:
                        TutorialBot.bot_mobster_field_cards[i].hp3 = 0
                    BotAI.current_scene = "Decissions"
            x += 430
                
    if BotAI.current_scene == "Reroll":
        if isMouseWithinSpace(10, 980, 95, 1070):
            BotAI.current_scene = "Decissions"
        if BotAI.can_reroll == True and isMouseWithinSpace(552, 976, 238, 100):
            BotAI.current_scene = "Reroll2"
            functions.reroll()
        
        x = 60
        y = 270
        for i in range(len(TutorialBot.bot_mobster_field_cards)):
            if TutorialBot.bot_mobster_field_cards[i].hp1 == functions.total or TutorialBot.bot_mobster_field_cards[i].hp2 == functions.total or TutorialBot.bot_mobster_field_cards[i].hp3 == functions.total:
                if isMouseWithinSpace(x, y, 400, 600):
                    if TutorialBot.bot_mobster_field_cards[i].hp1 == functions.total:
                        TutorialBot.bot_mobster_field_cards[i].hp1 = 0
                    elif TutorialBot.bot_mobster_field_cards[i].hp2 == functions.total:
                        TutorialBot.bot_mobster_field_cards[i].hp2 = 0
                    elif TutorialBot.bot_mobster_field_cards[i].hp3 == functions.total:
                        TutorialBot.bot_mobster_field_cards[i].hp3 = 0
                    BotAI.current_scene = "Decissions"
            x += 430
        
    if BotAI.current_scene == "Attack":
        if isMouseWithinSpace(10, 980, 95, 1070):
            BotAI.current_scene = "Decissions"
        if BotAI.can_reroll == True and isMouseWithinSpace(552, 976, 238, 100):
            BotAI.current_scene = "Reroll"
            functions.reroll()
        x = 60
        y = 270
        for i in range(len(TutorialBot.bot_mobster_field_cards)):
            if TutorialBot.bot_mobster_field_cards[i].hp1 == functions.total or TutorialBot.bot_mobster_field_cards[i].hp2 == functions.total or TutorialBot.bot_mobster_field_cards[i].hp3 == functions.total:
                if isMouseWithinSpace(x, y, 400, 600):
                    if TutorialBot.bot_mobster_field_cards[i].hp1 == functions.total:
                        TutorialBot.bot_mobster_field_cards[i].hp1 = 0
                    elif TutorialBot.bot_mobster_field_cards[i].hp2 == functions.total:
                        TutorialBot.bot_mobster_field_cards[i].hp2 = 0
                    elif TutorialBot.bot_mobster_field_cards[i].hp3 == functions.total:
                        TutorialBot.bot_mobster_field_cards[i].hp3 = 0
                    BotAI.current_scene = "Decissions"
            x += 430
    
    if BotAI.current_scene == "Decissions":
        if BotAI.can_attack == True and isMouseWithinSpace(552, 976, 238, 100):
            functions.roll()
            BotAI.current_scene = "Attack"
            BotAI.can_attack = False
            BotAI.can_reroll = True
        if isMouseWithinSpace(829, 973, 238, 100):
            BotAI.current_scene = "Play card"
        if isMouseWithinSpace(1114, 969, 238, 100):
            BotAI.nextPlayerTurn()
    
    if BotAI.current_scene == "Safe Dice":
        if isMouseWithinSpace(1512, 705, 120, 120):
            if BotAI.player == 1:
                if CardSelectorMaffia.current_card_page == "Blue_bot":
                    BotAI.red_saved_dice_value = functions.white_dice
                    BotAI.current_scene = "Decissions"
                elif CardSelectorFed.current_card_page == "Red_bot":
                    BotAI.blue_saved_dice_value = functions.white_dice
                    BotAI.current_scene = "Decissions"
        if isMouseWithinSpace(1700, 615, 120, 120):
            if BotAI.player == 1:
                if CardSelectorMaffia.current_card_page == "Blue_bot":
                    BotAI.red_saved_dice_value = functions.red_dice
                    BotAI.current_scene = "Decissions"
                elif CardSelectorFed.current_card_page == "Red_bot":
                    BotAI.blue_saved_dice_value = functions.red_dice
                    BotAI.current_scene = "Decissions"
         
    if BotAI.current_scene == "Play card":
        if isMouseWithinSpace(10, 980, 95, 1070):
            BotAI.current_scene = "Decissions"
        x = 100 * 0.3
        y = 450 * 0.3
        for i in range(len(TutorialBot.player_deck)):
            if i == 9:
                x = 100 * 0.3
                y = 1550 * 0.3
            if functions.isMouseWithinSpace2(x, y, 205, 310):
                if TutorialBot.player_deck[i].type == "Mobster" and len(TutorialBot.player_mobster_field_cards) < 3:
                    TutorialBot.player_mobster_field_cards.append(TutorialBot.player_deck[i])
                    TutorialBot.player_deck.pop(i)
                    BotAI.current_scene = "Decissions"
                elif TutorialBot.player_deck[i].type == "Job" and len(TutorialBot.player_job_field_cards) < 1:
                    TutorialBot.player_job_field_cards.append(TutorialBot.player_deck[i])
                    TutorialBot.player_deck.pop(i)
                    BotAI.current_scene = "Decissions"
                elif TutorialBot.player_deck[i].type == "Trap" and len(TutorialBot.player_trap_field_cards) < 1:
                    TutorialBot.player_trap_field_cards.append(TutorialBot.player_deck[i])
                    TutorialBot.player_deck.pop(i)
                    BotAI.current_scene = "Decissions"
            x += 700 * 0.3
    
    if BotAI.current_scene == "Retaliate":
        x = 300
        y = 400
        for i in range(len(TutorialBot.player_mobster_field_cards)):
            if isMouseWithinSpace(x, y, 410, 620):
                for k in range(3):
                    functions.hpResetter(TutorialBot.player_mobster_field_cards[i])
                TutorialBot.player_deck.append(TutorialBot.player_mobster_field_cards[i])
                TutorialBot.player_mobster_field_cards.pop(i)
                if TutorialBot.player_job_field_cards[0] == Cards.retaliate_Red1 or TutorialBot.player_job_field_cards[0] == Cards.retaliate_Red2:
                    BotAI.redjob_activated = True
                else:
                    BotAI.bluejob_activated = True
            x += 420
            
            
    
    if BotAI.current_scene == "Clairevoyance":
        x = 519
        y = -60
        scale(0.6)
        if clairevoyance_counter < 2:
            for i in range(len(TutorialBot.bot_held_cards)):
                if i == len(TutorialBot.bot_held_cards) - 1 and isMouseWithinSpace(x, y, 210, 310):
                    TutorialBot.bot_held_cards[i].display(300, 400)
                    clairevoyance_counter = clairevoyance_counter + 1
                elif isMouseWithinSpace(x, y, 63, 310):
                    TutorialBot.bot_held_cards[i].display(300, 400)
                    clairevoyance_counter = clairevoyance_counter + 1
                x = x + 63
        else:
            BotAI.current_scene = "Decissions"
    
    if BotAI.current_scene == "Select_deathcard":
        x = 300
        y = 400
        for i in range(len(TutorialBot.bot_mobster_field_cards)):
            if isMouseWithinSpace(x, y, 400, 600):
                TutorialBot.bot_graveyard.append(TutorialBot.bot_mobster_field_cards[i])
                TutorialBot.bot_mobster_field_cards.pop(i)
                TutorialBot.player_graveyard.append(TutorialBot.player_job_field_cards[0])
                TutorialBot.player_job_field_cards.pop()
                BotAI.current_scene = "Decissions"
            x = x + 410
    
    if BotAI.current_scene == "Sacrifice":
        x = 300
        y = 400
        if len(TutorialBot.player_mobster_field_cards) > 0:
            for i in range(len(TutorialBot.player_mobster_field_cards)):
                if TutorialBot.player_mobster_field_cards[i].hp1 > 0 and TutorialBot.player_mobster_field_cards[i].hp2 > 0 and TutorialBot.player_mobster_field_cards[i].hp3 > 0:
                    if isMouseWithinSpace(x, y, 400, 620):
                        TutorialBot.player_graveyard.append(TutorialBot.bot_mobster_field_cards[i])
                        TutorialBot.player_mobster_field_cards.pop(i)
                        BotAI.current_scene = "Select_deathcard"
                        if TutorialBot.player_job_field_cards[0] == Cards.sacrifice_Red1 or TutorialBot.player_job_field_cards[0] == Cards.sacrifice_Red2:
                            BotAI.redjob_activated = True
                        else:
                            BotAI.bluejob_activated = True
                    x += 410
        else:
            BotAI.current_scene = "Decissions"
    
    if BotAI.current_scene == "Damage card":
        x = 180
        y = 240
        for i in TutorialBot.player_mobster_field_cards:
            if i.hp1 > 0 or i.hp2 > 0 or i.hp3 > 0:
                if isMouseWithinSpace(x, y, 410, 620):
                    if i.hp1 > 0:
                        i.hp1 = 0
                    elif i.hp2 > 0:
                        i.hp2 = 0
                    elif i.hp3 > 0:
                        i.hp3 = 0
                    BotAI.current_scene = "Decissions"
                x += 420
    
    if BotAI.current_scene == "TOAAY":
        x = 180
        y = 240
        for i in TutorialBot.player_mobster_field_cards:
            if i.hp1 == 0 or i.hp2 == 0 or i.hp3 == 0:
                if isMouseWithinSpace(x, y, 410, 620):
                    if i.hp1 == 0:
                        functions.hpResetter(i)
                    elif i.hp2 == 0:
                        functions.hpResetter(i)
                    elif i.hp3 == 0:
                        functions.hpResetter(i)
                    BotAI.current_scene = "Damage card"
                x += 420
    
    if current_page == "Tutorial_Bot" and tutorial_load == True:
        # box clicker
        if isMouseWithinSpace(TutorialBot.main_menu_x, TutorialBot.main_menu_y, 265, 195):
            current_page = "Main_Menu"
            main_menu_load = False
            tutorial_load = False
        elif isMouseWithinSpace(TutorialBot.fed_x, TutorialBot.fed_y, 360, 195):
            current_page = "Card_selector_fed"
            main_menu_load = False
            tutorial_load = False
            card_selector_fed_load = False
        elif isMouseWithinSpace(TutorialBot.maffia_x, TutorialBot.maffia_y, 360, 195):
            current_page = "Card_selector_maffia"
            main_menu_load = False
            tutorial_load = False
            card_selector_maffia_load = False
        elif isMouseWithinSpace(TutorialBot.help_x, TutorialBot.help_y, 170, 115):
            current_page = "Handleiding"
            main_menu_load = False
            tutorial_load = False
            handleiding_load = False

    if current_page == "Timer" and timer_load == True:     
        # Home menu button
        if isMouseWithinSpace(36, 35, 270, 90):
            current_page = "Main_Menu"
            main_menu_load = False
            timer_load = False
 
        # 10 seconds timer button
        if isMouseWithinSpace(499, 65, 228, 122) and Timer.step_count == 2:
            Timer.time_left = 60000
            Timer.time_left_2 = 60000
            Timer.timer_start = False
            Timer.time_mode_choosen = 3 
            Timer.pickmode = True
            Timer.bonus_mode = False
            Timer.bonus_mode_2 = False
            Timer.bonus_mode_3 = False
            Timer.timer_10 = True
            Timer.timer_15 = False
            Timer.timer_20 = False
                           
        # 15 seconds timer button
        if isMouseWithinSpace(845, 65, 228, 122) and Timer.step_count == 2:
            Timer.time_left = 60000
            Timer.time_left_2 = 60000
            Timer.timer_start = False
            Timer.time_mode_choosen = 1
            Timer.pickmode = True
            Timer.bonus_mode = False
            Timer.bonus_mode_2 = False
            Timer.bonus_mode_3 = False    
            Timer.timer_10 = False
            Timer.timer_15 = True
            Timer.timer_20 = False
        
        # 20 seconds timer button
        if isMouseWithinSpace(1175, 65, 228, 122) and Timer.step_count == 2:
            Timer.time_left = 60000
            Timer.time_left_2 = 60000
            Timer.timer_start = False
            Timer.time_mode_choosen = 2
            Timer.pickmode = True
            Timer.bonus_mode = False
            Timer.bonus_mode_2 = False
            Timer.bonus_mode_3 = False            
            Timer.timer_10 = False
            Timer.timer_15 = False
            Timer.timer_20 = True
            
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
        if ((510 < mouseX < 870) and (470 <= mouseY <= 660)):
            current_page = "Random Deck Generator 2"
        if ((1070 < mouseX < 1440) and (470 <= mouseY <= 670)):
            current_page = "Random Deck Generator 2"
    if current_page == "Random Deck Generator" and generator_load == True:
        if ((30 < mouseX < 320) and (30 <= mouseY <= 120)):
            current_page = "Main_Menu"
    if current_page == "Random Deck Generator" and generator_load == True:
        if ((1700 < mouseX < 1870) and (920 <= mouseY <= 1035)):
            current_page = "Handleiding"
    if current_page == "Random Deck Generator 2" and generator2_load == True:
        if ((910 < mouseX < 1010) and (600 <= mouseY <= 700)):
            current_page = "Random Deck Generator 3"
    if current_page == "Random Deck Generator 2" and generator_load == True:
        if ((30 < mouseX < 320) and (30 <= mouseY <= 120)):
            current_page = "Main_Menu"
    if current_page == "Random Deck Generator 2" and generator_load == True:
        if ((790 < mouseX < 1160) and (540 <= mouseY <= 750)):
            current_page = "Random Deck Generator 3"    
    if current_page == "Random Deck Generator 3" and generator_load == True:
        if ((30 < mouseX < 320) and (30 <= mouseY <= 120)):
            current_page = "Main_Menu"   
    if current_page == "Random Deck Generator 3" and generator_load == True:
        if ((530 < mouseX < 901) and (800 <= mouseY <= 1005)):
            current_page = "Tutorial_Bot"      
    if current_page == "Random Deck Generator 3" and generator_load == True:
        if ((1080 < mouseX < 1445) and (800 <= mouseY <= 1010)):
            current_page = "Random Deck Generator 3"
            Generator3.rdg_step_count = True 
