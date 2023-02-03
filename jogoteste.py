import pygame
from pygame.locals import *
from random import randint

pygame.init()
pygame.mixer.init()

FPS = 60
clock = pygame.time.Clock()

#resolucao 3x4
#1024x768
window_width = 800
window_height = 600


camera_x = 0
camera_y = 0
gravity = 5
volume = 1

display = pygame.display.set_mode((window_width, window_height))
window = pygame.Surface((800, 600))
pygame.display.set_caption('Knight Awakens')


black = [0,0,0]
white = [255,255,255]
green = [0,255,0]
red = [255,0,0]

camera_x = 0
camera_y = 0

lifes = 4
damage_delay = 1000

#16x12
tm = 50

player_scale = 4
scale_fundo = 2

font = pygame.font.Font('fontes/VCR_OSD_MONO_1.001.ttf', 25)

#temporizador = fonte_t.render(tempo_tela, 1, preto)

#upload de imagens


skeleton = pygame.image.load('./skeleton/run/0.png').convert_alpha()
skeleton_image = pygame.transform.scale(skeleton, (skeleton.get_width()/player_scale, skeleton.get_height() / player_scale))
gosmenta = pygame.image.load('./gosmenta/run/0.png').convert_alpha()
gosmenta_image = pygame.transform.scale(gosmenta, (gosmenta.get_width()/ player_scale, gosmenta.get_height()/player_scale))
bullet_slime = pygame.image.load('./gota.png').convert_alpha()
bullet_slime = pygame.transform.scale(bullet_slime, (bullet_slime.get_width()/ 20, bullet_slime.get_height()/ 20))
eye_image = pygame.image.load('./eye.png').convert_alpha()
eye_image = pygame.transform.scale(eye_image, (eye_image.get_width()/ player_scale, eye_image.get_height()/player_scale))
menu = pygame.image.load('./projeto_menu.png').convert_alpha()
boss_image = pygame.image.load('./boss.png').convert_alpha()
game_over_image = pygame.image.load('./gam_over_game.png').convert_alpha()
pause_image = pygame.image.load('./pause.png').convert_alpha()
osso_imagem = pygame.image.load('./osso.png').convert_alpha()

espinhos_sound = pygame.mixer.Sound('sounds/espinhos.wav')
game_over_sound = pygame.mixer.Sound('sounds/game_over.wav')
menu_music = pygame.mixer.Sound('sounds/menu.wav')
click_sound = pygame.mixer.Sound('sounds/click.wav')
win_sound = pygame.mixer.Sound('sounds/win.wav')
cutscenes_sound = pygame.mixer.Sound('sounds/music.wav')
cutscenes_sound.set_volume(0.2)
misc_menu = pygame.mixer.Sound('sounds/misc_menu.wav')


opcoes_image = pygame.image.load('menus/menu_opcoes/opcoes_image.png')
creditos_image = pygame.image.load('menus/menu_creditos/creditos_image.png')
win_image = pygame.image.load('menus/win_menu.png')

on_menu = True
on_levels = False
on_creditos = False
on_opcoes = False
on_cutscenes = False
on_win = False
game_over = False
game = False
click = False
win = False
win_boss = False
last_check_point = [0,0]
score = 0

def winner():
    global win
    global win_boss
    global score
    if tile_map.level == 1:
        if player.x == 10000:
            win = True
    if tile_map.level == 2:
        if player.x == 8000:
            win = True
    if tile_map.level == 3:
        if player.x == 14000:
            win = True
    if tile_map.level == 4:
        if len(enemies) == 0:
            win_boss = True
    

def check_point():
  global last_check_point
  if tile_map.level == 1:
    if player.x >= 6000:
      last_check_point = [6000,100]
    elif player.x >= 2000:
      last_check_point = [2000,300]
    else:
      last_check_point = [500,200]
  elif tile_map.level == 3:
      last_check_point = [1000,200]

def main_menu():
        global click
        global on_menu
        global on_levels
        global on_opcoes
        global on_creditos
        global game_over
        game_over = False
        menu_music.stop()
        menu_music.play(-1)
        
        while True:
         menu_image = pygame.image.load('menus/menu_inicial/menu_image1.png').convert()
         
  
         mx, my = pygame.mouse.get_pos()

         if window_width == 1024:
          button_1 = pygame.Rect(424, 380, 200, 50)
         else:
          button_1 = pygame.Rect(330,300,146,40)
          button_2 = pygame.Rect(330,370,146,40)
          button_3 = pygame.Rect(330,440,146,40)
         if button_1.collidepoint((mx, my)):
            menu_image = pygame.image.load('menus/menu_inicial/menu_image2.png').convert()
            if click:
                on_menu = False
                on_levels = True
                click_sound.play()
                break

         if button_2.collidepoint((mx, my)):
            menu_image = pygame.image.load('menus/menu_inicial/menu_image3.png').convert()
            if click:
                on_menu = False
                on_opcoes = True
                click_sound.play()
                break

         if button_3.collidepoint((mx, my)):
            menu_image = pygame.image.load('menus/menu_inicial/menu_image4.png').convert()
            if click:
                on_menu = False
                on_creditos = True
                click_sound.play()
                break

         click = False
         for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
         window.blit(menu_image, (0,0))
         display.blit(pygame.transform.scale(window,(window_width,window_height)), (0,0))
         pygame.display.update()
         clock.tick(60)

