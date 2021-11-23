# GBIF_Analyzer
Analyze some GBIF bee data for funzies

This is a thing I did in order to take a deeper dive into the data from the paper "Worldwide occurrence records suggest a global decline in bee species richness" by Zattara and Aizen, published in the journal One Earth.

In order for this code to work, you need the data from https://www.gbif.org/occurrence/download/0058082-200221144449610
which is used as the input for GBIF-reader.py

Then GBIF-reader.py can slice the data and output a csv that can be further analyzed by GBIF-analyzer.py

GBIF-speader_counter is essentially a branch of GBIF-reader that counts up data from different sources.

I don't know why I did that way
