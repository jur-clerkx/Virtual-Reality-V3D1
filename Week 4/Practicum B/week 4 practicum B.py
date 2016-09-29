#Import
import viz
import vizcam
import vizact

#Set configuration
viz.setMultiSample(4)
viz.fov(60)
viz.clearcolor (viz.BLACK)
viz.collision(viz.ON)

#Start virtual world
viz.go (viz.FULLSCREEN)

#Bobcat
bobcat = viz.add('FinalHigh2.obj')
bobcat.setPosition(0,0,5)
bobcat.setEuler(90, 0, 0)
#bobcat.texture(bobcatText)
bobcat.shininess(1)

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
spotLamp.setPosition(0,3,0)
spotLamp.setScale(0.02,0.02,0.02)
spotLamp.color(1,1,1)
spot = viz.addLight()
spot.position(0,3,0)
spot.direction(0,-1,0)
spot.spread(90)
spot.intensity(1)
spot.spotexponent(2)
spot.setPosition(0,0,0)
spot.color(1,1,1)
#spot.disable()

#Add map
ground = viz.addChild('ground.osgb')
