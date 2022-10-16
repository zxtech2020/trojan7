#!/usr/bin/env python
#-*- coding:utf8 -*-

import os

def run(**args):
    
    print ("[*] In dirlister module. ")
    files = os.listdir(".")

    return str(files)

