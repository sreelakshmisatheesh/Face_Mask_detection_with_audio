# -*- coding: utf-8 -*-
"""
Created on Mon May 23 17:45:51 2022

@author: sreelakshmi
"""

from  gtts import gTTS
mytext= "Very good ,keep it up"
language='en'
myobj=gTTS(text=mytext,lang=language,slow=False)
myobj.save("mask.mp3")
gTTS(text='please wear your mask',lang='en',slow=False).save("wear_mask.mp3")
