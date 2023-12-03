from aocdata import datafile

inpfile = datafile(2023, 3)

testdata = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

sum = 0
schem = list()
def applic(inc):
  """ Order input i 2d array (with each number grouped in list where they occur)"""
  row = list()
  num = list()
  symbcoord = list()
  numcoord = list()
  for i in inc:
    if not i.isnumeric():
      if len(num) == 0:
        row.append(i)
      else:
        row.append([n for n in num])
        num.clear()
        row.append(i)
    else:
      num.append(i)
  schem.append(row)


def calc():
  """ Create two dictionaries, one for coordinates (keys) of numbers
      One for coordinates of symbols"""
  global sum
  symbcoord = dict()
  numcoord = dict()
  x, y = -1, -1
  for row in schem:
    y += 1
    x = 0
    for col in row:
      if col != '.' and not isinstance(col, list):
        symbcoord[(x,y)] = col
        x += 1
      elif isinstance(col, list):
        numcoord[(x,y)] = ''.join(col)
        x += len(numcoord[(x,y)])
      else:
        x += 1
  """ Calculate distance between each number (whole length of it) and symbols
      If it's short enough, add it to sum"""
  for numxy in numcoord:
    added = False
    for symxy in symbcoord:
      numlen = len(numcoord[numxy])
      for n in range(0,numlen):
        xdist = abs(numxy[0]+n - symxy[0])
        ydist = abs(numxy[1] - symxy[1])
        if xdist <= 1 and ydist <= 1:
          sum += int(numcoord[numxy])
          added = True
          break
      if added:
        break

def calc2():
  """Pretty much as calc, but store only gears (*) in symbcoord"""
  global sum
  symbcoord = dict()
  numcoord = dict()
  gearno = list()
  x, y = -1, -1
  for row in schem:
    y += 1
    x = 0
    for col in row:
      if col == '*':
        symbcoord[(x,y)] = col
        x += 1
      elif isinstance(col, list):
        numcoord[(x,y)] = ''.join(col)
        x += len(numcoord[(x,y)])
      else:
        x += 1
  """ Calculate distances and add if they're short enough, and check if gear has two adjacent numbers"""
  for symxy in symbcoord:
    gearno.clear()
    for numxy in numcoord:
      numlen = len(numcoord[numxy])
      for n in range(0, numlen):
        xdist = abs(numxy[0] + n - symxy[0])
        ydist = abs(numxy[1] - symxy[1])
        if xdist <= 1 and ydist <= 1:
          gearno.append(numcoord[numxy])
          added = True
          break
      if len(gearno)>1:
        gearmult = int(gearno[0]) * int(gearno[1])
        sum += gearmult
        break


def solve():
  with open(inpfile) as inp:
    for n, i in enumerate(inp):
      applic(i.strip())
  calc2()
  print(sum)

if __name__ == '__main__':
  solve()