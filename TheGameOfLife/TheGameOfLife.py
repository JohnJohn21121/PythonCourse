import pygame
import numpy as np
import time

pygame.init()

width, height = 1000, 1000
screen = pygame.display.set_mode((height, width))

bg = 25, 25, 25
screen.fill(bg)

nxC, nyC = 75, 75

dimCW = width / nxC
dimCH = height / nyC

#Cell Status . Alive = 1; Dead = 0;
gameState = np.zeros((nxC, nyC))

pauseEx = False

gameState[5,3] = 1
gameState[5,4] = 1
gameState[5,5] = 1

while True:

    newGameState = np.copy(gameState)
    screen.fill(bg)
    time.sleep(0.1)

    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.KEYUP:
            pauseEx = not pauseEx

        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick)>0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int (np.floor(posY / dimCH))
            newGameState[celX,celY] = 1

    for y in range(0, nxC):
        for x in range(0, nyC):
            if not pauseEx:
                n_neigh = gameState[(x-1) % nxC, (y - 1) % nyC] + \
                          gameState[(x) % nxC, (y - 1 ) % nyC] + \
                          gameState[(x+1) % nxC, (y - 1) % nyC] + \
                          gameState[(x-1) % nxC, (y) % nyC] + \
                          gameState[(x+1) % nxC, (y) % nyC] + \
                          gameState[(x-1) % nxC, (y + 1) % nyC] + \
                          gameState[(x) % nxC, (y+1) % nyC] + \
                          gameState[(x+1) % nxC, (y + 1) % nyC]

            #Rule 1 : if a cell is dead with 3 alive neighbour cells, it gets back to life.
                if gameState[x,y] == 0 and n_neigh == 3:
                    newGameState[x,y] = 1

            #Rule 2: if a living cell is with less than 2 alive neighbours or more than 3, it Dies.
                elif gameState[x, y] == 1 and (n_neigh<2 or n_neigh>3):
                    newGameState[x, y] = 0

            poly = [((x) *  dimCW, y * dimCH),
               ((x+1) * dimCW, y * dimCH),
               ((x+1) * dimCW, (y+1) * dimCH),
               ((x) *   dimCW, (y+1) *dimCH)]

            if newGameState[x,y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    gameState = np.copy(newGameState)

    pygame.display.flip()
    pass



