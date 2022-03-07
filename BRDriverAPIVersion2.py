#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 07:37:58 2022

@author: rajitha
"""

import requests
import pandas as pd
import Orange
import pickle


r=requests.get('https://run.opencravat.org/submit/annotate?chrom=chr10&pos=8073911&ref_base=-&alt_base=A&&annotators=mutpanning,aloft,chasmplus,prec,phi,ghis,loftool')

rJson=r.json()
toolValues = {'Mutpanning':0,'AloFT':0,'CHASMplus':0, 'P(rec)':0, 'P(HI)':0, 'GHIS':0, 'LoFtool':0}
 
if rJson['mutpanning'] is None:
    toolValues['Mutpanning'] = 0
    print(toolValues)
else:
    toolValues['Mutpanning'] = rJson["mutpanning"]["Max_Frequency"]


if rJson['aloft'] is None:
    toolValues['AloFT'] = 0
    print(toolValues)
else:
    toolValues['AloFT'] = rJson["aloft"]["dominant"]


if rJson['chasmplus'] is None:
    toolValues['CHASMplus'] = 0
    print(toolValues)
else:
    toolValues['CHASMplus'] = rJson["chasmplus"]["score"]


if rJson['prec'] is None:
    toolValues['P(rec)'] = 0
    print(toolValues)
else:
    toolValues['P(rec)'] = rJson["prec"]["prec"]


if rJson['phi'] is None:
    toolValues['P(HI)'] = 0
    print(toolValues)
else:
    toolValues['P(HI)'] = rJson["phi"]["phi"]


if rJson['ghis'] is None:
    toolValues['GHIS'] = 0
    print(toolValues)
else:
    toolValues['GHIS'] = rJson["ghis"]["ghis"]


if rJson['loftool'] is None:
    toolValues['LoFtool'] = 0
    print(toolValues)
else:
    toolValues['LoFtool'] = rJson["loftool"]["loftool_score"]

toolData = pd.DataFrame([toolValues])
toolData
toolData.to_excel('test.xlsx')

model = pickle.load(open('/PLEASE_CHANGE_THIS_PATH_WHERE_YOUR_FILE_IS_LOCATED/brcaModelVersion3.pkcls','rb'))
data = Orange.data.Table('test.xlsx')
print(model(data))


