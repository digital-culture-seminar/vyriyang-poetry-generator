#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:51:19 2018

@author: Vyri
"""

import random

# list of nouns
basicNouns = ["muse","monk","vampire","jewels","log","crowd","monastery",
              "graveyard", "studio","misery"]
adjNouns = ["simplicity","delight"]
basicObjectives = ["log","glass","vaults","censer","spectacle"]
basicObjectiveAs = ["altar","amusement"]
positiveNouns = ["birth"]
negativeNouns = ["death","poison","stupefaction"]

pronouns = ["I","we","they","you","he","she","it"]
pronounSingles = ["he","she","it"]
pronounNaturals = ["I","we","they","you"]
pronoun1s = ["my","our","their","your","his","her","its"]
pronoun2s = ["me","us","them","you","him","she","it"]

# list of verbs
verbs = ["love","fling","flash","slip","glean","chant","assign","labour"]
positiveVerbs = ["love","ennoble","praise"]
negativeVerbs = ["slip","fall"]

verbings = ["swing","warming","taking","living"]

# list of adjectives
adjectives = ["spiritual","misty","meager","vulgar"]

# list of positiveAdjectives
positiveAdjectives = ["gold","warm","steadfast"]

# list of negativeAdjectives
negativeAdjectives = ["venal","slothful","mud-soaked"]

# list of adverbs
adverbs = ["former"]

# list of positiveAdverbs
positiveAdverbs = ["cheerful"]

# list of negativeAdverbs
negativeAdverbs = ["sick","venal","wretched","bored"]

# list of orientationPreposition
orientationPrepositions = ["outside","inside","under","on","below","over","up",
                           "down"]
prepositionNouns = ["inner","outer"]


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

seasons = ["spring","summer","autumn","winter"]

# list of humanRalted 
# list of human
humans = ["man","woman","child","men","womem","children"]

# list of bodypart
bodyparts = ["head","neck","shoulders","wrist","hand","belly"]
bodypartAs = ["arm","eye"]



# list of animalRalted
# list of animal
animals = ["cat","monkey","dog","rabbit",]
animalAs = ["owl",]
animalYs = [""]

#list of placeRalted
countries = [""]
cities = [""]
locations = [""]
houses = ["bedroom","living room","balcony","bathroom","kitchen","window","door",
          "sink","wall","hall","graveyard","studio"]

# list of nature
# list of earth
earths = ["sun","star","noon","cloud","rain","wind","mist","moonbeam"]

weathers = ["sunny","cloudy","raining","windy","flash"]

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

# list of food
foods = ["bread"]







random.seed()
#random nouns
basicNoun = random.choice(basicNouns)
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



#random verb
verb = random.choice(verbs)
positiveVerb = random.choice(positiveVerbs)
negativeVerb = random.choice(negativeVerbs)

allVerbs = [verb, positiveVerb, negativeVerb]
allVerb = random.choice(allVerbs)

verbing = random.choice(verbings)

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
prepositionNoun = random.choice(prepositionNouns)


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


earth = random.choice(earths)
weather = random.choice(weathers)
greenery = random.choice(greeneries)
flower = random.choice(flowers)
outspace = random.choice(outspaces)
religion = random.choice(religions)
travel = random.choice(travels)
food = random.choice(foods)











 

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
        str = "{pronoun1} {adjective} {bodypart}，will {pronoun} {verb} \
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




# motion paragraph
        
        
        

# algorithm final form
        
T = TitleParagraphFormat()
forms1 = [T.form1(),T.form2(),T.form3(),T.form4(),T.form5(),T.form6(),
         T.form7(),T.form8(),T.form9(),T.form10(),T.form11(),T.form12(),
         T.form13(),T.form14(),T.form15(),T.form16()]




slice = random.sample(forms1,14)
random.shuffle(slice)




# print out
with open("The_flowers_of_Evil.md","w") as f:
    
    title = (str.title())
    f.write("## " + title + "\n")

    i = 0
    print 
    for sentence in slice:
#        i = i + 1
#        if (i<4):
#            space = "\n"*0
#        if (i==4):
#            space = "\n"*1
#        if (4<i<8):
#            space = "\n"*0
#        if (i==8):
#            space = "\n"*1
#        if (8<i<11):
#            space = "\n"*0
#        if (i==11):
#            space = "\n"*1
#        if (11<i<14):
#            space = "\n"*0
#        if (i==14):
#            space = "\n"*0
#        space = "\n"
        i = i + 1
        if (i<4):
            space = "\n"*2
        if (i==4):
            space = "\n"*4
        if (4<i<8):
            space = "\n"*2
        if (i==8):
            space = "\n"*4
        if (8<i<11):
            space = "\n"*2
        if (i==11):
            space = "\n"*4
        if (11<i<14):
            space = "\n"*2
        if (i==14):
            space = "\n"*2
            
        poem = (sentence) + space
            
        f.write(poem)


   
#with open("The_flowers_of_Evil.md","w") as f:
#    f.write("""
### {title}
#···
#{poem}
#···
#""".format(title=title, poem=poem))


        

    
    
    
    
    
    
    
#    f.write(title)
#    f.write("\n")
#    f.write("\n")
#    f.write(poem)
    
        
        
    
    
























