class Potwory():
  def __init__(self):
    self.kierunek = random.randint(1, 2)
    self.walk_count = 0
    
  def umrzyj(self):
    global lista_potworow
    if self.pkt_zycia == 0:
      lista_potworow.remove(self)
      
  def movement(self):
    if self.kierunek == 1:
      self.x += self.szybkosc
      self.walk_count += 1
      if self.walk_count == 31:
        self.szybkosc = self.szybkosc*(-1)
        self.walk_count = 0
    if self.kierunek == 2:
      self.y += self.szybkosc
      self.walk_count += 1
      if self.walk_count == 31:
        self.szybkosc = self.szybkosc*(-1)
        self.walk_count = 0

class Boss(Potwory):
  def __init__(self):
    self.nazwa="Donogo"
        self.pkt_zycia=200
        self.pkt_ataku_ogniem=40
        self.szybkosc = 2
        self.x = 1000
        self.y = 383
        self.width, self.height = 72, 72
        self.op_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.wykrycie = 100000000
        self.shot_count = 1
        self.immune = False
        self.timer = 0
        self.odbicia = 0
        
  def attack_movement(self):
    odleglosc_x = (self.x - gracz.x_position)
    odleglosc_y = (self.y - gracz.y_position)
    self.odleglosc = (odleglosc_x**2 + odleglosc_y**2)**(1/2)
     if self.odleglosc <= self.wykrycie and self.szybkosc < 0:
        self.szybkosc = self.szybkosc*(-1)
     if self.odleglosc <= self.wykrycie and self.odleglosc >= 100:
      if self.shot_count == 0:
        self.shoot()
      self.shot_count += 1
            if self.shot_count == 62:
                self.shot_count = 0
     elif self.odleglosc < 100:
      if odleglosc_x > 0:
        self.x += self.szybkosc
        self.op_rect.x += self.szybkosc
      elif odleglosc_x < 0:
        self.x -= self.szybkosc
        self.op_rect.x -= self.szybkosc
      if odleglosc_y > 0:
        self.y += self.szybkosc
        self.op_rect.y += self.szybkosc
      elif odleglosc_y < 0:
        self.y -= self.szybkosc
        self.op_rect.y -= self.szybkosc
        
  def shoot(self):
    global lista_pociskow
    lista_pociskow.append(Projectile(self.x+32, self.y+32, 25, 32, 32))
   
class Odolda(Potwory):
  def __init__(self,pozycja_x: int, pozycja_y: int):
    self.nazwa="Odolda"
    self.pkt_zycia=100
    self.atak=20
    self.szybkosc=2
    self.height, self.width = 32, 32
    self.odleglosc_od_gracza=0 
    self.promien_ataku=50
    self.x = pozycja_x
    self.y = pozycja_y
    self.kierunek = random.randint(1, 2)
    self.walk_count = 0
    self.op_rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    self.immune = False
    self.timer = 0
    self.odbicia = 0
    self.odleglosc = 10000000
    
  def attack_movement(self):
    odleglosc_x = (self.x - gracz.x_position)
    odleglosc_y = (self.y - gracz.y_position)
    self.odleglosc = (odleglosc_x**2 + odleglosc_y**2)**(1/2)
    if self.odleglosc <= self.wykrycie:
      if self.szybkosc < 0:
        self.szybkosc = self.szybkosc*(-1)
      if odleglosc_x > 0:
        self.x -= self.szybkosc
        self.op_rect.x -= self.szybkosc
      elif odleglosc_x < 0:
        self.x += self.szybkosc
        self.op_rect.x += self.szybkosc
      if odleglosc_y > 0:
        self.y -= self.szybkosc
        self.op_rect.y -= self.szybkosc
      elif odleglosc_y < 0:
        self.y += self.szybkosc
        self.op_rect.y += self.szybkosc 
    
class Black_Bow_Guard(Potwory): 
  def __init__(self,pozycja_x: int, pozycja_y: int):
    self.nazwa="Czarny łuk"
    self.pkt_zycia=50
    self.atak=15
    self.szybkosc=1
    self.wykrycie=400 
    self.height, self.width = 32, 32
    self.odleglosc_od_gracza=0
    self.x = pozycja_x
    self.y = pozycja_y
    self.kierunek = random.randint(1, 2)
    self.walk_count = 0
    self.op_rect = pygame.Rect(self.x, self.y, self.width, self.height)
    self.immune = False
    self.timer = 0
    self.odbicia = 0
    self.odleglosc = 10000000
    self.shot_count = 1
    
  def attack_movement(self):
    odleglosc_x = (self.x - gracz.x_position)
    odleglosc_y = (self.y - gracz.y_position)
    self.odleglosc = (odleglosc_x**2 + odleglosc_y**2)**(1/2)
    if self.odleglosc <= self.wykrycie and self.szybkosc < 0:
        self.szybkosc = self.szybkosc*(-1)
    if self.odleglosc <= self.wykrycie and self.odleglosc >= 100:
      if self.shot_count == 0:
        self.shoot()
        self.shot_count += 1
        if self.shot_count == 62:
          self.shot_count = 0
    elif self.odleglosc < 100:
      if odleglosc_x > 0:
        self.x += self.szybkosc
        self.op_rect.x += self.szybkosc
      elif odleglosc_x < 0:
        self.x -= self.szybkosc
        self.op_rect.x -= self.szybkosc
      if odleglosc_y > 0:
        self.y += self.szybkosc
        self.op_rect.y += self.szybkosc
      elif odleglosc_y < 0:
        self.y -= self.szybkosc
        self.op_rect.y -= self.szybkosc
  
  def shoot(self):
    global lista_pociskow
    lista_pociskow.append(Projectile(self.x+16, self.y+16, 10, 16, 16))
    
