import viz

viz.go()

fire = viz.add('fire.osg',pos=(0,2,2))
fire.hasparticles()
vizact.onkeydown(' ',fire.enable,viz.EMITTERS) 