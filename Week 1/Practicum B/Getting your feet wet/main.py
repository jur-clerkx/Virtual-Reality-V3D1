import viz
import vizshape
import vizact
import random
import vizcam
import math

#Start virtual world
viz.go(viz.FULLSCREEN)

#Add subwindow
BirdEyeWindow = viz.addWindow()
BirdEyeWindow.fov(60)
#Add subview
BirdEyeView = viz.addView() 
BirdEyeWindow.setView(BirdEyeView)
#Position subview
BirdEyeView.setPosition([0,25,0])
BirdEyeView.setEuler([0,90,0], viz.ABS_GLOBAL)
viewLink = viz.link(viz.MainView, BirdEyeView)
viewLink.preTrans([0, 15, 0])
viewLink.preEuler([0,90,0])

#Set configuration
viz.collision(viz.ON)
viz.setMultiSample(4)
viz.MainWindow.fov(60)
MOVE_SPEED = 5
TURN_SPEED = 60

view = viz.MainView
view.move([0, 0 ,-10])
view.setEuler([0, 0, 0])

#Map
piazza = viz.addChild('piazza.osgb')

#Objects
chair = viz.addChild('models/chair.dae')
chair.setPosition(0,0,-9)
chair.scale(17,17,17)

#male avatar
male = viz.addAvatar('vcc_male.cfg')
male.setPosition([4.5, 0, 7])
male.setEuler([0,0,0])
male.state(14)

#female avatar
female = viz.addAvatar('vcc_female.cfg')
female.setPosition([4.5, 0, 9])
female.setEuler([180, 0, 0])
female.state(14)

#plants
plants = []
for x in [-3,-2,-1,0]:
	for z in [4, 2, 0, -2, -4]:
		plant = viz.addChild('plant.osgb', cache=viz.CACHE_CLONE)
		plant.setPosition([x,0,z])
		plants.append(plant)
		
#Start the animation for the plants
spin = vizact.spin(0,1,0,30)
oldplant = None
def spinPlant(plant):
	global oldplant
	if oldplant:
		oldplant.clearActions()

	plant.addAction(spin)
	oldplant = plant

vizact.ontimer(3, spinPlant, vizact.choice(plants))


#Generate random pigeons
pigeons = []
for i in range(10):
	#Generate random positions
	x = random.randint(3, 10)
	z = random.randint(2, 8)
	yaw = random.randint(0, 360)
	
	#Load a pigeon
	pigeon = viz.addAvatar('pigeon.cfg')
	
	#Set the position
	pigeon.setPosition([x, 0, z])
	pigeon.setEuler([yaw, 0, 0])
	pigeon.state(1)
	
	pigeons.append(pigeon)
	
def walkAvatars():
	walk1 = vizact.walkTo([4.5, 0, -40])
	vizact.ontimer2(0.5, 0, female.addAction, walk1)
	
	walk2 = vizact.walkTo([3.5, 0, -40])
	male.addAction(walk2)
	
vizact.onkeydown('w', walkAvatars)

def pigeonsFeed():
	random_speed = vizact.method.setAnimationSpeed(0,vizact.randfloat(0.7,1.5))
	random_walk = vizact.walkTo([vizact.randfloat(3,10),0,vizact.randfloat(2,8)])
	random_animation = vizact.method.state(vizact.choice([1,3],vizact.RANDOM))
	random_wait = vizact.waittime(vizact.randfloat(5.0,10.0))
	pigeon_idle = vizact.sequence( random_speed, random_walk, random_animation, random_wait, viz.FOREVER)

	for pigeon in pigeons:
		pigeon.addAction(pigeon_idle)

vizact.onkeydown('p',pigeonsFeed)

