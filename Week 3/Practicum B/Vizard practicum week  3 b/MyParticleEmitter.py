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
	def Reset(self, particleTexture, position):
		"""Resets the particle 'birth' parameters"""
		self.position = position[:]
		self.size = 1
		self.currentLife = 0
		self.maxLife = random.randrange(10,100,1)
		self.alive = True
		self.quad.texture(particleTexture)
		self.velocity = random.random()
		self.direction = [0,-0.1,0]
		self.quad.visible = True
		self.quad.setScale(self.size, self.size)
	def __init__(self):
		"""Particle constructor. Creates a texquad in billboard mode"""
		self.quad = viz.addTexQuad()
		self.quad.billboard(viz.BILLBOARD_VIEW)

class Emitter(viz.EventClass):
	"""Simple particle emitter class"""
	position = [0,0,0]
	particles = []
	maxParticles = 50
	particleTexture = 0
	def Reset(self,texture):
		"""Resets the emitter. Creates new particles"""
		self.particleTexture = texture
		self.particles = []
		for i in range(self.maxParticles):
			p = GravityParticle()
			p.Reset(texture, self.position)
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
				particle.Reset(self.particleTexture, self.position)
	def TimerHandler(self, num):
		""" Timer callback in order to update the emitter"""
		self.Update()

class BirthRateEmitter(Emitter):
	spawnRate = 100
	def Reset(self,texture):
		"""Resets the emitter. Creates new particles"""
		self.particleTexture = texture
		self.particles = []
		self.callback(viz.TIMER_EVENT, self.TimerHandler)
		self.starttimer(1, 0.01, viz.FOREVER)
		self.starttimer(2, 1.0/self.spawnRate, viz.FOREVER)
	def Update(self):
		"""Updates the emitter, indirectly updates all particles"""
		for particle in self.particles:
			particle.Update()
			#If the particle has died, remove it from the list
			if(particle.alive != True):
				self.particles.remove(particle)
				particle.quad.remove()
	def TimerHandler(self, num):
		""" Timer callback in order to update the emitter"""
		if num == 1:
			self.Update()
		elif num == 2:
			p = RandomParticle()
			p.Reset(texture, self.position)
			self.particles.append(p)

#Particle with mostly random variables
class RandomParticle(Particle):
	def Reset(self, particleTexture, position):
		"""Resets the particle 'birth' parameters"""
		self.position = position[:]
		self.size = random.random()
		self.color = [random.random(),random.random(),random.random()]
		self.currentLife = 0
		self.maxLife = random.randrange(10,100,1)
		self.alive = True
		self.quad.texture(particleTexture)
		self.velocity = random.random()
		self.direction = [random.random()-0.5,random.random()-0.5,0]
		self.quad.visible = True
		self.quad.setScale(self.size, self.size)
		
class SmokeParticle(Particle):
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
				#Calculate new color and size
				self.size = self.startsize + (self.endsize - self.startsize) * (self.currentLife / self.maxLife)
				self.color[0] = self.startcolor[0] + (self.endcolor[0] - self.startcolor[0]) * (self.currentLife / self.maxLife)
				self.color[1] = self.startcolor[1] + (self.endcolor[1] - self.startcolor[1]) * (self.currentLife / self.maxLife)
				self.color[2] = self.startcolor[2] + (self.endcolor[2] - self.startcolor[2]) * (self.currentLife / self.maxLife)
				self.alpha = self.startalpha + (self.endalpha - self.startalpha) * (self.currentLife / self.maxLife)
				self.quad.setPosition(self.position)
				self.quad.setScale(self.size, self.size)
				#self.quad.alpha(self.alpha)
				self.quad.color( self.color)
	def Reset(self, particleTexture, position):
		"""Resets the particle 'birth' parameters"""
		self.position = position[:]
		self.size = random.random() + 1
		self.alpha = 0.9
		self.startalpha = 0.9
		self.endalpha = 0
		self.startsize = self.size
		self.endsize = self.size * 5
		self.color = [0.1,0.1,0.1]
		self.startcolor = self.color[:]
		self.endcolor = [1, 1, 1]
		self.currentLife = 0.0
		self.maxLife = random.randrange(100,500,1)
		self.alive = True
		self.quad.texture(particleTexture)
		self.velocity = random.random() / 10
		self.direction = [random.random()-0.5,random.random(),0]
		self.quad.visible = True
		self.quad.setScale(self.size)

