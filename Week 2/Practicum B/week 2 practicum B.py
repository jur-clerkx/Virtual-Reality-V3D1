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
viz.mouse.setVisible(False)

#Map
viz.addChild('ground.osgb')

#Load picture
#papier
pic1 = viz.addTexture('texture1.jpg')

#steen
pic2 = viz.addTexture('texture2.jpg')
pic2.wrap(viz.WRAP_T, viz.CLAMP_TO_BORDER)
pic2.wrap(viz.WRAP_S, viz.CLAMP_TO_BORDER)

#tegel
pic3 = viz.addTexture('texture3.jpg')
pic3.wrap(viz.WRAP_T, viz.MIRROR)
pic3.wrap(viz.WRAP_S, viz.MIRROR)

#Objects
#kubus1
vorm1 = viz.addChild('object 2.fbx')
vorm1.setScale(0.1,0.1,0.1)
vorm1.setPosition(0,0,5)
vorm1.texture(pic1)
matrix1 = vizmat.Transform()
matrix1.setScale(1.5,1.5,1)
matrix1.setTrans([-.25,-.25,1])
vorm1.texmat(matrix1)

#kubus2
vorm2 = viz.addChild('object 2.fbx')
vorm2.setScale(0.1,0.1,0.1)
vorm2.setPosition(0,0,10)
vorm2.texture(pic2)
matrix2 = vizmat.Transform()
matrix2.setScale(1.5,1.5,1)
matrix2.setTrans([-.25,-.25,1])
vorm2.texmat(matrix2)

#kubus3
vorm3 = viz.addChild('object 2.fbx')
vorm3.setScale(0.1,0.1,0.1)
vorm3.setPosition(4,0,5)
vorm3.texture(pic3)
matrix3 = vizmat.Transform()
matrix3.setScale(5,5,1)
matrix3.setTrans([-.5,-.5,1])
vorm3.texmat(matrix3)

#bol
vorm4 = viz.addChild('object 3.fbx')
vorm4.setScale(0.1,0.1,0.1)
vorm4.setPosition(8,0,-6)
vorm4.texture(pic3)
matrix4 = vizmat.Transform()
matrix4.setScale(2.5,2.5,1)
matrix4.setTrans([-.5,-.5,1])
vorm4.texmat(matrix4)

#kubus5
vorm5 = viz.addChild('object 2.fbx')
vorm5.setScale(0.1,0.1,0.1)
vorm5.setPosition(-4,0,10)
vorm5.texture(pic3)

#Create cube method
def createCube(size):
	#Bottom
	viz.startLayer(viz.POLYGON)
	viz.texCoord(0.0, 0.0)
	viz.vertex(0,0,0)
	viz.texCoord(1.0, 0.0)
	viz.vertex(size, 0, 0)
	viz.texCoord(1.0, 1.0)
	viz.vertex(size, 0, size)
	viz.texCoord(0.0, 1.0)
	viz.vertex(0, 0, size)
	
	#Front
	viz.startLayer(viz.POLYGON)
	viz.texCoord(0.0, 0.0)
	viz.vertex(0,0,0)
	viz.texCoord(1.0, 0.0)
	viz.vertex(size, 0, 0)
	viz.texCoord(1.0, 1.0)
	viz.vertex(size, size, 0)
	viz.texCoord(0.0, 1.0)
	viz.vertex(0, size, 0)
	
	#Right
	viz.startLayer(viz.POLYGON)
	viz.texCoord(0.0, 0.0)
	viz.vertex(size, 0, 0)
	viz.texCoord(1.0, 0.0)
	viz.vertex(size, 0, size)
	viz.texCoord(1.0, 1.0)
	viz.vertex(size, size, size)
	viz.texCoord(0.0, 1.0)
	viz.vertex(size, size, 0)
	
	#Left
	viz.startLayer(viz.POLYGON)
	viz.texCoord(0.0, 0.0)
	viz.vertex(0, 0, 0)
	viz.texCoord(0.0, 1.0)
	viz.vertex(0, size, 0)
	viz.texCoord(1.0, 1.0)
	viz.vertex(0, size, size)
	viz.texCoord(1.0, 0.0)
	viz.vertex(0, 0, size)
	
	#Back
	viz.startLayer(viz.POLYGON)
	viz.texCoord(0.0, 0.0)
	viz.vertex(0, 0, size)
	viz.texCoord(0.0, 1.0)
	viz.vertex(0, size, size)
	viz.texCoord(1.0, 1.0)
	viz.vertex(size, size, size)
	viz.texCoord(1.0, 0.0)
	viz.vertex(size, 0, size)
	
	#Top
	viz.startLayer(viz.POLYGON)
	viz.texCoord(0.0, 0.0)
	viz.vertex(0, size, 0)
	viz.texCoord(1.0, 0.0)
	viz.vertex(size, size, 0)
	viz.texCoord(1.0, 1.0)
	viz.vertex(size, size, size)
	viz.texCoord(0.0, 1.0)
	viz.vertex(0, size, size)
	cube = viz.endlayer()
	
	return cube

