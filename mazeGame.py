### title screen
title=Label("Maze Game", 200,50, size=40)
playButton=Group(
    Rect(200,360,120,60, fill=None, border=rgb(217,177,128),align="center", borderWidth=5),
    Label("PLAY", 200,360, size=40))
objectives=Group(
    Label("Objectives", 75,100, size=20),
    Label("Explore the maze.", 75, 150),
    Label("Search for keys", 75,170),
    Label("to unlock", 75, 190),
    Label("special doors.", 75, 210))
controls=Group(
    Label("Controls",325,100, size=20),
    Rect(315,150,20,20, borderWidth=3, border=rgb(217,177,128), fill=None),
    Label("W",325,160),
    Rect(315,167,20,20, borderWidth=3, border=rgb(217,177,128), fill=None),
    Label("S",325,177),
    Rect(298,167,20,20, borderWidth=3, border=rgb(217,177,128), fill=None),
    Label("A",308,177),
    Rect(332,167,20,20, borderWidth=3, border=rgb(217,177,128), fill=None),
    Label("D", 342, 177),
    Label("Use WASD controls",325,225),
    Label("to move around", 325, 245))
titleScreen = Group()
titleScreen.add(title,playButton,objectives,controls)

### player model
player=Circle(200,200,5)
player.visible=False

### inventory
inventory=Rect(275,340,115,50, fill=None, borderWidth=4, border='black')
inventory.visible=False

### keys
key1=Group(
    Circle(72,236,10, fill='gold', border='black'),
    Circle(72,236,4, fill='white', border='black'),
    Rect(68,244,8,30, fill='gold', border='black'),
    Rect(74,263,15,7, fill='gold', border='black'),
    Rect(74,255,14,7, fill='gold', border='black'))
key2=Group(
    Circle(72,236,10, fill='gold', border='black'),
    Circle(72,236,4, fill='white', border='black'),
    Rect(68,244,8,30, fill='gold', border='black'),
    Rect(74,263,15,7, fill='gold', border='black'),
    Rect(74,255,14,7, fill='gold', border='black'))
key2.obtained=False
key1.obtained=False
keys=Group(key1,key2)
key2.visible=False
key2.unlocked=False
invKey1=Group(Circle(72,236,10, fill='gold', border='black'),
    Circle(72,236,4, fill='white', border='black'),
    Rect(68,244,8,30, fill='gold', border='black'),
    Rect(74,263,15,7, fill='gold', border='black'),
    Rect(74,255,14,7, fill='gold', border='black'))
invKey2=Group(Circle(72,236,10, fill='gold', border='black'),
    Circle(72,236,4, fill='white', border='black'),
    Rect(68,244,8,30, fill='gold', border='black'),
    Rect(74,263,15,7, fill='gold', border='black'),
    Rect(74,255,14,7, fill='gold', border='black'))
invKeys=Group(invKey1,invKey2)

### door
door1=Rect(975,-408.1,50,8)
door1check=Rect(975,-400,50,20, opacity=0)
door1.opened=False
door2=Rect(975,-1208.1,50,8)
door2.opened=False
door2check=Rect(975,-1200, 50,20, opacity=0)
key2check=Rect(2380,-1025, 20,50, opacity=0)
door3=Line(1200,225,1200,175)
doors=Group(door1check,door2check,key2check)

### message
message= Group(
    Rect(90,40,210,60, fill='white', border=rgb(217,177,128), borderWidth=5),
    Label("You need a key for this door.", 195,70, size=15))
message.visible=False

### win room
exit=Group(
    Line(400,-1600,800,-1600),
    Line(400,-1600,400,-1200),
    Line(400,-1200,800,-1200),
    Line(800,-1200, 800, -1375),
    Line(800,-1600,800,-1425))
winMessage=Label("YOU WIN!!", 600,-1400, size=70)

### maze
maze=Group(door1,door2, door3, exit)

def makeRoom(x,y):
    maze.add(Line(x-75,y+25,x-75,y+75)),
    maze.add(Line(x-75,y-25,x-75,y-75)),
    maze.add(Line(x+75,y+25,x+75,y+75)),
    maze.add(Line(x+75,y-25,x+75,y-75)),
    maze.add(Line(x-75,y-75,x-25,y-75)),
    maze.add(Line(x-75,y+75,x-25,y+75)),
    maze.add(Line(x+75,y-75,x+25,y-75)),
    maze.add(Line(x+75,y+75,x+25,y+75)),
    maze.add(Line(x-75,y-25,x-200,y-25)),
    maze.add(Line(x-75,y+25,x-200,y+25)),
    maze.add(Line(x+75,y-25,x+200,y-25)),
    maze.add(Line(x+75,y+25,x+200,y+25)),
    maze.add(Line(x-25,y-75,x-25,y-200)),
    maze.add(Line(x+25,y-75,x+25,y-200)),
    maze.add(Line(x-25,y+75,x-25,y+200)),
    maze.add(Line(x+25,y+75,x+25,y+200))
    
### walls
for i in range(5):
    if i!= 1:
        if i!=2:
            maze.add(Line(175+400*i,800,225+400*i,800))
            
for x in range(4):
    if x!=1:
        maze.add(Line(-225+400*x,400,-175+400*x,400))
        
