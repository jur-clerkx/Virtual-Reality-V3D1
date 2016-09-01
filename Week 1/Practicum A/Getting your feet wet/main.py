import viz
import vizshape
import vizact
import random
import vizcam

#test23

#Start virtual world
viz.go()

#Set configuration
viz.collision(viz.ON)
viz.setMultiSample(4)
viz.MainWindow.fov(60)
#vizshape.addAxes()

viz.MainView.move([0, 0 ,-10])
viz.MainView.setEuler([0, 0, 0])

#Map
piazza = viz.addChild('piazza.osgb')

#male avatar
male = viz.addAvatar('vcc_male.cfg')
male.setPosition([4.5, 0, 7])
male.setEuler([0,0,0])
male.state(14)

#female avatar
female = viz.addAvatar('vcc_female.cfg')
female.setPosition([4.5, 0, 9])
female.setEuler([180, 0, 0])
female.state(14)

#plants
plants = []
for x in [-3,-2,-1,0]:
	for z in [4, 2, 0, -2, -4]:
		plant = viz.addChild('plant.osgb', cache=viz.CACHE_CLONE)
		plant.setPosition([x,0,z])
		plants.append(plant)
		

#Start the animation for the plants
spin = vizact.spin(0,1,0,15)
def spinPlant(plant):
	plant.addAction(spin)

vizact.ontimer2(3, 19, spinPlant, vizact.choice(plants))

#Generate random pigeons
pigeons = []
for i in range(10):
	#Generate random positions
	x = random.randint(3, 10)
	z = random.randint(2, 8)
	yaw = random.randint(0, 360)
	
	#Load a pigeon
	pigeon = viz.addAvatar('pigeon.cfg')
	
	#Set the position
	pigeon.setPosition([x, 0, z])
	pigeon.setEuler([yaw, 0, 0])
	pigeon.state(1)
	
	pigeons.append(pigeon)
	
def walkAvatars():
	walk1 = vizact.walkTo([4.5, 0, -40])
	vizact.ontimer2(0.5, 0, female.addAction, walk1)
	
	walk2 = vizact.walkTo([3.5, 0, -40])
	male.addAction(walk2)
	
vizact.onkeydown('w', walkAvatars)

def pigeonsFeed():
	random_speed = vizact.method.setAnimationSpeed(0,vizact.randfloat(0.7,1.5))
	random_walk = vizact.walkTo([vizact.randfloat(3,10),0,vizact.randfloat(2,8)])
	random_animation = vizact.method.state(vizact.choice([1,3],vizact.RANDOM))
	random_wait = vizact.waittime(vizact.randfloat(5.0,10.0))
	pigeon_idle = vizact.sequence( random_speed, random_walk, random_animation, random_wait, viz.FOREVER)

	for pigeon in pigeons:
		pigeon.addAction(pigeon_idle)

vizact.onkeydown('p',pigeonsFeed)