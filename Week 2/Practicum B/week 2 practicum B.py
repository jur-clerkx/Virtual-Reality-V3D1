import viz
import vizcam
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.clearcolor (viz.SKYBLUE)
viz.collision(viz.ON)

viz.go (viz.FULLSCREEN)

#Headlight
headLight = viz.MainView.getHeadLight()
headLight.disable(False)

#Movement
tracker = vizcam.addWalkNavigate(moveScale=2.0)
tracker.setPosition([0,1.8,0])
viz.link(tracker,viz.MainView)
#viz.mouse.setVisible(False)

#Map
viz.addChild('ground.osgb')

#Objects
#aanbeeld
vorm1 = viz.addChild('object 1.fbx')
vorm1.setScale(0.1,0.1,0.1)
vorm1.setPosition(0,0,5)
vorm1.color(255,255,255)

#kubus
vorm2 = viz.addChild('object 2.fbx')
vorm2.setScale(0.1,0.1,0.1)
vorm2.setPosition(0,0,10)
vorm2.color(0,255,0)

#bol
vorm3 = viz.addChild('object 3.fbx')
vorm3.setScale(0.1,0.1,0.1)
vorm3.setPosition(4,0,5)
vorm3.color(255,0,0)

#cilinder
vorm4 = viz.addChild('object 4.fbx')
vorm4.setScale(0.1,0.1,0.1)
vorm4.setPosition(8,0,-6)
vorm4.color(255,0,0)
vorm4.specular(0,255,0)
vorm4.shininess(100)

#pyramide
vorm5 = viz.addChild('object 5.fbx')
vorm5.setScale(0.1,0.1,0.1)
vorm5.setPosition(-4,0,10)
vorm5.emissive(0,0,255)