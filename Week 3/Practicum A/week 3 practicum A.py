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

viz.move(0,0,-10)

#Turn on the physics engine
viz.phys.enable()

#START VIRUTAL WORLD
viz.go (viz.FULLSCREEN)

#MOVEMENT
tracker = vizcam.addWalkNavigate(moveScale=2.0)
tracker.setPosition([0,1.8,0])
viz.link(tracker,viz.MainView)
viz.mouse.setVisible(True)

#ADD MAP
ground = viz.addChild('ground.osgb')
ground.collidePlane()

#OBJECTS
#kubus1
kubus1 = viz.addChild('object 2.fbx')
kubus1.setScale(0.1,0.1,0.1)
kubus1.setPosition(-2,0,10)
kubus1.color(0,.3,0)
kubus1.collideBox()

#kubus2
kubus2 = viz.addChild('object 2.fbx')
kubus2.setScale(0.1,0.1,0.1)
kubus2.setPosition(2,0,10)
kubus2.color(0,.3,0)
kubus2.collideBox()

#aanbeeld
aanbeeld = viz.addChild('object 1.fbx')
aanbeeld.setScale(0.1,0.1,0.1)
aanbeeld.setPosition(0,1,10)
aanbeeld.color(0,0,.6)
aanbeeld.collideMesh()

#pyramide
pyramide = viz.addChild('object 5.fbx')
pyramide.setScale(0.1,0.1,0.1)
pyramide.setPosition(0,5,10)
pyramide.color(.5,.5,0)
pyramide.collideMesh()

#load
load = viz.addChild('duck.wrl')
load.collideBox()
load.setPosition(0,10,0)

#bol
bol = viz.addChild('object 3.fbx')
bol.setScale(0.1,0.1,0.1)
bol.setPosition(4,3,4)
bol.color(.7,0,0)
bol.collideMesh()

#cilinder
cilinder = viz.addChild('object 4.fbx')
cilinder.setScale(0.1,0.1,0.1)
cilinder.setPosition(4,0,4)
cilinder.color(.7,0,0)
cilinder.collideMesh()

#ACT
def pushObject():
	info = viz.pick( True ) #Get object that cursor is pointing at
	if info.valid and ( info.object == load or info.object == pyramide or info.object == kubus1 ):
		#Create a vector from the mouse position into the world
		line = viz.MainWindow.screenToWorld(viz.mouse.getPosition())
		vec = viz.Vector( line.dir )
		vec.setLength( 1 )
		info.object.applyForce( dir = vec, duration = 0.1, pos = info.point )
		return True

vizact.onmousedown(viz.MOUSEBUTTON_LEFT, pushObject)

def reset():
	kubus1.reset()
	kubus1.setPosition(-2,0,10)
	
	pyramide.reset()
	pyramide.setPosition(0,5,10)
	
	load.reset()
	load.setPosition(0,10,0)

#Reset simulation
reset()

vizact.onkeydown(' ', reset)