def creditos_menu():
        global click
        global on_menu
        global on_creditos
        while True:
         window.blit(creditos_image, (0,0))
  
         mx, my = pygame.mouse.get_pos()


         button_1 = pygame.Rect(0, 0, 200, 150)
         if button_1.collidepoint((mx, my)):
            if click:
                on_menu = True
                on_creditos = False
                click_sound.play()
                break
 
 
         click = False
         for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

         display.blit(pygame.transform.scale(window,(window_width,window_height)), (0,0))
         pygame.display.update()
         clock.tick(60)

def opcoes_menu():
        global click
        global on_menu
        global on_opcoes
        global volume
        while True:
         window.blit(opcoes_image, (0,0))
  
         mx, my = pygame.mouse.get_pos()


         voltar = pygame.Rect(0, 0, 200, 150)
         volume_baixo = pygame.Rect(270, 220, 60, 45)
         volume_medio = pygame.Rect(380, 220, 60, 45)
         volume_alto = pygame.Rect(480, 220, 60, 45)
         if voltar.collidepoint((mx, my)):
            if click:
                on_menu = True
                on_opcoes = False
                click_sound.play()
                break
         if volume_baixo.collidepoint((mx, my)):
            if click:
              volume = 0.3
              click_sound.play()
         if volume_medio.collidepoint((mx, my)):
            if click:
              volume = 1.2
              click_sound.play()
         if volume_alto.collidepoint((mx, my)):
            if click:
              volume = 2
              click_sound.play()
 
         click = False
         for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
         game_over_sound.set_volume(volume)
         espinhos_sound.set_volume(volume)
         menu_music.set_volume(volume)
         click_sound.set_volume(0.5 + volume)
         display.blit(pygame.transform.scale(window,(window_width,window_height)), (0,0))
         pygame.display.update()
         clock.tick(60)

def levels_menu():
    global click
    global on_levels
    global game
    global game_over
    global on_menu
    global on_cutscenes
    levels_image = pygame.image.load('menus/menu_levels/levels_image1.png')


    mx, my = pygame.mouse.get_pos()
    voltar = pygame.Rect(0, 0, 200, 150)
    button_1 = pygame.Rect(70, 220, 200, 50)
    button_2 = pygame.Rect(70, 300, 200, 50)
    button_3 = pygame.Rect(70, 400, 200, 50)
  
    if button_1.collidepoint((mx, my)):
        levels_image = pygame.image.load('menus/menu_levels/levels_image2.png')
        if click:
            on_levels = False
            tile_map.level = 1
            on_cutscenes = True
            click_sound.play()
            menu_music.stop()        
    if button_2.collidepoint((mx, my)):
        levels_image = pygame.image.load('menus/menu_levels/levels_image4.png')
        if click:
            on_levels = False
            tile_map.level = 2
            game = True
            click_sound.play()
            menu_music.stop()
    if button_3.collidepoint((mx, my)):
        levels_image = pygame.image.load('menus/menu_levels/levels_image3.png')
        if click:
            on_levels = False
            tile_map.level = 3
            game = True
            click_sound.play()
            menu_music.stop()
    if voltar.collidepoint((mx,my)):
        if click:
            on_levels = False
            on_menu = True
            click_sound.play()
    
    click = False
    game_over = False

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
    window.blit(levels_image, (0,0))
    display.blit(pygame.transform.scale(window,(window_width,window_height)), (0,0))
    pygame.display.update()
    clock.tick(60)

def game_over_menu():
        global click
        global on_menu
        global game_over
        game_over_sound.play()
        while True:
  
          mx, my = pygame.mouse.get_pos()
 
          button_1 = pygame.Rect(335, 300, 100, 40)
          if button_1.collidepoint((mx, my)):
            if click:
                on_menu = True
                game_over = False
                click_sound.play()
                break
 
 
          click = False
          for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()


            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

          window.blit(game_over_image, (0,0))
          display.blit(pygame.transform.scale(window,(window_width,window_height)), (0,0))

          pygame.display.update()
          clock.tick(60)

def win_menu():
        global click
        global on_menu
        global win
        win_sound.play()
        while True:
  
          mx, my = pygame.mouse.get_pos()
 
          button_1 = pygame.Rect(335, 300, 100, 40)
          if button_1.collidepoint((mx, my)):
            if click:
                on_menu = True
                win = False
                click_sound.play()
                break
 
 
          click = False
          for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()


            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

          window.blit(win_image, (0,0))
          display.blit(pygame.transform.scale(window,(window_width,window_height)), (0,0))

          pygame.display.update()
          clock.tick(60)

def cutscenes_menu():
        global on_cutscenes
        global game
        i = 0
        passar = False
        voltar = False
        cutscenes_sound.play()
        while True:
          if passar:
            if i == 10:
              game = True
              on_cutscenes = False
              passar = False
              break
            else:
              i += 1
              click_sound.play()
              passar = False
          if voltar:
            if i != 0:
              i -= 1
              click_sound.play()
              voltar = False
          for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                if event.key == K_RIGHT:
                  passar = True
                if event.key == K_LEFT:
                  voltar = True
           
          image = pygame.image.load(f'cutscenes/{i}.png')
          window.blit(image, (0,0))

          display.blit(pygame.transform.scale(window,(window_width,window_height)), (0,0))

          pygame.display.update()
          clock.tick(60)
