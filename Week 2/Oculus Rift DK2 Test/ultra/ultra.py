import viz
import vizconnect
import vizact
import random

#Load input settings
vizconnect.go('vizconnect_config.py')
viz.setMultiSample(8)

viz.mouse.setVisible(False)

ultraStage = viz.add('model.dae')
ultraStage.scale(7,7,7)
ultraStage.setPosition(0,-4.2,5)

#Set on collission
viz.MainView.collision(viz.ON)
viz.MainView.gravity(10)

#Light settings
headLight = viz.MainView.getHeadLight() 
headLight.disable() 
myLight = viz.addLight() 
myLight.setEuler( 0, 20 ,0 )

#Music
backgroundsong = viz.addAudio('audio/01. Ummet Ozcan vs. The Aston Shuffle vs. Bassjackers & REEZ & KSHMR - Lost In Savior (G-Bæss & Mike Destiny Edit).wav')
backgroundsong.play()

def showLocation():
	print viz.MainView.getPosition()

#Front right
for i in range(35):
	#Generate random positions
	x = random.randint(4, 20) * -1
	z = random.randint(8, 25) * -1
	yaw = random.randint(-30, 70)
	animation = random.randint(3,5)
	
	#Load a pigeon
	pigeon = viz.addAvatar('vcc_male.cfg')
	
	#Set the position
	pigeon.setPosition([x, -4.2, z])
	pigeon.setEuler([yaw, 0, 0])
	pigeon.state(animation)
	

#Front left
for i in range(35):
	#Generate random positions
	x = random.randint(4, 20)
	z = random.randint(8, 25) * -1
	yaw = random.randint(-70, 30)
	animation = random.randint(3,5)
	
	#Load a pigeon
	pigeon = viz.addAvatar('vcc_male.cfg')
	
	#Set the position
	pigeon.setPosition([x, -4.2, z])
	pigeon.setEuler([yaw, 0, 0])
	pigeon.state(animation)


vizact.ontimer(1, showLocation)