for p in range(3):
    if p!=1:
        maze.add(Line(575+400*p,0,625+400*p,0))

for f in range(6):
    if f!=3:
        maze.add(Line(-225+400*f, -400,-175+400*f,-400))
            
for n in range(6):
    if n!=1:
        maze.add(Line(575+400*n,-800,625+400*n,-800))

for a in range(4):
    maze.add(Line(1375+400*a,-1200,1425+400*a,-1200))

for m in range(2):
    maze.add(Line(-400,225-400*m,-400,175-400*m))

for r in range(4):
    if r!=1:
        maze.add(Line(400,625-400*r,400,575-400*r))

for z in range(3):
    if z!=1:
        maze.add(Line(800,-175-400*z,800,-225-400*z))
        
for h in range(6):
    if h!=1:
        if h!=2:
            if h!=4:
                maze.add(Line(1200,625-400*h,1200,575-400*h))

for b in range(3):
    maze.add(Line(2000,575-400*b,2000,625-400*b))

maze.add(Line(975,-1600,1025,-1600))
maze.add(Line(0,625,0,575))
maze.add(Line(1600,175,1600,225))
maze.add(Line(2800,-975,2800,-1025))

### rooms
makeRoom(-200,200)
makeRoom(200,200)
makeRoom(600,200)
makeRoom(1000,200)
makeRoom(1400,200)
makeRoom(1800,200)
makeRoom(200,600)
makeRoom(1400,600)
makeRoom(1800,600)
makeRoom(-200,-200)
makeRoom(200,-200)
makeRoom(1000,-200)
makeRoom(1400,-200)
makeRoom(1800,-200)
makeRoom(600,-600)
makeRoom(1000,-600)
makeRoom(1000,-1000)
makeRoom(1400,-1000)
makeRoom(1800,-1000)
makeRoom(2200,-1000)
makeRoom(2600,-1000)
makeRoom(1000,-1400)

maze.visible=False

def onMousePress(mouseX,mouseY):
    if playButton.contains(mouseX,mouseY):
        titleScreen.clear()
        maze.visible=True
        player.visible=True
        key1.centerX=1400
        key1.centerY=200
        key2.centerX=1000
        key2.centerY=-1000
        inventory.visible=True
        invKeys.centerX=332.5
        invKeys.centerY=365
        invKeys.rotateAngle=90
        invKeys.visible=False

def onKeyHold(keys):
    if maze.visible:
        if 'd' in keys:
            maze.centerX-=5
            doors.centerX-=5
            key1.centerX-=5
            key2.centerX-=5
            winMessage.centerX-=5
            if player.hitsShape(maze):
                 maze.centerX+=5
                 doors.centerX+=5
                 key1.centerX+=5
                 key2.centerX+=5
                 winMessage.centerX+=5
        if 'w' in keys:
            maze.centerY+=5
            doors.centerY+=5
            key1.centerY+=5
            key2.centerY+=5
            winMessage.centerY+=5
            if player.hitsShape(maze):
                maze.centerY-=5
                doors.centerY-=5
                key1.centerY-=5
                key2.centerY-=5
                winMessage.centerY-=5
        if 's' in keys:
            maze.centerY-=5
            doors.centerY-=5
            key1.centerY-=5
            key2.centerY-=5
            winMessage.centerY-=5
            if player.hitsShape(maze):
                maze.centerY+=5
                doors.centerY+=5
                key1.centerY+=5
                key2.centerY+=5
                winMessage.centerY+=5
        if 'a' in keys:
            maze.centerX+=5
            doors.centerX+=5
            key1.centerX+=5
            key2.centerX+=5
            winMessage.centerX+=5
            if player.hitsShape(maze):
                maze.centerX-=5
                doors.centerX-=5
                key1.centerX-=5
                key2.centerX-=5
                winMessage.centerX-=5
                
    if player.hitsShape(door1check):
        if key1.obtained==False and door1.opened==False:
            message.visible=True
            message.toFront()
        elif key1.obtained:
            invKey1.visible=False
            key1.obtained=False
            maze.remove(door1)
            door1.opened=True
    else:
        message.visible=False

    if player.hitsShape(door2check):
        if key2.obtained==False and door2.opened==False:
            message.visible=True
            message.toFront()
        elif key2.obtained:
            invKey2.visible=False
            key2.obtained=False
            maze.remove(door2)
            door2.opened=True
    elif (door1.opened == True):
        message.visible=False
        
    if player.hitsShape(key2check):
        if key2.unlocked==False:
            key2.visible=True
            key2.unlocked=True
        
    if player.hitsShape(key1):
        key1.obtained=True
    if player.hitsShape(key2) and key2.unlocked==True:
        key2.obtained=True
        
def onStep():
    if key1.obtained==True:
        if key1.width >= 4:
            key1.rotateAngle+=10
            key1.width-=2
            key1.height-=2
            maze.remove(door3)
        else:
            key1.visible=False
            key1.obtained=True
            invKey1.visible=True
    if key2.obtained==True:
        if key2.width>=4:
            key2.rotateAngle-=10
            key2.width-=2
            key2.height-=2
        else:
            key2.visible=False
            key2.obtained=True
            invKey2.visible=True
