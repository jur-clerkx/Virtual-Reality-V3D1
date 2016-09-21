"""
Move the sliders and reset with the spacebar
to see how a nodes physical properties affect its behavior.
Click on an object to apply a force.
To move viewpoint use WASD keyboard controls.
"""
import viz
import vizact
import vizinfo

viz.setMultiSample(4)
viz.fov(60)
viz.go()

vizinfo.InfoPanel(align=viz.ALIGN_RIGHT_BOTTOM)

#Turn on the physics engine
viz.phys.enable()

#Interface to change box characteristics
boxInfo = vizinfo.InfoPanel('Box Material Characteristics', align=viz.ALIGN_LEFT_TOP)
boxInfo.addSeparator()
boxScale = boxInfo.addLabelItem('Scale',viz.addSlider())
boxDensity = boxInfo.addLabelItem('Density',viz.addSlider())
boxFriction = boxInfo.addLabelItem('Friction',viz.addSlider())
boxHardness = boxInfo.addLabelItem('Hardness',viz.addSlider())
boxBounce = boxInfo.addLabelItem('Bounce',viz.addSlider())
boxForce = boxInfo.addLabelItem('Force',viz.addSlider())
#Initial material settings
boxScale.set( .5 )
boxDensity.set( .5 )
boxForce.set( .3 )

#Interface to change ball characteristics
ballInfo = vizinfo.InfoPanel( 'Ball Material Characteristics', align=viz.ALIGN_RIGHT_TOP)
ballInfo.addSeparator()
ballScale = ballInfo.addLabelItem('Scale',viz.addSlider())
ballDensity = ballInfo.addLabelItem('Density',viz.addSlider())
ballFriction = ballInfo.addLabelItem('Friction',viz.addSlider())
ballHardness = ballInfo.addLabelItem('Hardness',viz.addSlider())
ballBounce = ballInfo.addLabelItem('Bounce',viz.addSlider())
ballForce = ballInfo.addLabelItem('Force',viz.addSlider())
#Initial material settings
ballScale.set( .5 )
ballDensity.set( .5 )
ballForce.set( .3 )

#Add lab
lab = viz.addChild('lab.osgb')
lab.collideMesh()
lab.disable(viz.DYNAMICS)

#Add one of the colliding objects
box = viz.addChild( 'crate.osgb' )

#Add the other colliding object
ball = viz.addChild( 'beachball.osgb' )


def reset():

	#Reset box

	#Place object in its starting position
	boxStartPOS = [ -3, .75, 2 ]
	box.setPosition( boxStartPOS )
	box.setEuler( [0, 0, 0] )

	#Scale according to slider
	scaleFactor = boxScale.get() * 2
	box.setScale( [scaleFactor]*3 )

	#Tell the box to collide as if it were a box and get the handle to its physics object
	box.collideNone() #remove existing physical shapes
	boxPhysicalShape = box.collideBox() #create new physical shape

	#Set the material properties from the sliders
	boxPhysicalShape.density = boxDensity.get()
	boxPhysicalShape.friction = boxFriction.get()
	boxPhysicalShape.hardness = boxHardness.get()
	boxPhysicalShape.bounce = boxBounce.get()

	#Place object on collision course with speed determined by the force slider
	box.applyForce( dir = [ 10 * boxForce.get(), 0, 0 ], duration=0.1, pos = boxStartPOS )


	#Reset Ball

	#Place object in its starting position
	ballStartPOS = [ 3, .5, 2 ]
	ball.setPosition( ballStartPOS )
	ball.setEuler( [0, 0, 0] )

	#Scale according to slider
	scaleFactor = ballScale.get() * 2
	ball.setScale( [scaleFactor]*3 )

	#Tell the ball to collide as if it were a sphere and get the handle to its physics object
	ball.collideNone() #remove existing physical shapes
	ballPhysicalShape = ball.collideSphere() #create new physical shape

	#Set the material properties from the sliders
	ballPhysicalShape.density = ballDensity.get()
	ballPhysicalShape.friction = ballFriction.get()
	ballPhysicalShape.hardness = ballHardness.get()
	ballPhysicalShape.bounce = ballBounce.get()

	#Place object on collision course with speed determined by the force slider
	ball.applyForce( dir = [ -10 * ballForce.get(), 0, 0 ], duration=0.1, pos = ballStartPOS )


reset()

vizact.onkeydown( ' ', reset )

#use keyboard navigation and use mouse for applying forces to objects
import vizcam
viz.cam.setHandler(vizcam.KeyboardCamera())

#Push objects around with mouse clicks
def pushObject():
	info = viz.pick( True ) #Get object that cursor is pointing at
	if info.valid and ( info.object == ball or info.object ==box ):
		#Create a vector from the mouse position into the world
		line = viz.MainWindow.screenToWorld(viz.mouse.getPosition())
		vec = viz.Vector( line.dir )
		vec.setLength( 1 )
		info.object.applyForce( dir = vec, duration = 0.1, pos = info.point )
		return True

vizact.onmousedown(viz.MOUSEBUTTON_LEFT, pushObject)

#Move viewpoint so that it can see the action
viz.MainView.setPosition([0, 2, -5])