def createCube(size):
	cube = viz.addGroup()
	
	#Bottom
	viz.startLayer(viz.POLYGON)
	viz.vertexColor(255, 0, 0)
	viz.vertex(0,0,0)
	viz.vertex(size, 0, 0)
	viz.vertex(size, 0, size)
	viz.vertex(0, 0, size)
	viz.endLayer(parent = cube)
	
	#Front
	viz.startLayer(viz.POLYGON)
	viz.vertexColor(255, 0, 0)
	viz.vertex(0,0,0)
	viz.vertex(size, 0, 0)
	viz.vertex(size, size, 0)
	viz.vertex(0, size, 0)
	viz.endlayer(parent = cube)
	
	#Right
	viz.startLayer(viz.POLYGON)
	viz.vertexColor(255, 0, 0)
	viz.vertex(size, 0, 0)
	viz.vertex(size, 0, size)
	viz.vertex(size, size, size)
	viz.vertex(size, size, 0)
	viz.endlayer(parent = cube)
	
	#Left
	viz.startLayer(viz.POLYGON)
	viz.vertexColor(255, 0, 0)
	viz.vertex(0, 0, 0)
	viz.vertex(0, size, 0)
	viz.vertex(0, size, size)
	viz.vertex(0, 0, size)
	viz.endlayer(parent = cube)
	
	#Back
	viz.startLayer(viz.POLYGON)
	viz.vertexColor(255, 0, 0)
	viz.vertex(0, 0, size)
	viz.vertex(0, size, size)
	viz.vertex(size, size, size)
	viz.vertex(size, 0, size)
	viz.endlayer(parent = cube)
	
	#Top
	viz.startLayer(viz.POLYGON)
	viz.vertexColor(255, 0, 0)
	viz.vertex(0, size, 0)
	viz.vertex(size, size, 0)
	viz.vertex(size, size, size)
	viz.vertex(0, size, size)
	viz.endlayer(parent = cube)
	
	cube.setPosition(2, 0, -5)
	return cube


def createCylinder(radius):
	cylinder = viz.addGroup()
	
	detail = int(radius * 20)
	if detail < 10:
		detail = 10
	angle = 360/detail;
	
	#Bottom
	viz.startLayer(viz.POLYGON)
	viz.vertexColor(viz.BLUE)
	for i in range(detail):
		x = radius * math.cos(((i*angle)*math.pi)/180)
		y = radius * math.sin(((i*angle)*math.pi)/180)
		viz.vertex(x,0,y)
	viz.endLayer(parent=cylinder)
	
	#Top
	viz.startLayer(viz.POLYGON)
	viz.vertexColor(viz.BLUE)
	for i in range(detail):
		x = radius * math.cos(((i*angle)*math.pi)/180)
		y = radius * math.sin(((i*angle)*math.pi)/180)
		viz.vertex(x,1.5,y)
	viz.endLayer(parent=cylinder)

	#Sides
	viz.startLayer(viz.QUADS)
	viz.vertexColor(viz.BLUE)
	for i in range(detail):
		x = radius * math.cos(((i*angle)*math.pi)/180)
		y = radius * math.sin(((i*angle)*math.pi)/180)
		if i == 0:
			viz.vertex(x,0,y)
			viz.vertex(x,1.5,y)
		elif i % 2 == 0:
			viz.vertex(x,0,y)
			viz.vertex(x,1.5,y)
			viz.vertex(x,0,y)
			viz.vertex(x,1.5,y)
		else:
			viz.vertex(x,1.5,y)
			viz.vertex(x,0,y)
			viz.vertex(x,1.5,y)
			viz.vertex(x,0,y)
	
	x = radius * math.cos(((0*angle)*math.pi)/180)
	y = radius * math.sin(((0*angle)*math.pi)/180)
	if (detail - 1) % 2 == 1:
		viz.vertex(x,0,y)
		viz.vertex(x,1.5,y)
	else:
		viz.vertex(x,1.5,y)
		viz.vertex(x,0,y)
	
	viz.endLayer(parent=cylinder)
	cylinder.setPosition(0, 0, -5)
	return cylinder

#Vars for scaling
selectedShape = 0
cubeSize = 1
cylinderSize = 1

#Create shapes
cylinder = createCylinder(1.2)
cube = createCube(1)

#Selection of the shapes
def selectShape(shape):
	global selectedShape
	if selectedShape == shape:
		selectedShape = 0
	else:
		selectedShape = shape

