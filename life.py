import numpy as np
import random

ALIVE = 1
DEAD = 0

def dead_state(width, height):
    '''
    Given a width and height, this function will initialize a board where each cell is
    given a DEAD state.
    '''
    board = []
    for row in range(height):
        new_row = []
        for col in range(width):
            new_row.append(DEAD)

        board.append(new_row)

    return board

def random_state(width, height):
    state = dead_state(width, height)

    for x in range(get_height(state)):
        for y in range(get_width(state)):
            val = random.random()
            if val >= 0.75:
                state[x][y] = ALIVE
            else:
                state[x][y] = DEAD

    return state

def render(state):
    '''
    Will take in a state and render the game of life simulation in terminal
    '''
    display = {
        DEAD: ' ', 
        ALIVE: u"\u2588" # This is a unicode character for a filled in square } row = state[0]
    }

    # Print the Header
    for i in range(get_width(state) * 2 + 2):
        print('-', end='')
    print('')

    for row in state:
        print('|', end='')
        for val in row:
            if val == ALIVE:
                print(display[ALIVE] * 2, end='')
            elif val == DEAD:
                print(display[DEAD] * 2, end='')

        print('|', end='')
        print('') # This takes the next row to a new line

    # Print the Footer
    for i in range(get_width(state) * 2 + 2):
        print('-', end='')
    print('')

def next_board_state(init_state):
    new_state = []

    for row in range(get_height(init_state)):
        new_row = []
        for col in range(get_width(init_state)):
            # Can check for ALIVE or DEAD first to shorten the if statements
            if alive_neighbors(init_state, row, col) <= 1 and init_state[row][col] == ALIVE:
                new_row.append(DEAD)
            elif alive_neighbors(init_state, row, col) <= 3 and init_state[row][col] == ALIVE:
                new_row.append(ALIVE)
            elif alive_neighbors(init_state, row, col) > 3 and init_state[row][col] == ALIVE:
                new_row.append(DEAD)
            elif alive_neighbors(init_state, row, col) == 3 and init_state[row][col] == DEAD:
                new_row.append(ALIVE)
            else:
                new_row.append(DEAD)

        new_state.append(new_row)

    return new_state

def alive_neighbors(state, row, col):
    neighbors = 0
    positions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]] # Possible shifts

    for pos in positions:
        new_row = row + pos[0]
        new_col = col + pos[1]
        if new_row >= 0 and new_row < get_height(state):
            if new_col >= 0 and new_col < get_width(state):
                if state[new_row][new_col] == ALIVE:
                    neighbors += 1

    return neighbors

def get_height(state):
    return len(state)


def get_width(state): 
    return len(state[0])

def run():
    '''
    Game of Life Infinite Loop
    '''
    state = random_state(30, 30)
    render(state)
    while True:
        state = next_board_state(state)
        render(state)


if __name__ == "__main__":
    run()
