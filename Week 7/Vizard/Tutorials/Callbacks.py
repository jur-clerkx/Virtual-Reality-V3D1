import viz
import vizact
import random
viz.go()

#Turn on the physics engine 
viz.phys.enable() 

#Add ground 
ground = viz.addChild('ground.osgb')
ground.collidePlane() #Make ground collide with objects as if it were an infinite plane

#Create a bumper prototype to copy for all other bumpers 
bumper = viz.addChild( 'table.wrl' ) 
bumper.setPosition([0,5,10])
bumper.setScale( 1, 1, 1 ) 
#Create a collideBox for each child node rather than one encompassing the entire model 
bumper.collideBox( node='Leg1', bounce = 1, friction = .00000001 ) 
bumper.collideBox( node='Leg2', bounce = 2, friction = .00000001 ) 
bumper.collideBox( node='Leg3', bounce = 1, friction = .00000001 ) 
bumper.collideBox( node='Leg4', bounce = 3, friction = .00000001 ) 
bumper.collideBox( node='Top', bounce = 1, friction = .00000001 ) 

bumper.enable( viz.COLLIDE_NOTIFY ) #We want to be notified of things colliding with the bumper 

#Called when two objects collide in the physics simulator  
def onCollide(e):
	#Change color of bumper
	e.obj1.color( random.choice( [viz.RED,viz.GREEN,viz.SKYBLUE,viz.YELLOW,viz.ORANGE,viz.PURPLE] ) )
	#Play sound at a volume appropriate for ball speed
	speed = vizmat.Vector( e.obj1.getVelocity() ).length()
	if speed > .7:
	    viz.playSound( 'crashNew.wav' )
	elif speed > .4:
	    viz.playSound( 'crashQuiet.wav' )
	elif speed > .1:
		viz.playSound( 'crashVeryQuiet.wav' )

viz.callback( viz.COLLIDE_BEGIN_EVENT, onCollide )