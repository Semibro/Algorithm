import math

def dist(x1, y1, x2, y2):
  result = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)
  return result

def line(x1, y1, x2, y2, x3, y3):
  if y2 - y1 == 0 or x2 - x1 == 0:
    if (x3 - x1) + y1 == y3:
      return True
    else:
      return False
  else:
    if ((y2 - y1) / (x2 - x1)) * (x3 - x1) + y1 == y3:
      return True
    else:
      return False

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

if (a[0] == b[0] == c[0]) or (a[1] == b[1] == c[1]) or line(a[0], a[1], b[0], b[1], c[0], c[1]):
  print('X')
elif dist(a[0], a[1], b[0], b[1]) == dist(b[0], b[1], c[0], c[1]) == dist(c[0], c[1], a[0], a[1]):
  print('JungTriangle')
elif dist(a[0], a[1], b[0], b[1]) == dist(b[0], b[1], c[0], c[1]):
  if dist(a[0], a[1], b[0], b[1]) + dist(b[0], b[1], c[0], c[1]) == dist(c[0], c[1], a[0], a[1]):
    print("Jikkak2Triangle")
  elif dist(a[0], a[1], b[0], b[1]) + dist(b[0], b[1], c[0], c[1]) < dist(c[0], c[1], a[0], a[1]):
    print('Dunkak2Triangle')
  elif dist(a[0], a[1], b[0], b[1]) + dist(b[0], b[1], c[0], c[1]) > dist(c[0], c[1], a[0], a[1]):
    print("Yeahkak2Triangle")
elif dist(b[0], b[1], c[0], c[1]) == dist(c[0], c[1], a[0], a[1]):
  if dist(b[0], b[1], c[0], c[1]) + dist(c[0], c[1], a[0], a[1]) == dist(a[0], a[1], b[0], b[1]):
    print('Jikkak2Triangle')
  elif dist(b[0], b[1], c[0], c[1]) + dist(c[0], c[1], a[0], a[1]) < dist(a[0], a[1], b[0], b[1]):
    print('Dunkak2Triangle')
  elif dist(b[0], b[1], c[0], c[1]) + dist(c[0], c[1], a[0], a[1]) > dist(a[0], a[1], b[0], b[1]):
    print('Yeahkak2Triangle')
elif dist(c[0], c[1], a[0], a[1]) == dist(a[0], a[1], b[0], b[1]):
  if dist(c[0], c[1], a[0], a[1]) + dist(a[0], a[1], b[0], b[1]) == dist(b[0], b[1], c[0], c[1]):
    print('Jikkak2Triangle')
  elif dist(c[0], c[1], a[0], a[1]) + dist(a[0], a[1], b[0], b[1]) < dist(b[0], b[1], c[0], c[1]):
    print('Dunkak2Triangle')
  elif dist(c[0], c[1], a[0], a[1]) + dist(a[0], a[1], b[0], b[1]) > dist(b[0], b[1], c[0], c[1]):
    print('Yeahkak2Triangle')
elif dist(a[0], a[1], b[0], b[1]) != dist(b[0], b[1], c[0], c[1]) != dist(c[0], c[1], a[0], a[1]):
  if dist(a[0], a[1], b[0], b[1]) == max(dist(a[0], a[1], b[0], b[1]), dist(b[0], b[1], c[0], c[1]), dist(c[0], c[1], a[0], a[1])):
    if dist(a[0], a[1], b[0], b[1]) == dist(b[0], b[1], c[0], c[1]) + dist(c[0], c[1], a[0], a[1]):
      print('JikkakTriangle')
    elif dist(a[0], a[1], b[0], b[1]) > dist(b[0], b[1], c[0], c[1]) + dist(c[0], c[1], a[0], a[1]):
      print('DunkakTriangle')
    elif dist(a[0], a[1], b[0], b[1]) < dist(b[0], b[1], c[0], c[1]) + dist(c[0], c[1], a[0], a[1]):
      print('YeahkakTriangle')
  elif dist(b[0], b[1], c[0], c[1]) == max(dist(a[0], a[1], b[0], b[1]), dist(b[0], b[1], c[0], c[1]), dist(c[0], c[1], a[0], a[1])):
    if dist(b[0], b[1], c[0], c[1]) == dist(c[0], c[1], a[0], a[1]) + dist(a[0], a[1], b[0], b[1]):
      print('JikkakTriangle')
    elif dist(b[0], b[1], c[0], c[1]) > dist(c[0], c[1], a[0], a[1]) + dist(a[0], a[1], b[0], b[1]):
      print('DunkakTriangle')
    elif dist(b[0], b[1], c[0], c[1]) < dist(c[0], c[1], a[0], a[1]) + dist(a[0], a[1], b[0], b[1]):
      print('YeahkakTriangle')
  elif dist(c[0], c[1], a[0], a[1]) == max(dist(a[0], a[1], b[0], b[1]), dist(b[0], b[1], c[0], c[1]), dist(c[0], c[1], a[0], a[1])):
    if dist(c[0], c[1], a[0], a[1]) == dist(a[0], a[1], b[0], b[1]) + dist(b[0], b[1], c[0], c[1]):
      print('JikkakTriangle')
    elif dist(c[0], c[1], a[0], a[1]) > dist(a[0], a[1], b[0], b[1]) + dist(b[0], b[1], c[0], c[1]):
      print('DunkakTriangle')
    elif dist(c[0], c[1], a[0], a[1]) < dist(a[0], a[1], b[0], b[1]) + dist(b[0], b[1], c[0], c[1]):
      print('YeahkakTriangle')