#Create dice cube method
def createDiceCube(size):
	#Bottom
	viz.startLayer(viz.POLYGON)
	viz.texCoord(0.0, 0.5)
	viz.vertex(0,0,0)
	viz.texCoord(0.333, 0.5)
	viz.vertex(size, 0, 0)
	viz.texCoord(0.333, 1)
	viz.vertex(size, 0, size)
	viz.texCoord(0.0, 1)
	viz.vertex(0, 0, size)
	
	#Front
	viz.startLayer(viz.POLYGON)
	viz.texCoord(0.0, 0.0)
	viz.vertex(0,0,0)
	viz.texCoord(0.3, 0.0)
	viz.vertex(size, 0, 0)
	viz.texCoord(0.3, 0.5)
	viz.vertex(size, size, 0)
	viz.texCoord(0.0, 0.5)
	viz.vertex(0, size, 0)
	
	#Right
	viz.startLayer(viz.POLYGON)
	viz.texCoord(0.333, 0.0)
	viz.vertex(size, 0, 0)
	viz.texCoord(0.666, 0.0)
	viz.vertex(size, 0, size)
	viz.texCoord(0.666, 0.5)
	viz.vertex(size, size, size)
	viz.texCoord(0.333, 0.5)
	viz.vertex(size, size, 0)
	
	#Left
	viz.startLayer(viz.POLYGON)
	viz.texCoord(0.333, 0.5)
	viz.vertex(0, 0, 0)
	viz.texCoord(0.333, 1.0)
	viz.vertex(0, size, 0)
	viz.texCoord(0.666, 1.0)
	viz.vertex(0, size, size)
	viz.texCoord(0.666, 0.5)
	viz.vertex(0, 0, size)
	
	#Back
	viz.startLayer(viz.POLYGON)
	viz.texCoord(0.666, 0.5)
	viz.vertex(0, 0, size)
	viz.texCoord(0.666, 1.0)
	viz.vertex(0, size, size)
	viz.texCoord(1.0, 1.0)
	viz.vertex(size, size, size)
	viz.texCoord(1.0, 0.5)
	viz.vertex(size, 0, size)
	
	#Top
	viz.startLayer(viz.POLYGON)
	viz.texCoord(0.666, 0.0)
	viz.vertex(0, size, 0)
	viz.texCoord(1, 0.0)
	viz.vertex(size, size, 0)
	viz.texCoord(1, 0.5)
	viz.vertex(size, size, size)
	viz.texCoord(0.666, 0.5)
	viz.vertex(0, size, size)
	cube = viz.endlayer()
	
	return cube

#Create the cube
cube = createCube(1)
cube.setPosition(0, .5, -5)

#load the texture
bricks = viz.addTexture('brick.jpg')
bricks.wrap(viz.WRAP_T, viz.REPEAT)
bricks.wrap(viz.WRAP_S, viz.REPEAT)

#Put texture on cube
cube.texture(bricks)

#Load dice texure
dice = viz.addTexture('dice.jpg')
bricks.wrap(viz.WRAP_T, viz.REPEAT)
bricks.wrap(viz.WRAP_S, viz.REPEAT)

#Create the dice
diceCube = createDiceCube(1)
diceCube.texture(dice)
diceCube.setPosition(-3, .5, -5)
