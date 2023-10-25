#!/usr/bin/python3
"""
    Box opener method.
"""

def canUnlockAll(boxes):
	kList = [0]

	for keys in kList:
		for i in boxes[keys]:
			if i not in kList and i < len(boxes):
				kList.append(i)

	for i in range(len(boxes)):
		if i not in kList:
			return False
	return True
