import viz
import vizcam

viz.setMultiSample(4)
viz.fov(60)
viz.clearcolor (viz.SKYBLUE)
viz.collision(viz.ON)

viz.go (viz.FULLSCREEN)

#Turn on the physics engine
viz.phys.enable()

#Move the viewpoint so that it can see the show
viz.MainView.setPosition(0,2,-20)

#Movement
tracker = vizcam.addWalkNavigate(moveScale=2.0)
tracker.setPosition([0,1.8,0])
viz.link(tracker,viz.MainView)
viz.mouse.setVisible(False)

#Map
ground = viz.addChild('ground.osgb')
ground.collidePlane() #Make ground collide with objects as if it were an infinite plane

#Create seesaw board
seesaw = viz.addChild('box.wrl')
seesaw.setScale(10,0.3,1)
seesaw.collideBox() #Make object collide as if a bounding box surrounded the object

#Create balance point of seesaw
fulcrum = viz.addChild('tut_cone.wrl')
fulcrum.setScale(0.5,0.5,0.5)
fulcrum.setPosition(0,.01,1)
fulcrum.collideMesh() #Make object collide if its actual gemoetry intersects another object
fulcrum.disable(viz.DYNAMICS) #Disables dynamic physics forces from action on the object

#Create weight on right side of seesaw
load = viz.addChild('duck.wrl')
load.collideBox()

#Create weight on left side of seesaw
counterWeight = viz.addAvatar('duck.cfg')
counterWeight.collideBox(density=5) #The high density parameter makes the object heavier

#Puts the moving objects in their original state
def reset():
	seesaw.reset() #Zeros out all forces
	seesaw.setPosition(0,3,5)
	seesaw.setEuler(0,0,0) #Puts object upright
	
	load.reset()
	load.setPosition(4,5,5)
	load.setEuler(0,0,0)
	
	counterWeight.reset
	counterWeight.setPosition(-4,10,5)
	counterWeight.setEuler(90,0,0)
	
#Reset simulation
reset()

vizact.onkeydown(' ', reset)

