#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# * Program de test

from p4game import *
from p4ai import *

part = party()
player =['H','P']
ia = p4ai

win = False
(win,wincolor) = (False,'-')
i=0
while (not win) and (i < 6*7-1):
	print ('Turn for', str(part.currentCol),player[i%2])
	if player[i%2]=='H':
		col = int(input("which column ?")) 
	else:
		col = ia.nextmove()
	print ("col :",col )
	part.playnext(int(col))
	print (part.p.hasfour(1,1))
	print (part.p)
	(win,wincolor) = part.iswin()
	print ('Iswin :',win)
	print (i,'\n')
	i += 1

if win:
	print ('!!!!! win !!!!!!!')