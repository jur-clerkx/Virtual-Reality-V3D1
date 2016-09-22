#IMPORT
import viz
import vizcam
import vizinfo
import vizact

#SET CONFIGURATION
viz.setMultiSample(4)
viz.fov(60)
viz.clearcolor (viz.SKYBLUE)
viz.collision(viz.ON)

#Turn on the physics engine
viz.phys.enable()

#START VIRUTAL WORLD
viz.go (viz.FULLSCREEN)

#MOVEMENT
tracker = vizcam.addWalkNavigate(moveScale=2.0)
tracker.setPosition([0,1.8,-10])
viz.link(tracker,viz.MainView)
viz.mouse.setVisible(True)

#ADD MAP
ground = viz.addChild('ground.osgb')
ground.collidePlane()

#Start block pyramide
kubus1 = viz.addChild('object 2.fbx')
kubus1.setScale(0.1,0.1,0.1)
kubus1.setPosition(-2.5,0,10)
kubus1.color(0,.3,0)
kubus1.collideBox(density=0.2, bounce=1)

kubus2 = viz.addChild('object 2.fbx')
kubus2.setScale(0.1,0.1,0.1)
kubus2.setPosition(0,0,10)
kubus2.color(0,.3,0)
kubus2.collideBox(density=0.2, bounce=1)

kubus3 = viz.addChild('object 2.fbx')
kubus3.setScale(0.1,0.1,0.1)
kubus3.setPosition(2.5,0,10)
kubus3.color(0,.3,0)
kubus3.collideBox(density=0.2, bounce=1)

kubus4 = viz.addChild('object 2.fbx')
kubus4.setScale(0.1,0.1,0.1)
kubus4.setPosition(-1.25,2.1,10)
kubus4.color(0,.3,0)
kubus4.collideBox(density=0.2, bounce=1)

kubus5 = viz.addChild('object 2.fbx')
kubus5.setScale(0.1,0.1,0.1)
kubus5.setPosition(1.25,2.1,10)
kubus5.color(0,.3,0)
kubus5.collideBox(density=0.2, bounce=1)

kubus6 = viz.addChild('object 2.fbx')
kubus6.setScale(0.1,0.1,0.1)
kubus6.setPosition(0,4.2,10)
kubus6.color(0,.3,0)
kubus6.collideBox(density=0.2, bounce=1)

pyramide = viz.addChild('object 5.fbx')
pyramide.setScale(0.1,0.1,0.1)
pyramide.setPosition(0,6.3,10)
pyramide.color(.5,.5,0)
pyramide.collideBox(density=0.2, bounce=1)

#Load duck
duck = viz.addChild('duck.wrl')
duck.setScale(1.5,1.5,1.5)
duck.setPosition(0,1.2,0)

#ACT
def pushObject():
	info = viz.pick( True ) #Get object that cursor is pointing at
	if info.valid and info.object == duck:
		duck.collideBox(density=2)
		#Create a vector from the mouse position into the world
		line = viz.MainWindow.screenToWorld(viz.mouse.getPosition())
		vec = viz.Vector( line.dir )
		vec.setLength( 200 )
		info.object.applyForce( dir = vec, duration = 0.5, pos = info.point )
		
vizact.onmousedown(viz.MOUSEBUTTON_LEFT, pushObject)

def reset():
	kubus1.reset()
	kubus1.setEuler(0,0,0)
	kubus1.setPosition(-2.5,0,10)
	
	kubus2.reset()
	kubus2.setEuler(0,0,0)
	kubus2.setPosition(0,0,10)
	
	kubus3.reset()
	kubus3.setEuler(0,0,0)
	kubus3.setPosition(2.5,0,10)
	
	kubus4.reset()
	kubus4.setEuler(0,0,0)
	kubus4.setPosition(-1.25,2.1,10)
	
	kubus5.reset()
	kubus5.setEuler(0,0,0)
	kubus5.setPosition(1.25,2.1,10)
	
	kubus6.reset()
	kubus6.setEuler(0,0,0)
	kubus6.setPosition(0,4.2,10)
	
	pyramide.reset()
	pyramide.setEuler(0,0,0)
	pyramide.setPosition(0,6.3,10)
	
	duck.reset()
	duck.setEuler(0,0,0)
	duck.setPosition(0,1.2,0)
	duck.collideNone()


vizact.onkeydown(' ', reset)
