import re
import os,sys

filename  = 'words.txt'
with open(filename) as f:
    words = f.readlines()

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


input_string = 'Ya nah its dat boi oh shit waddup shit shit'
input_string2 = 'Im sleeping with my cat'

#record of flag occurences
rec  = {}

for key,vals in d.items():
    #iterate over flags

    #zero the record
    rec[key] = 0
    
    for word in vals:
        #once per word in this flag
        count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word.lower()), input_string2.lower()))

        #add one to the record of
        rec[key] = rec[key] + count


print(rec)
