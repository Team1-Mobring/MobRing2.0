import functions

def setup():
    background(0)
    fill(255)
    textSize(100)
    text("Mobring!\nthe Dice War!", 500, 400)

def draw():
    pass

def text1():
    g = "The goal of the game is to eliminate all of your opponent's Mobsters on their side of the playing field. This is done by attacking your opponent's Mobsters with your dice outcome If the sum of your dice corresponds to a Ring of your opponent's Mobster, you can attack the Ring and hide it with a Ring Container You can also use Jobs and Traps to attack/remove cards of your opponent";
    background(240)
    #textSize(30)
    #fill(50);
    functions.drawText2(g, 500, 400, 0, 0, 0, 20)
    #text(g, 500, 400, 70, 80)# Text wraps within text box
    
def text2():
    background(0)
    a = "1. Both players choose a side: Mafia(Red playing board) or Federal Agency(Blue playing board).  And pick the corresponding colored cards to your playing board"
    b = "2. Both players choose and pick 2 out of 6 Origin cards."
    c = "3. Both players pick the corresponding Mobster Class cards Listed on the Origin cards)"
    d = "4. Both players choose 6 Job cards."
    e = "5.  Both players choose 3 Trap cards."
    f = "6.  Put all your choosen cards in a pile and shake them. This is now your Deck. Apart from the Origin cards, place them somewhere else so you can see what your bonus is"
    g = "7.  Take the top 5 cards from your deck and hold them in your hand, turn the rest upside down on the 'Deck' space on the field.  If you do not have 2 Mobsters in your hand, repeat step 7"
    
    textSize(30)
    text(a, 960, 900)
    text(b, 960, 850)
    text(c, 960, 800)
    text(d, 960, 750)
    text(e, 960, 700)
    text(f, 960, 650)
    text(g, 960, 600)

def text3():
    background(0)
    h = "THE RULES ARE:"
    i = "You have 2 actions each turn."
    j = "Cards can only be played on your own turn. Except for the activation of Trap cards.)"
    k = "You can have a maximum of 1 Trap card on your field."
    l = "Dice n' Slice can be done only once each turn."
    m = "You can only reroll the red dice unless otherwise indicated."
    n = "The Player has won the game when his opponent's Mobster FIELD! is empty."
    o = "Mobsters stay on the playing field until all of their rings are lost, or a Job / Trap card is used that indicated otherwise"
    
    textSize(30)
    text(h, 960, 900)
    text(i, 960, 850)
    text(j, 960, 800)
    text(k, 960, 750)
    text(l, 960, 700)
    text(m, 960, 650)
    text(n, 960, 600)
    text(o, 960, 550)
    
def text4():
    textAlign(CENTER);
    background(0)
    p = "The game is played in turns, where player 1 is determined by rolling the dice. Mobsters can be placed on the field and can then be attacked by your opponent. As soon as TWO of the same Origin's Mobsters are on your field, this Origin's bonus is active! When no Mobsters are left on your field, you lose"
    textSize(30)
    fill(50);
    text(p, 500, 700, 70, 80)  # Text wraps within text box
    
    q = "1. Player 1 starts to fill their field with at least one Mobster."
    r = "2. Player 2 then also fills their field with at least one Mobster."
    textSize(30)
    text(q, 960, 650)
    text(r, 960, 600)

    
    
