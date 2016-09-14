import viz
import vizcam
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.clearcolor (viz.BLACK)

viz.go (viz.FULLSCREEN)

#Movement
tracker = vizcam.addWalkNavigate(moveScale=2.0)
tracker.setPosition([0,1.8,0])
viz.link(tracker,viz.MainView)
#viz.mouse.setVisible(False)

#acts
moveForward = vizact.move(0,0,4,1)
turnRight = vizact.spin(0,1,0,90,1)
moveInSquare = vizact.sequence(moveForward,turnRight,16)

#Lights
#Headlight
headLight = viz.MainView.getHeadLight()
headLight.disable()

#Directional
directionalLamp = viz.addChild('object 1.fbx')
directionalLamp.setPosition(-4,5,0)
directionalLamp.setScale(0.02,0.02,0.02)
directionalLamp.color(255,255,255)
directional = viz.addLight()
directional.setPosition(-4,5,0)
directional.setEuler(90,0,0)
directional.color(10,0,0)
#directional.disable()


#Point
pointLamp = viz.addChild('object 2.fbx')
pointLamp.setPosition(-12,1,4)
pointLamp.setScale(0.02,0.02,0.02)
pointLamp.color(255,255,255)
point = viz.addLight()
point.position(-12,1,4)
point.spread(180)
point.intensity(1)
point.color(0,10,0)
#point.disable()

#Spot
spotLamp = viz.addChild('object 3.fbx')
spotLamp.setPosition(0,0,0)
spotLamp.setScale(0.02,0.02,0.02)
spotLamp.color(255,255,255)
spot = viz.addLight()
spot.position(0,0,0)
spot.direction(0,0,1)
spot.spread(90)
spot.intensity(1)
spot.spotexponent(2)
spot.setPosition(0,1,0)
spot.color(0,0,10)
#spot.disable()

#Mover
mover = viz.addLight()
mover.setPosition(6,4,-8)
mover.color(10,0,10)
vizact.onkeydown(' ',mover.addAction, moveInSquare)
moverLamp = viz.addChild('object 4.fbx')
moverLamp.setPosition(6,4,-8)
moverLamp.setScale(0.02,0.02,0.02)
moverLamp.color(255,255,255)
vizact.onkeydown(' ',moverLamp.addAction, moveInSquare)
#mover.disable()

#Map
viz.addChild('ground.osgb')

#Objects
#aanbeeld
vorm1 = viz.addChild('object 1.fbx')
vorm1.setScale(0.1,0.1,0.1)
vorm1.setPosition(0,0,5)
vorm1.color(255,255,255)

#kubus
vorm2 = viz.addChild('object 2.fbx')
vorm2.setScale(0.1,0.1,0.1)
vorm2.setPosition(0,0,10)
vorm2.color(0,255,0)

#bol
vorm3 = viz.addChild('object 3.fbx')
vorm3.setScale(0.1,0.1,0.1)
vorm3.setPosition(4,0,5)
vorm3.color(255,0,0)

#cilinder
vorm4 = viz.addChild('object 4.fbx')
vorm4.setScale(0.1,0.1,0.1)
vorm4.setPosition(8,0,-6)
vorm4.color(255,0,0)
vorm4.specular(0,255,0)
vorm4.shininess(100)

#pyramide
vorm5 = viz.addChild('object 5.fbx')
vorm5.setScale(0.1,0.1,0.1)
vorm5.setPosition(-4,0,10)
vorm5.emissive(0,0,255)

#Toggle directional light event method
def toggleDirectional(*args, **kw):
	if args[1]:
		if directional.getEnabled():
			directional.disable()
		else:
			directional.enable()
			
#Toggle moving light event method
def toggleMover(*args, **kw):
	if args[1]:
		if mover.getEnabled():
			mover.disable()
		else:
			mover.enable()

#Toggle spot light event method
def toggleSpot(*args, **kw):
	if args[1]:
		if spot.getEnabled():
			spot.disable()
		else:
			spot.enable()

#Toggle point light event method
def togglePoint(*args, **kw):
	if args[1]:
		if point.getEnabled():
			point.disable()
		else:
			point.enable()

#GUI
buttonDir = viz.addButtonLabel('Toggle directional')
buttonDir.setPosition(.1,.9)
buttonDir.addEventCallback(viz.BUTTON_EVENT, toggleDirectional)

buttonSpot = viz.addButtonLabel('Toggle spotlight')
buttonSpot.setPosition(.1,.85)
buttonSpot.addEventCallback(viz.BUTTON_EVENT, toggleSpot)

buttonMover = viz.addButtonLabel('Toggle moving light')
buttonMover.setPosition(.1,.8)
buttonMover.addEventCallback(viz.BUTTON_EVENT, toggleMover)

buttonPoint = viz.addButtonLabel('Toggle point light')
buttonPoint.setPosition(.1,.75)
buttonPoint.addEventCallback(viz.BUTTON_EVENT, togglePoint)


check = viz.add(viz.CHECKBOX)
check.setPosition(.1, .7)

#The checkbox will control if collision is enabled
vizact.onbuttondown(check,viz.collision,viz.ON)
vizact.onbuttonup(check,viz.collision,viz.OFF)

def createCube(size):
	#Bottom
	viz.startLayer(viz.POLYGON)
	viz.vertexColor(255, 0, 0)
	viz.vertex(0,0,0)
	viz.vertex(size, 0, 0)
	viz.vertex(size, 0, size)
	viz.vertex(0, 0, size)
	
	#Front
	viz.startLayer(viz.POLYGON)
	viz.vertexColor(255, 0, 0)
	viz.vertex(0,0,0)
	viz.vertex(size, 0, 0)
	viz.vertex(size, size, 0)
	viz.vertex(0, size, 0)
	
	#Right
	viz.startLayer(viz.POLYGON)
	viz.vertexColor(255, 0, 0)
	viz.vertex(size, 0, 0)
	viz.vertex(size, 0, size)
	viz.vertex(size, size, size)
	viz.vertex(size, size, 0)
	
	#Left
	viz.startLayer(viz.POLYGON)
	viz.vertexColor(255, 0, 0)
	viz.vertex(0, 0, 0)
	viz.vertex(0, size, 0)
	viz.vertex(0, size, size)
	viz.vertex(0, 0, size)
	
	#Back
	viz.startLayer(viz.POLYGON)
	viz.vertexColor(255, 0, 0)
	viz.vertex(0, 0, size)
	viz.vertex(0, size, size)
	viz.vertex(size, size, size)
	viz.vertex(size, 0, size)
	
	#Top
	viz.startLayer(viz.POLYGON)
	viz.vertexColor(255, 0, 0)
	viz.vertex(0, size, 0)
	viz.vertex(size, size, 0)
	viz.vertex(size, size, size)
	viz.vertex(0, size, size)
	cube = viz.endlayer()
	
	cube.setPosition(0, 0, -5)
	return cube

cube = createCube(3)