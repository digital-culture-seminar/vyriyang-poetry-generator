#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 20:10:06 2018

@author: Vyri
"""

#
import random
#
#
#random.seed()
#
## whitespace
#i = random.randint(1,10)
#whitespace = " " * i
#print whitespace+ "Hello word!"

names = ["spiderman","iron man","hulk","black widow",
         "captain america","loki","thor","hawkeye","scarlet witch","falcon",
         "winter soldier","vision"]
pronouns = ["he", "she","it"]


## indexing list
#print pronouns[1]

name_1 = random.choice(names)
pronoun = random.choice(pronouns)
name_2 = random.choice(names)

#print pronoun.capitalize() + " " + name_1
#
#name_1 = random.choice(names)
#pronoun = random.choice(pronouns)
#name_2 = random.choice(names)

# print the opening lines of the story
#print "One spring afternoon \
#the superhero {name_1} saved NYC. \
#{pronoun} went to eat {name_2} after the battle".format(name_1=name_1,
#name_2=name_2, pronoun=pronoun.capitalize())


diceRoll = random.randint(1,6)
print "{name_1} rolled a {diceRoll}".format(name_1=name_1.capitalize(),
       diceRoll=diceRoll)

#
#if diceRoll == 1:
#    print "Success! " + pronoun + " rolled a " + str(diceRoll)
#    print "Success! {pronoun} rolled a {diceRoll}.".format(pronoun=pronoun,
#                    diceRoll=diceRoll)

if diceRoll == 1:
    print "Bad luck!"
    
#if diceRoll == 1:
#    print "Good luck!"
    
elif diceRoll == 6:
    print "Good luck!"

else:
    print "Not so bad luck..."







