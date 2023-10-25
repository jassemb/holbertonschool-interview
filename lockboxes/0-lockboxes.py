#!/usr/bin/python3
"""
canUnlockAll : test if all boxes can be opened
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

