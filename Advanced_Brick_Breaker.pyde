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
    global moveX
    if axis >= min_coord and axis <= (min_coord + 100) and axis2 >= 880:
        return -1.03 * moveY
        moveX += random(1,4)
        
    else:
        return moveY
def draw_and_bounce(bally, bricky, ballx, brickstart, index, bricks):
    global moveY
    global score
    if bally >= bricky and bally <= bricky + 30 and ballx >= brickstart and ballx <= brickstart + 90 and bricks[index] == True:
        bricks[index] = False
        moveY = -moveY
        score += 100
    if bricks[index] == True:
        fill(255)
        rect(brickstart, bricky, 90, 30)
        moveY = moveY

def draw_brick_row(y, y1, x3, index, bricks):
    draw_and_bounce(y, y1, x, x3, index, bricks)
    
def setup():
    size(900,900)
    global x, x1, x2
    global y, y1
    global moveX, moveX1, moveX2
    global moveY
    global brick_set1, brick_set2, brick_MSet
    global score
    score = 0
    x = 325
    y = 800
    x1 = 0
    x2 = 700
    moveX1 = 15
    moveX2 = 12
    moveX = random(3)
    moveY = -12
    brick_set1 = []
    brick_set2 = []
    brick_MSet= []
    for i in range(1, 21):
        brick_set1.append(True)
    for i in range(1, 21):
        brick_set2.append(True)
    for i in range(1, 4):
        brick_MSet.append(True)
def draw():
    global x, x1, x2, x3, x4
    global y, y1, y2
    global moveX, moveX1, moveX2
    global moveY
    global brick_set1, brick_set2
    background(0)
    x += moveX
    y += moveY
    x1 += moveX1
    ball(x, y)
    paddle()
    moveY = Pad_Bounce(x, mouseX, moveY, y)
    moveY = top_bounce(y, moveY)
    moveX = bounce(x, 0, 750, moveX)
    moveX1 = bounce(x1, 0, 870, moveX1)
    moveX2 = bounce(x2, 0, 870, moveX2)
    textSize(15)
    fill(255)
    text("SCORE: " + str(score), 420, 20)
    for index in range(len(brick_set1)):
        y1 = (index // 10) * 30 + 30
        x3 = (index % 10) * 90
        draw_brick_row(y, y1, x3, index, brick_set1)
    for index in range(len(brick_set2)):
        y2 = (index // 10) * 30 + 350
        x4 = (index % 10) * 90
        draw_brick_row(y, y2, x4, index, brick_set2)
    for index in range(len(brick_MSet)):
        y2 = (index // 10) * 30 + 145
        x4 = (index % 10) * 90
        draw_brick_row(y, y2, x1, index, brick_MSet)
                
