import viz
import vizshape
import vizact
viz.go()
#Set default fog and mode
fogmode = 1
viz.fog(1, 30)
viz.fogcolor(255,255,255)

#Add the duck
duck = viz.add("duck.cfg")
duck.setPosition(0,0,10)
duck.setEuler(180,0,0)

#Add the sphere
sphere = vizshape.addSphere(1,100,100)
sphere.setPosition(5,0,15)
sphere.color(viz.WHITE)

#Add the character
character = viz.add("vcc_female.cfg")
character.setEuler(180,0,0)
character.setPosition(-2,0,15)

floor = viz.add("piazza.osgb")

# Perform a simple animation so light results are better noticable
moveForward = vizact.move(0,0,5,2) 
moveBackwards = vizact.move(0,0,-5,2) 
moveBackAndForth = vizact.sequence(moveForward,moveBackwards,viz.FOREVER) 
sphere.addAction(moveBackAndForth)
character.addAction(moveBackAndForth)

def toggleFogMode():
	global fogmode;
	if fogmode == 1:
		viz.fog(0.1)
		fogmode = 2
	elif fogmode == 2:
		viz.fog(0)
		fogmode = 3
	elif fogmode == 3:
		viz.fog(1,30)
		fogmode = 1


vizact.onkeydown('f', toggleFogMode)