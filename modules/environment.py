#!/usr/bin/env python
#-*- coding:utf8 -*-

import os

def run(**args):
    print ("[*] In environment module. ")
    return str(os.environ)

