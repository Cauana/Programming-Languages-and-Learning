import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

music_moeda = pygame.mixer.Sound('Snake\smw_coin.wav')
music_moeda.set_volume(0.9)
music_gameover = pygame.mixer.Sound('Snake\smw_lost_a_life.wav')
music_gameover.set_volume(0.9)
largura = 640
altura = 480
x_cobra = int(largura/2)
y_cobra = int(altura/2)
velocidade = 15
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo Snake')
relogio = pygame.time.Clock()
morreu = False


def aumenta_cobra(lista_cobra):
    for xey in lista_cobra:
        pygame.draw.rect(tela,(0,255,0), (xey[0], xey[1], 20, 20))
    
def reiniciar_jogo():
    global pontos, comp_inicial, x_cobra, y_cobra, lista_cabeca, lista_cobra,y_maca,x_maca,morreu
    pontos = 0
    comp_inicial = 3
    x_cobra = int(largura/2)
    y_cobra = int(altura/2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40,600)
    y_maca = randint(50,430)
    morreu = False
    


pontos = 0
fonte = pygame.font.SysFont('arial',40,True,True)
lista_cobra = []
comp_inicial = 3
x_maca = randint(40,600)
y_maca = randint(50,430)
x_controle = 20
y_controle = 0


while True:
    relogio.tick(20)
    tela.fill((0,0,0))
    
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem,True,(255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()   
        if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle= -velocidade 
                    y_controle = 0  
                
            if event.key == K_d or event.key == K_RIGHT:
                if x_controle == -velocidade: 
                    pass
                else:
                        x_controle = velocidade 
                        y_controle = 0    
            if event.key == K_w or event.key == K_UP:
                if y_controle == velocidade:
                    pass
                else:  
                    x_controle= 0 
                    y_controle =-velocidade 
            if event.key == K_s or event.key == K_DOWN:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle= 0
                    y_controle = velocidade        
    x_cobra += x_controle
    y_cobra += y_controle
    
    cobra = pygame.draw.rect(tela,(0,255,0), (x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela,(255,0,0), (x_maca,y_maca,20,20))
    
    if cobra.colliderect(maca):
        x_maca = randint(40,600)
        y_maca = randint(50,430)
        pontos +=1
        music_moeda.play()
        comp_inicial +=1
    
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)
    
    if lista_cobra.count(lista_cabeca)>1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem,True,(255,255,255))
        ret_texto = texto_formatado.get_rect()
        morreu = True
        if morreu == True:
            music_gameover.play()  
        while morreu:
            tela.fill((0,0,0))
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            ret_texto.center = (largura//2,altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()
     
    if x_cobra> largura:
        x_cobra = 0
    elif x_cobra <0:
        x_cobra = largura
    elif y_cobra<0:
        y_cobra = altura
    elif y_cobra>largura:
        y_cobra = 0     
        
    if len(lista_cobra)>comp_inicial:
        del lista_cobra[0]
    
    aumenta_cobra(lista_cobra)
    
    
    tela.blit(texto_formatado,(30,30))
    pygame.display.update()
