# -*- coding: utf-8 -*-
'''
Created on 2014年11月12日

@author: mzhli
'''
import pickle
import pprint

def writeDictToText(d, outfile):
    f = open(outfile, "w")
    pickle.dump(d, f)
    
def writeDictToBinary(d, outfile):
    f = open(outfile, "wb")
    pickle.dump(d, f, protocol=1)
    
def writeDictToBinary2(d, outfile):
    f = open(outfile, "wb")
    pickle.dump(d, f, protocol=2)
    
def readDictFromFile(infile):
    f = open(infile, "r")
    return pickle.load(f)
    

if __name__ == '__main__':
    sampleDict = {'name': 'mzhli', 
                  'title': 'Manager, Engineering', 
                  'department': 'Global Nav',
                  'team': {'liCong': {'title':'Sr. Software Engineer' },
                           'ZhouYinyin': {'title': 'Sr. Software Engineer'}, 
                           'YinWeiyi': {'title': 'Sr. Software Engineer'}}}
    outfileText = "./sampledict.tdp"
    outfileBin = "./sampledict.bdp"
    outfileBin2 = "./sampledict.bdp2"
    writeDictToText(sampleDict, outfileText)
    writeDictToBinary(sampleDict, outfileBin)
    writeDictToBinary2(sampleDict, outfileBin2)
    pprint.pprint(readDictFromFile(outfileText))
    pprint.pprint(readDictFromFile(outfileBin))
    pprint.pprint(readDictFromFile(outfileBin2))