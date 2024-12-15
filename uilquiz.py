import subprocess
import random
import linecache
from gtts import gTTS
global asklines
global speed
speed = 0
subprocess.run(["clear"])
def getword():
	global word
	with open("asklist.txt", "r+") as getlines:
		asklines = sum(1 for _ in getlines)
	if asklines < 1:
		asklines == asklines + 2
	line = random.randint(1,asklines)
	if line <= 5:
		line = random.randint(1,900)
		word = linecache.getline("2425list.txt",line).rstrip()
	else:
		line = random.randint(1,asklines)
		word = linecache.getline("asklist.txt",line).rstrip()
	if word == "":
		getword()
def askword():
	global guess
	gttsobj = gTTS(text=word,lang='en',slow=False)
	gttsobj.save('output.mp3')
	subprocess.run(["play","output.mp3","-q"])
	guess = input ("Type this word> ")
	if guess == "quit":
		subprocess.run(["clear"])
		quit()
def quiz():
	tries = 0
	getword()
	askword()
	while guess != word:
		subprocess.run(["clear"])
		print ("No, try again.")
		tries = tries+1
		speed = 1
		with open("asklist.txt","a") as asklist:
			asklist.write("\n"+word)
		if tries >= 2:
			print ('Hint - '+ word)
		askword()
	else:
		subprocess.run(["clear"])
		print ("Correct!")
		speed = 0
		if tries < 1:
			with open("asklist.txt", "r+") as addword:
				read = addword.readlines()
				addword.seek(0)
				for i in read:
					if i.strip("\n") != word:
						addword.write(i)
				addword.truncate()
print ("Welcome to the Interactive Spelling Quizzer, made by Jacob Gilbert!")
print ("Type quit at any time to get out of this program.")
ready = input("Hit enter to begin!")
subprocess.run(["clear"])
while True:
	quiz()
