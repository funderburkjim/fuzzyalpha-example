
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


----------------------------------------------------
FOR ACC:
mkdir acc
2. Select the ACC cases from AllvsMW.txt

python gen-only-notrxx.py ACC AllvsMW.txt acc/AllvsMw-ACC.txt
(365 records)

3. put the cases into page-order, which makes reviewing slightly more efficient
python pageord.py acc/AllvsMW-ACC.txt acc/acc-only-notrxx-page.txt  acc/acchw2.txt
365  headwords from acc/AllvsMW-ACC.txt
361  headwords after duplicates removed

Note: some 'hard-coding' (dcode, dyear) in fuzzyalpha.py

4. Generate fuzzy suggestions for the cases.
This step is quite slow, due to the pure Python implementation of levenshtein
edit-distance algorithm.  It will print a terminal message for each case,
so you can know it is working.

python fuzzyalpha.py ACC,2014 acc/acc-only-notrxx-page.txt  acc/acc-fuzzyalpha.txt  acc/acc-fuzzyalpha.html sanhw1.txt  acc/acchw2.txt

----------------------------------------------------
FOR KRM:
mkdir krm
2. Select the KRM cases from AllvsMW.txt

python gen-only-notrxx.py KRM AllvsMW.txt krm/AllvsMw-KRM.txt
(120 records)

3. put the cases into page-order, which makes reviewing slightly more efficient
python pageord.py krm/AllvsMW-KRM.txt krm/krm-only-notrxx-page.txt  krm/krmhw2.txt
120  headwords from krm/AllvsMW-KRM.txt
120  headwords after duplicates removed

4. Generate fuzzy suggestions for the cases.

python fuzzyalpha.py KRM,2014 krm/krm-only-notrxx-page.txt  krm/krm-fuzzyalpha.txt  krm/krm-fuzzyalpha.html sanhw1.txt  krm/krmhw2.txt

----------------------------------------------------
FOR SNP:
mkdir snp
2. Select the SNP cases from AllvsMW.txt

python gen-only-notrxx.py SNP AllvsMW.txt snp/AllvsMw-SNP.txt
(1 records)

3. put the cases into page-order, which makes reviewing slightly more efficient
python pageord.py snp/AllvsMW-SNP.txt snp/snp-only-notrxx-page.txt  snp/snphw2.txt
1  headwords from snp/AllvsMW-SNP.txt
1  headwords after duplicates removed

4. Generate fuzzy suggestions for the cases.

python fuzzyalpha.py SNP,2014 snp/snp-only-notrxx-page.txt  snp/snp-fuzzyalpha.txt  snp/snp-fuzzyalpha.html sanhw1.txt  snp/snphw2.txt

----------------------------------------------------
FOR IEG:
mkdir ieg
2. Select the IEG cases from AllvsMW.txt

python gen-only-notrxx.py IEG AllvsMW.txt ieg/AllvsMw-IEG.txt
(466 records)

3. put the cases into page-order, which makes reviewing slightly more efficient
python pageord.py ieg/AllvsMW-IEG.txt ieg/ieg-only-notrxx-page.txt  ieg/ieghw2.txt
466  headwords from ieg/AllvsMW-IEG.txt
427  headwords after duplicates removed

4. Generate fuzzy suggestions for the cases.

python fuzzyalpha.py IEG,2014 ieg/ieg-only-notrxx-page.txt  ieg/ieg-fuzzyalpha.txt  ieg/ieg-fuzzyalpha.html sanhw1.txt  ieg/ieghw2.txt

----------------------------------------------------
FOR PE:
mkdir pe
2. Select the PE cases from AllvsMW.txt

python gen-only-notrxx.py PE AllvsMW.txt pe/AllvsMw-PE.txt
(80 records)

3. put the cases into page-order, which makes reviewing slightly more efficient
python pageord.py pe/AllvsMW-PE.txt pe/pe-only-notrxx-page.txt  pe/pehw2.txt
80  headwords from pe/AllvsMW-PE.txt
80  headwords after duplicates removed

4. Generate fuzzy suggestions for the cases.

python fuzzyalpha.py PE,2014 pe/pe-only-notrxx-page.txt  pe/pe-fuzzyalpha.txt  pe/pe-fuzzyalpha.html sanhw1.txt  pe/pehw2.txt


----------------------------------------------------
FOR PGN:
mkdir pgn
2. Select the PGN cases from AllvsMW.txt

python gen-only-notrxx.py PGN AllvsMW.txt pgn/AllvsMw-PGN.txt
(6 records)

3. put the cases into page-order, which makes reviewing slightly more efficient
python pageord.py pgn/AllvsMW-PGN.txt pgn/pgn-only-notrxx-page.txt  pgn/pgnhw2.txt
6  headwords from pgn/AllvsMW-PGN.txt
6  headwords after duplicates removed

4. Generate fuzzy suggestions for the cases.

python fuzzyalpha.py PGN,2014 pgn/pgn-only-notrxx-page.txt  pgn/pgn-fuzzyalpha.txt  pgn/pgn-fuzzyalpha.html sanhw1.txt  pgn/pgnhw2.txt


----------------------------------------------------
FOR MCI:
mkdir mci
2. Select the MCI cases from AllvsMW.txt

python gen-only-notrxx.py MCI AllvsMW.txt mci/AllvsMw-MCI.txt
(13 records)

3. put the cases into page-order, which makes reviewing slightly more efficient
python pageord.py mci/AllvsMW-MCI.txt mci/mci-only-notrxx-page.txt  mci/mcihw2.txt
13  headwords from mci/AllvsMW-MCI.txt
13  headwords after duplicates removed

4. Generate fuzzy suggestions for the cases.

python fuzzyalpha.py MCI,2014 mci/mci-only-notrxx-page.txt  mci/mci-fuzzyalpha.txt  mci/mci-fuzzyalpha.html sanhw1.txt  mci/mcihw2.txt


----------------------------------------------------
FOR PD:
mkdir pd
2. Select the PD cases from AllvsMW.txt

python gen-only-notrxx.py PD AllvsMW.txt pd/AllvsMw-PD.txt
(1171 records)

3. put the cases into page-order, which makes reviewing slightly more efficient
python pageord.py pd/AllvsMW-PD.txt pd/pd-only-notrxx-page.txt  pd/pdhw2.txt
1171  headwords from pd/AllvsMW-PD.txt
1158  headwords after duplicates removed

4. Generate fuzzy suggestions for the cases.

python fuzzyalpha.py PD,2014 pd/pd-only-notrxx-page.txt  pd/pd-fuzzyalpha.txt  pd/pd-fuzzyalpha.html sanhw1.txt  pd/pdhw2.txt
begin 21:14:27
  end 

