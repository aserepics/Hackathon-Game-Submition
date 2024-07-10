import pygame, sys
#The smooth movemment was a thing that I learned from youtube
#  I did not come up with this concept of the movement myself.
#I Also learned the basic structure of a pygame program from youtube.
#Things like the event handler, screen, e.t.c.
pygame.init()

pygame.display.set_caption("Hackathon Game By Ashar Abed Islam Muahmmed Naser")

gameh = 650
gamew = 900
running = True
backgroundi = pygame.image.load("spaceback.png")
unwanted_background = (0,0,0)

gamescreen = pygame.display.set_mode((gamew, gameh))

spritesheet_image = pygame.image.load('spritesheet.png').convert_alpha()

def take_image(sheet, frame, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0,0),((frame*width),0, width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey(color)
    return image
frame_0 = take_image(spritesheet_image, 0, 24, 24, 6.5, unwanted_background)
frame_1 = take_image(spritesheet_image, 1, 24, 24, 6.5, unwanted_background)
frame_2 = take_image(spritesheet_image, 2, 24, 24, 6.5, unwanted_background)
frame_3 = take_image(spritesheet_image, 3, 24, 24, 6.5, unwanted_background)
frame_4 = take_image(spritesheet_image, 4, 24, 24, 6.5, unwanted_background)

class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.player = pygame.Rect(self.x, self.y, 50, 50)
        self.color = (250, 0, 0)
        self.velX = 0
        self.velY = 0
        self.a_pressed = False
        self.d_pressed = False
        self.w_pressed = False
        self.s_pressed = False
        self.speed = 0.5

    def draw(self, gamescreen):
        pygame.draw.rect(gamescreen, self.color, self.player)
     
    def update(self):
        self.velX = 0
        self.velY = 0
        if self.a_pressed and not self.d_pressed and not (self.x<0):
            self.velX = -self.speed
        if self.d_pressed and not self.a_pressed and not (self.x>868):
            self.velX = self.speed
        if self.w_pressed and not self.s_pressed and not (self.y<0):
            self.velY = -self.speed
        if self.s_pressed and not self.w_pressed and not (self.y>618):
            self.velY = self.speed
        
        self.x += self.velX
        self.y += self.velY

        self.player = pygame.Rect(int(self.x), int(self.y), 32, 32)

player = Player(gamew/2, gameh/2)

pygame.display.update()

while running:

    gamescreen.blit(backgroundi, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.a_pressed = True
            if event.key == pygame.K_d:
                player.d_pressed = True
            if event.key == pygame.K_w:
                player.w_pressed = True
            if event.key == pygame.K_s:
                player.s_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.a_pressed = False
            if event.key == pygame.K_d:
                player.d_pressed = False
            if event.key == pygame.K_w:
                player.w_pressed = False
            if event.key == pygame.K_s:
                player.s_pressed = False


    player.draw(gamescreen)
    player.update()
    pygame.display.flip()

        

