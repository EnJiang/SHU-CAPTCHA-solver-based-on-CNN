#coding=utf-8

from CaptchaSolver import solve
from PIL import Image


im = Image.open("test.jpg")
print solve(im)