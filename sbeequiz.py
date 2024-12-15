import subprocess
import random
import linecache
from gtts import gTTS
from datetime import datetime
global asklines
global speed
speed = 0
date = datetime.today().strftime("%Y%m%d")
subprocess.run(["clear"])
def getword():
	global word
	global line
	with open("sbasklist.txt", "r+") as getlines:
		asklines = sum(1 for _ in getlines)
	if asklines < 1:
		asklines = asklines + 2
	line = random.randint(1,asklines)
	if line <= 5:
		line = random.randint(1,450)
		word = linecache.getline("sbeelist.txt",line).rstrip()
	else:
		line = random.randint(1,asklines)
		word = linecache.getline("sbasklist.txt",line).rstrip()
	if word == "":
		getword()
def askword():
	global guess
	gttsobj = gTTS(text=word,lang='en',slow=speed)
	gttsobj.save('sboutput.mp3')
	subprocess.run(["play","sboutput.mp3","-q"])
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
		with open("sbasklist.txt","a") as asklist:
			asklist.write("\n"+word)
		if tries >= 2:
			print ('Hint - '+ word)
		askword()
	else:
		subprocess.run(["clear"])
		print ("Correct!")
		speed = 0
		if tries < 1:
			with open("sbasklist.txt", "r+") as addword:
				read = addword.readlines()
				addword.seek(0)
				for i in read:
					if i.strip("\n") != word:
						addword.write(i)
				addword.truncate()
print ("You are now studying the 2024-2025 School Spelling Bee Study List.")
print ("Type quit at any time to get out of this program.")
ready = input("Hit enter to begin!")
subprocess.run(["clear"])
#print (date)
while True:
	quiz()
