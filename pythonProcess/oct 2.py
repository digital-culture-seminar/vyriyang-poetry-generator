#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 19:21:50 2018

@author: Vyri
"""

import markovify as m

#with open ("Screenhot018-08-20t4.54.29.txt")as F1:
#    m1 = F1.read()
##    print venalMuse
#    
#with open ("Screenhot018-08-20t4.54.36.txt")as F1:
#    m2 = F1.read()    
#    
# 
#m1_model = m.Text(m1)
#m2_model = m.Text(m2)
#
##print muse_model.make_sentence()
##
##for i in range(3):
##    print muse_model.make_sentence()
#
#
#mWhole_model = m.combine([m1_model,m2_model],[2,1])
#
#print mWhole_model.make_sentence()



with open ("The_flowers_of_Evil/The_Venal_Muse.txt") as f1:
    text = f1.read()
#    print text
    
    
text_model = m.NewlineText(text)

for i in range(3):
    print text_model.make_sentence()
    
    
    
with open("poem.md","w") as f:
    f.write(text_model.make_sentence())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    