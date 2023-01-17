import math

while True:
  TC = input()
  if TC == "0":
    break
  if len(TC) == 1:
    print("yes")
  elif len(TC) == 2:
    if TC[0] == TC[1]:
      print("yes")
    else:
      print("no")
  elif len(TC) == 3:
    if TC[0] == TC[2]:
      print("yes")
    else:
      print("no")
  elif len(TC) == 4:
    if TC[0] == TC[3] and TC[1] == TC[2]:
      print("yes")
    else:
      print("no")
  elif len(TC) == 5:
    if TC[0] == TC[4] and TC[1] == TC[3]:
      print("yes")
    else:
      print("no")