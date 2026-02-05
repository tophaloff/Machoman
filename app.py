import pygame
import sys

# --- Initialisation ---
pygame.init()

# --- Paramètres du jeu ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Couleurs
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
RED = (255, 50, 50)
GREEN = (50, 200, 50)

# Physique
GRAVITY = 0.8
PLAYER_SPEED = 5
JUMP_STRENGTH = -16

# --- Configuration de la fenêtre ---
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mon Mini Jeu Mario")
clock = pygame.time.Clock()

# --- Classes ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(RED) # Bonhomme rouge pour l'instant
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = SCREEN_HEIGHT - 150
        self.vel_y = 0
        self.is_jumping = False

    def update(self):
        # Mouvements horizontaux
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

        # Gravité
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        # Collision bas de l'écran (sol temporaire)
        if self.rect.bottom >= SCREEN_HEIGHT - 50:
            self.rect.bottom = SCREEN_HEIGHT - 50
            self.vel_y = 0
            self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.vel_y = JUMP_STRENGTH
            self.is_jumping = True

# --- Instances ---
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# --- Boucle principale du jeu ---
running = True
while running:
    # 1. Gestion des événements (clavier, souris)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # Saut avec Espace
                player.jump()

    # 2. Mise à jour des objets
    all_sprites.update()

    # 3. Dessin
    screen.fill(BLUE) # Fond ciel
    
    # Dessiner le sol
    pygame.draw.rect(screen, GREEN, (0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50))
    
    all_sprites.draw(screen)

    # 4. Rafraîchissement de l'écran
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
