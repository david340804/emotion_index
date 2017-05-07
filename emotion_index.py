import re
import os,sys

def importFlagDict(filename):
    with open(filename) as f:
        words = f.readlines()

    #flag dictionary to use
    d = {}

    #import flags and markers from text file
    # a flag is an index, markers are the associated words whose occurences are summed to determine the flag value for a string
    for line in words:
        #take off trailing whitespace and newlines
        line = line.strip()

        #separate flag and markers
        line = line.split(':')
        flag = line[0]
        markers = line[1].split(',')

        #add to dictionary
        d[flag] = markers
    return d

#file that contains the flag dictionary
filename  = 'rose.txt'
flagdict = importFlagDict(filename)

#some sample strings to try
input_string = 'I love to eat free liberating foods when Im super angry bitter cross'
input_string2 = 'Im sleeping with my cat'

#create record of flag occurences
def flags(strang,flags):
    rec  = {}
    for key,vals in flags.items():
        #iterate over flags

        #zero the record
        rec[key] = 0
        
        for word in vals:
            #once per word in this flag
            count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word.lower()), strang.lower()))

            #add one to the record of
            rec[key] = rec[key] + count
    #return the flags counted dictionary
    return rec


print(flags(input_string,flagdict))
