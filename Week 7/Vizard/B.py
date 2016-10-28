""" 
Demonstrates the single function creation of a grab object relationship. 
The arrow keys move the hand object. 
The w, a, s, d, keys rotate the hand. 
The t, g, h, f, keys rotate the ball. 
The spacebar toggles the grabbing. 
""" 
import viz
import vizact
import vizshape
import vizproximity
import vizcam

viz.setMultiSample(4)
viz.fov(60)
viz.go()

import vizinfo
vizinfo.InfoPanel()

#Create proximity manager
manager = vizproximity.Manager()
manager.setDebug(viz.ON)

viz.addChild('ground.osgb')

viz.clearcolor(viz.SLATE)

#Movement
tracker = vizcam.addWalkNavigate(moveScale=2.0)
tracker.setPosition([0,1.8,0])
viz.link(tracker,viz.MainView)
viz.mouse.setVisible(True)

#Add the object that will do the grabbing
hand = vizshape.addCylinder()
handlink = viz.link(tracker, hand)
handlink.preTrans([0.2,-.8, 1])
handlink.preEuler([0, 70,0])
hand.setScale(0.05,2,0.05)



#Add the object that the marker will grab
ball = viz.addChild( 'basketball.osgb',scale=[2,2,2] )
ball.setPosition( [0.5, 1.8, 2.5] )
target = vizproximity.Target(ball)
manager.addTarget(target)

ball2 = viz.addChild( 'basketball.osgb',scale=[2,2,2] )
ball2.setPosition( [-1, 1.8, 2.5] )
target2 = vizproximity.Target(ball2)
manager.addTarget(target2)

ball3 = viz.addChild( 'basketball.osgb',scale=[2,2,2] )
ball3.setPosition( [2, 1.8, 2.5] )
target3 = vizproximity.Target(ball3)
manager.addTarget(target3)

#Activate sensor
sensor = vizproximity.addBoundingSphereSensor(hand,scale=1.5)
manager.addSensor(sensor)

link = None #The handle to the link object
target = None #The handle to the target object
#Grab or let go of the ball
def toggleLink():
	global link
	global target
	if link:
		#If link exits, stop grabbing
		link.remove()
		link = None
	elif target:
		#If no link, grab the ball with the hand
		link = viz.grab( hand, target )

vizact.onkeydown(' ',toggleLink)

#Change state of avatar to talking when the user gets near
def EnterProximity(e):
	global target
	target = e.target.getSourceObject()


#Change state of avatar to idle when the user moves away
def ExitProximity(e):
	global target
	target = None

manager.onEnter(sensor,EnterProximity)
manager.onExit(sensor,ExitProximity)

def printPos():
	print hand.getPosition()

def updateXEuler(x):
	handlink.preEuler([0, x,0])
def updateYEuler(y):
	handlink.preEuler([0, 0,y])
	
#Setup keyboard control of hand and ball
vizact.whilekeydown(viz.KEY_UP,updateXEuler,vizact.elapsed(-90))
vizact.whilekeydown(viz.KEY_DOWN,updateXEuler,vizact.elapsed(90))
vizact.whilekeydown(viz.KEY_RIGHT,updateYEuler,vizact.elapsed(90))
vizact.whilekeydown(viz.KEY_LEFT,updateYEuler,vizact.elapsed(-90))