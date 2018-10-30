#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:51:19 2018

@author: Vyri
"""

import random

# list of nouns
basicNouns = ["muse","monk","vampire","jewels","log","crowd","monastery",
              "graveyard", "studio","misery","shroud","tomb","flatness",
              "chill","course","weather-cock","wings","queen","king","shades",
              "daring","grief","recollection","wisps","alert","rust",
              "soldier","watchman","spirit","emptiness", "voice","urn","waves"]
pNouns = ["praise","sweet"]
nNouns = ["graveyard","shroud","tomb"]
adjNouns = ["simplicity","delight"]
basicObjectives = ["log","glass","vaults","censer","spectacle"]
basicObjectiveAs = ["altar","amusement"]
positiveNouns = ["birth"]
negativeNouns = ["death","poison","stupefaction","dead"]

pronouns = ["I","we","they","you","he","she","it"]
pronounSingles = ["he","she","it"]
pronounNaturals = ["I","we","they","you"]
pronoun1s = ["my","our","their","your","his","her","its"]
pronoun2s = ["me","us","them","you","him","she","it"]
pronoun3s = ["myself", "ourselves","themselves", "yourself","yourselves",
             "hisself","herself","itself"]

# list of verbs
verbs = ["love","fling","flash","slip","glean","chant","assign","labour",
         "fly","face","swirl","repeat","chant","fill","spill"]
positiveVerbs = ["love","ennoble","praise","raise"]
negativeVerbs = ["slip","fall","chill"]

verbings = ["swing","warming","taking","living","enveloping","growing",
            "chilling"]

verbeds = ["steeped", "cracked","said","stacked"]

# list of adjectives
adjectives = ["spiritual","misty","meager","vulgar","chill","hoarse","tepid",
              "blankest","continuous","pale","daring","bittersweet","old",
              "flickering","dignified","alert",]

# list of positiveAdjectives
positiveAdjectives = ["gold","warm","steadfast","great"]

# list of negativeAdjectives
negativeAdjectives = ["venal","slothful","mud-soaked","funereal","weakening",
                      "bloody"]

# list of adverbs
adverbs = ["former","faithfully","often"]

# list of positiveAdverbs
positiveAdverbs = ["cheerful"]

# list of negativeAdverbs
negativeAdverbs = ["sick","venal","wretched","bored"]

# list of orientationPreposition
orientationPrepositions = ["outside","inside","under","on","below","over","up",
                           "down","beside"]
prepositions = ["despite"]
prepositionNouns = ["inner","outer"]

conjunctions = ["though"]


# list of color
warmColors = ["red","purple"]
coldColors = ["blue","green"]
cheerfulColors = ["azure"]
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

seasons = ["spring","summer","autumn","winter","springtime","summertime",
           "autumntime","wintertime","season"]

# list of humanRalted 
# list of human
humans = ["man","woman","child","men","womem","children"]

# list of bodypart
bodyparts = ["head","neck","shoulders","wrist","hand","belly","breast",
             "face"]
bodypartAs = ["arm","eye"]



# list of animalRalted
# list of animal
animals = ["cat","monkey","dog","rabbit","raven"]
animalAs = ["owl"]
animalYs = [""]

#list of placeRalted
countries = [""]
cities = [""]
locations = [""]
houses = ["bedroom","living room","balcony","bathroom","kitchen","window","door",
          "sink","wall","hall","graveyard","studio","pool"]
rooms = ["bed","desk","lamp","light"]


# list of nature
# list of earth
earths = ["sun","star","noon","cloud","rain","wind","mist","moonbeam","sky",
          "frost"]

weathers = ["sunny","cloudy","raining","windy","flash"]

# list of plant
# list of greenery
greeneries = ["tree"]

# list of flower
flowers = ["rose"]

# list of outspace
outspaces = [""]

# lisy of religion
religions = ["religion"]


# list of journey
travels = ["voyage","range", "flight", "passage"]

# list of food
foods = ["bread"]

# list of stuff
stuffs = ["vapours","fire"]







random.seed()
#random nouns
basicNoun = random.choice(basicNouns)
pNoun = random.choice(pNouns)
nNoun = random.choice(nNouns)
adjNoun = random.choice(adjNouns)
basicObjective = random.choice(basicObjectives)
basicObjectiveA = random.choice(basicObjectiveAs)

allBasicObjectives =[basicObjective,basicObjectiveA]
allBasicObjective = random.choice(allBasicObjectives)


positiveNoun = random.choice(positiveNouns)
negativeNoun = random.choice(negativeNouns)

#random pronoun
pronoun = random.choice(pronouns)
pronounSingle = random.choice(pronounSingles)
pronounNatural = random.choice(pronounNaturals)
pronoun1 = random.choice(pronoun1s)
pronoun2 = random.choice(pronoun2s)
pronoun3 = random.choice(pronoun3s)


#random verb
verb = random.choice(verbs)
positiveVerb = random.choice(positiveVerbs)
negativeVerb = random.choice(negativeVerbs)

allVerbs = [verb, positiveVerb, negativeVerb]
allVerb = random.choice(allVerbs)

verbing = random.choice(verbings)

verbed = random.choice(verbeds)

#random adjective
adjective = random.choice(adjectives)
positiveAdjective = random.choice(positiveAdjectives)
negativeAdjective = random.choice(negativeAdjectives)

allAdjectives = [adjective, positiveAdjective, negativeAdjective]
allAdjective = random.choice(adjectives)

#random adverb
adverb = random.choice(adverbs)
positiveAdverb = random.choice(positiveAdverbs)
negativeAdverb = random.choice(negativeAdverbs)

adverbss = [adverb, positiveAdverb, negativeAdverb]
adverbs = random.choice(adverbss)

#random orientationPreposition 
orientationPreposition = random.choice(orientationPrepositions)
preposition = random.choice(prepositions)
prepositionNoun = random.choice(prepositionNouns)
conjunction = random.choice(conjunctions)


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
bodypartA = random.choice(bodypartAs)

allBodyparts = [bodypart, bodypartA]
allBodypart = random.choice(allBodyparts) 

#random animalRalted
animal = random.choice(animals)
animalA = random.choice(animalAs)
animalY = random.choice(animalYs)

allAnimals = [animal, animalA]
allAnimal = random.choice(allAnimals)

#random placeRalted
country = random.choice(countries)
city = random.choice(cities)
location = random.choice(locations)
house = random.choice(houses) 
room = random.choice(rooms)

earth = random.choice(earths)
weather = random.choice(weathers)
greenery = random.choice(greeneries)
flower = random.choice(flowers)
outspace = random.choice(outspaces)
religion = random.choice(religions)
travel = random.choice(travels)
food = random.choice(foods)
stuff = random.choice(stuffs)










 

#seek the whole category

singleAndPlurals = ["s",""]
singleAndPluralsY = ["ies","y"]
singleAndPlural = random.choice(singleAndPlurals)
singleAndPluralY = random.choice(singleAndPluralsY)



subject1s = [basicNoun, basicObjective, basicObjectiveA, 
             animal, animalA, bodypart, bodypartA,
             house,weather]
subject1 = random.choice(subject1s)






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
    if (titleType2 == "a"):
        if (subject1 == animalA):
            str = "an {subject1}".format(subject1=subject1)
        elif (subject1 == bodypartA):
            str = "an {subject1}".format(subject1=subject1)
        elif (subject1 == basicObjectiveA):
            str = "an {subject1}".format(subject1=subject1)
        else:
            str = "{titleType2} {subject1}".format(subject1=subject1,
                   titleType2=titleType2)
    else:
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


       
       
   

# paragraph related to the title       
class TitleParagraphFormat():
    def form1(self):
        pronoun = random.choice(pronouns)
        str = "Will {pronoun}, when {month} {verb} {pronoun1} {weather}".format(pronoun=pronoun, 
                    month=month, verb=verb, pronoun1=pronoun1,weather=weather)
        return(str)
        
    def form2(self):
        verb = random.choice(verbs)
        basicObjective = random.choice(basicObjectives)
        str = "{verb} {adjective} {basicObjective} to \
{positiveAdjective} {pronoun1} {color} {bodypart}".format(verb=verb.capitalize(), adjective=adjective,
        basicObjective=basicObjective, positiveAdjective=positiveAdjective,
        pronoun1=pronoun1,color=color,bodypart=bodypart)
        return(str)
        

        
    def form3(self):
        verb = random.choice(verbs)
        str = "{pronoun1} {adjective} {bodypart}, will {pronoun} {verb} \
to {positiveAdjective}".format(pronoun1=pronoun1.capitalize(), adjective=adjective, bodypart=bodypart,
        pronoun=pronoun, verb=verb, positiveAdjective=positiveAdjective)
        return(str)
        
        
    def form4(self):
        pronoun1 = random.choice(pronoun1s)
        verb = random.choice(verbs)
        str = "As {weather} {verb} {orientationPreposition} {pronoun1} \
{house} {basicNoun}".format(weather=weather,
        verb=verb,orientationPreposition=orientationPreposition,
        pronoun1=pronoun1,house=house,basicNoun=basicNoun)
        return(str)
        
    def form5(self):
        pronoun1 = random.choice(pronoun1s)
        str = "Knowing {pronoun1} {basicObjective} and {positiveNoun} both \
are {negativeNoun}".format(pronoun1=pronoun1,basicObjective=basicObjective,
        positiveNoun=positiveNoun,negativeNoun=negativeNoun)
        return(str)
        
    def form6(self):
        basicNoun = random.choice(basicNouns)
        verb = random.choice(verbs)
        str = "Will {pronoun} {verb} {warmColor} out of the \
{cheerfulColor} {basicNoun}".format(pronoun=pronoun,verb=verb,warmColor=warmColor,
        cheerfulColor=cheerfulColor,basicNoun=basicNoun)
        return(str)
        
    def form7(self):
        pronoun = random.choice(pronouns)
        verb = random.choice(verbs)
        pronoun1 = random.choice(pronoun1s)
        adjective = random.choice(adjectives)
        str = "{pronoun} must, to {verb} {pronoun1} {adjective} \
{time} {food}".format(pronoun=pronoun.capitalize(),verb=verb,pronoun1=pronoun1,
        adjective=adjective,time=time,food=food)
        return(str)
        
    def form8(self):
        verb = random.choice(verbs)
        negativeAdverb = random.choice(negativeAdverbs)
        verbing = random.choice(verbings)
        negativeVerb = random.choice(negativeVerbs)
        str = "{verb} a {negativeAdverb} {basicNoun} {verbing} \
{basicObjective}, {negativeVerb}".format(verb=verb.capitalize(),
        negativeAdverb=negativeAdverb,basicNoun=basicNoun,verbing=verbing,
        basicObjective=basicObjective,negativeVerb=negativeVerb)
        return(str)
        
    def form9(self):
        allVerb = random.choice(allVerbs)
        negativeAdjective = random.choice(negativeAdjectives)
        str = "To {allVerb} {basicObjective} to the \
{negativeAdjective} {basicNoun}".format(allVerb=allVerb, basicObjective=basicObjective,
        negativeAdjective=negativeAdjective, basicNoun=basicNoun)
        return(str)
        
    def form10(self):
        allAdjective = random.choice(allAdjectives)
        basicNoun = random.choice(basicNouns)
        orientationPreposition = random.choice(orientationPrepositions)
        positiveAdjective = random.choice(positiveAdjectives)
        house = random.choice(houses)
        str = "{allAdjective} {basicNoun} {orientationPreposition} \
{positiveAdjective} {house}".format(allAdjective=allAdjective.capitalize(),
        basicNoun=basicNoun,orientationPreposition=orientationPreposition,
        positiveAdjective=positiveAdjective,house=house)
        return(str)
        
    def form11(self):
        verbing = random.choice(verbings)
        prepositionNoun = random.choice(prepositionNouns)
        negativeAdjective =random.choice(negativeAdjectives)
        house = random.choice(houses)
        str = "{verbing} the {prepositionNoun} {human} in this \
{negativeAdjective} {house}".format(verbing=verbing.capitalize(),
        prepositionNoun=prepositionNoun,human=human,
        negativeAdjective=negativeAdjective,
        house=house)
        return(str)
        
    def form12(self):
        verbing = random.choice(verbings)
        basicNoun = random.choice(basicNouns)
        pronoun1 = random.choice(pronoun1s)
        house = random.choice(houses)
        str = "{verbing} the {basicNoun} as \
{pronoun1} {house}".format(verbing=verbing.capitalize(),basicNoun=basicNoun,
        pronoun1=pronoun1,house=house)
        return(str)
        
    def form13(self):
        positiveVerb = random.choice(positiveVerbs)
        negativeNoun = random.choice(negativeNouns)
        adjNoun = random.choice(adjNouns)
        str = "{positiveVerb} {negativeNoun}, in \
all {adjNoun}".format(positiveVerb=positiveVerb.capitalize(), 
        negativeNoun=negativeNoun,adjNoun=adjNoun)
        return(str)
        
    def form14(self):
        negativeAdjective = random.choice(negativeAdjectives)
        verb = random.choice(verbs)
        str = "O {negativeAdjective} {basicNoun}! \
Oh, when may I {verb}".format(negativeAdjective=negativeAdjective,
        basicNoun=basicNoun, verb=verb)
        return(str)
        
    def form15(self):
        verbing = random.choice(verbings)
        basicObjective = random.choice(basicObjectives)
        basicNoun = random.choice(basicNouns)
        str = "This {verbing} {basicObjective} \
of {basicNoun}".format(verbing=verbing,
                    basicObjective=basicObjective, basicNoun=basicNoun)
        return(str)
        
    def form16(self):
        verb = random.choice(verbs)
        allBodypart = random.choice(allBodyparts)
        bodypartA = random.choice(bodypartAs)
        adjNoun = random.choice(adjNouns)
        str = "To {verb} of my {allBodypart}, my \
{bodypartA}'s {adjNoun}".format(verb=verb,allBodypart=allBodypart,
        bodypartA=bodypartA, adjNoun=adjNoun)
        return(str)




# random paragraph 
class ParagraphFormat():
    def form1(self):
        season = random.choice(seasons)
        month = random.choice(monthes)
        negativeAdjective = random.choice(negativeAdjectives)
        time = random.choice(times)
        str = "{season}'s last days, {month} and {negativeAdjective} \
{time}".format(season=season.capitalize(),month=month,negativeAdjective=negativeAdjective,
        time=time)
        return(str)
       
    def form2(self):
        pronounNatural = random.choice(pronounNaturals)
        positiveVerb = random.choice(positiveVerbs)
        negativeNoun = random.choice(negativeNouns)
        pronounSingle = random.choice(pronounSingles)
        negativeVerb = random.choice(negativeVerbs)
        str = "{pronounNatural} {positiveVerb} the {negativeNoun} \
that {pronounSingle} {negativeVerb}s".format(pronounNatural=pronounNatural.capitalize(),
        positiveVerb=positiveVerb,negativeNoun=negativeNoun,pronounSingle=pronounSingle,
        negativeVerb=negativeVerb)
        return(str)       
        
    def form3(self):
        verbing = random.choice(verbings)
        pronoun1 = random.choice(pronoun1s)
        bodypart = random.choice(bodyparts)
        bodypartA = random.choice(bodypartAs)
        str = "By so {verbing} {pronoun1} {bodypart} and \
{bodypartA}".format(verbing=verbing, pronoun1=pronoun1,
        bodypart=bodypart,bodypartA=bodypartA)
        return(str)
        
    def form4(self):
        basicNoun = random.choice(basicNouns)
        stuff = random.choice(stuffs)
        nNoun = random.choice(nNouns)
        earth = random.choice(earths)
        greenery = random.choice(greeneries)
        str = "In {basicNoun} of {stuff}, {nNoun} of {earth} and \
{greenery}".format(basicNoun=basicNoun,stuff=stuff,nNoun=nNoun,
        earth=earth,greenery=greenery)
        return(str)
        
    def form5(self):
        positiveAdjective = random.choice(positiveAdjectives)
        basicNoun = random.choice(basicNouns)
        adjective = random.choice(adjectives)
        earth = random.choice(earths)
        str = "In this {positiveAdjective} {basicNoun} where the \
{adjective} {earth} course".format(positiveAdjective=positiveAdjective,
        basicNoun=basicNoun,adjective=adjective,earth=earth)
        return(str)
        
    def form6(self):
        time = random.choice(times)
        basicNoun = random.choice(basicNouns)
        verbing = random.choice(verbings)
        adjective = random.choice(adjectives)
        str = "Where through the {time} the {basicNoun} is {verbing} \
{adjective} ".format(time=time,basicNoun=basicNoun,verbing=verbing,
        adjective=adjective)
        return(str)
        
    def form7(self):
        pronoun1 = random.choice(pronoun1s)
        basicNoun = random.choice(basicNouns)
        season = random.choice(seasons)
        adjective = random.choice(adjectives)
        earth = random.choice(earths)
        str = "{pronoun1} {basicNoun}, more than in {season}'s \
{adjective} {earth}".format(pronoun1=pronoun1.capitalize(),
        basicNoun=basicNoun,season=season,adjective=adjective,
        earth=earth)
        return(str)
        
    def form8(self):
        verb = random.choice(verbs)
        pronoun1 = random.choice(pronoun1s)
        animal = random.choice(animals)
        basicNoun = random.choice(basicNouns)
        negativeVerb = random.choice(negativeVerbs)
        str = "Will {verb} {pronoun1} {animal}'s {basicNoun} to \
{negativeVerb}".format(verb=verb,pronoun1=pronoun1,animal=animal,
        basicNoun=basicNoun,negativeVerb=negativeVerb)
        return(str)
        
    def form9(self):
        adjective = random.choice(adjectives)
        season = random.choice(seasons)
        basicNoun = random.choice(basicNouns)
        pronoun1 = random.choice(pronoun1s)
        pNoun = random.choice(pNouns)
        str = "O {adjective} {season}, {basicNoun} of all \
{pronoun1} {pNoun}".format(adjective=adjective,season=season,
        basicNoun=basicNoun,pronoun1=pronoun1,pNoun=pNoun)
        return(str)
        
    def form10(self):
        pNoun = random.choice(pNouns)
        negativeAdjective = random.choice(negativeAdjectives)
        bodypart = random.choice(bodyparts)
        str = "Nothing is {pNoun} to the {negativeAdjective} \
{bodypart}".format(pNoun=pNoun,negativeAdjective=negativeAdjective,
        bodypart=bodypart)
        return(str)
        
    def form11(self):
        verbed = random.choice(verbeds)
        earth = random.choice(earths)
        house = random.choice(houses)
        str = "That has been {verbed} in {earth} and \
{house}".format(verbed=verbed,earth=earth,house=house)
        return(str)
        
    def form12(self):
        adjective = random.choice(adjectives)
        bodypart = random.choice(bodyparts)
        pronoun1 = random.choice(pronoun1s)
        negativeAdjective = random.choice(negativeAdjectives)
        basicNoun = random.choice(basicNouns)
        str = "But the {adjective} {bodypart} of {pronoun1} \
{negativeAdjective} {basicNoun}".format(adjective=adjective,bodypart=bodypart,
        pronoun1=pronoun1,negativeAdjective=negativeAdjective,
        basicNoun=basicNoun)
        return(str)
        
    def form13(self):
        basicNoun = random.choice(basicNouns)
        room = random.choice(rooms)
        verb = random.choice(verbs)
        pronoun1 = random.choice(pronoun1s)
        nNoun = random.choice(nNouns)
        positiveVerb = random.choice(positiveVerbs)
        str = "{basicNoun} in {room} to {verb} {pronoun1} \
{nNoun} to {positiveVerb}".format(basicNoun=basicNoun.capitalize(), room=room,
        verb=verb, pronoun1=pronoun1, nNoun=nNoun, positiveVerb=positiveVerb)
        return(str)
        
    def form14(self):
        adjective = random.choice(adjectives)
        season = random.choice(seasons)
        time = random.choice(times)
        str = "How {adjective} it is on {season} \
{time}".format(adjective=adjective,season=season,time=time)
        return(str)
        
    def form15(self):
        verb = random.choice(verbs)
        adjective = random.choice(adjectives)
        basicNoun = random.choice(basicNouns)
        positiveVerb = random.choice(positiveVerbs)
        pronoun3 = random.choice(pronoun3s)
        str = "To {verb} {adjective} {basicNoun} \
{positiveVerb} {pronoun3}".format(verb=verb,adjective=adjective,
        basicNoun=basicNoun,positiveVerb=positiveVerb,pronoun3=pronoun3)
        return(str)
        
    def form16(self):
        adjective = random.choice(adjectives)
        stuff = random.choice(stuffs)
        basicNoun = random.choice(basicNouns)
        room = random.choice(rooms)
        str = "Around the {adjective} {stuff}'s {basicNoun} of \
{room}".format(adjective=adjective, stuff=stuff,basicNoun=basicNoun,
        room=room)
        return(str)
        
    def form17(self):
        adjective = random.choice(adjectives)
        negativeAdjective = random.choice(negativeAdjectives)
        preposition = random.choice(prepositions)
        pronoun1 = random.choice(pronoun1s)
        basicNoun = random.choice(basicNouns)
        str = "{adjective} and {negativeAdjective} {preposition} \
{pronoun1} {basicNoun}".format(adjective=adjective.capitalize(),
        negativeAdjective=negativeAdjective,preposition=preposition,
        pronoun1=pronoun1,basicNoun=basicNoun)
        return(str)
        
    def form18(self):
        adverb = random.choice(adverbs)
        verb = random.choice(verbs)
        religion = random.choice(religions)
        basicNoun = random.choice(basicNouns)
        str = "Who {adverb} {verb} {religion}'s \
{basicNoun}".format(adverb=adverb,verb=verb,religion=religion,basicNoun=basicNoun)
        return(str)
        
    def form19(self):
        adjective = random.choice(adjectives)
        basicNoun = random.choice(basicNouns)
        verb = random.choice(verbs)
        nNoun = random.choice(nNouns)
        pNoun = random.choice(pNouns)
        str = "As the {adjective} {basicNoun} {verb} a \
{nNoun}'s {pNoun}".format(adjective=adjective,basicNoun=basicNoun,
        verb=verb,nNoun=nNoun,pNoun=pNoun)
        return(str)
        
    def form20(self):
        pronoun1 = random.choice(pronoun1s)
        basicNoun = random.choice(basicNouns)
        conjunction = random.choice(conjunctions)
        verbed = random.choice(verbeds)
        pronounSingle = random.choice(pronounSingles)
        str = "{pronoun1} {basicNoun}, {conjunction}, is {verbed}; \
when as {pronounSingle} can".format(pronoun1=pronoun1.capitalize(),basicNoun=basicNoun,
        conjunction=conjunction,verbed=verbed,pronounSingle=pronounSingle)
        return(str)
        
    def form21(self):
        pronounNatural = random.choice(pronounNaturals)
        verb = random.choice(verbs)
        negativeVerb = random.choice(negativeVerbs)
        adjective = random.choice(adjectives)
        time = random.choice(times)
        basicNoun = random.choice(basicNouns)
        str = "{pronounNatural} {verb} to {negativeVerb} the \
{adjective} {time}'s {basicNoun}".format(pronounNatural=pronounNatural.capitalize(),
        verb=verb,negativeVerb=negativeVerb,adjective=adjective,time=time,
        basicNoun=basicNoun)
        return(str)
        
    def form22(self):
        adverb = random.choice(adverbs)
        pronoun1 = random.choice(pronoun1s)
        negativeAdjective = random.choice(negativeAdjectives)
        basicNoun = random.choice(basicNouns)
        verbed = random.choice(verbeds)
        str = "Too {adverb} can {pronoun1} {negativeAdjective} \
{basicNoun} be {verbed}".format(adverb=adverb,pronoun1=pronoun1,
        negativeAdjective=negativeAdjective,
        basicNoun=basicNoun, verbed=verbed)
        return(str)
        
    def form23(self):
        orientationPreposition = random.choice(orientationPrepositions)
        negativeAdjective = random.choice(negativeAdjectives)
        house = random.choice(houses)
        verbed = random.choice(verbeds)
        negativeNoun = random.choice(negativeNouns)
        str = "{orientationPreposition} a {negativeAdjective} \
{house}, {verbed} with the {negativeNoun}".format(orientationPreposition=orientationPreposition.capitalize(),
        negativeAdjective=negativeAdjective,house=house,verbed=verbed,
        negativeNoun=negativeNoun)
        return(str)
        
    def form24(self):
        verb = random.choice(verbs)
        pronoun1 = random.choice(pronoun1s)
        basicNoun = random.choice(basicNouns)
        positiveAdjective = random.choice(positiveAdjectives)
        nNoun = random.choice(nNouns)
        verbing = random.choice(verbings)
        earth = random.choice(earths)
        str = "{verb} from {pronoun1} {basicNoun} \
{positiveAdjective} {nNoun} of {verbing} \
{earth}".format(verb=verb.capitalize(),pronoun1=pronoun1,
        basicNoun=basicNoun,positiveAdjective=positiveAdjective,
        nNoun=nNoun,verbing=verbing,earth=earth)
        return(str)
        
        




# motion paragraph
        
        
        

# algorithm final form
        
T = TitleParagraphFormat()
P = ParagraphFormat()
    
forms1 = [T.form1(),T.form2(),T.form3(),T.form4(),T.form5(),T.form6(),
         T.form7(),T.form8(),T.form9(),T.form10(),T.form11(),T.form12(),
         T.form13(),T.form14(),T.form15(),T.form16()]

forms2 = [P.form1(),P.form2(),P.form3(),P.form4(),P.form5(),P.form6(),
         P.form7(),P.form8(),P.form9(),P.form10(),P.form11(),P.form12(),
         P.form13(),P.form14(),P.form15(),P.form16(),P.form17(),P.form18(),
         P.form19(),P.form20(),P.form21(),P.form22(),P.form23(),P.form24()]


resultList1 = random.sample(forms1,7)
resultList2 = random.sample(forms2,20)

resultLists = []
resultLists.extend(resultList1)
resultLists.extend(resultList2)


slice = random.sample(resultLists,14)
random.shuffle(slice)




# print out md
with open("The_flowers_of_Evil.md","w") as f:
    
    title = (str.title())
    f.write("## " + title + "\n")

    i = 0
    print 
    for sentence in slice:

        i = i + 1
        if (i<4):
            space = "\n"*1
        if (i==4):
            space = "\n"*2
        if (4<i<8):
            space = "\n"*1
        if (i==8):
            space = "\n"*2
        if (8<i<11):
            space = "\n"*1
        if (i==11):
            space = "\n"*2
        if (11<i<14):
            space = "\n"*1
        if (i==14):
            space = "\n"*1
            
        poem = " "+" "+" "+" "+(sentence) + space
            
        f.write(poem)
        
        
# for reading        
with open("The_flowers_of_Evil_Read.md","w") as r:
    
    title = (str.title())
    r.write(title+"\n"+"\n")
    
    i = 0
    print 
    for sentence in slice:

        i = i + 1
        if (i<4):
            space = "\n"*1
        if (i==4):
            space = "\n"*2
        if (4<i<8):
            space = "\n"*1
        if (i==8):
            space = "\n"*2
        if (8<i<11):
            space = "\n"*1
        if (i==11):
            space = "\n"*2
        if (11<i<14):
            space = "\n"*1
        if (i==14):
            space = "\n"*1
            
        poemR = (sentence) + space
            
        r.write(poemR)


   

    
        
from playsound import playsound
from gtts import gTTS


with open("The_flowers_of_Evil_Read.md") as f:
    poem = f.read()
    
    print poem
    

    
    

    
    
    
tts = gTTS(text=poem,lang="en")

tts.save("The_flowers_of_Evil.mp3")        
    
    
























