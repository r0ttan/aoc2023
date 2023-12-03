from aocdata import datafile

inpfile = datafile(2023, 2)

testdata = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

bag = {'red':12, 'green': 13, 'blue': 14 }
gidtot = 0

def applic(inc):
  global gidtot
  bag = {'red': 12, 'green': 13, 'blue': 14}
  gameind = inc.index(':')
  gameid = int(inc[:gameind].split()[1])
  gamesets = inc[gameind+2:].split(';')
  #print(f'{gameid=} >> {gamesets=}')
  potential = gameid
  for game in gamesets:
    for set in game.split(','):
      #print(set.split())
      col = set.split()[1]
      val = int(set.split()[0])
      if val > bag[col]:
        potential = None
  if potential:
    gidtot += gameid
    #print(gidtot)


def applic2(inc):
  global gidtot
  bag = {'red': 12, 'green': 13, 'blue': 14}
  gameind = inc.index(':')
  gameid = int(inc[:gameind].split()[1])
  gamesets = inc[gameind+2:].split(';')
  #print(f'{gameid=} >> {gamesets=}')
  potential = gameid
  minimum = {'red': 0, 'green': 0, 'blue': 0}
  pow = 1
  for game in gamesets:
    for set in game.split(','):
      #print(set.split())
      col = set.split()[1]
      val = int(set.split()[0])
      if val > minimum[col]:
        minimum[col] = val
  print(minimum)
  for v in minimum.values():
    pow *= v
  print(pow)
  gidtot += pow
    #print(gidtot)

def solve():
  with open(inpfile) as inp:
    for n, i in enumerate(inp):
      applic2(i.strip())
  print(gidtot)
  #for g in testdata.split('\n'):
  #  applic2(g)
  #  print(gidtot)

if __name__ == '__main__':
  solve()