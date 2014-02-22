#! /usr/local/bin/python
"""Play the Monty Hall game, with n doors and k reveals. 

I wanted a better intuition for the proof.

usage: python ./monty.py n k [, i]

n is the door number, k is the number of doors revealed, and i is 
the number of simulations to run (optional, defaults to 10,000).

For example, the canonoical version with three doors and 1 reveal 
is run as

$ python ./monty.py 3 1

While the more intuitive 100 door version is run as

$ python ./monty.py 100 98

If you like to run only 10 iterations (which is very unreliable):

$ python ./monty.py 3 1 10
"""
import sys
from monty.game import play, summarize


n = int(sys.argv[1])
k = int(sys.argv[2])
try:
    i = int(sys.argv[3])
except IndexError:
    i = 10000

summarize(n, k, i, *play(n, k, i))

