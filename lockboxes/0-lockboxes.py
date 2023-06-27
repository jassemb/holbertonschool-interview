#!/usr/bin/python3
def canUnlockAll(boxes):
    j = 0
    while (j != len(boxes)-1):
        for i in range(j+1, len(boxes)):
            if (i in boxes[j]):
                j += 1
            else:
                return (False)
            break
    return (True)
