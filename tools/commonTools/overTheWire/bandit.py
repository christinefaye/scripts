#!/usr/bin/python

import sys
sys.path.append("/home/christine/st/scripts/tools/commonMod")
from cmHost import cHost

def main():
  url='bandit.labs.overthewire.org'
  usr='bandit0'
  pw='bandit0'

  # Bandit host
  b = cHost(usr,pw,url=url)
  # Connect to host
  b.createCnxn()

if __name__=="__main__":
  main()

