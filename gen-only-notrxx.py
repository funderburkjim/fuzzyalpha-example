""" gen-only-notrxx.py  Apr 16, 2015
 Start with AllvsMW.txt (or similar) and a dictionary code D
 Select list of list of AllvsMW.txt which
 (a) occur only in dictionary D
 (b) do NOT have rxx form in the faultfinder reason.
 Usage example:
 python gen-only-notrxx.py INM ../AllvsMW.txt 2015Apr15/INM-test.txt

"""
import sys, re
import codecs

class AllvsMW(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  (self.key,self.reasontype,self.reason,dictstring) = re.split(r'[:=]',line)
  self.dictcodes = re.split(',',dictstring)

def generate(inrecs,code,fileout):
 fout = codecs.open(fileout,'w','utf-8')
 code = code.upper()
 nout = 0
 for inrec in inrecs:
  if len(inrec.dictcodes) > 1: 
   continue
  if code != inrec.dictcodes[0]:
   continue
  if re.search(r'r(.)\1',inrec.reason):
   continue
  # found one!
  nout = nout + 1
  fout.write("%s\n" % inrec.line)
 fout.close()
 print nout,"records written to",fileout

if __name__=="__main__":
 code = sys.argv[1]
 filein = sys.argv[2] 
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  inrecs = [AllvsMW(line) for line in f]
 fileout = sys.argv[3] #
 generate(inrecs,code,fileout)