class AttractionEmitter(Emitter):
	maxParticles = 40
	def Reset(self,texture):
		"""Resets the emitter. Creates new particles"""
		self.particleTexture = texture
		self.particles = []
		for i in range(self.maxParticles):
			p = AttractionParticle(self)
			p.Reset(texture, self.position)
			self.particles.append(p)
			#Creates a timer callback object to update itself in a timely fashion.
		self.callback(viz.TIMER_EVENT, self.TimerHandler)
		self.starttimer(1, 0.01, viz.FOREVER)

class AttractionParticle(Particle):
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
				#Update particle direction
				self.direction[0] = (self.target.position[0] - self.position[0])
				self.direction[1] = (self.target.position[1] - self.position[1])
				self.direction[2] = (self.target.position[2] - self.position[2])
				#Update the particle parameters.
				self.position[0] += self.velocity * self.direction[0]
				self.position[1] += self.velocity * self.direction[1]
				self.position[2] += self.velocity * self.direction[2]
				self.quad.setPosition(self.position)
				self.quad.color( self.color)
	def Reset(self, particleTexture, position):
		"""Resets the particle 'birth' parameters"""
		self.position = [position[0] + (random.random() * 5) - 2.5, position[1] + (random.random() * 5) - 2.5, 0]
		self.size = 1
		self.currentLife = 0
		self.maxLife = random.randrange(10,100,1)
		self.alive = True
		self.quad.texture(particleTexture)
		self.velocity = random.random()
		self.direction = [random.random()*.2-0.1,random.random()*.2-0.1,0]
		self.color = [1,1,1]
		self.quad.visible = True
		self.quad.setScale(self.size, self.size)
	def __init__(self, target):
		"""Particle constructor. Creates a texquad in billboard mode"""
		self.target = target
		self.quad = viz.addTexQuad()
		self.quad.billboard(viz.BILLBOARD_VIEW)

class GravityParticle(Particle):
	explosionParticles = []
	def Update(self):
		"""Updates the particle"""
		if(self.alive):
			self.currentLife+=1
			#check if the particle is still alive. If not disable it.
			if self.position[1] < 0:
				self.currentLife = 0
				self.alive = False
				self.quad.visible = False
				self.explosionParticles.append(ExplosionParticle(self.position))
			else:
				#Update the particle parameters.
				self.position[0] += self.velocity * self.direction[0]
				self.position[1] += self.velocity * self.direction[1]
				self.position[2] += self.velocity * self.direction[2]
				#Update velocity
				self.direction[1] = self.direction[1] - 0.005
				self.quad.setPosition(self.position)
				self.quad.color( self.color)
		for expl in self.explosionParticles:
			expl.Update()
			if not expl.alive:
				self.explosionParticles.remove(expl)
	def Reset(self, particleTexture, position):
		"""Resets the particle 'birth' parameters"""
		self.position = position[:]
		self.size = 1
		self.currentLife = 0
		self.maxLife = random.randrange(100,200,1)
		self.alive = True
		self.quad.texture(particleTexture)
		self.velocity = random.random() + 0.1
		self.direction = [random.random()*0.4-0.2,random.random()*0.2 + 0.4,0]
		self.quad.visible = True
		self.quad.setScale(self.size, self.size)
	
	def __init__(self):
		"""Particle constructor. Creates a texquad in billboard mode"""
		self.quad = viz.addTexQuad()
		self.quad.billboard(viz.BILLBOARD_VIEW)
		
class ExplosionParticle():
	position = [0,0,0]
	alive = True
	def __init__(self, position):
		"""Particle constructor. Creates a texquad in billboard mode"""
		self.position = position
		self.currentLife = 0
		self.size = 0.1
		self.quad = viz.addTexQuad()
		self.quad.billboard(viz.BILLBOARD_VIEW)
		self.quad.texture(smokey)
		self.quad.setPosition(position)
		self.quad.setScale(self.size, self.size)
		self.quad.setEuler(0, 0,random.random()*360-180)
	def Update(self):
		if self.alive:
			self.currentLife += 1
			self.size += 0.005
			self.quad.setScale(self.size, self.size)
			if self.currentLife > 1000:
				self.alive = False
				self.quad.remove()

# Load texture
texture = viz.addTexture('particle_alpha.png')
smokey = viz.addTexture('rookwolk.png')
#Create the emitter and add a texture
e = BirthRateEmitter()
e.Reset(texture)
#Position the viewpoint.
view = viz.MainView
view.setPosition(0,-2,-50)
