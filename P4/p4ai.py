#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# * Program de test

from random import randrange
from p4game import *

class p4ai:
	def __init__(self,party,mycolor):
		self.score = 0
		self.maxdepth = 5
		self.party = party
		self.color = mycolor
	
	def nextmove(self):
		startNode = node()
		return randrange(7)

	def min(prof,p4):
		(win,wincolor) = p4.iswin()
		if win:
			return self.evaluate(p4,win,wincolor,prof)
		elseif prof >= self.maxdepth:
			return 0
		min_val = 1000
		for i in range(col):
			if p4.testplay(i):
				nextp4 = p4
				nextp4.play(i)
				val = self.max(prof+1,nextp4)
				if val < min_val:
					min_val = val
		return min_val
		
	def max(prof,p4):
		(win,wincolor) = p4.iswin()
		if win:
			return self.evaluate(p4,win,wincolor,prof)
		elseif prof >= self.maxdepth:
			return 0
		max_val = -1000
		for i in range(col):
			if p4.testplay(i):
				nextp4 = p4
				nextp4.play(i)
				val = self.min(prof+1,nextp4)
				if val > max_val:
					max_val = val
		return max_val
		
	def evaluate(p4,win,wincolor,depth):
		if win:
			if wincolor == self.mycolor:
				return 100-depth
			else:
				return -100+depth
		 elif depth >= self.maxdepth:
			return 0
		
		return 0
			
	
	

class node:
	def __init__(self):
		self.parent = None
		self.party = None
		self.evaluation = 0
		self.children = [None]*col
		print (self.children)
	
class liste:
	def __init__(self):
		self.start = node()
		