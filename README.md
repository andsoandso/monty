A python module and program (see ./bin/monty.py) for playing the Monty hall game with `n` doors and `k` reveals.

Install to a location on your python path by

	git clone 
	

# Interactive use

	from monty.game import play, summarize
	

# Command line use

After cloning install the program `monty.py` (in `monty/bin/monty.py`) to somewhere on your path, e.g.

	cp ./monty/bin/monty.py /usr/local/bin/

---
	
usage: python ./monty.py n k [, i]

n is the door number, k is the number of doors revealed, and i is 
the number of simulations to run (optional, defaults to 10,000).

For example, the canonoical version with three doors and 1 reveal 
is run as

	$ monty.py 3 1

While the more intuitive 100 door version is run as

	$ monty.py 100 98

If you like to run only 10 iterations (which is very unreliable):

	$ monty.py 3 1 10