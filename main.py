import pygame

from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
	pygame.init()
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	frame_limiter = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)
	player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
	asteroidfield = AsteroidField()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0, 0, 0))
		for object in drawable:
			object.draw(screen)
		for object in updatable:
			object.update(dt)
		for object in asteroids:
			if object.collision(player) == True:
				print("Game over!")
				pygame.QUIT
				return
		pygame.display.flip()
		frame_limiter.tick(60)
		dt = (frame_limiter.get_time() / 100)

if __name__ == "__main__":
	main()
