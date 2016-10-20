""" 
This script demonstrates how to project textures onto objects. 
The texture is being projected from a position above the origin. 
Use the controls to adjust the projection FOV and alpha. 
""" 
import viz
import vizfx
import vizact
import vizconfig
import math

viz.setMultiSample(4)
viz.fov(60)
viz.go()

#Move the viewpoint
viz.MainView.move([0,1,-3])

# Add environment
vizfx.addChild('lab.osgb')

# Add objects to environment
vizfx.addChild('beachball.osgb', pos=(-1.5,2,3.5))
vizfx.addChild('duck.cfg',pos=(1.5,0,1))

# Add a texture which will be projected
texture = viz.addTexture('dots.png')

# Create a projector using the texture
proj = vizfx.addProjector(texture, blend=vizfx.BLEND_OVERLAY)

# Translate the projector to the center of the room
proj.setPosition([0,5,0])
proj.setEuler([0,90,0])

#Set the projectors fov
proj.setFov(120)

# Apply the projector effect to the global composer
vizfx.getComposer().addEffect(proj.getEffect())

# Spin an object around the y axis at 90 deg/sec for 5 seconds. 
spinAction = vizact.spin(0,0,1,10)

proj.addAction(spinAction)