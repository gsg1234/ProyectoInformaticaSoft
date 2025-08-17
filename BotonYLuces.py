import pygame
import sys
import threading

class PanelLuces:
    def __init__(self, width=400, height=300):
        # Inicializar Pygame
        pygame.init()
        self.WIDTH, self.HEIGHT = width, height
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Botón y Luces Indicadoras")

        # Colores
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (180, 180, 180)
        self.GRAY2 = (100,100,100)
        self.GREEN = (0, 200, 0)
        self.RED = (200, 0, 0)
        self.YELLOW = (200, 200, 0)
        self.DARK = (50, 50, 50)

        # Luces
        self.light_positions = {
            "roja": (100, 200),
            "amarilla": (200, 200),
            "verde": (300, 200)
        }
        self.lights = {"roja": False, "amarilla": False, "verde": False}

        # Botón
        self.button_rect = pygame.Rect(150, 50, 100, 40)
        self.button_pressed = False

        # Control del bucle
        self.running = True

        # Lock para sincronización con otros hilos
        self.lock = threading.Lock()

    # ==============================
    # FUNCIONES DE CONTROL DE LUCES
    # ==============================
    def apagar_luces(self):
        with self.lock:
            for key in self.lights:
                self.lights[key] = False

    def encender_luz(self, color, estado=True):
        with self.lock:
            if color in self.lights:
                self.lights[color] = estado

    # ==============================
    # FUNCIONES DE DIBUJO
    # ==============================
    def dibujar_luces(self):
        with self.lock:
            for nombre, pos in self.light_positions.items():
                color = (
                    self.RED if nombre == "roja" and self.lights[nombre] else
                    self.YELLOW if nombre == "amarilla" and self.lights[nombre] else
                    self.GREEN if nombre == "verde" and self.lights[nombre] else self.DARK
                )
                pygame.draw.circle(self.screen, color, pos, 30)

    def dibujar_boton(self):
        if self.button_pressed:
            pygame.draw.rect(self.screen, self.GRAY2, self.button_rect)
        else:
            pygame.draw.rect(self.screen, self.GRAY, self.button_rect)
        font = pygame.font.SysFont(None, 24)
        text = font.render("BOTÓN", True, self.BLACK)
        self.screen.blit(text, (self.button_rect.x + 20, self.button_rect.y + 10))

    # ==============================
    # LOOP PRINCIPAL
    # ==============================
    def run(self):
        clock = pygame.time.Clock()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect.collidepoint(event.pos):
                        self.button_pressed = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.button_pressed = False

            # Dibujar
            self.screen.fill(self.BLACK)
            self.dibujar_boton()
            self.dibujar_luces()
            pygame.display.flip()
            clock.tick(30)