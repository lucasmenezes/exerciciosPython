#!/usr/bin/env python

import oi
import random
import string


def fahrenheit_celsius(grau):
	return 'C =', (grau - 32)/1.8

def celsius_fahrenheit(grau):
	return 'F =', grau * 1.8 + 32



#print fahrenheit_celsius(68)
#print celsius_fahrenheit(20)

print oi.digaOi()
print random.choice(string.ascii_uppercase)

