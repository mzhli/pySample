# -*- coding: utf-8 -*-
'''
Created on 2014年11月13日

@author: mzhli
'''
import os

def removeThenCreate(filepath):
    # Remove file first anyway
    if os.path.exists(filepath):
        os.remove(filepath)
    # Test the existence of file
    print "Does file '%s' exist? %s" % (filepath, os.path.exists(filepath))
    # Create a new file
    fd = open(filepath, 'w')
    print "File '%s' created..." % (filepath)
    fd.close()
    # Test again
    print "Does file '%s' exist now? %s" % (filepath, os.path.exists(filepath))
    
def normalizePath(origpath):
    return os.path.realpath(origpath)

if __name__ == '__main__':
    # Test path normalization
    origpath = "/home/mzhli/tmp/../code/./python"
    print "Orig path: %s\nNormalized path: %s" %(origpath, normalizePath(origpath))
    
    # Test file existence testing
    targetfile = "./testfile.txt"
    removeThenCreate(targetfile)
