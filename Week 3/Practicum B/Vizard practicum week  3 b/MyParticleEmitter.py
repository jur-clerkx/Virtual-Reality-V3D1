import viz
import random
viz.go()

class Particle:
	"""Simple particle object"""
	size = 1
	color = [0,0,1]
	position = [0,0,0]
	maxLife = 100
	currentLife = 0
	alive = True
	direction = [0,0,0]
	velocity = 0
	quad = 0
	def Update(self):
		"""Updates the particle"""
		if(self.alive):
			self.currentLife+=1
			#check if the particle is still alive. If not disable it.
			if self.currentLife > self.maxLife:
				self.currentLife = 0
				self.alive = False
				self.quad.visible = False
			else:
				#Update the particle parameters.
				self.position[0] += self.velocity * self.direction[0]
				self.position[1] += self.velocity * self.direction[1]
				self.position[2] += self.velocity * self.direction[2]
				self.quad.setPosition(self.position)
				self.quad.color( self.color)
	def Reset(self, particleTexture):
		"""Resets the particle 'birth' parameters"""
		self.position = [random.randrange(-5,5,1),0,0]
		self.size = 1
		self.currentLife = 0
		self.maxLife = random.randrange(10,100,1)
		self.alive = True
		self.quad.texture(particleTexture)
		self.velocity = random.random()
		self.direction = [0,-0.1,0]
		self.quad.visible = True
	def __init__(self):
		"""Particle constructor. Creates a texquad in billboard mode"""
		self.quad = viz.addTexQuad()
		self.quad.billboard(viz.BILLBOARD_VIEW)
class Emitter(viz.EventClass):
	"""Simple particle emitter class"""
	particles = []
	maxParticles = 200
	particleTexture = 0
	def Reset(self,texture):
		"""Resets the emitter. Creates new particles"""
		self.particleTexture = texture
		for i in range(self.maxParticles):
			p = Particle()
			p.Reset(texture)
			self.particles.append(p)
			#Creates a timer callback object to update itself in a timely fashion.
		self.callback(viz.TIMER_EVENT, self.TimerHandler)
		self.starttimer(1, 0.01, viz.FOREVER)
	def Update(self):
		"""Updates the emitter, indirectly updates all particles"""
		for particle in self.particles:
			particle.Update()
			#If the particle has died, respawn it.
			if(particle.alive != True):
				 particle.Reset(self.particleTexture)
	def TimerHandler(self, num):
		""" Timer callback in order to update the emitter"""
		self.Update()

# Load texture
texture = viz.addTexture('particle_alpha.png')
#Create the emitter and add a texture
e = Emitter()
e.Reset(texture)

#Position the viewpoint.
view = viz.MainView
view.setPosition(0,-2,-50)
		





