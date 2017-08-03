# endurance-stats
Python script to calculate stats on endurance racing

Number of laps
Mean
Median
Min
Percentile 85

It uses the alkamel files generated on the IMSA, ELMS and WEC.

Tto run the script

python3 stats.py SERIES YEAR Files

For example

python3 stats.py WEC 2016 Bahrein.CSV

It creates 2 files, one at driver level and other at team level.

It supports multiple files

python3 stats.py WEC 2016 Bahrein.CSV Silverstone.CSV
