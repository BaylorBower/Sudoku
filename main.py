from random import sample
# On a scale of 1-100 difficulty
Difficulty = 100


# baseline valid solution
def pattern(r, c):
    return (base*(r % base)+r//base+c) % side


# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s):
    return sample(s,len(s))

base = 3
side = base*base
rBase = range(base)
rows = [g*base + r for g in shuffle(rBase) for r in shuffle(rBase)]
cols = [g*base + c for g in shuffle(rBase) for c in shuffle(rBase)]
nums = shuffle(range(1,base*base+1))

# produce board using randomized baseline pattern
board = [[nums[pattern(r, c)] for c in cols] for r in rows]
squares = side*side
empties = squares * Difficulty//110
for p in sample(range(squares), empties):
    board[p//side][p % side] = 0

numSize = len(str(side))


# Solves the grid recursively using backtracking
def solve(bo):
    find = findEmpty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0
    return False


def printBoard(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def findEmpty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None


# Checks to see if the number is valid in a certain position
def valid(bo, num, pos):
    # Row Check
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Column check
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Box Check
    boxx = pos[1] // 3
    boxy = pos[0] // 3

    for i in range(boxy * 3, boxy * 3 + 3):
        for j in range(boxx * 3, boxx * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True

