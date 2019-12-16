import functions

def setup():
    global background_image, goal_image, setup_image, rules_image, start_image, \
    course_image, course2_image
    
    background_image = loadImage("ManualMenu.png")
    goal_image = loadImage("goal.png")
    setup_image = loadImage("setup.png")
    rules_image = loadImage("rules.png")
    start_image = loadImage("start.png")
    course_image = loadImage("course.png")
    course2_image = loadImage("course2.png")
    
def draw():
    image(background_image, 0, 0)
    
