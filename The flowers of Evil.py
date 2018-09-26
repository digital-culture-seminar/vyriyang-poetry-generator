#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:51:19 2018

@author: Vyri
"""

import random

# list of nouns
basicNouns = ["muse","monk"]
positiveNouns = ["death"]
negativeNouns = ["birth"]

pronouns = ["I","he","she","it"]


# list of verbs
verbs = ["love","fling",""]

# list of adjectives
adjectives = ["spiritual"]

# list of positiveAdjectives
positiveAdjectives = ["gold","warm",]

# list of negativeAdjectives
negativeAdjectives = ["venal",]

# list of adverbs
adverbs = ["former"]

# list of positiveAdverbs
positiveAdverbs = ["cheerful"]

# list of negativeAdverbs
negativeAdverbs = ["sick","venal","wretched",]

# list of color
warmColors = ["red","purple",""]
coldColors = ["blue","green",]
cheerfulColors = [""]
sadColors = ["gray"]



# list of timeRalted
# list of month
monthes = ["January","February", "March", "April", "May", "June", "July",
           "August", "September", "October", "November", "December"]

# list of day
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", 
        "Saturday", "Sunday"]

times = ["breaking dawn","twilight","morning","noon","afternoon",
         "evening","night","midhignt"]

seasons = ["spring","summer","autumn","winter"]

# list of humanRalted 
# list of human
humans = ["man","woman","child","men","womem","children"]

# list of bodypart
bodyparts = ["head","neck","shoulders","arm","wrist","hand"]


# list of animalRalted
# list of animal
animals = ["cat","dog","rabbit","owl"]
animalsY = [""]

#list of placeRalted
countries = [""]
cities = [""]
locations = [""]
houses = ["bedroom","living room","Balcony","bathroom","kitchen"]

# list of nature
# list of earth
earths = ["sun","star","noon","cloud","rain","wind","mist"]

weathers = ["sunny","cloudy","raining","windy"]

# list of plant
# list of greenery
greeneries = ["tree"]

# list of flower
flowers = ["rose"]

# list of outspace
outspaces = [""]

# lisy of religion
religions = [""]


# list of journey
travels = ["voyage","range", "flight", "passage"]







random.seed()
basicNoun = random.choice(basicNouns)
positiveNoun = random.choice(positiveNouns)
negativeNoun = random.choice(negativeNouns)
pronoun = random.choice(pronouns)
verb = random.choice(verbs)
adjective = random.choice(adjectives)
positiveAdjective = random.choice(positiveAdjectives)
negativeAdjective = random.choice(negativeAdjectives)
adverb = random.choice(adverbs)
positiveAdverb = random.choice(positiveAdverbs)
negativeAdverb = random.choice(negativeAdverbs)

#random color
warmColor = random.choice(warmColors)
coldColor = random.choice(coldColors)
cheerfulColor = random.choice(cheerfulColors)
sadColor = random.choice(sadColors)

colors = [warmColor, coldColor,cheerfulColor,sadColor]
color = random.choice(colors)

#timeRalted
month = random.choice(monthes)
day = random.choice(days)
time = random.choice(times)
season = random.choice(seasons)

timeRalteds = [month, day, time]
timeRalted = random.choice(timeRalteds)

#random humanRalted
human = random.choice(humans)
bodypart = random.choice(bodyparts)

#random animalRalted
animal = random.choice(animals)
animalY = random.choice(animalsY)

#random placeRalted
country = random.choice(countries)
city = random.choice(cities)
location = random.choice(locations)
house = random.choice(houses) 


earth = random.choice(earths)
weather = random.choice(weathers)
greenery = random.choice(greeneries)
flower = random.choice(flowers)
outspace = random.choice(outspaces)
religion = random.choice(religions)
travel = random.choice(travels)

 

#seek the whole category

singleAndPlurals = ["s",""]
singleAndPluralsY = ["ies","y"]
singleAndPlural = random.choice(singleAndPlurals)
singleAndPluralY = random.choice(singleAndPluralsY)

subject1s = [basicNoun, animal, bodypart,house,weather]
subject1 = random.choice(subject1s)




allAdjectives = [adjective, positiveAdjective, negativeAdjective]
allAdjective = random.choice(allAdjectives)

#seek the title
theTitles = ["title1","title2","title3","title4"]

theTitle = random.choice(theTitles)

if (theTitle == "title1"):
    if (subject1 == animal):
        str = "{subject1}s".format(subject1=subject1)
       
    else:
        str = "{subject1}".format(subject1=subject1)
        

    
elif (theTitle == "title2"):
    titleType2s = ["a","the"]
    titleType2 = random.choice(titleType2s)
    str = "{titleType2} {subject1}".format(subject1=subject1,
           titleType2=titleType2)
    
    
elif (theTitle == "title3"):
    titleType3s = ["a","the"]
    titleType3 = random.choice(titleType3s)
    str = "{titleType3} {allAdjective} {subject1}".format(subject1=subject1,
           titleType3=titleType3, allAdjective=allAdjective)
   
    
elif (theTitle == "title4"):
    subjectTitle4s = [human, basicNoun, animal, bodypart, house, weather]
    subjectTitle4 = random.choice(subjectTitle4s)
    if (subjectTitle4 == human):
        str = "{human} and {subject1}{singleAndPlural}".format(subject1=subject1,
           human=human, singleAndPlural=singleAndPlural)
       
    else:
        str = "{subjectTitle4} and {subject1}{singleAndPlural}".format(subject1=subject1,
           subjectTitle4=subjectTitle4, singleAndPlural=singleAndPlural)

print(str.title())
       
        
        
        



# paragraph test       


        
        
        
    
    
























