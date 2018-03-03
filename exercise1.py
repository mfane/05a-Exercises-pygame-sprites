#!/usr/bin/env python
'''

For every line, please add a comment describing what it does. 

Try to describe each line within the context of the program as a whole, rather than just mechanically

Feel free to alter the parameters to see how things change. That can be a great way to be able to intuit what is supposed to be happening

I will do the first few lines for you as an example


'''
import sys, logging, pygame	# imports the sys, logging, and pygame modules so they can be used in this program
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' # requires that the Python 3.4 (or higher version) interpreter is being used; i.e., not compatible with Python 2

logging.basicConfig(level=logging.CRITICAL)#sets the logger to only print out Critical messages
logger = logging.getLogger(__name__)#creates a logger

screen_size = (800,600)#makes a tupple called screen-size and sets it to 800,600
FPS = 60# makes an int called fps and sets it to 60
red = (255,0,0) #createss a tupple callexd red
black = (0,0,0) #creates a tupple called black

class Block(pygame.sprite.Sprite): #creates a class called block that inherites from the sprite class in pygame
	def __init__(self, position, direction): #creates the initialiser for the block class, takes two args
		pygame.sprite.Sprite.__init__(self) #initialises the sprite class in pygame
		self.image = pygame.Surface((50, 50))# sets image to equal pygame.surface((50,50))
		self.image.fill(red)#makess the image the color red
		self.rect = self.image.get_rect()#sets rect to equal the rect from image
		(self.rect.x,self.rect.y) = position #sets the pos of the rect to equal the given pos
		self.direction = direction #sets direction to equal the given direction

	def update(self):#creates a method called update
		(dx,dy) = self.direction #creates a tuple from the direction
		self.rect.x += dx#updates the rects x pos
		self.rect.y += dy#updates the rects y pos
		(WIDTH,HEIGHT) = screen_size#sets width and height to equal the screen size
		if self.rect.left > WIDTH:#checks to see if the rect left the screen on the right side
			self.rect.right = 0#sets the rect to show up on the left side of the screen
		if self.rect.right < 0:#checks to see if the square exited the left side of the screen
			self.rect.left = WIDTH#sets the rect to be on the right side of the screen
		if self.rect.top > HEIGHT:#check to see if the rect exited the bottom of the screeen
			self.rect.bottom = 0#sets the rect to be above the screen
		if self.rect.bottom < 0:#checks to see if the rect left the top of the screen
			self.rect.top = HEIGHT#sets the rect below the screen


def main():#creates a function called main
	pygame.init()#initialises pygame
	screen = pygame.display.set_mode(screen_size)#sets up the screen based off of screen_size
	clock = pygame.time.Clock()#creates a clock

	blocks = pygame.sprite.Group()#creates a sprite group called blocks
	block = Block((200,200),(-1,1))#creates a variable called block which is a Block
	blocks.add(block)#adds block to blocks

	while True:#creates an infinte loop
		clock.tick(FPS)#makes the program only go as fast as fps
		screen.fill(black)#fills the screen with the color black

		for event in pygame.event.get():#gets all the events that the player did
			if event.type == pygame.QUIT:#checks to see if an event of type quit happened
				pygame.quit()#quits out of pygame
				sys.exit(0)#exits the system

		blocks.update()#moves the blocks
		blocks.draw(screen)#draws all the blocks onto the screen
		pygame.display.flip()#displays all the images that have been placed on the screen

if __name__ == '__main__':#checks to see if the program is being run as the main program
	main()#calles th function main