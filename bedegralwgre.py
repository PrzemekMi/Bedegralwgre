#bede grał w gre kolko i krzyzyk
#najpierw PvP
#potem sztuczna inteligencja
#heckyeah

#tablica zawierająca stan rozgrywki
stan = [
     [0,0,0],
     [0,0,0],
     [0,0,0],]

stanX = [
     [0,0,0],
     [0,0,0],
     [0,0,0],]

stan0 = [
     [0,0,0],
     [0,0,0],
     [0,0,0],]

nowyX = 0
nowyX = int(input("podaj numer dla krzyżyka"))

#umieszczanie x w tabeli
if (nowyX == 1):
     stanX[2][0] = 1
if (nowyX == 2):
     stanX[2][1] = 1
if (nowyX == 3):
     stanX[2][2] = 1
if (nowyX == 4):
     stanX[1][0] = 1
if (nowyX == 5):
     stanX[1][1] = 1
if (nowyX == 6):
     stanX[1][2] = 1
if (nowyX == 7):
     stanX[0][0] = 1
if (nowyX == 8):
     stanX[0][1] = 1
if (nowyX == 9):
     stanX[0][2] = 1
#koniec umieszzania

nowy0 = 0
nowy0 = int(input("Podaj numer dla kółka"))

#umieszczanie 0 w tabeli
if (nowy0 == 1):
     stan0[2][0] = 1
if (nowy0 == 2):
     stan0[2][1] = 1
if (nowy0 == 3):
     stan0[2][2] = 1
if (nowy0 == 4):
     stan0[1][0] = 1
if (nowy0 == 5):
     stan0[1][1] = 1
if (nowy0 == 6):
     stan0[1][2] = 1
if (nowy0 == 7):
     stan0[0][0] = 1
if (nowy0 == 8):
     stan0[0][1] = 1
if (nowy0 == 9):
     stan0[0][2] = 1
#koniec umieszzania

#wypisywanie tablicy X
for row in stanX:
     print()
     for element in row:
          print(element,end=" ")
#koniec wypisywania

#wypisywanie tablicy 0
for row in stan0:
     print()
     for element in row:
          print(element,end=" ")
#koniec wypisywania

for i in range(3):
     print()
     for j in range(3):
          if stanX[i][j] == 1:
               print("jeden")

#sprawdzenie wygranej
#for row in stan
     
#koniec sprawdzenia
