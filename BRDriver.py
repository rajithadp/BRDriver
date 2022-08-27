#!/usr/bin/env python

import PySimpleGUI as sg
import requests
import pandas as pd
import Orange
import pickle

layout = [
	[sg.Text('Chromosome Number',size=(30, 1),justification='right',font=("Arial",20),text_color='Blue',background_color='White'), sg.InputText('10',key='-Chr-',size=(10, 1),text_color='Black',background_color='White')],
	[sg.Text('Chromosomal Position',size=(30, 1),justification='right',font=("Times New Roman",20),text_color='Blue',background_color='White'), sg.InputText('8073911',key='-Pos-',size=(10, 1),text_color='Black',background_color='White')],
    [sg.Text('Reference Allele',size=(30, 1),justification='right',font=("Times New Roman",20),text_color='Blue',background_color='White'), sg.InputText('-',key='-Ref-',size=(10, 1),text_color='Black',background_color='White')],
    [sg.Text('Alternative Allele',size=(30, 1),justification='right',font=("Times New Roman",20),text_color='Blue',background_color='White'), sg.InputText('A',key='-Alt-',size=(10, 1),text_color='Black',background_color='White')],
    [sg.Text('',background_color='White')],
    [sg.T(" "*66,background_color='White'),sg.Submit(font=("Times New Roman",20)), sg.Button('Clear',font=("Times New Roman",20))],
    [sg.Text( key='-Result-', font=("Times New Roman",20),text_color='Black',background_color='White')]
]

window = sg.Window("BRDriver",layout,size=(700, 300),grab_anywhere=True,background_color='White')

while True:
    event, values = window.read()
    
    _url = 'https://run.opencravat.org/submit/annotate?chrom=%s&pos=%s&ref_base=%s&alt_base=%s&&annotators=mutpanning,aloft,chasmplus,prec,phi,ghis,loftool'%('chr'+values['-Chr-'],values['-Pos-'],values['-Ref-'],values['-Alt-'])

    r=requests.get(_url)
    rJson=r.json()

    toolValues = {'Mutpanning':0,'AloFT':0,'CHASMplus':0, 'P(rec)':0, 'P(HI)':0, 'GHIS':0, 'LoFtool':0, 'hugo':'' }

    toolValues['Mutpanning'] = rJson["mutpanning"]["Max_Frequency"] if rJson['mutpanning'] is not None else toolValues['Mutpanning'] 
    toolValues['AloFT'] = rJson["aloft"]["dominant"] if rJson['aloft'] is not None else toolValues['AloFT']
    toolValues['CHASMplus'] = rJson["chasmplus"]["score"] if rJson['chasmplus'] is not None else toolValues['CHASMplus']
    toolValues['P(rec)'] = rJson["prec"]["prec"] if rJson['prec'] is not None else toolValues['P(rec)']
    toolValues['P(HI)'] = rJson["phi"]["phi"] if rJson['phi'] is not None else toolValues['P(HI)']
    toolValues['GHIS'] = rJson["ghis"]["ghis"] if rJson['ghis'] is not None else toolValues['GHIS']
    toolValues['LoFtool'] = rJson["loftool"]["loftool_score"] if rJson['loftool'] is not None else toolValues['LoFtool']
    toolValues['Hugo'] = rJson["crx"]["hugo"] if rJson['crx'] is not None else toolValues['Hugo']
    
    toolData = pd.DataFrame([toolValues])

    toolData.to_excel('test.xlsx')
    model = pickle.load(open('src/model/brcaModelVersion3.pkcls','rb'))
    data = Orange.data.Table('test.xlsx')

    result = model(data)

    window['-Result-'].update(result)
    
    if result == 1:
        window['-Result-'].update('This '+toolValues['Hugo']+' gene is a Breast Cancer Driver gene' )
    else:
        window['-Result-'].update('This '+toolValues['Hugo']+'gene is not a driver gene')

    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Clear':
        window['-Chr-'](''), window['-Pos-'](''), window['-Ref-'](''), window['-Alt-'](''), window['-Result-']('') 

window.close()
