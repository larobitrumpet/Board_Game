def Board(P1Place, P2Place, i):
   t = i
   print("")
   if P1Place > i:
      print("             P1")
   if P2Place > i:
      print("             P2")
   print("          _____")
   while i >= 0:
      if i == 0:
         if P1Place == i:
            if P1Place == P2Place:
               print("          P1 P2          P1 has " + str(t - P1Place + 1) + " spaces to go.   P2 has " + str(t - P2Place + 1) + " spaces to go.")
               break
            else:
               print("             P1               P1 has " + str(t - P1Place + 1) + " spaces to go.   P2 has " + str(t - P2Place + 1) + " spaces to go.")
               break
         elif P2Place == i:
            print("             P2               P1 has " + str(t - P1Place + 1) + " spaces to go.   P2 has " + str(t - P2Place + 1) + " spaces to go.")
            break
         else:
            print("                   P1 has " + str(t - P1Place + 1) + " spaces to go.   P2 has " + str(t - P2Place + 1) + " spaces to go.")
            break
      if P1Place == i:
         if P1Place == P2Place:
            print("         |P1 P2|")
            print("         |_____|   " + str(i))
            i = i - 1
            continue
         else:
            print("         |  P1 |")
            print("         |_____|   " + str(i))
      elif P2Place == i:
         print("         |  P2 |")
         print("         |_____|   " + str(i))
      elif i == 3:
         print("         | +4  |")
         print("         |_____|   " + str(i))
      elif i == 14:
         print("         | +4  |")
         print("         |_____|   " + str(i))
      elif i == 6:
         print("         | -4  |")
         print("         |_____|   " + str(i))
      elif i == 17:
         print("         | -4  |")
         print("         |_____|   " + str(i))
      elif i == 10:
         print("         | P->P|")
         print("         |_____|   " + str(i))
      elif i == 19:
         print("         | P->P|")
         print("         |_____|   " + str(i))
      elif i == 12:
         print("         |P<->P|")
         print("         |_____|   " + str(i))
      elif i == 8:
         print("         | P->V|")
         print("         |_____|   " + str(i))
      else:
         print("         |     |")
         print("         |_____|   " + str(i))
      i = i - 1
   print("")
def Volcano(P1vPlace, P2vPlace, i):
   print("")
   if P1vPlace != None:
      if P1vPlace > i:
         print("             P1")
   if P2vPlace != None:
      if P2vPlace > i:
         print("             P2")
   print("          _____")
   while i >= 0:
      if i == 0:
         if P1vPlace == 0:
            if P1vPlace == P2vPlace:
               print("          P1 P2")
               break
            if P1vPlace != P2vPlace:
               print("             P1")
               break
         elif P2vPlace == 0:
            print("             P2")
            break
      if P1vPlace == i:
         if P1vPlace == P2vPlace:
            print("         |P1 P2|")
            print("         |_____|   " + str(i))
            i = i - 1
            continue
         else:
            print("         |  P1 |")
            print("         |_____|   " + str(i))
      elif P2vPlace == i:
         print("         |  P2 |")
         print("         |_____|   " + str(i))
      else:
         print("         |     |")
         print("         |_____|   " + str(i))
      i = i - 1
   print("")
