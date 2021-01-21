import pygame, random
pygame.init()

class pongGame:
    run = False
    
    paddleX = 380
    paddleY = 120

    borderX = 10
    topBorderY = 10
    bottomBorderY = 280

    ballX = 200
    ballY = 150
    ballRadius = 10
    vx = 10
    vy = 10

    def __init__(self, display, white):
        self.display = display
        self.white = white

    def player(self):
        pygame.draw.rect(self.display, self.white, [self.paddleX, self.paddleY, 10, 50])

    def ball(self):
        pygame.draw.circle(self.display, self.white, (self.ballX, self.ballY), self.ballRadius)
    
    def border(self):
        pygame.draw.rect(self.display, self.white, [self.borderX, self.topBorderY, 365, 10])
        pygame.draw.rect(self.display, self.white, [self.borderX, self.bottomBorderY, 365, 10])
        pygame.draw.rect(self.display, self.white, [self.borderX, self.topBorderY, 10, 280])
    
    def ballMovement(self):

        self.ballY = self.ballY - self.vy
        
        if self.ballY == 20:
             self.vy = -10

        elif self.ballY == 270:
            self.vy = 10

        self.ballX = self.ballX - self.vx

        if self.ballX == 20:
             self.vx = -10

        elif self.ballX == 380:
            if self.ballY < (self.paddleY + 50) and self.ballY > (self.paddleY - 50):
                self.vx = 10


    def movement(self):
        move = pygame.key.get_pressed()

        if self.paddleY < 10:
            self.paddleY = 10
        
        elif move[pygame.K_UP]:
            self.paddleY = self.paddleY - 10
        
        elif self.paddleY > 240:
            self.paddleY = 240

        elif move[pygame.K_DOWN]:
            self.paddleY = self.paddleY + 10
    