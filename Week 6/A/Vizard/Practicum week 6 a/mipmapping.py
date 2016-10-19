import viz
import vizact
viz.go()

#texture unit
texUnit = 0

# Load texture
tex = viz.addTexture('brick1.jpg')

#set mip map filters
tex.filter(viz.MIN_FILTER,viz.NEAREST)
tex.filter(viz.MAG_FILTER,viz.NEAREST)

# Create surface to wrap the texture on
quad = viz.addTexQuad()
quad.setPosition([0, 2, 1]) #put quad in view
# Wrap texture on quad
quad.texture((tex),unit=texUnit)

#move the brick wall
moveForward = vizact.move(0,0,-3,5) 
moveBackward = vizact.move(0,0,3,5) 
keepMoving = vizact.sequence(moveBackward,moveForward,viz.FOREVER) 

quad.addAction(keepMoving)

filterArray = [[viz.LINEAR, viz.LINEAR, 'LINEAR - LINEAR'],
				[viz.NEAREST, viz.LINEAR, 'NEAREST - LINEAR'],
				[viz.LINEAR_MIPMAP_LINEAR, viz.LINEAR, 'LINEAR_MIPMAP_LINEAR - LINEAR'],
				[viz.LINEAR_MIPMAP_NEAREST, viz.LINEAR, 'LINEAR_MIPMAP_NEAREST - LINEAR'],
				[viz.NEAREST_MIPMAP_LINEAR, viz.LINEAR, 'NEAREST_MIPMAP_LINEAR - LINEAR'],
				[viz.NEAREST_MIPMAP_NEAREST, viz.LINEAR, 'NEAREST_MIPMAP_NEAREST - LINEAR'],
				[viz.LINEAR, viz.NEAREST, 'LINEAR - NEAREST'],
				[viz.NEAREST, viz.NEAREST, 'NEAREST - NEAREST'],
				[viz.LINEAR_MIPMAP_LINEAR, viz.NEAREST, 'LINEAR_MIPMAP_LINEAR - NEAREST'],
				[viz.LINEAR_MIPMAP_NEAREST, viz.NEAREST, 'LINEAR_MIPMAP_NEAREST - NEAREST'],
				[viz.NEAREST_MIPMAP_LINEAR, viz.NEAREST, 'NEAREST_MIPMAP_LINEAR - NEAREST'],
				[viz.NEAREST_MIPMAP_NEAREST, viz.NEAREST, 'NEAREST_MIPMAP_NEAREST - NEAREST']]
counter = 0;
textScreen = viz.addText('NEAREST - NEAREST',viz.SCREEN)
textScreen.alignment(viz.ALIGN_RIGHT_BOTTOM)
textScreen.setPosition([0.95,0.05,0])
textScreen.fontSize(50)

def toggleFilterMode():
	global counter
	tex.filter(viz.MIN_FILTER,filterArray[counter][0])
	tex.filter(viz.MAG_FILTER,filterArray[counter][1])
	textScreen.message(filterArray[counter][2])
	counter += 1
	if counter == len(filterArray):
		counter = 0

vizact.onkeydown('m', toggleFilterMode)