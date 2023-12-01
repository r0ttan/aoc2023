import requests, json
from pathlib import Path
#from os import environ

"""
Puzzle inputs differ by user. For this reason, you can't get your data with an unauthenticated request. Here's how to get your session cookie for aocd to use:

Login on AoC with github or whatever
Open browser's developer console (e.g. right click --> Inspect) and navigate to the Network tab
GET any input page, say adventofcode.com/2016/day/1/input, and look in the request headers.
It's a long hex string. Export that to an environment variable AOC_SESSION. Or, if you prefer more persistence, you can write it to a plain text file at ~/.config/aocd/token.
"""

def getdata(url, token):
  header = {'Cookie': f'session={token}', 'User-Agent': 'https://github.com/.../edit/main/aocdata.py by yourmail@yourmail.com'}
  r = requests.get(url, headers=header)
  if len(r.text) > 0:
    return r.text

def datafile(yearno, dayno):
  filename = f'aoc_day{dayno}.txt'
  path = Path(filename)
  if path.is_file():
    print(f'{filename} present')
  else:
    with open('.config/token') as conf:
      token = json.load(conf)['session']
    dat = getdata(f'https://adventofcode.com/{yearno}/day/{dayno}/input', token)
    with open(filename, 'w') as inp:
      inp.write(dat)
  return filename

if __name__ == '__main__':
  main(2022, 1)