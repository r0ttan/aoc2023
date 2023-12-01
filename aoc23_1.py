from aocdata import datafile
import re

inpfile = datafile(2023, 1)
testdata = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
eightfour2fourvzksqhxmlkpkfktmdzpmthreetwonehv
1
one
onetwothreefourfivesixseveneightnine"""


globvar = list()
total = 0

#del1
def applic(inc):
  """ helper function, eg applic something foreach row of data """
  global total
  val = list()
  for v in inc:
    if v.isnumeric():
      val.append(v)
      break
  for v in inc[::-1]:
    if v.isnumeric():
      val.append(v)
      break
  total += int(''.join(val))

def applic2(inc):
  """ helper function, eg applic something foreach row of data """
  global total
  prevtotal = total
  alphnum = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
  nums = [b for b in alphnum]
  val = list()
  anumlast = None

  n = [no for no in re.findall(r"(?=("+'|'.join(nums)+r"|\d))", inc)]
  if n:
    anumfirst = n[0]
    if anumfirst.isnumeric():
      val.append(anumfirst)
    else:
      val.append(alphnum[anumfirst])
    anumlast = n[-1]
    if anumlast.isnumeric():
      val.append(anumlast)
    else:
      val.append(alphnum[anumlast])
  total += int(''.join(val))

def solve():
  with open(inpfile) as inp:
    for n, i in enumerate(inp):
      applic2(i.strip())
  #for a in testdata.split('\n'):
  #  applic2(a.strip())
  print(f'{n} rows processed')
  print(total)

if __name__ == '__main__':
  solve() #50844 to low, 54504 correct