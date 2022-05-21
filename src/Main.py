from Snake import snakeGame
from Pong import pongGame
import pygame
import random
pygame.init()


def main():
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    white = (255, 255, 255)

    size = (400, 300)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Retro Games')

    font = pygame.font.SysFont(None, 20)

    gameMenu = True

    pong = pongGame(screen, white)
    snake = snakeGame(screen, green, white, red)

    while gameMenu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameMenu = False

        game = pygame.key.get_pressed()

        if game[pygame.K_1]:
            snake.run = True
            while snake.run:

                pygame.time.delay(50)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        snake.run = False

                snake.movement()

                if (snake.appleX == snake.snakeX and
                        snake.appleY == snake.snakeY):

                    snake.appleX = round(random.randrange(0, 400 - 10)/10)*10
                    snake.appleY = round(random.randrange(0, 300 - 10)/10)*10
                    snake.score += 1
                    snake.lengthOfSnake += 1

                snakeHead = []
                snakeHead.append(snake.snakeX)
                snakeHead.append(snake.snakeY)
                snake.snakeList.append(snakeHead)

                if len(snake.snakeList) > snake.lengthOfSnake:
                    del snake.snakeList[0]

                for i in snake.snakeList[:-1]:
                    if i == snakeHead:
                        snake.run = False

                screen.fill(black)

                snake.snakeHead()
                snake.totalScore()
                snake.apple()

                pygame.display.update()

        elif game[pygame.K_2]:
            pong.run = True
            while pong.run:

                pygame.time.delay(40)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pong.run = False

                pong.movement()

                if pong.ballX == 410:
                    pong.run = False

                screen.fill(black)

                pong.ball()
                pong.ballMovement()
                pong.player()
                pong.border()

                pygame.display.update()

        screen.fill(black)

        value1 = font.render("Press 1 for Snake", True, white)
        screen.blit(value1, [10, 10])
        value2 = font.render("Press 2 for Pong ", True, white)
        screen.blit(value2, [10, 30])

        snake.snakeX = 200
        snake.snakeY = 150
        snake.score = 0
        snake.moveX = 0
        snake.moveY = 0
        snake.snakeList = []
        snake.lengthOfSnake = 1

        pong.ballX = 200
        pong.ballY = 150
        pong.paddleX = 380
        pong.paddleY = 120
        pong.vx = 10
        pong.vy = 10

        pygame.display.update()

    pygame.quit


main()