score = 0
#remover funcoes----------------------------------------------------------------------------------------------------------
def show_score(score, tamanho, color):
  fonte = pygame.font.SysFont('Arial', tamanho, False, False)
  msg = f'SCORE {score}'
  text = font.render(msg, True, color)
  return text

def show_lifes(lifes, tamanho, color):
  msg = f'x{lifes}'
  text = font.render(msg, True, color)
  return text

def show_timer(time, tamanho, color):
  msg = f'TIME {int(time)}'
  text = font.render(msg, True, color)
  return text



#verifica as colisoes                                  
def colliding(rect1, rect2):
  if not(rect1.x + rect1.width <= rect2.x or rect2.x + rect2.width <= rect1.x):
    if not(rect1.y + rect1.height <= rect2.y or rect2.y + rect2.height <= rect1.y):
      return True
  return False

def would_collide(rect1, current_map):
    for y in range(len(current_map)):
        for x in range(len(current_map[y])):
            if current_map[y][x] == '1' or current_map[y][x] == '2' or current_map[y][x] == '3':
                x = (x ) 
                map_rect = pygame.Rect(x * tm - camera_x, y * tm - camera_y, tm, tm)
                if colliding(rect1, map_rect):
                    return True
    return False

class Object:
  def __init__(self,x,y,image):
    self.x = x
    self.y = y
    self.image = image

class Tile_map:
   def __init__(self):
    self.tile_map = []
    self.level = 1
    self.grama = pygame.image.load('mapas/mapa1/com_grama.png').convert()
    self.sem_grama = pygame.image.load('mapas/mapa1/sem_grama.png').convert()
    self.corner_left = pygame.image.load('mapas/mapa1/ponta_esquerda.png').convert_alpha()
    self.corner_right = pygame.image.load('mapas/mapa1/ponta_direita.png').convert_alpha()
    self.agua = pygame.image.load('mapas/mapa1/agua.png').convert_alpha()
    self.sem_grama_direita = pygame.image.load('mapas/mapa1/sem_grama_direita.png').convert_alpha()
    self.sem_grama_esquerda = pygame.image.load('mapas/mapa1/sem_grama_esquerda.png').convert_alpha()
    self.background = pygame.image.load('mapas/mapa1/background.png').convert_alpha()

   def update_map(self):
      if self.level == 1:
        self.grama = pygame.image.load('mapas/mapa1/com_grama.png').convert()
        self.sem_grama = pygame.image.load('mapas/mapa1/sem_grama.png').convert()
        self.corner_left = pygame.image.load('mapas/mapa1/ponta_esquerda.png').convert_alpha()
        self.corner_right = pygame.image.load('mapas/mapa1/ponta_direita.png').convert_alpha()
        self.background = pygame.image.load('mapas/mapa1/background.png').convert_alpha()
        self.agua = pygame.image.load('mapas/mapa1/agua.png')
        self.tile_map = [
 '...........................................................................................................................................................................................................................',
 '........................................................................................311111111112.......................................................32..............................................................',
 '.........................................................................................................................................311112............................................................................',
 '...............................................312.................755555555555555556...................3111112....................3112..........3111112...............311111111112........................................',
 '...................................................................444444444444444444..............................311111111112..............................31112.........................................................',
 '.......................................311112......................444444444444444444.............................31111111111112...........................................................................................',
 '...............................................................3111111111111111111111111111111111111111111111111111111111111111111111111111111ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ111111111111111111111111111111111111111',
 '..............3111111112........................311.......311111111111111111111111111111111111111111111111111111111111111111111111111111111111ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ111111111111111111111111111111111111111',
 '112.......311111111111111111112......31111111111111.......111111111111111111111111111111111111111111111111111111111111111111111111111111111111ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ111111111111111111111111111111111111111',
 '1111111111111111111111111111111XXXXXX11111111111111XXXXXXX111111111111111111111111111111111111111111111111111111111111111111111111111111111111ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ111111111111111111111111111111111111111',
 '1111111111111111111111111111111XXXXXX11111111111111XXXXXXX11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111',
 '1111111111111111111111111111111XXXXXX11111111111111XXXXXXX11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111',
 '1111111111111111111111111111111XXXXXX11111111111111XXXXXXX11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111',
 '1111111111111111111111111111111XXXXXX11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111',
 '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111',
]   
      if self.level == 2:
        global camera_x
        camera_x = 0
        player.x = 40
        player.y = 100
        self.grama = pygame.image.load('mapas/mapa2/com_grama.png').convert()
        self.sem_grama = pygame.image.load('mapas/mapa2/sem_grama.png').convert()
        self.corner_left = pygame.image.load('mapas/mapa2/ponta_esquerda.png').convert_alpha()
        self.corner_right = pygame.image.load('mapas/mapa2/ponta_direita.png').convert_alpha()
        self.background = pygame.image.load('mapas/mapa2/background.png').convert_alpha()
        self.tile_map = [
 '.........................................................................................................',
 '.........................................................................................................',
 '.........................................................................................................',
 '..............................................311111111112..........312..................................',
 '.........................311111111112....................................................................',
 '.........................................................................................................',
 '...............................................................311111111111111111111111111111111111111111',
 '................................................311111111111111111111111111111111111111111111111111111111',
 '111111111....................................311111111111111111111111111111111111111111111111111111111111',
 '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111',
 '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111',
 '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111',
 '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111',
 '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
]   
      if self.level == 3:
        camera_x = 0
        player.x = 60
        player.y = 100
        self.grama = pygame.image.load('mapas/mapa3/com_grama.png').convert_alpha()
        self.sem_grama = pygame.image.load('mapas/mapa3/sem_grama.png').convert()
        self.corner_left = pygame.image.load('mapas/mapa3/ponta_esquerda.png').convert_alpha()
        self.corner_right = pygame.image.load('mapas/mapa3/ponta_direita.png').convert_alpha() 
        self.agua = pygame.image.load('mapas/mapa3/lava.png')
        self.background = pygame.image.load('mapas/mapa3/background.jpg').convert_alpha()
        self.tile_map = [
 '111111111111111...........................................................................................................................................................111111111111111111111',
 '111111111111111...........................................................................................................................................................111111111111111111111',
 '111111111111111...........................................................................................................................................................111111111111111111111',
 '111111111111111..............................................................311111111112.................................................................................111111111111111111111',
 '111111111111111.............................................31111111112...................................................................................................111111111111111111111',
 '111111111111111...........................................................................................................................................................111111111111111111111',
 '111111111111111......................................31112................................................................................................................111111111111111111111',
 '111111111111111...............31111112.......312..........................................................................................................................111111111111111111111',
 '111111111111111.........31112.............................................................................................................................................111111111111111111111',
 '111111111111111...................3111112.................................................................................................................................111111111111111111111',
 '111111111111111111111111111111111111111111111111112.......................................................................................................................111111111111111111111',
 '111111111111111111111111111111111111111111111111111XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX111111111111111111111',
 '111111111111111111111111111111111111111111111111111XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX111111111111111111111',
 '111111111111111111111111111111111111111111111111111XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX111111111111111111111',
 '111111111111111111111111111111111111111111111111111XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX111111111111111111111'
]    

      if self.level == 4:
        camera_x = 0
        player.x = 60
        player.y = 100
        self.tile_map = [
 '11111..........................................111111111111',
 '11111..........................................111111111111',
 '11111..........................................111111111111',
 '11111..........................................111111111111',
 '11111..........................................111111111111',
 '11111.....................31111112.............111111111111',
 '11111..........................................111111111111',
 '11111..........................................111111111111',
 '11111111111111111111111111111111111111111111111111111111111',
 '11111111111111111111111111111111111111111111111111111111111',
 '11111111111111111111111111111111111111111111111111111111111',
 '11111111111111111111111111111111111111111111111111111111111'
]    
class Bullet:
  def __init__(self,  image, x, y, direction, fired_art):
    self.image = image
    self.x = x
    self.y = y
    self.direction = direction
    self.fired_art = fired_art
    
  def move(self):
    if self.direction == 'left':
      self.x -= 7
    else:
      self.x += 7
  def move_y(self):
      self.y += 5

  def would_collide(self, x, current_map):
    rect = pygame.Rect(self.x, self.y, 10, 3)
    window.blit(bullet_slime, (self.x - camera_x  , (self.y + 10 - camera_y)))
    return would_collide(rect, current_map)
  
  def touched_player(self, player):
    player_rect = player.rect
    bullet_rect = pygame.Rect(self.x - camera_x, self.y + 10 - camera_y, 15, 15)
    return colliding(player_rect, bullet_rect)
  
