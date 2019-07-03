add_library('minim')
minim = Minim(this)

def setup():
    size(900,900)
    global x, x1, x2
    global m, m1, m2, m3
    global mb1, mb2, mb3, mb4
    global p, u, moveU
    global y, y1
    global moveX, moveX1, moveX2, moveX3, moveX4
    global moveY
    global brick_set1, brick_set2, brick_MSet
    global score, backg
    global theme, hit, win, lose, power, break_brick

    score = 0
    x = 325
    y = 800
    m = 0
    m1 = 250
    m2 = 500
    m3 = 750
    x2 = 700
    moveX1 = 15
    moveX2 = 12
    moveX3 = 10
    moveX4 = 8
    moveX = random(3)
    moveY = -12
    p = random(900)
    u = 0
    moveU = 8
    brick_set1 = []
    brick_set2 = []
    brick_MSet= []
    
    theme = minim.loadFile("Tetris-99--Main-Theme.mp3")
    win = minim.loadFile("166392__questiion__8bit-blix-aka-lost-moons-make-me-a-game-snippet-notify-if-longer-version-is-needed.wav")
    hit = minim.loadFile("270326__littlerobotsoundfactory__hit-01.wav")
    break_brick = minim.loadFile("270310__littlerobotsoundfactory__explosion-04.wav")
    lose = minim.loadFile("171673__leszek-szary__failure-1.wav")
    power = minim.loadFile("77245__studiocopsey__power-up.wav")
    
    theme.play()
    
    for i in range(1, 21):
        brick_set1.append(True)
    for i in range(1, 21):
        brick_set2.append(True)
    mb1 = True
    mb2 = True
    mb3 = True
    mb4 = True
    frameRate(50)

def ball(x, y):
    fill(255)
    ellipse(x, y, 25, 25)
    
def paddle():
    fill (255)
    rect(mouseX, 880, 100, 20)
    
def moving_brick(x, y):
    fill(255)
    rect(x, y, 50, 25)
def top_bounce(y, speed):
    global hit, moveY
    if y <= 0:
        hit.rewind()   
        hit.play() 
        return -speed
    elif y > 920:
        return 0
    else:
        return speed

def brick(x, y):
    fill(255)
    rect(x, y, 90, 30)
    
def bounce(axis, min_coord, max_coord, speed):
    global hit
    if axis <= min_coord or axis >= max_coord:
      #  hit.rewind()   
      #  hit.play() 
        return -1 * speed
    elif axis >= min_coord or axis <= max_coord:
        return speed
def Pad_Bounce(axis, min_coord, speed, axis2):
    global moveX
    global hit
    if axis >= min_coord and axis <= (min_coord + 100) and axis2 >= 880:
        hit.rewind()   
        hit.play() 
        moveX += random(1,4)
        return -1.03 * speed
    else:
        return moveY
def moving_bricks(mx, my, y, x, speed, mb):
    global moveY, moveX1
    global score
    mx = mx + speed
    speed = bounce(mx, 0, 500, speed)
    if y >= my and y <= my + 30 and x >= mx and x <= mx + 75 and mb == True:
        moveY  = -1.02 * moveY
    if mb == True:
        fill(255)
        rect(mx, my, 75, 30)
        moveY = moveY
def draw_and_bounce(bally, bricky, ballx, brickstart, index, bricks):
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
    while key =='p':
        theme.pause()
        noLoop()
        if key == 'o':
            theme.play()
            loop()
def slow(speed):
    return speed / 2
    
def powerup(p, u, speed):
    fill(148, 0, 211)
    ellipse(p, u, 35, 35)
    return u + speed
        
        
def game_over():
    global score, y, lose, theme
    if score < 4000 and y >900:
        background(0)
        textSize(100)
        fill(255)
        text('GAMEOVER!!', 140, 420)
        theme.pause()
        lose.play()
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
    global x, x2, x3, x4
    global m, m1, m2, m3
    global mb1, mb2, mb3, mb4
    global y, y1, y2
    global moveX, moveX1, moveX2, moveX3, moveX4
    global moveY
    global brick_set1, brick_set2, backg
    global theme, hit, win, lose, power, breack_brick
    global p, u, moveU
    background(0)
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
        x3 = (index % 10) * 90
        draw_and_bounce(y, y1, x, x3, index, brick_set1)
    for index in range(len(brick_set2)):
        y2 = (index // 10) * 30 + 350
        x4 = (index % 10) * 90
        draw_and_bounce(y, y2, x, x4, index, brick_set2)
    moving_bricks(m, 145, y, x, 15, mb1)
    moving_bricks(m1, 175, y, x, 13, mb2)
    moving_bricks(m2, 205, y, x, 11, mb3)
    moving_bricks(m3, 235, y, x, 9, mb4)
    if score >= 2000:
        u = powerup(p,u, moveU)
        if p >= mouseX and p <= mouseX + 100 and u >= 880:
            moveY = slow(moveY)
    pause_play()
    game_over()
    winner()
                
