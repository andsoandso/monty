A python module and program (see ./bin/monty.py) for playing the (fucking not-at-all-intuitive) Monty hall game with `n` doors and `k` reveals.

---

	git clone https://github.com/andsoandso/monty.git
	
Gets you the code.

# Interactive use

	>>> from monty.game import play, summarize
	>>> n = 3; k = 1; i = 10000
	>>> # 3 doors, 1 reveal, 10000 iterations
	>>> summarize(n, k, *play(n, k, i))
	Of 3 doors 1 was opened.
	Win percent with stay: 0.3316
	Win percent with change: 0.6684


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