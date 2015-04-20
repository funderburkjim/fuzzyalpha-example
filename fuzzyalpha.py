""" fuzzyalpha.py
  Apr 19, 2015 for PUI - applied to faultfinder 
  See readme.txt for details

"""
import re
import sys
import levenshtein
import string
tranfrom="aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh"
tranto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvw"
trantable = string.maketrans(tranfrom,tranto)

def slp_cmp(a,b):
 a1 = string.translate(a,trantable)
 b1 = string.translate(b,trantable)
 return cmp(a1,b1)

class Sanhw(object):
    def __init__(self,line):
        line = line.rstrip('\r\n')
        self.line =line
        self.n = None # subscript . Filled in later
        (self.key,self.dictstr)=re.split(r':',line)
        self.dicts = re.split(',',self.dictstr)
        self.len = len(self.key) # Feb 3, 2015, used by suggest_v3
    def __repr__(self):
        return "Sanhw[%s]"%self.line
class Sanhws(object):
 def __init__(self,filename='../../../../awork/sanhw1/sanhw1.txt'):
  with open(filename,'r') as f:
   # the 'if (not...) clause is to skip ':AP90' in sanhw1.txt
   self.sanhws = [Sanhw(x) for x in f if (not x.startswith(':'))]
  self.sanhwsd = {}
  for sanhw in self.sanhws:
   self.sanhwsd[sanhw.key] = sanhw

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


def suggest_v3(w,sanhws,m=2,skipexact=True):
    # modified to screen further by length of word
    # Assume first letter of 'w' is correct.
    # For efficiency, consider only sanhws that start with same letter
    # Do not return exact match 
    w0 = w[0]
    hws=[x for x in sanhws if x.key[0] == w0]
    # Feb 3, 2015
    lw = len(w)
    hws = [x for x in hws if (abs(x.len - lw) < m)] #? < m or > m ?
    #print "%s headwords start with %s" %(len(hws),w0)
    nearlist=[] # list of hws whose levenshtein distance from w is <= 
    low = 99
    for hw in hws:
        if (w == hw.key) and skipexact:
            continue
        d=levenshtein.levenshtein1(w,hw.key,m)
        if d == -1:
            continue
        nearlist.append((d,hw))
        if (d < low): # update low distance
            low = d
    # include ones only = low
    ans = [x[1] for x in nearlist if x[0] == low]
    
    #s = sorted(nearlist,key=lambda(x):x[0]) # sort by d
    return ans

def process_alphaerr(i,dicthws,sanhws,sanhwsd,fout,fhtml,n,pagecol,dcode,dyear):
 outarr = []
 dashes=('-'*72)
 hw = dicthws[i].hw
 case='a'
 outarr.append('%s'%dashes)
 #f.write('%03d %s %s !< %s\n' %(n,case,dicthws[i-1].line,dicthws[i].line))
 suggestions = suggest_v3(hw,sanhws,6) # last parameter is tunable
 print "dbg: hw %s has %s suggestions" %(hw,len(suggestions))
 #print i,len(dicthws),hw
 hw0 = dicthws[i-1].hw
 hw1 = dicthws[i+1].hw
 ordered=[[],[]]  # yes/no
 for suggestion in suggestions:
  hwsuggest = suggestion.key
  if (slp_cmp(hw0,hwsuggest) < 0) and (slp_cmp(hwsuggest,hw1) < 0):
   ordered[0].append(hwsuggest)
  else:
   ordered[1].append(hwsuggest)  
 outarr.append('%03d %s'%(n,hw0))
 out=[', '.join(ordered[0]),','.join(ordered[1])]  #Apr 14, 2015 comma-space
 outarr.append('%03d %s -> %s (%s)' %(n,hw,out[0],out[1])) 
 outarr.append('%03d %s'%(n,hw1))
 pagelink = page_link(pagecol,dcode,dyear) # 4th line requested by Dhaval
 hwlink = headword_link(hw,dcode,dyear)
 out =  '%03d headword %s ---  page %s' % (n,hwlink,pagelink)
 outarr.append('%s' % out)
 outarr.append('') # extra blank line
 # write text lines
 for out in outarr:
  fout.write("%s\n" %out)
 # write html lines
 for out in outarr:
  fhtml.write("%s<br/>\n" %out)
 return 0

