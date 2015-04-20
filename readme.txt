
These are the steps to create fuzzyalph suggestions for PUI dictionary.
The two external inputs are sanhw1.txt and puihw2.txt.

1. Regenerate faultfinder suggestions (relative to MW dictionary):
php faultfinder3a.php MW sanhw1.txt AllvsMW.txt

2. Select the PUI cases from AllvsMW.txt

python gen-only-notrxx.py PUI AllvsMW.txt AllvsMw-PUI.txt
(554 records)

3. put the cases into page-order, which makes reviewing slightly more efficient
python pageord.py AllvsMW-PUI.txt pui-only-notrxx-page.txt  puihw2.txt
554  headwords from AllvsMW-PUI.txt
549  headwords after duplicates removed

Note: some 'hard-coding' (dcode, dyear) in fuzzyalpha.py

4. Generate fuzzy suggestions for the cases.
This step is quite slow, due to the pure Python implementation of levenshtein
edit-distance algorithm.  It will print a terminal message for each case,
so you can know it is working.

python fuzzyalpha.py PUI,2014 pui-only-notrxx-page.txt pui-fuzzyalpha.txt pui-fuzzyalpha.html sanhw1.txt puihw2.txt
