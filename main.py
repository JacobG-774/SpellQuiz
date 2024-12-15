import subprocess
subprocess.run(["clear"])
def getquiz():
	quiz=input("Type which list you want to study, or type help to see all available lists.\n>")
	if quiz == "quit":
		subprocess.run(["clear"])
		quit()
	elif quiz == "help":
		print ("Available quizzes include:\nSchool spelling bee - type schoolbee\nUIL Spelling for the 2024-2025 school year - type 2425uil")
		getquiz()
	elif quiz == "schoolbee":
		import sbeequiz
	elif quiz == "2425uil":
		import uilquiz
	else:
		print ("You did not enter a valid quiz.")
		print ("Available quizzes include:\nSchool spelling bee - type schoolbee\nUIL Spelling for the 2024-2025 school year - type 2425uil")
		getquiz()
print ("Welcome to SpellQuiz, a Python project by Jacob Gilbert!")
print ("Type quit at the word prompt to exit this program.")
getquiz()
