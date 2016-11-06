#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# * Program de test
col = 7


class p4:
	def __init__(self):
		self.col = col
		self.row = 6
		self.game = [['-'] * self.row for _ in range(self.col)]
		self.color = ("B","R")
		
	def lignestr(self,li):
		chaine = ''
		for c in range(self.col):
			chaine += '|'
			chaine += self.game[c][li]
		chaine += '|'
		return chaine
	
	def __str__(self):
		chaine = ''
		
		for l in reversed(range(self.row)):
			chaine += str(l+1)
			chaine += self.lignestr(l)
			chaine +='\n'
		chaine += ' '
		for i in range(self.col):
			chaine += '-' + str(i+1)
		chaine += '-'
		return chaine
		
	def testplay(self,col):
		l = 0
		ok = False
		while l<self.row and not(ok):
			if self.game[col-1][l]=='-':
				ok = True
			l += 1
		return ok

	def play(self,color,col):
		l = 0
		ok = False
		col -= 1
		while l<self.row and not(ok):
			if self.game[col][l]=='-':
				ok = True
				self.game[col][l]=color
			l += 1
		return self

	def hasfourdir(self,col,li,pcol,pli):
		colstart = self.game[col][li]
		testcol = col
		testli = li
		count = 1
		hasfourdir = True
		while hasfourdir and count<4:
			hasfourdir &= colstart ==  self.game[col+count*pcol][li+count*pli]
			count += 1
		return hasfourdir
	
	def hasfour(self,col,li):
		colstart = self.game[col][li]
		hasfour = False
		
		if (col>self.col-4) or (li>self.row-4) or (colstart not in self.color):
			return (hasfour,colstart)
		#horizontal
		hasfour = self.hasfourdir(col,li,1,0)
		if (not hasfour):
			#vertical
			hasfour = self.hasfourdir(col,li,0,1)
			if (not hasfour):
				#diagonal
				hasfour = self.hasfourdir(col,li,1,1)
			
		return (hasfour,colstart)
		
	def iswin(self):
		iswin = False
		li = 0
		col = 0
		while (iswin == False) and (li<=self.row-4):
			col = 0
			while (iswin == False) and (col<=self.col-4):
				(iswin,color) = self.hasfour(col,li)
				col += 1
			li += 1
		return (iswin,color)
		
class party:
	def __init__(self):
		self.round=0
		self.p = p4()
		self.player =['H','P']
		self.currentCol='B'
		self.currentplayer='H'
		self.listturn = []
		print ('Init party')
	
	
	def playnext(self,col):
		if self.p.testplay(col):
			self.p.play(self.currentCol,col)
			print (self.round)
			self.listturn.append((col,self.currentCol))
			print ('maliste',self.listturn)
			self.round += 1
			self.currentCol = self.p.color[self.round%2]
			self.currentplayer = self.player[self.round%2]
			
		else:
			print ("error try again !") 
	
	def iswin(self):
		return self.p.iswin()
	