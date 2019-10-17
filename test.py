import re

import os
import codecs
import sys
import logging
import glob
import json

with open("keyword_kdd",'r') as tt:
   keyphrases= json.load(tt)
doc_key = '10008070'

doc_value = ['Consensus group stable feature selection feature selection ',
 'Stability is an important yet under-addressed issue in feature selection from high-dimensional feature selection and small sample data .',
 'In this paper , we show that stability of feature selection has a strong dependency on sample size .',
 'We propose a novel framework for stable feature selection which first identifies consensus feature groups from subsampling of training samples , and then performs feature selection by treating each consensus feature group as a single entity .',
 'Experiments on both synthetic and real-world data sets show that an algorithm developed under this framework is effective at alleviating the problem of small sample size and leads to more stable feature selection results and comparable or better generalization performance than state-of-the-art feature selection algorithms .',
 'Synthetic data sets and algorithm source code are available.']


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
                    
                    
        print(line)
        print('----------------')
        print(temp_line)
        print('-----------------------------')
        print('-----------------------------')