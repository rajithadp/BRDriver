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

_chrom = 'chr'+input('Chromosome Number: ')
_pos = input('Chromosome Position: ')
_ref_base = input('Reference Base: ')
_alt_base = input('Alternative Base: ')

_url = 'https://run.opencravat.org/submit/annotate?chrom=%s&pos=%s&ref_base=%s&alt_base=%s&&annotators=mutpanning,aloft,chasmplus,prec,phi,ghis,loftool'%(_chrom,_pos,_ref_base,_alt_base)

r=requests.get(_url)
rJson=r.json()

toolValues = {'Mutpanning':0,'AloFT':0,'CHASMplus':0, 'P(rec)':0, 'P(HI)':0, 'GHIS':0, 'LoFtool':0}

toolValues['Mutpanning'] = rJson["mutpanning"]["Max_Frequency"] if rJson['mutpanning'] is not None else toolValues['Mutpanning'] 
toolValues['AloFT'] = rJson["aloft"]["dominant"] if rJson['aloft'] is not None else toolValues['AloFT']
toolValues['CHASMplus'] = rJson["chasmplus"]["score"] if rJson['chasmplus'] is not None else toolValues['CHASMplus']
toolValues['P(rec)'] = rJson["prec"]["prec"] if rJson['prec'] is not None else toolValues['P(rec)']
toolValues['P(HI)'] = rJson["phi"]["phi"] if rJson['phi'] is not None else toolValues['P(HI)']
toolValues['GHIS'] = rJson["ghis"]["ghis"] if rJson['ghis'] is not None else toolValues['GHIS']
toolValues['LoFtool'] = rJson["loftool"]["loftool_score"] if rJson['loftool'] is not None else toolValues['LoFtool']


toolData = pd.DataFrame([toolValues])
toolData
toolData.to_excel('test.xlsx')

model = pickle.load(open('/PLEASE_CHANGE_THIS_PATH_WHERE_YOUR_FILE_IS_LOCATED/brcaModelVersion3.pkcls','rb'))
data = Orange.data.Table('test.xlsx')
print(model(data))

if model(data) == 1:
    print('Your gene is a Breast Cancer Driver Gene')
else:
    print('Your gene is Not a Breast Cancer Driver Gene')

