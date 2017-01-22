import random


# function to create initial grid, takes in population density and disease chance
# along with the dimesnions of the grid as its parameters. returns a dictionary
# with x, y coordinate keys
def create_grid(n, density, disease):
    # empty dictionary where values will be added to each x, y coordinate key
    grid = {}
    # goes through every x, y coordinate point from (0,0) to (n-1,n-1)
    # generates random number r to see if the value will be an occupied
    # cell and then uses another random number h to see if that occupied
    # cell will become diseased.
    for y in range(n):
        for x in range(n):
            r = random.random()
            if r < density:
                grid[(x, y)] = 0
                h = random.random()
                if h < disease:
                    grid[(x, y)] = 1
            # if the point doesn't become occupied it will be an empty
            # cell represented by a dot
            else:
                grid[(x, y)] = "."
    return grid



def print_grid(n, grid):
    # for loop that goes through every value of y from 0 to n - 1
    for y in range(n):
        # every time y increments by 1 we need to create a new empty string that will
        # contain grid point values
        line = ""
        for x in range(n):
            # add every value with the same y and incrementing x values to the end of
            # the line and print that line after. this creates grid with grid values
            line += str(grid[(x,y)]) + " "
        print(line)





def surrounding(x, y, grid, n):
    d = []
    if (x + 1 != n):
        d.append(grid[x + 1, y])
        if y - 1 != -1:
            d.append(grid[x + 1, y - 1])
        if y + 1 != n:
            d.append(grid[x + 1, y + 1])

    if (x-1 != -1):
        d.append(grid[x - 1, y])
        if y - 1 != -1:
            d.append(grid[x - 1, y - 1])
        if y + 1 != n:
            d.append(grid[x - 1, y + 1])

    if y + 1 != n:
        d.append(grid[x, y + 1])

    if y - 1 != -1:
        d.append(grid[x, y - 1])
    return d

# function to test surrounding() function which returns list of surrounding
# point values
def test_surrounding():
    x = create_grid(5, .4, .4)
    print_grid(5, x)
    l = surrounding(4, 4, x, 5)
    print()
    print(l)

# test_surrounding()

def infected(x, y, grid, n, spread):
    points = surrounding(x, y, grid, n)
    for e in points:
        if type(e) == int:
            if e > 0:
                r = random.random()
                if r < spread:
                    return 1
    return 0

def test_infected_birth():
    x = create_grid(5, .4, .4)
    print_grid(5, x)
    if x[3, 2] == 0:
        print(infected(3, 2, x, 5, .4))
    if x[3, 2] == ".":
        print(birth_chance(3, 2, x, 5, .4))

def infected_fate(mortality):
    # generate a random number
    r = random.random()
    # if the random number is less than the mortality rate that the cell dies
    # and we return a dot which will be the new state of the cell
    if r < mortality:
        return "."
    # otherwise we return a 0 to indicate that the cell became healthy and the
    # new state of the cell is now alive
    else:
        return 0


def birth_chance(x, y, grid, n, birth):
    points = surrounding(x, y, grid, n)
    for e in points:
        if e == 0:
            r = random.random()
            if r < birth:
                return 0
    return "."


# test_infected_birth()

def new_grid(n, grid, birth, spread, duration, mortality):
    gridn = {}
    for y in range(n):
        for x in range(n):
            # store value of grid[x, y] in state so that we don't have to write
            # grid[x, y] over and over again
            state = grid[x, y]
            # if the type of state is an int then we know the cell is either alive or infected
            if type(state) == int:
                # if the cell is infected and not on its last day of infection then the new state
                # of the cell is 1 more then the integer it was before
                if 0 < state < duration:
                    gridn[x, y] = state + 1
                # if the cell is alive then we need to check if it becomes infected by any of its
                # neighbors. The function infected does so and returns 1 if the cell becomes infected
                # or 0 if the cell stays alive and healthy and then we store that in the new grid
                elif state == 0:
                    gridn[x, y] = infected(x, y, grid, n, spread)
                # The else statement only works on cells that are infected and are on their last day
                # of being infected. If so we need to check if the cell will die or become healthy again
                else:
                    # function infected_fate returns a dot if the cell dies and a 0 if it becomes healthy
                    # once again
                    gridn[x, y] = infected_fate(mortality)
            # if the state of the cell is not an int it can only be a dot. if so check if the
            # cell becomes alive using the birth() function which returns a dot if the cell remains
            # empty and a 0 if it becomes alive due to its neighbors
            else:
                gridn[x, y] = birth_chance(x, y, grid, n, birth)

    return gridn

# function to test new_grid function
def test_newgrid():
    x = create_grid(5, .4, .4)
    print_grid(5, x)
    print()
    h = new_grid(5, x, .4, .3, 3, .4)
    print_grid(5, h)

def zombie_sim(size=20, density=.15, disease=.1, birth=.1, spread=.1, duration=3, mortality=.5, days=500):
    day = 0
    prev_grid = create_grid(size, density, disease)
    print("Grid at start of simulation: ")
    print_grid(size, prev_grid)
    while(day != days):
        print()
        day += 1
        print("Grid state after day {0}: ".format(day))
        print()
        current_grid = new_grid(size, prev_grid, birth, spread, duration, mortality)
        print_grid(size, current_grid)
        prev_grid = current_grid


# zombie_sim(10, .15, .1, .3, .2, 3, .5, 200)

# test_newgrid()

if __name__ == "__main__":
    zombie_sim()
