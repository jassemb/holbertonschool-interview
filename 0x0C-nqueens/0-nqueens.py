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