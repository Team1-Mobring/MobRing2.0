import functions, TutorialBot

def setup():
    global background_image, goal_image, setup_image, setup2_image, rules_image, start_image, \
    course_image, course2_image, handleiding_page, highlightMenu_1, traps_image, \
    origins_image, classes_image, mobsters_image, jobs_image, highlight1, highlight2, highlight3, highlight4, highlight5, highlightnext, highlightprevious
    
    background_image = loadImage("ManualMenu.png")
    goal_image = loadImage("goal.png")
    setup_image = loadImage("setup.png")
    setup2_image = loadImage("setup2.png")
    rules_image = loadImage("rules.png")
    start_image = loadImage("start.png")
    course_image = loadImage("course.png")
    course2_image = loadImage("course2.png")
    highlightMenu_1 = loadImage("MainMenuHighlight.png")
    handleiding_page = 1
    traps_image = loadImage("traps.png")
    origins_image = loadImage("origins.png")
    classes_image = loadImage("classes.png")
    mobsters_image = loadImage("mobsters.png")
    jobs_image = loadImage("jobs.png")

    highlight1 = loadImage("HighlightButton1.png")
    highlight2 = loadImage("HighlightButton2.png")
    highlight3 = loadImage("HighlightButton3.png")
    highlight4 = loadImage("HighlightButton4.png")
    highlight5 = loadImage("HighlightButton5.png")
    highlightnext = loadImage("NextHighlight.png")
    highlightprevious = loadImage("PreviousHighlight.png")
    
def draw():
    global handleiding_page, highlightMenu_1
    image(background_image, 0, 0)
    
    if handleiding_page == 1:
        image(goal_image, 15, -28)
        
    if handleiding_page == 2:
        image(setup_image, 15, -28)
        
    if handleiding_page == 3:
        image(setup2_image, 15, -28)
        
    if handleiding_page == 4:
        image(rules_image, 15, -28)
        
    if handleiding_page == 5:
        image(start_image, 15, -28)
        
    if handleiding_page == 6:
        image(course_image, 15, -28)
        
    if handleiding_page == 7:
        image(course2_image, 15, -28)
        
    if handleiding_page == 8:
        image(origins_image, 0, 0)
        
    if handleiding_page == 9:
        image(classes_image, 0, 0)
        
    if handleiding_page == 10:
        image(mobsters_image, 0, 0)
        
    if handleiding_page == 11:
        image(jobs_image, 0, 0)
        
    if handleiding_page == 12:
        image(traps_image, 0, 0)
        
    # Highlights
    if functions.isMouseWithinSpace2(1185, 855, 85, 80):
        image(highlightnext, 0, 0)
        
    if functions.isMouseWithinSpace2(633, 854, 85, 80):
        image(highlightprevious, 0, 0)
            
    if functions.isMouseWithinSpace2(TutorialBot.main_menu_x, TutorialBot.main_menu_y, 265, 90):
        image(highlightMenu_1, 0, 0)
        
    if functions.isMouseWithinSpace2(515, 125, 150, 50):
        image(highlight1, 0, 0)
            
    if functions.isMouseWithinSpace2(705, 125, 150, 50):
        image(highlight2, 0, 0)
            
    if functions.isMouseWithinSpace2(900, 125, 150, 50):
        image(highlight3, 0, 0)
        
    if functions.isMouseWithinSpace2(1095, 125, 150, 50):
        image(highlight4, 0, 0)
            
    if functions.isMouseWithinSpace2(1285, 125, 150, 50):
        image(highlight5, 0, 0)
