import pygame, random
pygame.init()

class snakeGame:
    run = False

    size = 10
    snakeSpeed = 10

    font = pygame.font.SysFont(None, 20)
    score = 0

    snakeX = 200
    snakeY = 150

    moveX = 0
    moveY = 0

    appleX = round(random.randrange(0, 400 - 10)/10)*10
    appleY = round(random.randrange(0, 300 - 10)/10)*10

    snakeList = []
    lengthOfSnake = 1

    def __init__(self, display, green, white, red):
        self.display = display
        self.green = green
        self.white = white
        self.red = red
    
    def snakeHead(self):
        for i in self.snakeList:
            pygame.draw.rect(self.display, self.green, [i[0], i[1], self.size, self.size])

    def totalScore (self):
        value = self.font.render("Your score: " + str(self.score), True, self.white)
        self.display.blit(value, [0, 0])

    def apple(self):
        pygame.draw.rect(self.display, self.red, [self.appleX, self.appleY, self.size, self.size])

    def movement(self):
        move = pygame.key.get_pressed()

        if self.snakeX < 0:
            self.run = False
       
        elif move[pygame.K_LEFT]:
            self.moveX = -self.snakeSpeed
            self.moveY = 0

        elif self.snakeX > 400:
            self.run = False
        
        elif move[pygame.K_RIGHT]:
            self.moveX = self.snakeSpeed
            self.moveY = 0

        elif self.snakeY < 0:
            self.run = False
        
        elif move[pygame.K_UP]:
            self.moveY = -self.snakeSpeed
            self.moveX = 0

        elif self.snakeY > 300:
            self.run = False

        elif move[pygame.K_DOWN]:
            self.moveY = self.snakeSpeed
            self.moveX = 0

        self.snakeX += self.moveX
        self.snakeY += self.moveY
