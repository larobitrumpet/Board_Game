def P1(P1Place, P1vPlace):
   import random
   print("")
   r = input("P1, press 'enter' to roll dice")
   n = random.randint(1, 6)
   if P1vPlace == None:
      P1Place = P1Place + n
      return (str(P1Place) + " " + str(n))
   if P1vPlace != None:
      P1vPlace = P1vPlace + n
      return (str(P1vPlace) + " " + str(n))
def P2(P2Place, P2vPlace):
   import random
   print("")
   r = input("P2, press 'enter' to roll dice")
   n = random.randint(1, 6)
   if P2vPlace == None:
      P2Place = P2Place + n
      return (str(P2Place) + " " + str(n))
   if P2vPlace != None:
      P2vPlace = P2vPlace +n
      return (str(P2vPlace) + " " + str(n))
