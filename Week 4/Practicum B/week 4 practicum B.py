#Import
import viz
import vizcam
import vizact
import random

#Set configuration
viz.setMultiSample(4)
viz.fov(60)
viz.clearcolor (viz.BLACK)
viz.collision(viz.OFF)

#Start virtual world
viz.go (viz.FULLSCREEN)

#Turn on the physics engine
viz.phys.enable()

#Movement
tracker = vizcam.addWalkNavigate(moveScale=2.0)
tracker.setPosition([0,1.8,0])
viz.link(tracker,viz.MainView)
viz.mouse.setVisible(True)

#Lights
#Headlight
headLight = viz.MainView.getHeadLight()
headLight.disable()

#Spot
spotLamp = viz.addChild('object 3.fbx')
spotLamp.setPosition(0,15,5)
spotLamp.setScale(0.02,0.02,0.02)
spotLamp.color(1,1,1)
spot = viz.addLight()
spot.position(0,15,5)
spot.spread(180)
spot.intensity(.1)
#spot.disable()

#Add map
ground = viz.addChild('ground.osgb')
ground.collidePlane()

#Load peugeot
peugeot = viz.add('Peugeot 207/Peugeot_207.obj')
peugeot.setPosition(0,0,5)
peugeot.setScale(0.0015,0.0015,0.0015)
peugeot.collideBox(density=1, bounce=0.1, friction=0.1)

#Add object
ramp = viz.addChild('object 2.fbx')
ramp.setScale(0.3,0.015,0.5)
ramp.setPosition(0,.5,12)
ramp.setEuler(0,-10,0)
ramp.color(1,1,0)
ramp.collideBox(density=100, bounce= 0, friction = 0)
ramp.disable(viz.DYNAMICS)

#Randomlight
lamp2 = viz.addLight()
lamp2.position(-5, 10,0)
lamp2.spread(180)
lamp2.intensity(.1)

def toggleLamp2():
	if lamp2.getEnabled():
		lamp2.disable()
	else:
		lamp2.enable()
	vizact.ontimer2(random.random() * 2, 0,toggleLamp2)

vizact.ontimer2(random.random() * 2, 0,toggleLamp2)

#Particle system
snow = viz.add('snow.osg', pos=[0,8,0])
snow.hasparticles()
snow.disable(viz.EMITTERS)
i = 0
def toggleParticle():
	global i
	if i:
		snow.disable(viz.EMITTERS)
		i = 0
	else:
		snow.enable(viz.EMITTERS)
		i = 1

vizact.onkeydown(' ', toggleParticle)

#Push car
def pushCar():
	peugeot.applyForce(dir = [0,0,900], duration = 1, pos=peugeot.getPosition())
	
vizact.onkeydown('p', pushCar)

#Get wheels
wheel1 = peugeot.getChild('Wheel_(1)0')
wheel2 = peugeot.getChild('Wheel_(1)0.Wheel_(1)1')
wheel3 = peugeot.getChild('Wheel_(1)0.Wheel_(1)2')
wheel4 = peugeot.getChild('Wheel_(1)0.Wheel_(1)3')
#Pick part
def pick():
	object = viz.pick()
	if object.valid():
		if object == wheel1 or object == wheel2 or object == wheel3 or object == wheel4:
			spinAction = vizact.spin(0,1,0,90,4)
			wheel1.addAction(spinAction)
			wheel2.addAction(spinAction)
			wheel3.addAction(spinAction)
			wheel4.addAction(spinAction)

vizact.onmousedown(viz.MOUSEBUTTON_LEFT, pick)