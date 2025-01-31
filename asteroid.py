import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

	def update(self, dt):
		self.position += (self.velocity * dt)

	def split(self):
		self.kill()
		if self.radius < ASTEROID_MIN_RADIUS:
			return
		else:
			random_angle = random.uniform(20, 50)
			first_vector = self.velocity.rotate(random_angle)
			second_vector = self.velocity.rotate(random_angle * -1)
			new_radius = (self.radius - ASTEROID_MIN_RADIUS)
			new_asteroid_one = Asteroid(self.position[0], self.position[1], new_radius)
			new_asteroid_two = Asteroid(self.position[0], self.position[1], new_radius)
			new_asteroid_one.velocity = (first_vector * 1.2)
			new_asteroid_two.velocity = (second_vector * 1.2)
