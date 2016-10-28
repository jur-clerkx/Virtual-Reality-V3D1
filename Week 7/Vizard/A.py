import viz
import vizact
import vizshape
import random
viz.go()

#Turn on the physics engine 
viz.phys.enable()
 
#Add ground 
ground = viz.addChild('ground.osgb')
ground.collidePlane() #Make ground collide with objects as if it were an infinite plane

body = viz.add('box.wrl',scale=[1.5,1,4],pos=[0,1,0]) # Body 
body.collideBox(density=.5) 

front = viz.add('ball.wrl',pos=[0,.5,2]) # Front Wheel 
front.collideSphere() 
frontJoint = viz.phys.addWheelJoint(body,front,pos=(0,.5,2),axis0=(0,-1,0),axis1=(1,0,0)) 

duck = viz.add('duck.cfg',pos=[0,2,0])
duck.setScale(.5,.5,.5)
duck.collideBox()
duckJoint = viz.phys.addUniversalJoint(duck,body,pos=[0,1,0])
duckJoint.setAxisLimit(0,-45,45)
duckJoint.setAxisLimit(1,-45,45)

rearLeft = viz.add('ball.wrl',pos=[-1,.5,-1.5]) # Rear Left Wheel 
rearLeft.collideSphere() 
rearLeftJoint = viz.phys.addHingeJoint(body,rearLeft,pos=(-1,.5,-1.5),axis0=(-1,0,0)) 
rearRight = viz.add('ball.wrl',pos=[1,.5,-1.5]) # Rear Right Wheel 
rearRight.collideSphere() 
rearRightJoint = viz.phys.addHingeJoint(body,rearRight,pos=(1,.5,-1.5),axis0=(-1,0,0)) 

def steer(val): 
    frontJoint.setMotorAngle(0,val,0xFF,.1) 

def SetThrottle(val): 
	frontJoint.setMotorThrottle(1,-val,1,1e6)
	rearLeftJoint.setMotorThrottle(100,-val,1,1e6)
	rearRightJoint.setMotorThrottle(100,-val,1,1e6)
vizact.onkeydown(viz.KEY_UP,SetThrottle,1) # Move forward 
vizact.onkeydown(viz.KEY_RIGHT,steer,45) # Steer Right 
vizact.onkeydown(viz.KEY_LEFT,steer,-45) # Steer Left 
vizact.onkeydown(viz.KEY_DOWN,SetThrottle,-1) # Move backwards