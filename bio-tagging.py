from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import
import re

import os
import codecs
import sys
import logging
import glob
import json

logging.basicConfig(level=logging.INFO)

conv = {'-LRB-':'(',
        '-RRB-':')',
        '-LCB-':'{',
        '-RCB-':'}',
        '-LSB-':'[',
        '-RSB-':']'}
        
with open("keyword_kdd",'r') as tt:
   keyphrases= json.load(tt)

    
documents={}
for input_file in glob.glob('kpdata/KDD/abstracts/'+'[0-9]*'):
    file_id =input_file.split('/')[-1].split('\\')[1]
    logging.info("extracting text from {}".format(file_id))
    if not file_id in keyphrases.keys():
        continue 
    with open(input_file, 'r') as f:
        lines =f.readlines()
        text =[]
        for line in lines:
            tokens = line.strip().split()
            if True:
                untagged_tokens = [token.split('_')[0] for token in tokens]
                untagged_tokens = [conv[u] if u in conv else u for u in untagged_tokens]
                text.append(' '.join(untagged_tokens))
        documents[file_id]=text

tag_documents = {}
for doc_key, doc_value in documents.items():
    temp_document =[]
    for line in doc_value:
        temp_line = line
        keyphrase = keyphrases[doc_key]
        keyphr = [' '+p+' ' for p in keyphrase]
        for index, kp in enumerate(keyphr):
            res = [m.start() for m in re.finditer(kp,temp_line)]
            count = 0
            for i in res:
                offset = count+i
                temp1 = temp_line[0:offset]
                length = len(kp)
                temp2 = temp_line[offset+length:]
                split_kp = kp.split()
                split_kp = keyphrase[index].split()
                l = len(split_kp)
                tag =[' '+value+'_B-KP' if index is 0  else value+'_I-KP' for index, value in enumerate(split_kp)]
                temp3 =' '.join(tag)
                new_line = temp1+temp3+' '+temp2
                count = count+l*5
                temp_line = new_line
                    
                    
#        print(line)
#        print('----------------')
#        print(temp_line)
#        print('-----------------------------')
#        print('-----------------------------')
        temp_document.append(temp_line)
    tag_documents[doc_key] = temp_document


with open("bio-tag_documents.json", 'w') as o:
    json.dump(tag_documents, o, sort_keys = True, indent = 4)
    
with open("documents.json", 'w') as d:
    json.dump(documents, d, sort_keys = True, indent = 4)
    
            

