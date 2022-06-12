import os


class Boss():
  def __init_(self):
    self.nazwa="Donogo"
        self.pkt_zycia=200
        self.pkt_ataku_ogniem=40
        
   def atak_bossa(self,Gracz:Player):
    self.pkt_zycia_gracza-=Gracz
      
   def pociski_bossa():
    if self.status_pocisku==True:
      window.fill((255, 255, 255))
      pygame.draw.circle(win,(255, 81, 51),
                   [300, 300], 25, 0)
      pygame.display.update()
    else:
      pass
  
class Potwory():
  def __init__(self, pozycja_x: int, pozycja_y: int):
    self.wykrycie=150
    self.spawnowane_potwory = 0
    self.kierunek = random.randint(1, 2)
    self.walk_count = 0
    
  def miejsce_sprawnu_potwora(self):
    self.lista_potworow=[] 
    self.pozycja_x=random.randint(0,40)
    self.pozycja_y=random.randint(0,50)
    
  def umrzyj(self):
    global lista_potworow
    if self.pkt_zycia == 0:
      lista_potworow.remove(self)
    
  def liczba_potworow(self): 
    while self.spawnowane_potwory<=wylosowana_liczba_potworow:
      self.rodzaj=random.randint(1,2)
      if self.rodzaj==1:
        self.lista_potworow.append("Odolda") 
        self.self.spawnowane_potwory+=1
      else:
        self.lista_potworow.append("Czarny łuk")
        self.self.spawnowane_potwory+=1
        
  def atak_potworow(self):
    for potwor in self.lista_potworow:
      self.pkt_zycia_gracza-=self.pkt_ataku_mieczem  
      print("Gracz otrzymał obrażenia.")
    while self.liczba_strzal>0:
      if status_pocisku==True:
        pygame.draw.rect(win, (255, 195, 11),[100, 50, 100, 30], 0)
        pygame.display.update()
      else:
        pass
      self.pkt_zycia_gracza-=self.pkt_ataku_lukiem
      self.liczba_strzal-=1
      print("Gracz otrzymał obrażenia.")
      time.sleep()
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
    self.op_rect = pygame.Rect(self.x, self.y, self.width, self.height)
      
class Odolda(Potwory): #miecz
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
    
class Black_Bow_Guard(Potwory): #łuk
  def __init__(self,pozycja_x: int, pozycja_y: int):
    self.nazwa="Czarny łuk"
    self.pkt_zycia=50
    self.atak=15
    self.szybkosc=1
    self.odleglosc_od_gracza=0 
    self.promien_ataku=300
    self.liczba_strzal=random.randint(1,3)
    self.x = pozycja_x
    self.y = pozycja_y
    self.kierunek = random.randint(1, 2)
    self.walk_count = 0
    self.op_rect = pygame.Rect(self.x, self.y, self.width, self.height)
    self.immune = False
    self.timer = 0
    
class Projectile: # pocisk szuka drogi do gracza
    pass

def oponent_spawn():
  global lista_potworow 
  for i in range(1, 3):
    pozycja_x = random.randint(i*320, i*640-(32))
    pozycja_y = random.randint(i*180, i*360-(32))
    typ = random.choice([1, 2])
    if typ == 1:
      lista_potworow.append(Odolda(pozycja_x, pozycja_y))
    else:
      lista_potworow.append(Black_Bow_Guard(pozycja_x, pozycja_y))
  for j in range(1, 3):
    if j == 1:
      pozycja_x = random.randint(0, 640)
      pozycja_y = random.randint(360, 720-32)
    else:
      pozycja_x = random.randint(640, 1280-32)
      pozycja_y = random.randint(0, 360)
      typ = random.choice([1, 2])
      if typ == 1:
        lista_potworow.append(Odolda(pozycja_x, pozycja_y))
      else:
        lista_potworow.append(Black_Bow_Guard(pozycja_x, pozycja_y))
  return True
