import pygame
import sys
import time

# Inicializar pygame
pygame.init()

# Configuración de ventana
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Botón y Luces Indicadoras")

# Colores
WHITE   = (255, 255, 255)
BLACK   = (0, 0, 0)
GRAY    = (180, 180, 180)
GRAY2   = (100,100,100)
GREEN   = (0, 200, 0)
RED     = (200, 0, 0)
YELLOW  = (200, 200, 0)
DARK    = (50, 50, 50)  # para luces apagadas

# Posiciones de luces
light_positions = {
    "roja": (100, 200),
    "amarilla": (200, 200),
    "verde": (300, 200)
}

# Estados de luces
lights = {
    "roja": False,
    "amarilla": False,
    "verde": False
}

# Botón
button_rect = pygame.Rect(150, 50, 100, 40)
button_pressed = False

# Control del parpadeo
last_toggle_time = time.time()

# ==============================
# FUNCIONES
# ==============================

def toggle_lights():
    """Alterna el estado de todas las luces"""
    for key in lights:
        lights[key] = not lights[key]

def apagar_luces():
    """Apaga todas las luces"""
    for key in lights:
        lights[key] = False

def dibujar_luces():
    """Dibuja las luces según su estado"""
    for nombre, pos in light_positions.items():
        color = (
            RED if nombre == "roja" and lights[nombre] else
            YELLOW if nombre == "amarilla" and lights[nombre] else
            GREEN if nombre == "verde" and lights[nombre] else DARK
        )
        pygame.draw.circle(screen, color, pos, 30)

def dibujar_boton():
    """Dibuja el botón"""
    if button_pressed:
        pygame.draw.rect(screen, GRAY2, button_rect)
    else:
        pygame.draw.rect(screen, GRAY, button_rect)
    font = pygame.font.SysFont(None, 24)
    text = font.render("BOTÓN", True, BLACK)
    screen.blit(text, (button_rect.x + 20, button_rect.y + 10))

# ==============================

# Bucle principal
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                button_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            button_pressed = False
            apagar_luces()

    # Si el botón está presionado -> hacer titilar
    ###############################################################
    ###############################################################
    #Llenar con codigo
    button_was_pressed=False
    if button_pressed:
        if not button_was_pressed:
            button_was_pressed=True
    
    if not button_pressed:
        if  button_was_pressed:
            button_was_pressed=False




    
    ###############################################################
    ###############################################################
    # Fondo
    screen.fill(BLACK)

    # Dibujar elementos
    dibujar_boton()
    dibujar_luces()

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(30)