class Character:
  def __init__(self, x, y, width, height, speed, image, looking, health):
    self.x = x 
    self.y = y
    self.width = width
    self.height = height
    self.speed = speed
    self.image = image
    self.looking = looking
    self.max_health = health
    self.health = health
    self.bullets = []
    self.attack_distance = 5
    self.attack_rect = pygame.Rect(self.x + self.attack_distance, self.x, self.width, self.height)

  def shoot(self, camera=False):
    x = self.x 
    if self.looking == 'right':
      x + self.width
    else:
      x - 5
    if camera:
      x += (camera_x)
    self.bullets.append(Bullet(self.image,x,self.y, self.looking, pygame.time.get_ticks()))

  #verifica a colisao do character com o mapa
  def would_collide(self ,x, y, current_map):
    character_rect = pygame.Rect(self.x + x - camera_x, self.y + y - camera_y, self.width, self.height)
    for y in range( len(current_map)):
     for x in range( len(current_map[y])):
      if current_map[y][x] == '1'or current_map[y][x] == '2' or current_map[y][x] == '3':
        rect = pygame.Rect((x * tm - camera_x), y * tm - camera_y, tm, tm)
        if colliding(character_rect, rect):
          return True
    return False

  #verifica a colisao do character com o mapa de fundo
  def would_collide_bg(self ,x, y, current_map):
    character_rect = pygame.Rect(self.x + x - camera_x, self.y + y - camera_y, self.width, self.height)
    for y in range( len(current_map)):
     for x in range( len(current_map[y])):
      if current_map[y][x] == '5' or current_map[y][x] == '6' or current_map[y][x] == '7':
        rect = pygame.Rect((x * tm - camera_x ), y * tm - camera_y, tm, 2)
        if colliding(character_rect, rect):
          return True
    return False
    

    
