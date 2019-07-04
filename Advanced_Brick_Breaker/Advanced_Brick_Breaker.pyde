add_library('minim')
minim = Minim(this) #Adds library that enables sound

def setup():
    size(900,900)
    global x
    global m, m1, m2, m3
    global mb1, mb2, mb3, mb4
    global p, u, moveU
    global y, y1
    global moveX, moveX1, moveX2, moveX3, moveX4
    global moveY
    global brick_set1, brick_set2
    global score, run
    global theme, hit, win, lose, power, break_brick, theme2  #Globalizes all variables

    score = 0 #Tracks score
    x = 325 #Tracks x-coordinate of the ball
    y = 800 #Tracks y-coordinate of the ball
    m = 0 #Tracks x-coordinate of 1st moving brick(highest)
    m1 = 250 #Tracks x-coordinate of 2nd moving brick
    m2 = 500 #Tracks x-coordinate of 3rd moving brick
    m3 = 750 #Tracks x-coordinate of 4th moving brick(lowest)
    moveX1 = 15 #Moves 1st moving brick
    moveX2 = 12 #Moves 2nd moving brick
    moveX3 = 10 #Moves 3rd moving brick
    moveX4 = 8 #Moves 4th moving brick
    moveX = random(3) #Moves ball left and right
    moveY = -12 #Moves ball up and down
    p = random(900) #Sets x-coordinate for Slow Powerup
    u = 0 #Sets y-coordinate for Slow powerup
    moveU = 3 #Moves y-coordinate of Slow powerup down the screen
    brick_set1 = [] #Creates list that will be filled with True values needed to create the upper row of bricks
    brick_set2 = [] #Creates list that will be filled with True values needed to create the lower row of bricks
    
    theme = minim.loadFile("Tetris-99--Main-Theme.mp3") #Loads theme played for when score is below 2000
    theme2 = minim.loadFile("Undertale-Remixed--Bonetrousle-Holder-Remix-Papyrus-Theme--GameChops.mp3") #Loads theme played for when score is above 2000
    win = minim.loadFile("166392__questiion__8bit-blix-aka-lost-moons-make-me-a-game-snippet-notify-if-longer-version-is-needed.wav") #Loads theme played when game is won
    hit = minim.loadFile("270326__littlerobotsoundfactory__hit-01.wav") #Loads sound played when moving brick, paddle, or boundary is hit by ball
    break_brick = minim.loadFile("270310__littlerobotsoundfactory__explosion-04.wav") #Loads sound played when brick is broken
    lose = minim.loadFile("171673__leszek-szary__failure-1.wav") #Loads sound played when game is lost
    power = minim.loadFile("77245__studiocopsey__power-up.wav") #Loads sound played when powerup is collected
    
    for i in range(1, 21):
        brick_set1.append(True) #Fills brick_set1 with True values
    for i in range(1, 21):
        brick_set2.append(True) #Fills brick_set2 with True values
    mb1 = True #Sets 1st moving brick as True *(UNNECESSARY)*
    mb2 = True #Sets 2nd moving brick as True *(UNNECESSARY)*
    mb3 = True #Sets 3rd moving brick as True *(UNNECESSARY)*
    mb4 = True #Sets 4th moving brick as True *(UNNECESSARY)*
    run = True #Makes it so that the Slow powerup runs only once
    
    theme.play() #Plays first theme  to start
    
def ball(x, y): #Function that creates the ball
    fill(255)
    ellipse(x, y, 25, 25)
    
def paddle(): #Function that creates the paddle
    fill (255)
    rect(mouseX, 880, 100, 20)
    
def top_bounce(y, speed): #Fucntion that makes the ball bounce off the top of the screen and stay on the bottom of the screen if it passes the paddle
    global hit, moveY
    if y <= 0:
        hit.rewind()   
        hit.play() #Plays 'hit' sound
        return -speed
    elif y > 920:
        return 0
    else:
        return speed
    
def bounce(axis, min_coord, max_coord, speed): #Function used to make things bounce off each other
    global hit
    if axis <= min_coord or axis >= max_coord:
        return -1 * speed
    elif axis >= min_coord or axis <= max_coord:
        return speed
def Pad_Bounce(axis, min_coord, speed, axis2): #Function that makes ball bounce off the paddle
    global moveX
    global hit
    if axis >= min_coord and axis <= (min_coord + 100) and axis2 >= 880:
        hit.rewind()   
        hit.play() #Plays hit sound
        moveX += random(-4,4) #Randomizes the way the ball comes off the paddle
        return -1.03 * speed
    else:
        return moveY
