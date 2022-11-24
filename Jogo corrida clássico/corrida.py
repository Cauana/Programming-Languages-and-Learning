import pygame
from pygame.locals import *
import random


#Configurações tela
altura = 800
largura = 800

road_largura = int(largura/1.6)
marca_road_larg = int(largura/80)
lado_direito = largura/2 + road_largura/4
lado_esquerdo = largura/2 - road_largura/4
speed = 4

pygame.init()
running = True

screen = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo de corrida clássico')

screen.fill((60,220,0))
pygame.display.update()

#Carros
carro_vermelho = pygame.image.load("Jogo corrida clássico\car1.png")
carro_vermelho = pygame.transform.scale(carro_vermelho, (250, 250))
carro_vermelho_loc = carro_vermelho.get_rect()
carro_vermelho_loc.center = lado_direito, altura*0.8

carro_amarelo = pygame.image.load("Jogo corrida clássico\car2.png")
carro_amarelo_loc = carro_vermelho.get_rect()
carro_amarelo_loc.center = lado_esquerdo , altura*0.2
carro_amarelo = pygame.transform.scale(carro_amarelo, (250, 250))

counter = 0
while running:
   
    counter += 1
    if counter == 100:
        speed += 0.5
        counter = 0
        print("Level up", speed)
        
    carro_amarelo_loc[1] += speed
    if carro_amarelo_loc[1] > altura:
        if random.randint(0,1) == 0:
            carro_amarelo_loc.center = lado_direito,-200
        else:
            carro_amarelo_loc.center = lado_esquerdo,-200
    #End game
    if carro_vermelho_loc[0] == carro_amarelo_loc[0] and carro_amarelo_loc[1] > carro_vermelho_loc[1]-250:
           print('END GAME')
           break     
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                carro_vermelho_loc = carro_vermelho_loc.move([-int(road_largura/2),0])
            if event.key == K_d or event.key == K_RIGHT:
                carro_vermelho_loc = carro_vermelho_loc.move([int(road_largura/2),0])
     #Graphics
    #Road
    pygame.draw.rect(screen,(50,50,50),(largura/2-road_largura/2, 0,road_largura,altura))
    #Marca Road
    pygame.draw.rect(screen,(255,240,60), (largura/2-marca_road_larg/2,0,marca_road_larg,altura))
    #Marca das ruas
    pygame.draw.rect(screen,(255,255,255), (largura/2-road_largura/2 + marca_road_larg*2,0,marca_road_larg,altura))
    #Outro lado da rua
    pygame.draw.rect(screen,(255,255,255), (largura/2+road_largura/2 - marca_road_larg*3,0,marca_road_larg,altura))

    screen.blit(carro_vermelho,carro_vermelho_loc)
    screen.blit(carro_amarelo,carro_amarelo_loc)
    pygame.display.update()


pygame.quit()