import random
import DiceRollAlpha4
import DisplayBoardAlpha4
P1Place = 0
P2Place = 0
r = 0
i = 20
s = 0
P1vPlace = None
P2vPlace = None
print("")
print("Welcome.")
print("In this game, two players roll a dice and")
print("move along the game board.")
print("Who ever gets to the last space")
print("first wins!")
print("")
c = input("Press 'enter' to continue")
while True:
   r = r + 1
   print("")
   print("------------------------------------------")
   print("")
   print("Round " + str(r))
   if r == 1:
      DisplayBoardAlpha4.Board(P1Place, P2Place, i)
      if P1vPlace != None:
         DisplayBoardAlpha4.Volcano(P1vPlace, P2vPlace, 6)
      elif P2vPlace != None:
         DisplayBoardAlpha4.Volcano(P1vPlace, P2vPlace, 6)
   d = DiceRollAlpha4.P1(P1Place, P1vPlace)
   d = d.split()
   if P1vPlace == None:
      P1Place = int(d[0])
   else:
      P1vPlace = int(d[0])
   n = d[1]
   if P1vPlace == None:
      if P1Place == 3:
         P1Place = P1Place + 4
         s = 1
      elif P1Place == 14:
         P1Place = P1Place + 4
         s = 1
      elif P1Place == 6:
         P1Place = P1Place - 4
         s = 2
      elif P1Place ==17:
         P1Place = P1Place - 4
         s = 2
      elif  P1Place == 10:
         P1Place = P2Place
         s = 3
      elif P1Place == 19:
         P1Place = P2Place
         s = 3
      elif P1Place == 12:
         P1Place, P2Place = P2Place, P1Place
         s = 4
      elif P1Place == 8:
         if P1vPlace == None:
            P1vPlace = 0
            print("You have fallen into the volcano!")
            print("")
         s = 5
   print("")
   DisplayBoardAlpha4.Board(P1Place, P2Place, i)
   if P1vPlace != None:
      DisplayBoardAlpha4.Volcano(P1vPlace, P2vPlace, 6)
   elif P2vPlace != None:
      DisplayBoardAlpha4.Volcano(P1vPlace, P2vPlace, 6)
   print("")
   print("You rolled a " + str(n) + "!")
   print("")
   if P1vPlace == None:
      if s == 1:
         print("Boost! Move forward 4 spaces!")
         print("")
      elif s == 2:
         print("Too bad. Move back 4 spaces.")
         print("")
      elif s == 3:
         print("An alien has taken you to P2!")
         print("")
      elif s == 4:
         print("Aliens have caused you and")
         print("P2 to trade places!")
         print("")
   if s == 5:
      if P1vPlace == 0:
         print("You have fallen into the volcano!")
         print("")
   print("You are now on space " + str(P1Place) + "!")
   if P1Place > i:
      break
   if P1vPlace != None:
      if P1vPlace > 6:
         print("")
         print("You are now out of the volcano!")
         P1vPlace = None
   s = 0
   print("")
   c = input("Press ' enter' to continue")
   print("")
   d = DiceRollAlpha4.P2(P2Place, P2vPlace)
   d = d.split()
   if P2vPlace == None:
      P2Place = int(d[0])
   else:
      P2vPlace = int(d[0])
   n = d[1]
   if P2vPlace == None:
      if P2Place == 3:
         P2Place = P2Place + 4
         s = 1
      elif P2Place == 14:
         P2Place = P2Place + 4
         s = 1
      elif P2Place == 6:
         P2Place = P2Place - 4
         s = 2
      elif P2Place == 17:
         P2Place = P2Place - 4
         s = 2
      elif  P2Place == 10:
         P2Place = P1Place
         s = 3
      elif  P2Place == 19:
         P2Place = P1Place
         s = 3
      elif P2Place == 12:
         P2Place, P1Place = P1Place, P2Place
         s = 4
   if P2Place == 8:
      if P2vPlace == None:
         P2vPlace = 0
         print("You have fallen into the volcano!")
         print("")
      s = 5
   print("")
   DisplayBoardAlpha4.Board(P1Place, P2Place, i)
   if P1vPlace != None:
      DisplayBoardAlpha4.Volcano(P1vPlace, P2vPlace, 6)
   elif P2vPlace != None:
      DisplayBoardAlpha4.Volcano(P1vPlace, P2vPlace, 6)
   print("")
   print("You rolled a " + str(n) + "!")
   print("")
   if P2vPlace == None:
      if s == 1:
         print("Boost! Move forward 4 spaces!")
         print("")
      elif s == 2:
         print("Too bad. Move back 4 spaces.")
         print("")
      elif s == 3:
         print("An alien has taken you to P1!")
         print("")
      elif s == 4:
         print("Aliens have caused you and")
         print("P1 to trade places!")
         print("")
   if s == 5:
      if P2vPlace == 0:
         print("You have fallen into the volcano!")
         print("")
   print("You are now on space " + str(P2Place) + "!")
   if P2Place > i:
      break
   if P2vPlace != None:
      if P2vPlace > 6:
         print("")
         print("You are now out of the volcano!")
         P2vPlace = None
   s = 0
   print("")
   c = input("Press ' enter' to continue")
if P1Place > i:
   print("")
   c = input("Press ' enter' to continue")
   print("")
   print("-----------------------------------------")
   print("")
   print("P1 wins!")
if P2Place > i:
   print("")
   c = input("Press ' enter' to continue")
   print("")
   print("-----------------------------------------")
   print("")
   print("P2 wins!")
print("")
print("Thank you for playing!")
