# -*- coding: utf-8 -*-
'''
Created on 2014年11月12日

@author: mzhli
'''

def funcWithMultiPositionalParams(arg1, arg2, *args):
    print "----------------------------------\n" \
          "Total Number = %d\n" \
          "arg1 = \"%s\"\n" \
          "arg2 = \"%s\"\n" \
          "others = \"%s\"" % (len(args)+2, arg1, arg2, str(args))
          
def funcWithMultiKeyParams(arg1, arg2, **kwargs):
    print "----------------------------------\n" \
          "Total Number = %d\n" \
          "arg1 = \"%s\"\n" \
          "arg2 = \"%s\"\n" \
          "others = \"%s\"" % (len(kwargs)+2, arg1, arg2, str(kwargs))

if __name__ == '__main__':
    arg1 = "1st argument"
    arg2 = "2nd argument"
    
    funcWithMultiPositionalParams(arg1, arg2)
    funcWithMultiPositionalParams(arg1, arg2, "3rd argument")
    funcWithMultiPositionalParams(arg1, arg2, "3rd argument", "4th argument")
    funcWithMultiPositionalParams(arg1, arg2, "3rd argument", *["4th argument", "5th argument"])
    
    funcWithMultiKeyParams(arg1, arg2, arg3='3rd argument')
    funcWithMultiKeyParams(arg1, arg2, arg3='3rd argument', arg4='4th argument')
    funcWithMultiKeyParams(arg1, arg2, arg3='3rd argument', **{'arg4':'4th argument', 'arg5':'5th argument'})
    