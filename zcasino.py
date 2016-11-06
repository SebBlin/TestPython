#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# * Program de test

from random import randrange

def tirage():
	nombre = randrange(0,50)
	return nombre
	
def calcgain(guess, somme, res):
	gain = 0
	couleur_noir_guess  = not(bool(guess%2))
	couleur_noir_re = not(bool(res%2))
	print ("la boule est noire ", couleur_noir_re )
	
	if guess == res:
		gain = somme*3
	else:
		if couleur_noir_guess == couleur_noir_re:
			print("même couleur ")
			gain = somme / 2
		else:
			print("différente couleur ")
			
	return gain

def pause():
    programPause = input("Press the <ENTER> key to continue...")
	

#début
argent = 100
while argent>0:
	nombre_tire = tirage()
	print ("vous avez tiré le nombre ",nombre_tire,".",sep='')
	
	pari = 12
	if argent < pari:
		break
	argent -= pari
	gain = calcgain(10,pari,nombre_tire)
	print ("vous avez parié", pari, "et gangné",gain)
	if gain > 0:
		print("\targent",argent)
		argent += pari
		print("\targent",argent)
		argent += gain
	print ("\t\til vous reste", argent,"\n")	
	#pause()
	


	