class Player(Character):
   def __init__(self, x,y, width, height,image, looking, health):
      super().__init__(x,y,width, height, 5, image, looking, health)
      self.jump = False
      self.on_air = False
      #tamanho maximo do pulo do player
      self.max_jumps = 35
      #guarda quanto falta para atingir o maximo
      self.jumps_left = self.max_jumps
      self.last_damage = 0
      self.attack = False
      self.last_attack = pygame.time.get_ticks()
      self.attack_sound = pygame.mixer.Sound('sounds/attack.wav')
      self.animation_list = ['static', 'run', 'jump']
      self.action = 0
      self.i = 0
      self.cont = 0
   #movimenta o player
   def movement(self, key):
      global attack_sound
      global camera_x

      if self.jump:
        if not(self.would_collide(0, -self.speed, tile_map.tile_map)) and self.jumps_left != 0:
          
          self.y -= gravity
          self.on_air = True
        else:
          self.jump = False
          self.on_air = True
          self.jumps_left = self.max_jumps
        self.jumps_left -= 1


      if not(self.would_collide(0, self.speed, tile_map.tile_map)) and not (self.jump) and not (self.would_collide_bg(0, self.speed, tile_map.tile_map)):
        self.on_air = True
        self.y += gravity
      else: 
        self.on_air = False
        
      if key[pygame.K_LEFT] and not(self.would_collide(-self.speed, 0, tile_map.tile_map)):
       self.image = pygame.image.load('./player/0.png').convert_alpha()
       if tile_map.level != 4:
         if player.x >= 500:
           self.x -= self.speed
           self.looking = 'left'
       else:
           self.x -= self.speed
           self.looking = 'left'
      if key[pygame.K_RIGHT] and not(self.would_collide(self.speed, 0, tile_map.tile_map)):
        self.x += self.speed
        self.looking = 'right'
        self.image = pygame.image.load('./player/1.png').convert_alpha()

  
      if key[pygame.K_SPACE] and not(self.jump) and not(self.on_air):
        self.jump = True

      if key[pygame.K_DOWN] and player.last_attack +1000 <= pygame.time.get_ticks():
       self.attack_sound.play()
       self.attack = True 
       self.last_attack = pygame.time.get_ticks()
      else:
        self.attack = False

   def on_air_dead(self, current_map):
    for y in range( len(current_map)):
     for x in range( len(current_map[y])):
      if current_map[y][x] == 'X' or  current_map[y][x] == 'Z':
        rect = pygame.Rect((x * tm - camera_x), y * tm - camera_y, tm, tm)
        if pygame.Rect.colliderect(self.rect, rect):
          return True
    return False

   def update_rect(self):
      self.rect = pygame.Rect(self.x - (camera_x), self.y - camera_y, self.width, self.height)


      if self.looking == 'left':
        self.attack_distance = 20
        self.attack_rect = pygame.Rect(self.x - self.attack_distance - camera_x, self.y - camera_y, 30, self.height)

      else:
        self.attack_distance = self.width
        self.attack_rect = pygame.Rect(self.x + self.attack_distance - camera_x, self.y - camera_y, 30, self.height)
       

