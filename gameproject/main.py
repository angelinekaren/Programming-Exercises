import pygame
import sys
import os
import random


pygame.font.init()
pygame.init()

display_width = 750
display_height = 750
window_size = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Space Invasion")
icon = pygame.image.load(os.path.join("assets", "main_ship.png"))
pygame.display.set_icon(icon)

# Load Images

# Background
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'background-black.png')), (display_width, display_height))

# Ships
RED_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'red_ship.png')), (100, 100))
YELLOW_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'yellow_ship.png')), (100, 100))
GREEN_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'green_ship.png')), (100, 100))
SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'main_ship.png')), (100, 100))

# Lasers
RED_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_red.png'))
YELLOW_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_yellow.png'))
GREEN_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_green.png'))
MAIN_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_blue.png'))

class Ship:
    COOLDOWN = 30

    def __init__(self, x, y , health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_image = None
        self.laser_image = None
        self.lasers = []
        self.cool_down_count = 0

    def draw(self, window):
        window.blit(self.ship_image, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def ship_width(self):
        return self.ship_image.get_width()

    def ship_height(self):
        return self.ship_image.get_height()

    def shoot(self):
        if self.cool_down_count == 0:
            laser = Laser(self.x, self.y, self.laser_image)
            self.lasers.append(laser)
            self.cool_down_count = 1

    def cool_down(self):
        if self.cool_down_count >=  self.COOLDOWN:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1

    def move_lasers(self, velocity, object):
        self.cool_down()
        for laser in self.lasers:
            laser.move(velocity)
            if laser.off_screen(display_height):
                self.lasers.remove(laser)
            elif laser.collision(object):
                object.health -= 10
                self.lasers.remove(laser)

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_image = SPACE_SHIP
        self.laser_image = MAIN_LASER
        self.mask = pygame.mask.from_surface(self.ship_image)
        self.max_health = health

    def move_lasers(self, vel, objects):
        self.cool_down()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(display_height):
                self.lasers.remove(laser)
            else:
                for object in objects:
                    if laser.collision(object):
                        objects.remove(object)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.health_bar(window)

    def health_bar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.ship_image.get_height() + 10, self.ship_image.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_image.get_height() + 10, self.ship_image.get_width() * (self.health / self.max_health), 10))

class EnemyShip(Ship):
    COLOR_SHIP_MAP = {
        "red": (RED_SPACE_SHIP, RED_LASER),
        "green": (GREEN_SPACE_SHIP, GREEN_LASER),
        "yellow": (YELLOW_SPACE_SHIP, YELLOW_LASER),
    }
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_image, self.laser_image = self.COLOR_SHIP_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_image)

    def move(self, vel):
        self.y += vel


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel # move downwards

    def off_screen(self, height):
        return not(self.y >= 0 and self.y <= height)

    def collision(self, obj):
        return collide(obj, self)

def collide(ship1, ship2):
    offset_x = ship2.x - ship1.x
    offset_y = ship2.y - ship1.y
    return ship1.mask.overlap(ship2.mask, (offset_x, offset_y)) != None

def run():
    FPS = 60
    loop = True
    level = 0
    lives = 5
    main_font = pygame.font.SysFont('comicsans', 50)
    game_over_font = pygame.font.SysFont('comicsans', 60)

    enemies = []
    num_enemies = 5
    enemy_vel = 1

    laser_velocity = 5

    game_over = False
    game_over_count = 0

    clock = pygame.time.Clock()

    player = Player(300, 630)

    def redraw_window():
        window_size.blit(BACKGROUND, (0, 0))
        # drawing text into surfaces and put it on screen
        level_label = main_font.render(f'Level: {level}', 1, (255, 255, 255))
        lives_label = main_font.render(f'Lives: {lives}', 1, (255, 255, 255))
        window_size.blit(level_label, (20, 20))
        window_size.blit(lives_label, (600, 20))

        for enemy in enemies:
            enemy.draw(window_size)

        player.draw(window_size)

        if game_over:
            game_over_label = game_over_font.render('Game Over', 1, (255, 255, 255))
            window_size.blit(game_over_label, (display_width/2 - game_over_label.get_width()/2, 350))

        pygame.display.update()

    while loop:
        clock.tick(FPS)
        redraw_window()
        if lives <= 0 or player.health <= 0:
            game_over = True
            game_over_count += 1

        if game_over:
            if game_over_count > FPS*2:
                loop = False
            else:
                continue


        if len(enemies) == 0:
            level += 1
            num_enemies += 5
            for i in range(num_enemies):
                enemy = EnemyShip(random.randrange(50, display_width-100), random.randrange(-1500, -100), random.choice(['red', 'green', 'yellow']))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # returns a dictionary and tells whether they are pressed
        # at the current time
        increment_value = 5
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - increment_value > 0:
            player.x -= increment_value
        if keys[pygame.K_RIGHT] and player.x + increment_value + player.ship_width() < display_width:
            player.x += increment_value
        if keys[pygame.K_UP] and player.y - increment_value > 0:
            player.y -= increment_value
        if keys[pygame.K_DOWN] and player.y + increment_value + player.ship_height() + 20 < display_height:
            player.y += increment_value
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_velocity, player)
            if random.randrange(0, 3*60) == 1:
                enemy.shoot()
            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.ship_height() > display_height:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_velocity, enemies)

def main_menu():
    title_font = pygame.font.SysFont("comicsans", 70)
    loop = True
    while loop:
        window_size.blit(BACKGROUND, (0,0))
        title_label = title_font.render("Press mouse to begin...", 1, (255,255,255))
        title_label2 = title_font.render('Use arrow to move', 1, (255, 255, 255))
        window_size.blit(title_label, (display_width/2 - title_label.get_width()/2, 350))
        window_size.blit(title_label2, (display_width/2 - title_label2.get_width()/2, 400))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run()
    pygame.quit()
    sys.exit()

main_menu()









