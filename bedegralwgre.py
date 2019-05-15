#bede grał w gre kolko i krzyzyk
#najpierw PvP
#potem sztuczna inteligencja
#heckyeah

#tablica zawierająca stan rozgrywki
stan = [
     [0,0,0],
     [0,0,0],
     [0,0,0],]

for k in range(9):   
     nowy = int(input("podaj numer dla krzyżyka"))

     
     #umieszczanie x w tabeli
     if (nowy == 1):
          if ( stan[2][0] == 2 or stan[2][0] == 1):
               break
          else:
               stan[2][0] = 1
     if (nowy == 2):
          if ( stan[2][1] == 2 or stan[2][1] == 1):
               break
          else:
               stan[2][1] = 1
     if (nowy == 3):
          if ( stan[2][2] == 2 or stan[2][2] == 2):
               break
          else:
               stan[2][2] = 1
     if (nowy == 4):
          if ( stan[1][0] == 2 or stan[1][0] == 1):
               break
          else:
               stan[1][0] = 1
     if (nowy == 5):
          if ( stan[1][1] == 2 or stan[1][1] == 1):
               break
          else:
               stan[1][1] = 1
     if (nowy == 6):
          if ( stan[1][2] == 2 or stan[1][2] == 1):
               break
          else:
               stan[1][2] = 1
     if (nowy == 7):
          if ( stan[0][0] == 2 or stan[0][0] == 1):
               break
          else:
               stan[0][0] = 1
     if (nowy == 8):
          if ( stan[0][1] == 2):
               break
          else:
               stan[0][1] = 1
     if (nowy == 9):
          if ( stan[0][2] == 2 or stan[0][2] == 1):
              break
          else:
               stan[0][2] = 1
     #koniec umieszczania

     nowy = int(input("Podaj numer dla kółka"))

     #umieszczanie 0 w tabeli
     if (nowy == 1):
          if ( stan[2][0] == 2 or stan[2][0] == 1):
               break
          else:
               stan[2][0] = 2
     if (nowy == 2):
          if ( stan[2][1] == 2 or stan[2][1] == 1):
               break
          else:
               stan[2][1] = 2
     if (nowy == 3):
          if ( stan[2][2] == 2 or stan[2][2] == 2):
               break
          else:
               stan[2][2] = 2
     if (nowy == 4):
          if ( stan[1][0] == 2 or stan[1][0] == 1):
               break
          else:
               stan[1][0] = 2
     if (nowy == 5):
          if ( stan[1][1] == 2 or stan[1][1] == 1):
               break
          else:
               stan[1][1] = 2
     if (nowy == 6):
          if ( stan[1][2] == 2 or stan[1][2] == 1):
               break
          else:
               stan[1][2] = 2
     if (nowy == 7):
          if ( stan[0][0] == 2 or stan[0][0] == 1):
               break
          else:
               stan[0][0] = 2
     if (nowy == 8):
          if ( stan[0][1] == 2):
               break
          else:
               stan[0][1] = 2
     if (nowy == 9):
          if ( stan[0][2] == 2 or stan[0][2] == 1):
              break
          else:
               stan[0][2] = 2
     #koniec umieszczania

#wypisywanie tablicy
for row in stan:
     print()
     for element in row:
          print(element,end=" ")
#koniec wypisywania


for i in range(3):
     for j in range(3):
          if stanX[i][j] == 1:
               print("jeden")

#sprawdzenie wygranej
#for row in stan
     
#koniec sprawdzenia
