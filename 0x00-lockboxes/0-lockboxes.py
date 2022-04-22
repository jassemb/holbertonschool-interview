#!/usr/bin/python3
"""
    Method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
        Return True if ALL boxes can be opened, else return False.
    """
    visted = set()

    def dfs(boxe):
        visted.add(boxe)
        for i in boxes[boxe]:
            if i not in visted:
                dfs(i)
    dfs(0)
    return len(visted) == len(boxes)