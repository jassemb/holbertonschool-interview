#!/usr/bin/python3
"""
    Box opener method.
"""


def canUnlockAll(boxes):
    test = [0]



    for id, box in enumerate(boxes):
        if not box:
            continue
        for k in box:
            if k not in test and k != id and k<len(boxes):
                test.append(k)
    
    
    
    if len(test) == len(boxes):
        return True
    return False
