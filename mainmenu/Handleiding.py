import functions

def setup():
    global background_image, goal_image, setup_image, setup1_image, rules_image, start_image, \
    course_image, course2_image
    
    background_image = loadImage("ManualMenu.png")
    goal_image = loadImage("goal.png")
    setup_image = loadImage("setup.png")
    setup2_image = loadImage("setup2.png")
    rules_image = loadImage("rules.png")
    start_image = loadImage("start.png")
    course_image = loadImage("course.png")
    course2_image = loadImage("course2.png")
    
def draw():
    image(background_image, 0, 0)
    
def text1():
    image(goal_image, 0, 0)
    
def text2():
    image(setup_image, 0, 0)
    
def text3():
    image(setup2_image, 0, 0)
    
def text4():
    image(rules_image, 0, 0)
    
def text5():
    image(start_image, 0, 0)
    
def text6():
    image(course_image, 0, 0)
    
def text7():
    image(course2_image, 0, 0)