class Projectile:
  def __init__(self, x: int, y: int, damage: int, length: int, height: int):
        self.x = x
        self.y = y
        self.damage = damage
        self.length = length
        self.height = height
        self.x_speed = 5
        self.y_speed = 4
        self.los = random.choice([1, 2, 3, 4])

  def projectile_movement(self):
    if self.los == 1:
      self.x += self.x_speed
      self.rect.x += self.x_speed
    if self.los == 2:
      self.x -= self.x_speed
      self.rect.x -= self.x_speed
    if self.los == 3:
      self.y += self.y_speed
      self.rect.y += self.y_speed
    if self.los == 4:
      self.y -= self.y_speed
      self.rect.y -= self.y_speed
   
def oponent_spawn():
  global lista_potworow 
  for i in range(1, 3):
    pozycja_x, pozycja_y = 0, 0
    check_rect = pygame.Rect(pozycja_x, pozycja_y, 32, 32)
    for k in range(len(walls)):
      for m in range(k+1):
        while check_rect.colliderect(walls[m]):
          pozycja_x = random.randint(i*320, i*640-96)
          pozycja_y = random.randint(i*180, i*360-96)
    typ = random.choice([1, 2])
    if typ == 1:
      lista_potworow.append(Odolda(pozycja_x, pozycja_y))
    else:
      lista_potworow.append(Black_Bow_Guard(pozycja_x, pozycja_y))
  for j in range(1, 3):
    pozycja_x, pozycja_y = 0, 0
    check_rect = pygame.Rect(pozycja_x, pozycja_y, 32, 32)
    for k in range(len(walls)):
      for m in range(k+1):
        while check_rect.colliderect(walls[m]):
          if j == 1:
            pozycja_x = random.randint(0, 640)
            pozycja_y = random.randint(360, 720-96)
            check_rect = pygame.Rect(pozycja_x, pozycja_y, 32, 32)
          else:
            pozycja_x = random.randint(640, 1280-96)
            pozycja_y = random.randint(0, 360)
            check_rect = pygame.Rect(pozycja_x, pozycja_y, 32, 32)
            typ = random.choice([1, 2])
    if typ == 1:
      lista_potworow.append(Odolda(pozycja_x, pozycja_y))
    else:
      lista_potworow.append(Black_Bow_Guard(pozycja_x, pozycja_y))
  return True

def spawn_boss():
  global lista_potworow
  boss = Boss()
  lista_potworow.append(boss)
  
def oponent_walka():
  global gracz_im_timer, map
  for oponent in lista_potworow:
    if gracz.rectangle.colliderect(oponent.op_rect) and not gracz.immune:
      gracz.health_points -= oponent.atak
      gracz.death()
      gracz.immune = True
    if gracz.immune:
      gracz_im_timer += 1
      if gracz_im_timer == len(lista_potworow)*62:
        gracz_im_timer = 0
        gracz.immune = False
    if (oponent.op_rect.colliderect(gracz.sword_rect) and not oponent.immune and gracz.sword_exists):
      oponent.pkt_zycia -= gracz.attack_points
      oponent.umrzyj()
      oponent.immune = True
    if oponent.immune:
      oponent.timer += 1
      if oponent.timer == 31:
        oponent.timer = 0
        oponent.immune = False
    if oponent.op_rect.colliderect(wybuch.expl_rect) and wybuch.exists:
      oponent.pkt_zycia = 0
      oponent.umrzyj()
  
def ruchy_niezalezne():
  global bomb_count, expl_count
  if bomba.isSet:
    bomb_count += 1
    bomba.explode()
  if wybuch.exists:
    expl_count += 1
    wybuch.vaporize()
  for oponent in lista_potworow:
    odleglosc_x = (oponent.x - gracz.x_position)
    odleglosc_y = (oponent.y - gracz.y_position)
    oponent.odleglosc = (odleglosc_x**2 + odleglosc_y**2)**(1/2)
    if oponent.odleglosc > oponent.wykrycie:
      oponent.movement()
    elif oponent.odleglosc <= oponent.wykrycie:
      oponent.attack_movement()
  for projectile in lista_pociskow:
    projectile.projectile_movement()
    
def oponent_wall_collision(oponent: Potwory):
  for wall in walls:
    if oponent.op_rect.colliderect(wall):
      if oponent.odleglosc > oponent.wykrycie:
        if oponent.kierunek == 1:
          if oponent.szybkosc > 0:
            oponent.op_rect.x -= oponent.szybkosc
            oponent.x -= oponent.szybkosc
          else:
            oponent.op_rect.x += oponent.szybkosc
            oponent.x += oponent.szybkosc
        else:
          if oponent.szybkosc > 0:
            oponent.op_rect.y -= oponent.szybkosc
            oponent.y -= oponent.szybkosc
          else:
            oponent.op_rect.y += oponent.szybkosc
            oponent.y += oponent.szybkosc
      else:
        if oponent.op_rect.x > wall.x:
          oponent.op_rect.x += oponent.szybkosc
          oponent.x += oponent.szybkosc
        if oponent.op_rect.x < wall.x:
          oponent.op_rect.x -= oponent.szybkosc
          oponent.x -= oponent.szybkosc
        if oponent.op_rect.y > wall.y:
          oponent.op_rect.y += oponent.szybkosc
          oponent.y += oponent.szybkosc
        if oponent.op_rect.y < wall.y:
          oponent.op_rect.y -= oponent.szybkosc
          oponent.y -= oponent.szybkosc    
  
lista_potworow = []
oponent_spawn()

lista_pociskow = []
