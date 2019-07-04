add_library('minim')
minim = Minim(this) #Adds library that enables sound

def setup():
    size(900,900)
    global x, padWidth
    global m, m1, m2, m3
    global mb1, mb2, mb3, mb4
    global p, u, moveU, pp, pu, movePU, ep, eu, moveEU
    global y, y1
    global moveX, moveX1, moveX2, moveX3, moveX4
    global moveY
    global brick_set1, brick_set2
    global score, run, runP, runE
    global theme, hit, win, lose, power, break_brick, theme2, loser, so_close, applause  #Globalizes all variables

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
    padWidth = 100
    p = random(900) #Sets x-coordinate for Slow Powerup
    u = 0 #Sets y-coordinate for Slow powerup
    moveU = 3 #Moves y-coordinate of Slow powerup down the screen
    pp = random(900)
    pu = 0
    movePU = 8
    ep = 450
    eu = 0
    moveEU = 12
    brick_set1 = [] #Creates list that will be filled with True values needed to create the upper row of bricks
    brick_set2 = [] #Creates list that will be filled with True values needed to create the lower row of bricks
    
    theme = minim.loadFile("Tetris-99--Main-Theme.mp3") #Loads theme played for when score is below 2000
    theme2 = minim.loadFile("Undertale-Remixed--Bonetrousle-Holder-Remix-Papyrus-Theme--GameChops.mp3") #Loads theme played for when score is above 2000
    win = minim.loadFile("166392__questiion__8bit-blix-aka-lost-moons-make-me-a-game-snippet-notify-if-longer-version-is-needed.wav") #Loads theme played when game is won
    hit = minim.loadFile("270326__littlerobotsoundfactory__hit-01.wav") #Loads sound played when moving brick, paddle, or boundary is hit by ball
    break_brick = minim.loadFile("270310__littlerobotsoundfactory__explosion-04.wav") #Loads sound played when brick is broken
    applause = minim.loadFile("Applause Crowd Cheering sound effect.mp3") #Loads sound that congratulates user with a round of applause
    loser = minim.loadFile("Looooser Looooser.mp3") #Loads sound that mocks user for losing quickly
    so_close = minim.loadFile("Ooh you almost had it....mp3") #Loads sound that encourages user to try again after a close loss
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
    run = False #Makes it so that the Slow powerup runs only once
    runP = False
    runE = False
    
    theme.play() #Plays first theme  to start
    
def ball(x, y): #Function that creates the ball
    fill(255)
    ellipse(x, y, 25, 25)
    
def paddle(padWidth): #Function that creates the paddle
    fill (255)
    rect(mouseX, 880, padWidth, 20)
    
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
def Pad_Bounce(axis, min_coord, speed, axis2, padWidth): #Function that makes ball bounce off the paddle
    global moveX
    global hit
    if axis >= min_coord and axis <= (min_coord + padWidth) and axis2 >= 880:
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
    if mb == True: #UNNECESSARY
        fill(255)
        rect(mx, my, 75, 30)
        moveY = moveY
def static_bricks(bally, bricky, ballx, brickstart, index, bricks): #Function used to create the static rows of bricks
    global moveY
    global score
    global break_brick
    if bally >= bricky and bally <= bricky + 30 and ballx >= brickstart and ballx <= brickstart + 90 and bricks[index] == True:
        bricks[index] = False
        moveY = -moveY
        score += 100
        break_brick.rewind()
        break_brick.play() #Plays break sound
    if bricks[index] == True:
        fill(255)
        rect(brickstart, bricky, 90, 30)
        moveY = moveY

def pause_play(): #CFunction used to make a pause and a play button
    while key == 'p': # 'p' = pause
        theme.pause() 
        noLoop()
        if key == 'v': # 'v' = start
            theme.play()
            loop()
            
def slow(speed): #Function used to slow ball movement for the Slow powerup
    print(speed)
    return speed * .75

def extend():
    return 200

def eliminator():
    global mb1, mb2, mb3, mb4
    mb1 = False
    mb2 = False
    mb3 = False
    mb4 = False

    
def slow_powerup(p, u, speed): #Function used to create the powerup ball
    fill(148, 0, 211)
    ellipse(p, u, 35, 35)
    return u + speed

def paddle_powerup(pp, pu, speed):
    fill(0, 211, 148)
    ellipse(pp, pu, 35, 35)
    return pu + speed

def eliminator_ball(ep, eu, speed):
    fill(210, 25, 25)
    ellipse(ep, eu, 35, 35)
    return eu + speed
        
        
