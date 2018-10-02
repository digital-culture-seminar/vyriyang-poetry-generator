#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 22:35:42 2018

@author: Vyri
"""


import random

# list of nouns
basicNouns = ["muse","monk","vampire","jewels","log","crowd"]
adjNouns = ["simplicity"]
basicObjectives = ["log","glass","vaults","censer"]
basicObjectiveAs = ["altar","amusement"]
positiveNouns = ["birth"]
negativeNouns = ["death","poison"]

pronouns = ["I","we","they","you","he","she","it"]
pronoun1s = ["my","our","their","your","his","her","its"]
pronoun2s = ["me","us","them","you","him","she","it"]

# list of verbs
verbs = ["love","fling","flash","slip","glean","chant"]
positiveVerbs = ["love"]
negativeVerbs = ["slip"]

verbings = ["swing"]

# list of adjectives
adjectives = ["spiritual","misty","meager","vulgar"]

# list of positiveAdjectives
positiveAdjectives = ["gold","warm"]

# list of negativeAdjectives
negativeAdjectives = ["venal"]

# list of adverbs
adverbs = ["former"]

# list of positiveAdverbs
positiveAdverbs = ["cheerful"]

# list of negativeAdverbs
negativeAdverbs = ["sick","venal","wretched","bored"]

# list of orientationPreposition
orientationPrepositions = ["outside","inside"]
prepositionNouns = ["inner","outer"]


# list of color
warmColors = ["red","purple",""]
coldColors = ["blue","green",]
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
bodyparts = ["head","neck","shoulders","wrist","hand"]
bodypartAs = ["arm"]


# list of animalRalted
# list of animal
animals = ["cat","dog","rabbit",]
animalAs = ["owl",]
animalYs = [""]

#list of placeRalted
countries = [""]
cities = [""]
locations = [""]
houses = ["bedroom","living room","balcony","bathroom","kitchen","window","door",
          "sink"]

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








#class Timerelated:
#    def sayMonth(self,month):
#        self.month = month
#        print(self.month)
#    def sayDay(self,day):
#        self.day = day
#        print(self.day)
#    def sayTime(self,time):
#        self.time = time
#        print(self.time)
#
#
#
#T = Timerelated()
#T.sayMonth('{month}'.format(month=month))
#T.sayDay('{day}'.format(day=day))
#T.sayMonth('{month}'.format(month=month))


#print("1. sad")
#print("2. happy")
#choice=int(input("Chose a mood:"))
#if choice == 1:
#    print('{month}'.format(month=month))
#elif choice == 2:
#    print('{day}'.format(day=day))
#else:
#    print("Invalid, please chose 1 or 2.")  




#class FirstParagraph:
#    def firstSentence(self,subject,mood):
#        self.subject=subject
#        self.mood=mood
#        print "{month}".format(month=month).capitalize()+"'s",\
#        self.subject,"is",self.mood
#        
#FP=FirstParagraph()
#FP.firstSentence('heat','sad')
        
        
        
#class FirstParagraph:
#    def form1(self):
#        print "{month}".format(month=month).capitalize()
#        
#        
#        
#        
#class SecondParagraph(FirstParagraph):
#    def form2(self):
#        print "{day}".format(day=day).capitalize()
#        
#       
#        
#P = SecondParagraph()
#P.form1()
#P.form2()

#
#class Format():
#    def form(self):
#        forms = P.form1(),P.form2()
#        formType = random.choice(forms)
#        print "{formType}".format(formType=formType)
#        
#F=Format()
#F.form()


#forms = [P.form1(),P.form2()]
#
##formType = random.choice(forms)
##print "{formType}".format(formType=formType)
#
#random.shuffle(P.forms)
#for P.form in P.forms:
#    print P.form


    


    
   


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

print'\n'+(str.title()) +'\n'






# paragraph test     
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
of {basicNoun}".format(verbing=verbing.capitalize(),
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
        
        
        
#class ParagraphFormat():
#    def form1(self):
#        str = "{month} {month}".format(month=month)
#        return(str.capitalize())
#       
#    def form2(self):
#        return "{day}".format(day=day).capitalize()
#    def form3(self):
#        return "{basicNoun}".format(basicNoun=basicNoun).capitalize()
#    def form4(self):
#        return "{positiveNoun}".format(positiveNoun=positiveNoun).capitalize()
#    def form5(self):
#        return "{negativeNoun}".format(negativeNoun=negativeNoun).capitalize()
#    def form6(self):
#        str = "{time}".format(time=time)
#        return(str.capitalize())
#    def form7(self):
#        str = "{bodypart}".format(bodypart=bodypart)
#        return(str.capitalize())
#    def form8(self):
#        str = "{house}".format(house=house)
#        return(str.capitalize())
#    def form9(self):
#        str = "{earth}".format(earth=earth)
#        return(str.capitalize())
#    def form10(self):
#        str = "{weather}".format(weather=weather)
#        return(str.capitalize())
#    def form11(self):
#        str = "{greenery}".format(greenery=greenery)
#        return(str.capitalize())
#    def form12(self):
#        str = "{flower}".format(flower=flower)
#        return(str.capitalize())
#    def form13(self):
#        str = "{travel}".format(travel=travel)
#        return(str.capitalize())
#    def form14(self):
#        str = "{season}".format(season=season)
#        return(str.capitalize())
#    def form15(self):
#        str = "{sadColor}".format(sadColor=sadColor)
#        return(str.capitalize())
#    def form16(self):
#        str = "{negativeAdverb}".format(negativeAdverb=negativeAdverb)
#        return(str.capitalize())
#    def form17(self):
#        str = "{negativeAdverb}".format(negativeAdverb=negativeAdverb)
#        return(str.capitalize())
#    def form18(self):
#        str = "{negativeAdverb}".format(negativeAdverb=negativeAdverb)
#        return(str.capitalize())
#    def form19(self):
#        str = "{negativeAdverb}".format(negativeAdverb=negativeAdverb)
#        return(str.capitalize())
#    def form20(self):
#        str = "{negativeAdverb}".format(negativeAdverb=negativeAdverb)
#        return(str.capitalize())
#    def form21(self):
#        str = "{negativeAdverb}".format(negativeAdverb=negativeAdverb)
#        return(str.capitalize())
#    def form22(self):
#        str = "{negativeAdverb}".format(negativeAdverb=negativeAdverb)
#        return(str.capitalize())
#    def form23(self):
#        str = "{negativeAdverb}".format(negativeAdverb=negativeAdverb)
#        return(str.capitalize())
#    def form24(self):
#        str = "{negativeAdverb}".format(negativeAdverb=negativeAdverb)
#        return(str.capitalize())
#        
#        
T = TitleParagraphFormat()
#P = ParagraphFormat()
#    
forms1 = [T.form1(),T.form2(),T.form3(),T.form4(),T.form5(),T.form6(),
         T.form7(),T.form8(),T.form9(),T.form10(),T.form11(),T.form12(),
         T.form13(),T.form14(),T.form15(),T.form16()]
#
#forms2 = [P.form1(),P.form2(),P.form3(),P.form4(),P.form5(),P.form6(),
#         P.form7(),P.form8(),P.form9(),P.form10(),P.form11(),P.form12(),
#         P.form13(),P.form14(),P.form15(),P.form16(),P.form17(),P.form18(),
#         P.form19(),P.form20(),P.form21(),P.form22(),P.form23(),P.form24()]
#
#
#resultList1 = random.sample(forms1,7)
#resultList2 = random.sample(forms2,20)
#
#resultLists = []
#resultLists.extend(resultList1)
#resultLists.extend(resultList2)
#
#
#slice = random.sample(resultLists,14)

slice = random.sample(forms1,14)
random.shuffle(slice)



i = 0
print 
for slice in slice:
    i = i + 1
    if (i<4):
        space = '\n'*0
    if (i==4):
        space = '\n'*1
    if (4<i<8):
        space = '\n'*0
    if (i==8):
        space = '\n'*1
    if (8<i<11):
        space = '\n'*0
    if (i==11):
        space = '\n'*1
    if (11<i<14):
        space = '\n'*0
    if (i==14):
        space = '\n'*0
        
    print (slice) + space    




#random.shuffle(forms)
#print 
#for form in forms:
#    print form






#import random;
# 
##1、利用递归生成
#resultList=[];#用于存放结果的List
#A=1; #最小随机数
#B=10 #最大随机数
#COUNT=10
# 
##生成随机数的递归数学，参数counter表示当前准备要生成的第几个有效随机数
#def generateRand(counter): 
#    tempInt=random.randint(A,B); # 生成一个范围内的临时随机数，
#    if(counter<=COUNT): # 先看随机数的总个数是不是够了，如果不够
#        if(tempInt not in resultList): # 再检查当前已经生成的临时随机数是不是已经存在，如果不存在
#            resultList.append(tempInt); #则将其追加到结果List中
#            counter+=1;# 然后将表示有效结果的个数加1. 请注意这里，如果临时随机数已经存在，则此if不成立，那么将直接执行16行，counter不用再加1
#        generateRand(counter); # 不管上面的if是否成立，都要递归。如果上面的临时随机数有效，则这里的conter会加1，如果上面的临时随机数已经存在了，则需要重新再生成一次随机数,counter不能变化
#generateRand(1);#调用递归函数，并给当前要生成的有效随机数的个序号置为1，因为要从第一个开始嘛
#print(resultList)# 打印结果
# 
##2、利用Python中的randomw.sample()函数实现
#resultList=random.sample(range(A,B+1),COUNT); # sample(x,y)函数的作用是从序列x中，随机选择y个不重复的元素。上面的方法写了那么多，其实Python一句话就完成了。











#formType = random.choice(forms)
#print "{formType}".format(formType=formType)   
    
    
#formType1 = P.form1()
#formType2 = P.form2()
#
#
#formTypes = [formType1,formType2]
#formType = random.choice(formTypes)
#print "{formType}".format(formType=formType)













#slice = random.sample(monthes,3)
#print 
#for slice in slice:
#    print (slice)
#       
#  
#print monthes.index(slice);


















    
    
#class GDistance:
#    def __init__(self,g):
#        self.g=g
#    def __call__(self,t):
#        return(self.g*t**2)/2
#        
#if __name__ == '__main__':
#    e__gdist = GDistance(9.8)
#    for t in range(11):
#        print(format(e__gdist(t),"0.2f"))


#
#import random
#random.seed(1)
#for i in range(10):
#    print(random.randint(23,33))





#
#subjects = [noun, positiveNoun, negativeNoun]
#subject = random.choice(subjects)
#
#print "{subject}".format(subject=subject)
#print "{subject}".format(subject=subject)
#
#subjects = [noun, positiveNoun, negativeNoun]
#subject = random.choice(subjects)
#
#print "{subject}".format(subject=subject)
#
#class Theme:
#    def saySubject(self,subject):
#        self.subject=subject
#        print(self.subject)
#        
#        
#T = Theme()
#T.saySubject("{subject}".format(subject=subject))
#T.saySubject("{subject}".format(subject=subject))
#T.saySubject("{subject}".format(subject=subject))



 
#subjects = [noun, positiveNoun, negativeNoun]
#subject = random.choice(subjects)
#
#if (subject == noun):
#    print "{subject}s".format(subject=subject)
#    
#else:
#    print "{subject}".format(subject=subject)


#T.saySubject("{subject}".format(subject=subject))





#random.shuffle(subjects)
#
#deck1=[]
#for i in range(1):
#    deck1.append(subjects.pop())
#
#print(deck1)
#
#
#
#
#if (pronoun == "I"):
#    print "{pronoun} am".format(pronoun=pronoun)
#    
#else:
#    print "{pronoun} is".format(pronoun=pronoun)


    













