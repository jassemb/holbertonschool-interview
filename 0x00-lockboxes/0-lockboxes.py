#!/usr/bin/python3
"""
    Method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
        Return True if ALL boxes can be opened, else return False.
    """
    visted = set()
    stack = [0]
    while stack:
        box = stack.pop()
        visted.add(box)
        for key in boxes[box]:
            if key not in visted:
                stack.append(key)
    return len(visted) == len(boxes)
