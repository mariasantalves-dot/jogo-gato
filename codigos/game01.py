import pygame

# Inicializando o Pygame
pygame.init()

# definindo o tamanho da janela
LARGURA, ALTURA = 720, 720
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("nome da janela")

# loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.quit:
            rodando = False

    # atualizar a tela 
    pygame.display.flip()

 # finalizar o pygame
pygame.quit()
