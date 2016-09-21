#IMPORT
import viz
import vizcam
import vizinfo
import vizact

#SET CONFIGURATION
viz.setMultiSample(4)
viz.fov(60)
#viz.clearcolor (viz.SKYBLUE)
viz.collision(viz.ON)

viz.move(0,0,-10)

#START VIRUTAL WORLD
viz.go (viz.FULLSCREEN)

#MOVEMENT
tracker = vizcam.addWalkNavigate(moveScale=2.0)
tracker.setPosition([0,1.8,0])
viz.link(tracker,viz.MainView)
viz.mouse.setVisible(True)

#ADD MAP
ground = viz.addChild('ground.osgb')

#Load textures
pic1 = viz.addTexture('bier.jpg')

pic2 = viz.addTexture('kroeg.jpg')

pic3 = viz.addTexture('model.jpg')

#Objects
quad1 = viz.addTexQuad()
quad1.setPosition(-2,2,12)
quad1.texture(pic1)
quad1.billboard(viz.BILLBOARD_VIEW)

quad2 = viz.addTexQuad()
quad2.setPosition(0,2,6)
quad2.texture(pic2)
quad2.billboard(viz.BILLBOARD_YAXIS)

quad3 = viz.addTexQuad()
quad3.setPosition(2,2,12)
quad3.texture(pic3)
quad3.billboard(viz.BILLBOARD_VIEW_POS)

#kubus
kubus = viz.addChild('object 2.fbx')
kubus.setScale(0.1,0.1,0.1)
kubus.setPosition(-5,0,10)
kubus.color(0,.3,0)
kubus.billboard()

#particles
fire = viz.add('fire2.osg',pos=[0,1.8,2])
fire.hasparticles()