class Enemy(Character):
  def __init__(self,  x, y, width, height, speed, image, looking , r, health, type):
    super().__init__( x, y, width, height, 2, image, looking, health)
    self.initial_x = x
    self.initial_y = y
    self.range = r
    self.alive = True
    self.type = type
    self.interval = 50
    self.count = 0
    self.last_attack = pygame.time.get_ticks()
    self.cont = 0
    self.i = 0
    
  def movement_skeleton(self, player):
   if self.alive:
    if player.x >= (self.initial_x - self.range) and player.x <= (self.initial_x + self.range * 2)  and self.y + tm >= player.y + 10:
      enemy_x = self.x 
      if enemy_x <= player.x:
        if self.looking != 'right':
          self.looking = 'right'
          self.image = pygame.transform.flip(self.image, True, False)
      else:
        if self.looking != 'left':
          self.looking = 'left'
          self.image = pygame.transform.flip(self.image, True, False)
      if len(self.bullets) == 0 or self.last_bullet.fired_art + 1200 < pygame.time.get_ticks():
        self.shoot(osso_imagem)

    else:
      if self.looking == 'right':
        self.x += self.speed
        if self.x + self.speed > self.initial_x + self.range:
          self.image = pygame.transform.flip(self.image, True, False)
          self.looking = 'left'
      else:
        self.x -= self.speed
        if self.x - self.speed < self.initial_x:
          self.image = pygame.transform.flip(self.image, True, False)
          self.looking = 'right'

  def movement_gosmenta(self):
    self.cont +=1
    self.image = pygame.image.load(f'gosmenta/run/{self.i}.png')
    if self.looking == 'right':
      self.image = pygame.transform.flip(self.image, True, False)
    if self.i == 11:
      self.i = 0
    if self.cont >= 10:
      self.cont = 0
      self.i += 1
    if self.looking == 'right':
      self.x += self.speed
      if self.x + self.speed > self.initial_x + self.range:
        self.looking = 'left'
  
    else:
      self.x -= self.speed
      if self.x - self.speed < self.initial_x:

        self.looking = 'right'
    
  def movement_eyes(self):
    self.x -= 5
    self.count += 1
    if self.count >= self.interval:
      self.bullets.append(Bullet(self.image,self.x,self.y, self.looking, pygame.time.get_ticks()))
      self.count = 0
    if self.looking == 'donw':

      self.y += 2
      if self.y + 2 > self.initial_y + self.range:
        self.looking = 'up'
    else:

      self.y -= 2
      if self.y - 2 < self.initial_y:
        self.looking = 'donw'

  def movement_boss(self):
    if player.x >= (self.initial_x - self.range) and player.x <= (self.initial_x + self.range * 2)  and self.y + tm >= player.y + 10:
      enemy_x = self.x 
      if enemy_x <= player.x:
        if self.looking != 'right':
          self.looking = 'right'
          self.image = pygame.transform.flip(self.image, True, False)
      else:
        if self.looking != 'left':
          self.looking = 'left'
          self.image = pygame.transform.flip(self.image, True, False)


    
    if self.looking == 'right':
        self.x += self.speed
        if self.x + self.speed > self.initial_x + self.range:
          self.image = pygame.transform.flip(self.image, True, False)
          self.looking = 'left'
    else:
        self.attack_distance = -5
        self.attack_rect = pygame.Rect(self.x + self.attack_distance, self.x, self.width, self.height)

        self.x -= self.speed
        if self.x - self.speed < self.initial_x:
          self.image = pygame.transform.flip(self.image, True, False)
          self.looking = 'right'
     



  def touched_player(self, player):
       return pygame.Rect.colliderect(self.rect, player.rect)

  def update_rect(self):
      self.rect = pygame.Rect(self.x - (camera_x), self.y - camera_y, self.width, self.height)

      if self.looking == 'left':
        self.attack_distance = 20
        self.attack_rect = pygame.Rect(self.x - self.attack_distance - camera_x, self.y - camera_y, 10, self.height)

      else:
        self.attack_distance = 10 + self.width
        self.attack_rect = pygame.Rect(self.x + self.attack_distance - camera_x, self.y - camera_y, 10, self.height)

  def gravidade(self):
      global gravity
      if not(self.would_collide(0, self.speed, tile_map.tile_map)):
        self.y += gravity

class Espinho():
  def __init__(self, x, y, delay):
    self.x = x
    self.y = y
    self.delay = delay
    self.images = [pygame.image.load('mapas/mapa3/espinhos1.png'),pygame.image.load('mapas/mapa3/espinhos2.png')]
    self.ativo = False
    self.rect = pygame.Rect(self.x - camera_x ,self.y - camera_y, 50, 10)

  def controlar_espinhos(self):
      if self.ativo:
        self.image = self.images[0]
        if self.delay + randint(600,1000) <= pygame.time.get_ticks():
          self.ativo = False
          self.delay = pygame.time.get_ticks()
      else:
        self.image = self.images[1]
        if self.delay + randint(800,1200) <= pygame.time.get_ticks():
          self.ativo = True
          self.delay = pygame.time.get_ticks()
      window.blit(self.image, (self.x- camera_x, self.y - camera_y))
      self.rect = pygame.Rect(self.x - camera_x ,self.y + 45 - camera_y, 50, 10)
      #pygame.draw.rect(window, red, self.rect)

  def dano_dos_espinhos(self):
      global lifes
      if self.ativo:
        if pygame.Rect.colliderect(self.rect, player.rect):
          if player.last_damage + damage_delay <= pygame.time.get_ticks():
            player.last_damage = pygame.time.get_ticks()
            lifes -= 1
            espinhos_sound.play()



def draw_window(current_map, player, enemies):
  #desenha o mapa
  for y in range(len(current_map)):
    for x in range(len(current_map[y])):
      if current_map[y][x] == '1':
        #verifica e desenha a terra e a grama
        if y != 0 and current_map[y-1][x] != '1' and current_map[y-1][x] != '2' and current_map[y-1][x] != '3':
          window.blit(tile_map.grama, (x * tm - camera_x , y * tm - camera_y))
        else:
          window.blit(tile_map.sem_grama, (x  * tm - camera_x, y * tm - camera_y))

      if current_map[y][x] == '2':
        window.blit(tile_map.corner_right, (x * tm - camera_x , y * tm - camera_y))
      
      if current_map[y][x] == '3':
        window.blit(tile_map.corner_left, (x * tm - camera_x , y * tm - camera_y))
      
      if current_map[y][x] == '4':
        window.blit(tile_map.sem_grama, (x  * tm - camera_x , y * tm - camera_y))

      if current_map[y][x] == '5':
        window.blit(tile_map.grama, (x * tm - camera_x , y * tm - camera_y))

      if current_map[y][x] == '6':
        window.blit(tile_map.corner_right, (x * tm - camera_x , y * tm - camera_y))
      
      if current_map[y][x] == '7':
        window.blit(tile_map.corner_left, (x * tm - camera_x , y * tm - camera_y))
      
      if current_map[y][x] == '8':
        window.blit(tile_map.sem_grama_esquerda, (x * tm - camera_x , y * tm - camera_y))

      if current_map[y][x] == '9':
        window.blit(tile_map.sem_grama_direita, (x * tm - camera_x , y * tm - camera_y))

      if current_map[y][x] == 'X':
        window.blit(tile_map.agua, (x * tm - camera_x , y * tm - camera_y))

  for enemy in enemies:
    for bullet in enemy.bullets:
      rect = pygame.Rect(bullet.x - camera_x, (bullet.y + 50 - camera_y),15,15)
      
      if would_collide(rect, tile_map.tile_map):
        enemy.bullets.remove(bullet)
      #pygame.draw.rect(window,red,rect)

    
  window.blit(player.image,((player.x - 30 - camera_x), (player.y - 40- camera_y)))
  #pygame.draw.rect(window,green,player.rect)

