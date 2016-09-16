import viz
import vizcam

viz.setMultiSample(4)
viz.fov(60)
viz.clearcolor (viz.SKYBLUE)
viz.collision(viz.ON)

viz.go (viz.FULLSCREEN)

#Turn on the physics engine
viz.phys.enable()

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
