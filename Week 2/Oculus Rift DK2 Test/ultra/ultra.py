import viz
import vizconnect
import vizact
import random

#Load input settings
vizconnect.go('vizconnect_config.py')
viz.setMultiSample(8)

viz.mouse.setVisible(False)
viz.clearcolor(viz.BLUE)

ultraStage = viz.add('model.dae')
ultraStage.scale(7,7,7)
ultraStage.setPosition(5,0,20)

head_tracker = vizconnect.getTracker('rift_with_mouse_and_keyboard').getNode3d()

#Setup lightning
headLight = viz.MainView.getHeadLight() 
headLight.disable()
myLight = viz.addLight() 
myLight.setEuler(-15 ,15 ,15)

#Music
backgroundsong = viz.addAudio('audio/01. Ummet Ozcan vs. The Aston Shuffle vs. Bassjackers & REEZ & KSHMR - Lost In Savior (G-Bæss & Mike Destiny Edit).wav')
backgroundsong.play()

def up():
	head_tracker.translate([0,0.5,0])

def down():
	head_tracker.translate([0, -0.5, 0])

vizact.onkeydown(' ', up)
vizact.onkeydown(viz.KEY_CONTROL_L, down)