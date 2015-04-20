""" pageord.py
  Apr 16, 2015 for VEI - applied to faultfinder 
  Since there are so many cases in vei-only-notrxx-ff.txt, it may be
  more efficient to order the cases by page.
  Usage: python26 pageord.py vei-only-notrxx-ff.txt vei-only-notrxx-page.txt  ../../veihw2.txt
   (e.g. Xhw2.txt where X is yat, wil, sch, etc.)
  
   input.txt is a list of headwords, one per line, in slp1 transliteration
    Note: This is specialized to vei-only-notrxx-ff.txt
   fuzzyalpha.txt is the output file name
    Hard-coded inputs:
     path to sanhw1.txt
     path to veihw2.txt
 Note: input.txt lines can also have the form:
 hw:other junk
"""
import re
import sys

class Dicthw(object):
    def __init__(self,line):
        line = line.rstrip('\r\n')
        self.line =line
        self.n = None # subscript . Filled in later
        (self.page,self.hw,self.lrange)=re.split(r':',line)
    def __repr__(self):
        return self.line

class Dicthws(object):
 def __init__(self,filename):
  with open(filename,'r') as f:
   self.dicthws = [Dicthw(x) for x in f]

def main():
 filename = sys.argv[1]
 fileout = sys.argv[2]

 file_dicthw2 = sys.argv[3] # '../dicthw2.txt'
 # initialize from dicthw2.txt
 c = Dicthws(file_dicthw2)
 dicthws = c.dicthws
 # dictionary for dicthws:
 #  Associate to each dicthws.hw
 # info message
 dicthwsd = {}
 ndicthws = len(dicthws)
 for i in xrange(0,ndicthws):
  dicthw = dicthws[i]
  hw = dicthw.hw
  if hw not in dicthwsd:
   dicthwsd[hw] = []
  dicthwsd[hw].append(i)
 # inrecs = keys in input file
 inrecs = []
 f = open(filename,'r')
 for line in f:
  line = line.strip()
  # kfAzwa:VV=fA:VEI
  parts = re.split(r':',line)
  hw = parts[0]
  inrecs.append(hw)
 f.close()
 # remove duplicates
 print len(inrecs)," headwords from",filename
 inrecs = list(set(inrecs))
 print len(inrecs)," headwords after duplicates removed"
 # recs : a tuple (i,hw) where i is the (first) index of the hw in dicthwsd.
 recs = [(dicthwsd[hw][0],hw) for hw in inrecs]
 # sort recs by 'i'
 recs.sort(key=lambda tup: tup[0])
 # generate output
 fout = open(fileout,'w')
 for rec in recs:
  (i,hw) = rec # unpack tuple
  page = dicthws[i].page
  out = "%s:%s" %(hw,page)
  fout.write("%s\n" % out)
 
 f.close()
if __name__=="__main__":
 main()
