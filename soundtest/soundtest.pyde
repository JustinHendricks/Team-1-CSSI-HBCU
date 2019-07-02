
add_library('minim')

minim = Minim(this)

def setup():
    size(500,500)
    theme = minim.loadFile("Tetris-99--Main-Theme.mp3")
    win = minim.loadFile("166392__questiion__8bit-blix-aka-lost-moons-make-me-a-game-snippet-notify-if-longer-version-is-needed.wav")
    hit = minim.loadFile("270326__littlerobotsoundfactory__hit-01.wav")
    break_brick = minim.loadFile("270310__littlerobotsoundfactory__explosion-04.wav")
    lose = minim.loadFile("171673__leszek-szary__failure-1.wav")
    power = minim.loadFile("77245__studiocopsey__power-up.wav")
    theme.play()
    
    global theme
    global hit
    global x
    global speedX
    global y
    global speedY
    x =250
    speedX =3
    y =250
    speedY =7

def pause():
    noLoop()
    theme.pause()
    textSize(100)
    fill(255)
    text('PAUSE', 230, 470)
def play():
    loop()
    theme.play()
    
    
def draw():
    background(0)
    global x
    global speedX
    global y
    global speedY
    global hit
    global theme
    
    if x >= 500 or x <0:
        speedX = -speedX
        hit.rewind()
        hit.play()
    if y <=0 or y>= 500:
        speedY = -speedY
        hit.rewind()
        hit.play()
        
    x = x+speedX
    y = y+speedY
    fill(255,255,255)
    ellipse(x,y,25,25)
