
import random
from collections import deque

def match(list):
	if len(list) <= 1:
		return

	random.shuffle(list)
	vals = deque(list)
	vals.rotate()
	return dict(zip(list,vals))

def writeToFile(matches):
	with open("Matches.txt", mode = "w") as f:
		for key in matches:
			f.write(key + " got " + matches[key] + "\n")

def writeToIndividualFiles(matches):
	for key in matches:
		with open(key + ".txt", mode = "w") as f:
			f.write(key + ", you got " + matches[key])

def genSecretSantas():
	names = [item for item in input("Enter participant names separated by spaces: ").split()]

	matches = match(names)
	writeToFile(matches)
	writeToIndividualFiles(matches)

# Run main func
genSecretSantas()