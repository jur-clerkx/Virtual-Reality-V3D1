import viz
viz.go()

#texture unit
texUnit = 0

# Load texture
tex = viz.addTexture('star.jpg')
texUniform = viz.addUniformInt('colorMap0', 0)
texBrick = viz.addTexture('brick.jpg')
texBrickUniform = viz.addUniformInt('colorMap1', 1)

# Create surface to wrap the texture on
quadA = viz.addTexQuad()
quadB = viz.addTexQuad()

quadA.setPosition([-.75, 2, 3]) #put quad in view
quadB.setPosition([.75,2,3]) 	#put second quad on screen

# Wrap texture on quad
quadA.texture((tex),unit=0)
quadA.texture((texBrick), unit=1)
quadB.texture((tex),unit=texUnit)

shader = viz.addShader(vert='texShader.vert',frag= 'texShader.frag' )
quadA.apply(shader)

quadA.apply(texUniform)
quadA.apply(texBrickUniform)

textureBlend = viz.addUniformFloat('textureBlend', 0.2)
quadA.apply(textureBlend)