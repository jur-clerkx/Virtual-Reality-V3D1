#Import
import viz
import vizcam
import vizact

#Set configuration
viz.setMultiSample(4)
viz.fov(60)
viz.clearcolor (viz.SKYBLUE)
viz.collision(viz.ON)

#Start virtual world
viz.go (viz.FULLSCREEN)

#Movement
tracker = vizcam.addWalkNavigate(moveScale=2.0)
tracker.setPosition([0,1.8,0])
viz.link(tracker,viz.MainView)
viz.mouse.setVisible(True)

#Add map
ground = viz.addChild('ground.osgb')

#Add objects
aanbeeld = viz.addChild('object 1.fbx')
aanbeeld.setScale(0.1,0.1,0.1)
aanbeeld.setPosition(3,0,8)

kubus = viz.addChild('object 2.fbx')
kubus.setScale(0.1,0.1,0.1)
kubus.setPosition(3,0,0)

bol = viz.addChild('object 3.fbx')
bol.setScale(0.1,0.1,0.1)
bol.setPosition(0,0,4)

cilinder = viz.addChild('object 4.fbx')
cilinder.setScale(0.1,0.1,0.1)
cilinder.setPosition(-4,0,2)

pyramide = viz.addChild('object 5.fbx')
pyramide.setScale(0.1,0.1,0.1)
pyramide.setPosition(0,0,12)

arrow = viz.addChild('arrow.wrl')
arrow.setScale([0.4,0.4,0.4])
arrow.visible(viz.OFF)

#Definition
def pick():
	object = viz.pick()
	if object.valid():
		pos = object.getPosition()
		pos[1] += 3.6
		arrow.setPosition(pos)
		arrow.visible(viz.ON)
		if object.valid() and object != arrow:
			arrow.disable(viz.PICKING)
	linepos = viz.MainWindow.screenToWorld(viz.mouse.getPosition())
	viz.startlayer(viz.LINES)
	if object:
		viz.vertexcolor(viz.RED)
	else:
		viz.vertexcolor(viz.BLUE)
	viz.vertex(linepos.begin)
	viz.vertex(linepos.end)
	line = viz.endlayer()
			
vizact.onmousedown(viz.MOUSEBUTTON_LEFT, pick)

