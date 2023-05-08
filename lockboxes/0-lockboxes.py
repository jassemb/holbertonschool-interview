#!/usr/bin/python3
"""
    Box opener method.
"""

def concat(A,B):
    res=[]
    for w in B:
        res+=A[w]
    return res

def canUnlockAll(boxes):
    index = 0
    total = list(set(boxes[0])|{0})
    sum = True
    while sum:
        sum=False
        for j in concat(boxes,total[index:]):
            if j not in total:
                total.append(j)
                index = index + 1
                sum=True
    return len(total) == len(boxes)