def game_over(): #Function that creates the game over screen
    global score, y, lose, theme, loser, so_close
    if score < 2000 and y >900: 
        background(112, 25, 25)
        textSize(100)
        fill(255)
        text('LOSER!!', 260, 420) #Shows message
        theme.pause() #Pauses the background theme
        lose.play() #Plays lose music
        loser.play() #Plays 'loser call' from Spongebob
        textSize(100)
        fill(255)
        text('Score: ' + str(score), 180, 220) #Prints Score
        noLoop()
    elif score>= 2000 and y >900: 
        background(112, 25, 25)
        textSize(100)
        fill(255)
        text('SO CLOSE!!', 210, 420) #Shows message
        theme.pause() 
        theme2.pause() #Stops whichever theme was playing when the player loses
        so_close.play() #Plays 'gotta be quicker than that' from the commercial
        lose.play() #Plays lose music
        textSize(100)
        fill(255)
        text('Score: ' + str(score), 190, 220) #Shows score
        noLoop()
    
def winner(): #Function that makes the winner screen
    global score, win, theme, applause
    if score >= 4000:
        background(random(255), random(255), random(255))
        textSize(100)
        fill(255)
        text('YOU WIN!!', 190, 420) #Shows message
        theme.pause() 
        theme2.pause() #Pauses the theme that was last played
        win.play() #Plays winner song
        applause.play() #Applause sound effect
        noLoop()
    
def draw():
    global x, x1, x4
    global m, m1, m2, m3, padWidth
    global mb1, mb2, mb3, mb4
    global y, y1, y2
    global moveX, moveX1, moveX2, moveX3, moveX4
    global moveY
    global brick_set1, brick_set2, run, runP, runE
    global theme, hit, win, lose, power, breack_brick, theme2
    global p, u, moveU, pp, pu, movePU, ep, eu, moveEU #Globalizes variables used
    background(25, 25, 112) #Blue background
    x += moveX #Lets moveX control ball's x-coordinate
    y += moveY #Lets moveY control ball's Y-coordinate
    m += moveX1 #Lets moveX1 control moving brick1's x-coordinate
    m1+= moveX2 #Lets moveX2 control moving brick2's x-coordinate
    m2+= moveX3 #Lets moveX3 control moving brick3's x-coordinate
    m3+= moveX4 #Lets moveX4 control moving brick4's x-coordinate
    ball(x, y) #Creates ball
    paddle(padWidth) #Creates paddle
    moveY = Pad_Bounce(x, mouseX, moveY, y, padWidth) #Makes ball bounce off paddle
    moveY = top_bounce(y, moveY) #Makes ball bounce off top of screen ansd stay at the bottom of the screen
    moveX = bounce(x, 0, 900, moveX) #Makes ball bounce of the walls of the screen
    moveX1 = bounce(m, 0, 870, moveX1) #Makes ball bounce off moving brick1
    moveX2 = bounce(m1, 0, 870, moveX2) #Makes ball bounce off moving brick2
    moveX3 = bounce(m2, 0, 870, moveX3) #Makes ball bounce off moving brick3
    moveX4 = bounce(m3, 0, 870, moveX4) #Makes ball bounce off moving brick4
    textSize(15)
    fill(255)
    text("SCORE: " + str(score), 420, 20) #Shows score constantly on the top of the screen
    for index in range(len(brick_set1)): #This for loop creates the top row of static bricks
        y1 = (index // 10) * 30 + 30
        x1 = (index % 10) * 90
        static_bricks(y, y1, x, x1, index, brick_set1)
    for index in range(len(brick_set2)): #This for loop creates the bottom row of static bricks
        y2 = (index // 10) * 30 + 350
        x4 = (index % 10) * 90
        static_bricks(y, y2, x, x4, index, brick_set2)
    moving_bricks(m, 145, y, x, 15, mb1) #Creates moving brick1
    moving_bricks(m1, 175, y, x, 13, mb2) #Creates moving brick2
    moving_bricks(m2, 205, y, x, 11, mb3) #Creates moving brick3
    moving_bricks(m3, 235, y, x, 9, mb4) #Creates moving brick4
    if score >= (1000): #Creates Slow Powerup when score is 1000
        u = slow_powerup(p,u, moveU)
        if p >= mouseX and p <= mouseX + padWidth and u >= 880 and u <= 900 and run == False:
            moveY = slow(moveY)
            power.play()
            run = True
            if runP == True:
                padWidth = 100
                runP = False
    if score >= 2000: #Creates Extend Powerup when score is 2000
        pu = paddle_powerup(pp, pu, movePU)
        if pp >= mouseX and pp <= mouseX + padWidth and pu >= 880 and pu <= 900 and runP == False:
            padWidth = extend()
            power.play()
            runP = True
            if runP == True:
                runE = False
                run = False
    
    if score >= 3000:
        eu = eliminator_ball(ep, eu, moveEU)
        if ep >= mouseX and ep <= mouseX + padWidth and eu >= 880 and eu <= 900 and runE == False:
            eliminator()
            power.play()
            runE = True
        if runP == True:
            padWidth = 100
            runP = False
    if score > 2000: #Changes song at half way point
        theme.pause()
        theme2.play()
    pause_play() #Calls pause and play button
    game_over() #Calls game over screen
    winner() #Calls win screen
                
