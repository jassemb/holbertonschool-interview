#!/usr/bin/python3
"""
The N queens puzzle
"""


import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    int(sys.argv[1])
except Exception:
    print("N must be a number")
    exit(1)
if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)
if not isinstance(int(sys.argv[1]), int):
    print("N must be a number")
    exit(1)

n = int(sys.argv[1])

def is_valid_state(state):
    return True

def get_candidates(state):
    return []

def search(state, solutions):
    if is_valid_state(state):
        solutions.append(state.copy())
        # return

    for candidate in get_candidates(state):
        state.add(candidate)
        search(state, solutions)
        state.remove(candidate)

def solve():
    solutions = []
    state = set()
    search(state, solutions)
    return solutions