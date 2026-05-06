import pygame
import os

pygane.init()

# Caninho das Imagens

BASE = os.path.dirname(os.path.abspath(_file_))
IMG = os.path.join(os.path.dirname(BASE), "imagens")

def carregar_imagen(nome, largura, altura):
    caminhos.path.join(ING, name)
    imagem = pygame.image.load(caminho).convert_alpha()
    return pygame.transfore.scale(imagem, (largura, altura))

#Tela
LARGURA = 720
ALTURA = 720
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Game 07 - pulo")

rel = pygame.time.Clock()

Imagens
personagen = carregar_imagem("personagem.png", 85, 85)
obstaculo = carregar_imagem("obstaculo1.png", 80, 80)
objetivo = carregar_imagem("objetivo.png", 75, 75)

#Chao
chao = 700

#Personagen
x = 80
y = chao - 85
vel = 5

#Pulo
pulando = False
velocidade_pulo = 0
forca_pulo = -20
gravidade = 0.9

#Objetos
obstaculo_x = 390
obstaculo_y = chao - 80

objetivo_x = 620
objetivo_y = chao - 75

rodando = True
while rodando:
     for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
             rodando = False

    teclas = pygame.key.get_pressed()

    if teclas [pygane.K_RIGHT]:
        x += vel

    if teclas[pygame.K_LEFT]:
        x -= vel

    if teclas [pygame.K SPACE] and not pulando:
        pulando = True
        velocidade_pulo = forca_pulo

    if pulando:
        y += velocidade_pulo
        velocidade_pulo += gravidade

        if y >= chao - 85:
            y = chao - 85
            pulando = False

    tela.fill((135, 206, 235))

    tela.blit(personagen, (x, y))
    tela.blit(obstaculo, (obstaculo_x, obstaculo_y))
    tela.blit(objetivo, (objetivo_x, objetivo_y))

    pygame.display.flip()