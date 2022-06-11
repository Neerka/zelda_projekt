class Boss():
  def __init_(self):
    self.nazwa="Donogo"
        self.pkt_zycia=200
        self.pkt_ataku_ogniem=40
   def atak_bossa(self,Gracz):
        self.pkt_zycia_gracza-=Gracz
  
class Potwory():
  def __init__(self):
    self.promien_zauwazenia_gracza=120
    self.wylosowana_liczba_potworow=random.randint(1,4)
    self.spawnowane_potwory=0
    
  def miejsce_sprawnu_potwora(self):
    self.lista_potworow=[] #potwory będą się spawnić tylko raz na daną mapę
    self.pozycja_x=random.randint(0,40)
    self.pozycja_y=random.randint(0,50)
    
  def liczba_potworow(self): 
    while self.spawnowane_potwory<=wylosowana_liczba_potworow:
      self.rodzaj=random.randint(1,2)
      if self.rodzaj==1:
        self.lista_potworow.append("Odolda") 
        self.self.spawnowane_potwory+=1
      else:
        self.lista_potworow.append("Czarny łuk")
        self.self.spawnowane_potwory+=1
        
  def atak_potworow(self): #czyli jak będzie kolizja gracza z Odoldą = atak
    for potwor in self.lista_potworow:
      self.pkt_zycia_gracza-=self.pkt_ataku_mieczem  #wprowadzić namierzanie pozycji gracza
      print("Gracz otrzymał obrażenia.")
    while self.liczba_strzal>0:
      self.pkt_zycia_gracza-=self.pkt_ataku_lukiem
      self.liczba_strzal-=1
      print("Gracz otrzymał obrażenia.")
      
class Odolda(Potwory): #miecz
  def __init__(self):
    self.nazwa="Odolda"
    self.pkt_zycia=100
    self.pkt_ataku_mieczem=20
    self.szybkosc=6
    self.odleglosc_od_gracza=0 #wprowadzić namierzanie pozycji gracza
    self.promien_ataku=50
    
class Black_Bow_Guard(Potwory): #łuk
  def __init__(self):
    self.nazwa="Czarny łuk"
    self.pkt_zycia=50
    self.pkt_ataku_lukiem=15
    self.szybkosc=2
    self.odleglosc_od_gracza=0 #wprowadzić namierzanie pozycji gracza
    self.promien_ataku=300
    self.liczba_strzal=random.randint(1,3)
