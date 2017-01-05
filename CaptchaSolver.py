#coding=utf-8

from keras.models import model_from_json
import numpy as np
from PIL import Image

X_list=[]

table = ['0','1','2','3','4','5','6','7','8','9',\
               'a','b','c','d','e','f','g','h','i','j','k',\
               'l','m','n','o','p','q','r','s','t','u','v',\
               'w','x','y','z','A','B','C','D','E','F','G',\
               'H','I','J','K','L','M','N','O','P','Q','R',\
               'S','T','U','V','W','X','Y','Z']

model = model = model_from_json(open('shu_captcha_CNN_structure.json').read())
model.load_weights('shu_captcha_CNN_weights.h5')


def solve(im):
  X_list=[]
  result=''
  for i in range(4):
    region = (15*i,0,15*i+15,22)
    cim = im.crop(region)
    X_list.append(np.array(cim))
  p = model.predict(np.array(X_list))
  for each in p:
    index=0
    for i in range(len(each)):
      if(each[i]>each[index]):
        index=i
    result+=(table[index])
  return (result)