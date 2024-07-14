# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 03:36:12 2024

@author: Lenovo
"""

from PyQt5 import uic
with open ("widgets_kullanıcı.py","w",encoding="utf-8")as fout:
    uic.compileUi("kullanıcı.ui",fout)