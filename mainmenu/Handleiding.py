import functions, TutorialBot

def setup():
    global background_image, goal_image, setup_image, setup2_image, rules_image, start_image, \
    course_image, course2_image, handleiding_page, highlightMenu_1
    
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
    
    if functions.isMouseWithinSpace2(TutorialBot.main_menu_x, TutorialBot.main_menu_y, 265, 90):
        image(highlightMenu_1, 0, 0)
        
    if handleiding_page == 8:
        image(traps_image, 15, -28)
        
    if handleiding_page == 9:
        image(origins_image, 15, -28)
        
    if handleiding_page == 10:
        image(classes_image, 15, -28)
        
    if handleiding_page == 11:
        image(mobsters_image, 15, -28)
        
    if handleiding_page == 12:
        image(jobs_image, 15, -28)
        
        
# def text1():
#     image(goal_image, 0, 0)
    
# def text2():
#     image(setup_image, 0, 0)
    
# def text3():
#     image(setup2_image, 0, 0)
    
# def text4():
#     image(rules_image, 0, 0)
    
# def text5():
#     image(start_image, 0, 0)
    
# def text6():
#     image(course_image, 0, 0)
    
# def text7():
#     image(course2_image, 0, 0)
