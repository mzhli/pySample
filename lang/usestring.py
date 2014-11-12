# -*- coding: utf-8 -*-
'''
Created on 2014年11月12日

@author: mzhli
'''
import re

def pickMatchedStrings(pattern, listInputString):
    result = [ astr for astr in listInputString if re.search(pattern, astr) ]
    return result

if __name__ == '__main__':
    inputdata = ["mzhli2000", "mzhli", "zuludic@hotmail.com", "mzhli@telenav.cn"]
    patterns = ['^mzhli', '\d', '@']
    print "Input strings: %s" % (str(inputdata))
    for pattern in patterns:
        print "Pattern '%s' => %s" % (pattern, pickMatchedStrings(pattern, inputdata))