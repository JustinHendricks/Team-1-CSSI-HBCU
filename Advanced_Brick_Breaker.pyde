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
    if y <= 0:
        return -speed
    elif y > 920:
        return 0
    else:
        return speed

def brick(x, y):
    fill(255)
    rect(x, y, 90, 30)
    
def bounce(axis, min_coord, max_coord, speed):
    if axis <= min_coord or axis >= max_coord:
        return -speed
    else:
        return speed
def Pad_Bounce(axis, min_coord, speed, axis2):
    global moveY
    if axis >= min_coord and axis <= (min_coord + 100) and axis2 >= 880:
        return -moveY
    else:
        return moveY
def draw_and_bounce(bally, bricky, ballx, brickstart, index):
    global moveY
    global bricks
    if bally >= bricky and bally <= bricky + 30 and ballx >= brickstart and ballx <= brickstart + 100:
        bricks[index] = False
        moveY = -moveY
    if brick == True:
        fill(255)
        rect(brickstart, bricky, 100, 30)

def draw_brick_row(y, y1, x, index):
    x3 = 0
    while x3 < 900:
        draw_and_bounce(y, y1, x, x3, index)
        x3 += 100
def pause():
    global pAuse
    noLoop()
    textSize(100)
    fill(255)
    text('PAUSE', 230, 470)
    pAuse = True
def play():
    global pAuse
    loop()


    
    
def setup():
    size(750,900)
    global x, x1, x2
    global y, y1
    global moveX, moveX1, moveX2
    global moveY
    global bricks
    x = 325
    y = 800
    x1 = 0
    x2 = 700
    moveX1 = 8
    moveX2 = 8
    moveX = random(3)
    moveY = -6
    bricks = []
    for i in range(1, 21):
        bricks.append(True)
def draw():
    global x, x1, x2, x3
    global y, y1
    global moveX, moveX1, moveX2
    global moveY
    global bricks
    background(0)
    x += moveX
    y += moveY
    x1 += moveX1
    x2 -= moveX2
    ball(x, y)
    paddle()
    moving_brick(x1,175)
    moving_brick(x2, 210) 
    moveY = Pad_Bounce(x, mouseX, moveY, y)
    moveY = top_bounce(y, moveY)
    moveX = bounce(x, 0, 750, moveX)
    moveX1 = bounce(x1, 0, 700, moveX1)
    moveX2 = bounce(x2, 0, 700, moveX2)
    textSize(20)
    fill(255)
    text("SCORE: ", 600, 50)
    if key == 'p':
        pause()
        y1 = 350
        while y1 < 381:
            draw_brick_row(y, y1, x, index)
            y1 +=30 
                
