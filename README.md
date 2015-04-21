# fuzzyalpha-example

Provide a self-contained example of construction of candidate headword
spelling errors with suggested corrections.


The example constructs the pui-fuzzyalpha.txt and pui-fuzzyalpha.html files
mentioned [here](https://github.com/sanskrit-lexicon/CORRECTIONS/issues/101).

There are two data inputs:

*  [sanhw1.txt](https://github.com/sanskrit-lexicon/CORRECTIONS/blob/master/sanhw1/sanhw1.txt)  is a list of all the headwords in the various Sanskrit dictionaries at the [Cologne Sanskrit Lexicon](http://www.sanskrit-lexicon.uni-koeln.de/)

* puihw2.txt is list of headwords for the Purana Index, which is part of the
  puixml.zip [download](http://www.sanskrit-lexicon.uni-koeln.de/scans/PUIScan/2014/web/webtc/download.html).

Command-line instructions for recreating the example are in the readme.txt file
of this repository.

The faultinder3a.php program is drawn from 
[SanskritSpellCheck](https://github.com/drdhaval2785/SanskritSpellCheck/).

The Python programs are run with version 2.7 Python.

The extension-notes folders contains a revised version of 
fuzzyalpha.py that can work with some other dictionaries.  The readme.txt
program in that file indicates the execution sequence for the other
specialized dictionaries.
