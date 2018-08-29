#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 19:16:09 2018

@author: Vyri
Description: python text generator
license: 
"""

import random



# list of nouns
nouns = ["spiderman","iron man","hulk","black widow",
         "captain america","loki","thor","hawkeye","scarlet witch","falcon",
         "winter soldier","vision"]


# list of verbs
verbs = ["laughed out loud", "rolled on the floor laughing", 
         "slept", "read", "declaimed", "roared", "glittered"]

# list of adjectives
adjectives = ["giant", "raucous", "playful", "sparkling", "sleepy", 
              "scornful", "arrogant", "stealthy", "mechanical", "magical", 
              "ancient"]

# list of adverbs
adverbs = ["loudly", "silently", "playfully", "sneakily", "proudly", 
           "tearfully", "mindfully", "boldly", "gently", "disdainfully", 
           "daintily", "patiently"]



#i = 0
#for noun in nouns:
#    print nouns[i]
#    i = i + 1

#noun = random.choice(nouns)
#print "{noun}".format (noun=noun)

#noun = random.choice(nouns)
#print noun
#verb = random.choice(verbs)
#print verb
#adjective = random.choice(adjectives)
#print adjective
#adverb = random.choice(adverbs)
#print adverb



random.seed()

noun = random.choice(nouns)
verb = random.choice(verbs)
adjective = random.choice(adjectives)
adverb = random.choice(adverbs)
second_adjective = random.choice(adjectives)


# print a sentence with random words from the lists

print "The" + " " + adjective + " " + second_adjective + " " + noun + \
" " + adverb + " " + verb + " "

print " "

random.seed()
noun = random.choice(nouns)
verb = random.choice(verbs)
adjective = random.choice(adjectives)
adverb = random.choice(adverbs)
second_adjective = random.choice(adjectives)

print "The {adjective} {second_adjective}\
 {noun} {adverb} {verb}.".format(adjective=adjective, 
           second_adjective=second_adjective, noun=noun, adverb=adverb, 
           verb=verb)


print ""


random.shuffle(nouns)

i = 0
print "The"
for noun in nouns:
    i = i + 1
    print noun
print "{adverb} {verb}.".format(adverb=adverb, verb=verb)

print " "


random.shuffle(nouns)

i = 0
print "The"
for noun in nouns:
    i = i + 1
    whitespace = " " * i
    print whitespace + noun
    
print "{adverb} {verb}.".format(adverb=adverb, verb=verb)







    
    







