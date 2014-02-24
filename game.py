from random import randint, shuffle


def play(n, k, i):
    """Monty's problem, with n doors and k reveals run for i iterations.
    
    Parameters
    ---------
    n : int
        The number of doors
    k : int
        The number of reveals
    i : int, optional
        How many games to play, i.e. simulations to run
    
    Returns
    ------
    (stay, change) : (list, list)
        The binomial outcomes for when a contestant stays or changes,
        1 --> win, 0 --> lose.
        
    Examples
    -------
	>>> n = 3; k = 1; i = 10000
	>>> # 3 doors, 1 reveal, 10000 iterations
	>>> summarize(n, k, *play(n, k, i))
	Of 3 doors 1 were opened.
	Win percent with stay: 0.3316
	Win percent with change: 0.6684
    """

    if (n - k) < 2:
        raise ValueError("n must be 2 greater than k")

    # Init, lists of binary results 
    # (1: win, 0: lose)
    stay = []
    change = []
    for ith in range(i):
        # Make the doors, 
        # pick a winner, 
        # and shuffle
        doors = [0, ] * n
        doors[randint(0, n-1)] = 1
        shuffle(doors)

        # Contestant picks a door.
        pick = doors.pop()

        # Host reveals k doors
        kth = 0
        while kth < k:
            reveal = randint(0, len(doors)-1)
            # Don't reveal the winner
            if (doors[reveal] != 1):
                doors.pop(reveal)
                kth += 1
        
        # Imagine the Contestant picked again
        # from the remaining doors
        repick = doors.pop()

        # Store ith results
        stay.append(pick)
        change.append(repick)

    return stay, change


def summarize(n, k, stay, change):
    """Summarize the results from playing the game.
    
    Parameters
    ---------
    n : int
        The number of doors
    k : int
        The number of reveals
    stay : list
        The binomial wins and losses if the contestant stayed
    change: list
        The binomial wins and losses if the contestant changed
    """
    
    i = len(stay)
    if i != len(change):
        raise ValueError("stay and change must be the same length")
    
    if k < 2:
        print("Of {0} doors {1} was opened.".format(n, k))
    else:
        print("Of {0} doors {1} were opened.".format(n, k))

    print("Win percent with stay: {0}".format(sum(stay) / float(i)))
    print("Win percent with change: {0}".format(sum(change) / float(i)))
    