#Sizing of the shapes
def sizeShape(expand):
	global selectedShape
	
	if selectedShape == 1:
		global cube
		global cubeSize
		if expand:
			cubeSize = cubeSize + 0.1
		else:
			cubeSize = cubeSize - 0.1
		cube.scale(cubeSize, cubeSize, cubeSize)
	if selectedShape == 2:
		global cylinder
		global cylinderSize
		if expand:
			cylinderSize = cylinderSize + 0.1
		else:
			cylinderSize = cylinderSize - 0.1
		cylinder.scale(cylinderSize, cylinderSize, cylinderSize)

#Set callbacks for selection keys
vizact.onkeydown('1',selectShape, 1)
vizact.onkeydown('2',selectShape, 2)
#Set callbacks for size keys
vizact.onkeydown(viz.KEY_KP_ADD, sizeShape, True)
vizact.onkeydown(viz.KEY_KP_SUBTRACT, sizeShape, False)

####Get child with local transformations
seat = chair.getChild('seat001', viz.CHILD_REPLACE_TRANSFORM)

#Seatspinning
def seatspinning():
	seat.setEuler([15 * viz.elapsed(), 0, 0], viz.ABS_LOCAL)

vizact.ontimer(0, seatspinning)

#Timer
def updateMovement():
	if viz.key.isDown(viz.KEY_UP):
		view.move([0,0,MOVE_SPEED*viz.elapsed()],viz.BODY_ORI)
	if viz.key.isDown(viz.KEY_DOWN):
		view.move([0,0,-MOVE_SPEED*viz.elapsed()],viz.BODY_ORI)
	if viz.key.isDown(viz.KEY_RIGHT):
		view.setEuler([TURN_SPEED*viz.elapsed(),0,0],viz.BODY_ORI,viz.REL_PARENT)
	if viz.key.isDown(viz.KEY_LEFT):
		view.setEuler([-TURN_SPEED*viz.elapsed(),0,0],viz.BODY_ORI,viz.REL_PARENT)

vizact.ontimer(0,updateMovement)

#########################CREATE ROBOT################################
#Create body
body = createCube(1)
body.scale(0.8, 1, 0.5)
body.setPosition(3,0.8,-10)
body.name = "erik_body"

#Create legs
leg1 = createCylinder(0.2)
leg1.scale(1, 0.533, 1)
leg1.setParent(body)
leg1.setPosition(0.2,-0.8, 0.4)
leg1.name = "erik_leg1"
leg2 = createCylinder(0.2)
leg2.scale(1, 0.533, 1)
leg2.setParent(body)
leg2.setPosition(0.8,-0.8, 0.4)
leg2.name = "erik_leg2"

#Create arms
arm1 = createCylinder(0.2)
arm1.scale(1, 0.533, 1)
arm1.setParent(body)
arm1.setPosition(0, 1, 0.4)
arm1.name = "erik_arm1"
arm2 = createCylinder(0.2)
arm2.scale(1, 0.533, 1)
arm2.setParent(body)
arm2.setPosition(1, 1, 0.4)
arm2.name = "erik_arm2"

#Create head
head = createCylinder(0.4)
head.scale(1, 0.2, 1)
head.setParent(body)
head.setPosition(0.5, 1, 0.4)
head.name = "erik_head"

def helicopterArms():
	arm1.setEuler([0,60*viz.elapsed(),0], viz.REL_LOCAL)
	arm2.setEuler([0,-35*viz.elapsed(),0], viz.REL_LOCAL)

vizact.ontimer(0, helicopterArms)

#Screen text
textScreen = viz.addText('Screen Text',viz.SCREEN)
textScreen.alignment(viz.ALIGN_RIGHT_BOTTOM)
textScreen.setPosition([0.95,0.05,0])

textScreen.message('')
def updateScreenText():
    object = viz.MainWindow.pick(info=True)
    if object.valid:
        name = object.name
        if name.startswith('erik_') or True:
            textScreen.message(name)
        else:
            textScreen.message('')

vizact.ontimer(0.1,updateScreenText)