def draw_lifes():
  global lifes

  image_life = pygame.image.load('./lifes/sprite_0.png').convert_alpha()
  if lifes == 4 :
    image_life = pygame.image.load('./lifes/sprite_0.png').convert_alpha()
  if lifes == 3 :
    image_life = pygame.image.load('./lifes/sprite_1.png').convert_alpha()
  if lifes == 2 :
    image_life = pygame.image.load('./lifes/sprite_2.png').convert_alpha()
  if lifes == 1 :
    image_life = pygame.image.load('./lifes/sprite_3.png').convert_alpha()
  if lifes == 0 :
    image_life = pygame.image.load('./lifes/sprite_4.png').convert_alpha()
  
  image_life = pygame.transform.scale(image_life, (image_life.get_width() / 2, image_life.get_height() / 2))
    
  window.blit(image_life,(40,40)) 

image = pygame.image.load('./player/0.png').convert_alpha()
image = pygame.transform.flip(image, True, False)
player = Player(800,50,60,90, image,'left',25)
enemies = []

end_game = False 
exit = False

tile_map = Tile_map()
time = 250


game_over = False

def main_game():
   global tile_map
   global time
   global enemies
   global player
   global espinhos
   global end_game
   global camera_x
   global camera_y
   global lifes
   global score
   global game_over
   global win
   enemies = []
   espinhos = []
   pause = False
   score = 0
   objects = []
   if tile_map.level == 1:
    time = 300
    music = pygame.mixer.music.load('sounds/Gyro-Field001.wav')

    enemies.append(Enemy(5200,50,40,70,3, skeleton_image, 'left', 100,10,'skeleton'))
    enemies.append(Enemy(1170,350,40,30,3, gosmenta_image, 'left', 280,30,'gosmenta'))
    enemies.append(Enemy(3630,180,40,30,3, gosmenta_image, 'left', 250,30,'gosmenta'))
    enemies.append(Enemy(10000,-200,70,70,3, eye_image, 'left', 150,20,'eyes'))
    enemies.append(Enemy(6905,300,40,30,3, gosmenta_image, 'left', 250,20,'gosmenta'))

   if tile_map.level == 2:
    time = 100
    music = pygame.mixer.music.load('sounds/Gyro-Dungeon001.wav')

    enemies.append(Enemy(100,200,40,30,3, gosmenta_image, 'left', 200,20,'gosmenta'))
    enemies.append(Enemy(3000,0,40,70,3, skeleton_image, 'left',200,10,'skeleton'))
    enemies.append(Enemy(1430,100,40,30,3, gosmenta_image, 'left', 250,30,'gosmenta'))
    enemies.append(Enemy(20000,20,70,70,3, eye_image, 'left', 100,20,'eyes'))
    enemies.append(Enemy(2000,300,40,30,3, gosmenta_image, 'left', 250,20,'gosmenta'))
    objects.append(Object(600,300, pygame.image.load('mapas/mapa2/arvore.png')))
    objects.append(Object(2700,200, pygame.image.load('mapas/mapa2/arvore.png')))

   if tile_map.level == 3:
    time = 100
    music = pygame.mixer.music.load('sounds/Gyro-Battle001.wav')
    
    espinhos.append(Espinho(1200,350,pygame.time.get_ticks()))
    espinhos.append(Espinho(1250,350,pygame.time.get_ticks()))
    espinhos.append(Espinho(1300,350,pygame.time.get_ticks()))
    espinhos.append(Espinho(1700,300,pygame.time.get_ticks()))
    espinhos.append(Espinho(2700,250,pygame.time.get_ticks()))
   if tile_map.level == 4:
    time = 100
    music = pygame.mixer.Sound('sounds/Gyro-Battle004.wav')
    enemies.append(Enemy(300,350,70,70,3, boss_image, 'left', 500,20,'boss'))
   lifes = 4
   tile_map.update_map()
   player.x = 800
   player.y = 200
   last_sumon = pygame.time.get_ticks()
   pygame.mixer.music.set_volume(volume)
   pygame.mixer.music.play(-1)


   while True:
    if not game_over and not pause:
     time -= 0.06

     camera_x += (player.x - camera_x - 440)/15
     camera_y += (player.y - camera_y - 300)/15

     clock.tick(FPS)
     print(f'{player.x}, {player.y}')
     check_point()
     key = pygame.key.get_pressed()
     #desenha o fundo
     window.blit(tile_map.background, (0,0))

     #chama a movimentaçao do player
     player.movement(key)
     player.last_damage += 10
     player.update_rect()

     if player.on_air_dead(tile_map.tile_map):
      player.x = last_check_point[0]
      player.y = last_check_point[1]
      lifes -= 1      

     #verifica as teclas
     for event in pygame.event.get():
      if event.type == pygame.QUIT:
           pygame.quit()
           exit = True
           end_game = True
      if event.type == pygame.KEYDOWN:
        if event.key == K_t:
         if pause != True:
            pause = True
            pygame.mixer.music.pause()
  
     for enemy in enemies:
      if enemy.alive:
        enemy.update_rect()
        if enemy.health <= 0:
          score += randint(3,10)
          enemy.alive = False
          enemies.remove(enemy)
        if enemy.type == 'skeleton':
          enemy.gravidade()
          enemy.movement_skeleton(player)
          window.blit(enemy.image, ((enemy.x - camera_x - 20, enemy.y - camera_y - 30)))
          if enemy.touched_player(player) and player.attack == True:
            enemy.health -= 5
            player.attack = False
            print(enemy.health)
            
        if enemy.type == 'gosmenta':
          enemy.gravidade()
          enemy.movement_gosmenta()
          if enemy.touched_player(player) and player.on_air:
            enemy.health -= 30
            print(enemy.health)
            player.jump = True
          else:
            if enemy.touched_player(player) and player.y >= enemy.y and player.last_damage >= damage_delay:
             if lifes != 0:
              lifes -= 1
              player.last_damage = 0
            
          if pygame.Rect.colliderect(enemy.rect, player.attack_rect) and player.attack == True:
            enemy.health -= 5
            print(enemy.health)
            player.attack = False

          window.blit(enemy.image, ((enemy.x - camera_x - 50, enemy.y - camera_y - 100)))

        if enemy.type == 'eyes':
          enemy.movement_eyes()
          window.blit(enemy.image, ((enemy.x - camera_x, enemy.y - camera_y )))
        if enemy.type == 'boss':
          if enemy.speed <= 3:
            enemy.speed += 0.1
          enemy.movement_boss()
          window.blit(enemy.image, ((enemy.x - camera_x , enemy.y - camera_y)))
          if pygame.Rect.colliderect(enemy.rect, player.attack_rect) and player.attack == True:
            enemy.health -= 10
            print(enemy.health)
            player.attack = False
          if last_sumon + 8000 <= pygame.time.get_ticks():
            enemies.append(Enemy(randint(60, 700),350,70,70,3, gosmenta_image, 'left', 200,20,'gosmenta'))
            last_sumon = pygame.time.get_ticks()
          if enemy.last_attack + 3000 <=  pygame.time.get_ticks():
           if pygame.Rect.colliderect( enemy.attack_rect, player.rect):
            enemy.speed = 1
            enemy.last_attack = pygame.time.get_ticks()
            lifes -= 1

      for bullet in enemy.bullets:
        if len(enemy.bullets) >= 3:
          enemy.bullets.remove(bullet)
        enemy.last_bullet = bullet

        if enemy.type == 'eyes':
          bullet.move_y()
        else:
          bullet.move()

        if bullet.would_collide(10, tile_map.tile_map):
          enemy.bullets.remove(bullet)
        if bullet.touched_player(player) and player.last_damage + damage_delay <= pygame.time.get_ticks():
          enemy.bullets.remove(bullet)
          if lifes != 0:
            lifes -= 1
          print(lifes)
          player.last_damage = pygame.time.get_ticks()
     for espinho in espinhos:
      espinho.controlar_espinhos()
      espinho.dano_dos_espinhos()
     for objeto in objects:
      window.blit(objeto.image, (objeto.x - camera_x,objeto.y - camera_y))
     winner()
     draw_window(tile_map.tile_map, player, enemies)
     draw_lifes()
     if tile_map.level == 3:
       text_score = show_score(score, 30, white)
       show_lifes2 = show_lifes(lifes,30, white)
       if time >= 50:
        show_timer2 = show_timer(time,30, white)
       else:
        show_timer2 = show_timer(time,30, red)
     else:
       text_score = show_score(score, 30, black)
       show_lifes2 = show_lifes(lifes,30,black)
       if time >= 50:
        show_timer2 = show_timer(time,30, black)
       else:
        show_timer2 = show_timer(time,30, red)
     window.blit(show_lifes2, (100,50))
     window.blit(text_score,(630,50))
     window.blit(show_timer2, (350, 50))


    if lifes <= 0 or time <=0:
      tile_map.level = 1
      tile_map.update_map()
      pygame.mixer.music.stop()
      game_over = True
      game = False
      
      break
    if pause:
        window.blit(pause_image,(0,0))
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
           end_game = True
         if event.type == pygame.KEYDOWN:
          if event.key == K_t:
           if pause == True:
             pause = False
             pygame.mixer.music.unpause()

    if win:
      pygame.mixer.music.stop()
      game = False
      break
    display.blit(pygame.transform.scale(window,(window_width,window_height)), (0,0))
    pygame.display.update()

while not exit:
  if on_menu:
   main_menu()
  elif on_levels:
    levels_menu()
  elif game_over:
    game_over_menu()
  elif on_creditos:
    creditos_menu()
  elif on_opcoes:
    opcoes_menu()
  elif on_cutscenes:
    cutscenes_menu()
  elif win:
    win_menu()
  elif game:
    main_game()
  
