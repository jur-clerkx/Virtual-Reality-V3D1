import viz
import vizshape
viz.go()


# Create a shader object by loading the vertex shader
# and fragment shader from the external files.
shader = viz.addShader(vert = "lightshader.vert",frag = "lightshadertoon.frag")

# Create the light parameters
# Green lightcolor
lightColor = (0.3,0.9,0.3,1.0)
# lightposition slightly behind the origin
lightPosition = (0.0,0.0,-6.0,0.0)


# Create the sphere
sphere = vizshape.addSphere(1,100,100)
sphere.color(viz.WHITE)

# Create uniform parameters.
# These will be passed to the shader.

# Step 1 Add light color uniform and apply to the sphere
uniformLightColor = viz.addUniformFloat('lightColor', lightColor)
sphere.apply(uniformLightColor)

# Step 2 Add light position uniform and apply to the sphere
uniformLightPosition = viz.addUniformFloat('lightPosition', lightPosition)
sphere.apply(uniformLightPosition)

# Set sphere settings and attach the shader to it.
sphere.setPosition(-2.0,2.0,6.0)
sphere.color(0.9,0.9,0.9)
sphere.apply(shader)

# Perform a simple animation so light results are better noticable
moveForward = vizact.move(0,0,4,1) 
turnRight = vizact.spin(0,1,0,90,1) 
moveInSquare = vizact.sequence(moveForward,turnRight,viz.FOREVER) 
sphere.addAction(moveInSquare)