def moving_bricks(mx, my, y, x, speed, mb): #Function used to create the moving bricks *(COULD BE IMPROVED BY MAKING IT SO THAT THIS FUNCTION CREATES ALL MOVING BRICKS INSTEAD OF 1)*
    global moveY, moveX1
    global score
    mx = mx + speed #Makes brick move left and right
    speed = bounce(mx, 0, 500, speed) #Ball bounces off the paddle
    if y >= my and y <= my + 30 and x >= mx and x <= mx + 75 and mb == True: #if the y/x-coordinate of the ball is on the y/x-coordinate of the brick, the ball bounces. (TRUE PORTION IS UNNECESSARY AS BRICKS ARE OBSTACLES AND DON'T DISAPPEAR)
        moveY  = -1.03 * moveY 
    if mb == True:
        fill(255)
        rect(mx, my, 75, 30)
        moveY = moveY
def static_bricks(bally, bricky, ballx, brickstart, index, bricks):
    global moveY
    global score
    global break_brick
    if bally >= bricky and bally <= bricky + 30 and ballx >= brickstart and ballx <= brickstart + 90 and bricks[index] == True:
        bricks[index] = False
        moveY = -moveY
        score += 100
        break_brick.rewind()
        break_brick.play()
    if bricks[index] == True:
        fill(255)
        rect(brickstart, bricky, 90, 30)
        moveY = moveY

def pause_play():
    while key == 'p':
        theme.pause()
        noLoop()
        if key == 'o':
            theme.play()
            loop()
def slow(speed):
    print(speed)
    return speed * .75

    
def powerup(p, u, speed):
    fill(148, 0, 211)
    ellipse(p, u, 35, 35)
    return u + speed
        
        
def game_over():
    global score, y, lose, theme
    if score < 2000 and y >900:
        background(112, 25, 25)
        textSize(100)
        fill(255)
        text('LOSER!!', 260, 420)
        theme.pause()
        lose.play()
        textSize(100)
        fill(255)
        text('Score: ' + str(score), 190, 220)
        noLoop()
    elif score>= 2000 and y >900:
        background(112, 25, 25)
        textSize(100)
        fill(255)
        text('SO CLOSE!!', 210, 420)
        theme2.pause()
        lose.play()
        textSize(100)
        fill(255)
        text('Score: ' + str(score), 190, 220)
        noLoop()
    
def winner():
    global score, win, theme
    if score >= 4000:
        background(0)
        textSize(100)
        fill(255)
        text('YOU WIN!!', 190, 420)
        theme.pause()
        win.play()
        noLoop()

def draw():
    global x, x1, x4
    global m, m1, m2, m3
    global mb1, mb2, mb3, mb4
    global y, y1, y2
    global moveX, moveX1, moveX2, moveX3, moveX4
    global moveY
    global brick_set1, brick_set2, run
    global theme, hit, win, lose, power, breack_brick, theme2
    global p, u, moveU
    background(25, 25, 112)
    x += moveX
    y += moveY
    m += moveX1
    m1+= moveX2
    m2+= moveX3
    m3+= moveX4
    ball(x, y)
    paddle()
    moveY = Pad_Bounce(x, mouseX, moveY, y)
    moveY = top_bounce(y, moveY)
    moveX = bounce(x, 0, 900, moveX)
    moveX1 = bounce(m, 0, 870, moveX1)
    moveX2 = bounce(m1, 0, 870, moveX2)
    moveX3 = bounce(m2, 0, 870, moveX3)
    moveX4 = bounce(m3, 0, 870, moveX4)
    textSize(15)
    fill(255)
    text("SCORE: " + str(score), 420, 20)
    for index in range(len(brick_set1)):
        y1 = (index // 10) * 30 + 30
        x1 = (index % 10) * 90
        static_bricks(y, y1, x, x1, index, brick_set1)
    for index in range(len(brick_set2)):
        y2 = (index // 10) * 30 + 350
        x4 = (index % 10) * 90
        static_bricks(y, y2, x, x4, index, brick_set2)
    moving_bricks(m, 145, y, x, 15, mb1)
    moving_bricks(m1, 175, y, x, 13, mb2)
    moving_bricks(m2, 205, y, x, 11, mb3)
    moving_bricks(m3, 235, y, x, 9, mb4)
    if score >= 1000:
        u = powerup(p,u, moveU)
        if p >= mouseX and p <= mouseX + 100 and u >= 880 and run == True:
            moveY = slow(moveY)
            power.play()
            run = False
    if score > 2000:
        theme.pause()
        theme2.play()
    print(moveY)
    pause_play()
    game_over()
    winner()
                
