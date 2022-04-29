
def read_board(path):

    with open(path, 'r') as file:

        skip_comments = lambda line: line[0] != '#'
        lines = filter(skip_comments, file)

        N = int(next(lines))
        D = int(next(lines))
        Rs = int(next(lines))
        Rp = int(next(lines))

        cities = list()

        for line in lines:
            x, y = line.split()
            cities.append((int(x), int(y)))

    assert len(cities) == N

    return N, D, Rs, Rp, cities

def write_solution(path, towers):
    """ Takes a single solution, given as a list of towers to place, and writes it out to a given file path. """

    with open(path, 'w') as file:

        file.write(f'{len(towers)}\n')
        
        for tower in towers:
            file.write(f'{tower[0]} {tower[1]}\n')


def get_solutions(solver):

    """ Runs a given algorithm on the class inputs, and writes using the correct output format. """

    