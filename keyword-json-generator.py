from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import


import os
import sys
import glob
import logging
import json
from nltk.stem.snowball import SnowballStemmer as Stemmer

logging.basicConfig(level=logging.INFO)

references = {}
test ="ste"

for input_file in glob.glob('kpdata/KDD/gold/'+'[0-9]*'):
    file_id = input_file.split('/')[-1].split('\\')[1]
    logging.info("loading references from {}".format(file_id))

    with open(input_file, 'r') as f:
        lines = f.readlines()
        keyphrases = []
        for line in lines:
            words = line.strip().split()
            if test == "stem":
                stems = [Stemmer('porter').stem(w.lower()) for w in words]
                keyphrases.append([' '.join(stems)])
            else:
                keyphrases.append(' '.join([w.lower() for w in words]))
        t = set(keyphrases)
            
        references[file_id] = tuple(t)
with open("keyword_kdd.json", 'w') as o:
    json.dump(references, o, sort_keys = True, indent = 4)
    