def page_link(volpage,d,y):
 """ return 'href' string for link to scanned image for PUI for page 'page'
 """
 base = "http://www.sanskrit-lexicon.uni-koeln.de/scans"
 url = "%s/%sScan/%s/web/webtc/servepdf.php" %(base,d,y)
 #(page,col) = re.split('-',volpage) # 
 #pageparm = page
 pageparm = volpage
 parms = "page=%s" % pageparm
 href = "%s?%s" % (url,parms) 
 ans = "<a target='_PUIpage' href='%s'>%s</a>" %(href,volpage)
 return ans

def headword_link(hw,d,y):
 """ return 'href' string for link to basic  display for pwg for headword hw
     Use this form, which GitHub accepts, so that link opens in same
     tab always
 """
 d = "PUI" 
 y = "2014"
 base = "http://www.sanskrit-lexicon.uni-koeln.de/scans"
 url = "%s/%sScan/%s/web/webtc/indexcaller.php" %(base,d,y)
 parms = "input=slp1&output=deva&key=%s" % hw
 href = "%s?%s" % (url,parms) 
 ans = "<a target='_PUIword' href='%s'>%s</a>" %(href,hw)
 return ans

def html_headers(f,dictcode):
 f.write("<html>\n")
 f.write("<head>\n")
 f.write("<title>%s fuzzyalpha</title>\n"%dictcode)
 f.write("</head>\n")
 f.write("<body>\n")

def html_footers(f):
 f.write("</body>\n")
 f.write("</html>\n")
 
def main(dcode,dyear,filename,fileout,filehtml,file_sanhw1,file_dicthw2):
 # initialize from sanhw1.txt
 c = Sanhws(file_sanhw1)
 sanhws = c.sanhws
 sanhwsd = c.sanhwsd
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
 print "%s records from %s" %(len(dicthws),file_dicthw2)
 print "%s records from %s" %(len(sanhws),file_sanhw1)
 f = open(filename,'r')
 fout = open(fileout,'w')
 fhtml= open(filehtml,'w')
 html_headers(fhtml,dcode) # write html boilerplate 
 # process dicthws line by line, looking for alphabetical misorderings
 notordered=0
 nline = 0 # case number
 mline = 10 # for debug
 mline = 1000000 # for production. 
 for line in f:
  line = line.strip()
  # akznA:007-2
  parts = re.split(r':',line)
  (hw,volpage) = parts  # Apr 14, 2015
  #hw = parts[0]
  #hw = parts[1]  # chksort1.txt, angya
  nline = nline + 1
  if nline > mline:
   print "exiting after ",nline
   break
  if hw not in dicthwsd:
   print "word %s not a headword" % hw
   continue
  idicts = dicthwsd[hw]
  for idict in idicts:
   dicthw = dicthws[idict]
   icase=process_alphaerr(idict,dicthws,sanhws,sanhwsd,fout,fhtml,nline,volpage,dcode,dyear)
 
 f.close()
 fout.close()
 html_footers(fhtml) #finsh html
 fhtml.close()
if __name__=="__main__":
 (dcode,dyear) = re.split(',',sys.argv[1])
 filename = sys.argv[2]
 fileout = sys.argv[3]  # text form
 filehtml = sys.argv[4]  # html form
 file_sanhw1 = sys.argv[5] #sanhw1.txt
 file_dicthw2 = sys.argv[6] # xhw2.txt'
 print "Using dcode=%s, dyear=%s" %(dcode,dyear)
 print "May need to adjust page_link for ",dcode
 main(dcode,dyear,filename,fileout,filehtml,file_sanhw1,file_dicthw2)
