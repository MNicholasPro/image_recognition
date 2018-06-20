#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 23:32
# @Author  : zhoumingkai
# @Site    : 
# @File    : 1.py
# @Software: PyCharm


import pytesseract
from PIL import Image

image = Image.open("../tuxiangshibie/pic/shibie3.jpeg")
code = pytesseract.image_to_string(image,lang="chi_sim+eng",config="-psm 6")
print(code)