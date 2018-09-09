#!/usr/bin/env python3
"""toothy.py: a text-based telepresence of professor toothy"""

__author__	= "Jack B. Du (Jiadong Du)"
__email__	= "jackbdu@nyu.edu"
__created__	= "Oct. 6, 2015"

class Professor(object):
	
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return "Professor " + self.name

	def introduce(self):
		print("Professor " + self.name + ": I'm Professor " + self.name)

	def say(self, content):
		print("Professor " + self.name + ": " + content)

def main():
	questions = ["Wouldn't you much rather have some delicious juicy lamb chop?", "Speaking of lunch, how about a nice tender lamb chop?"]
	toothy = Professor("Toothy")
	toothy.introduce()
	toothy.say(questions[0])
	while(input().lower() != "yes"):
		toothy.say("Do you wanna some lamb chop?")

	toothy.say("Here you go, eat up that spicy lamb chop!\n")

	toothy.introduce()
	toothy.say(questions[1])
	while(input().lower() != "yes"):
		toothy.say("Do you wanna some lamb chop?")

	toothy.say("Here you go, eat up that spicy lamb chop!")

main()
