from processing import *
def setup():
  size(500,500)
  
  global x
  global speedX
  global y
  global speedY
  global paddle
  global brick1
  global brick2
  global brick3
  global brick4
  global brick5
  x =250
  speedX =3
  y =250
  speedY =7
  brick1 = 0
  brick2 = 0
  brick3 = 0
  brick4 = 0
  brick5 = 0
  
def draw():
  background(0,0,0)
  global x
  global speedX
  global y
  global speedY
  global paddle
  global brick1
  global brick2
  global brick3
  global brick4
  global brick5
  
  
  fill(255,255,255)
  rect(mouseX,470,100,25)
  
  if x >= 500 or x <0:
    speedX = -speedX
  if y <=0 :
    speedY = -speedY
  if y >=470 and y<=495 and x >=mouseX and x <= mouseX+100:
    speedY = -speedY
  
  if brick1 == 0:
    fill(255,0,0)
    rect(0,10,100,50)
  if brick2 == 0:
    fill(255,0,0)
    rect(100,10,100,50)
  if brick3 == 0:
    fill(255,0,0)
    rect(200,10,100,50)
  if brick4 == 0:
    fill(255,0,0)
    rect(300,10,100,50)
  if brick5 ==0:
    fill(255,0,0)
    rect(400,10,100,50)
  

    
  if y <=60 and x >=0 and x <100:
    brick1 = brick1 +1
  if y <=60 and x >=100 and x <200:
    brick2 = brick2 +1
  if y <=60 and x >=200 and x <300:
    brick3=brick3+ 1
  if y <=60 and x >=300 and x <400:
    brick4=brick4 + 1
  if y <=60 and x >=400 and x <500:
    brick5=brick5 + 1
  
  if brick1 >=1 and brick2 >=1 and brick3 >=1 and brick4 >=1 and brick5 >=1:
    print("YOU WIN")
  elif y >=500:
    print("GAME OVER")

  x = x+speedX
  y = y+speedY
  fill(255,255,255)
  ellipse(x,y,25,25)
