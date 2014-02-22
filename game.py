from random import randint, shuffle


def play(n, k, i):
    """Monty's problem, with n doors and k reveals run for i iterations."""

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


def summarize(n, k, i, stay, change):
    print("Of {0} doors {1} were opened.".format(n, k))
    print("Win percent with stay: {0}".format(sum(stay) / float(i)))
    print("Win percent with change: {0}".format(sum(change) / float(i)))
    