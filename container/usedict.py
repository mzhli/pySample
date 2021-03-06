# -*- coding: utf-8 -*-
'''
Created on 2014年11月12日

@author: mzhli
'''
import pickle
import pprint

def writeDictAsTextfile(d, outfile):
    f = open(outfile, "w")
    pickle.dump(d, f)
    
def writeDictAsBinaryfile(d, outfile):
    f = open(outfile, "wb")
    pickle.dump(d, f, protocol=1)
    
def writeDictToBinaryfile2(d, outfile):
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
    writeDictAsTextfile(sampleDict, outfileText)
    writeDictAsBinaryfile(sampleDict, outfileBin)
    writeDictToBinaryfile2(sampleDict, outfileBin2)
    pprint.pprint(readDictFromFile(outfileText))
    pprint.pprint(readDictFromFile(outfileBin))
    pprint.pprint(readDictFromFile(outfileBin2))