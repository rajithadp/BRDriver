import PySimpleGUI as sg
import requests
import pandas as pd
import Orange
import pickle

layout = [
	[sg.Text('Enter Chromosome Number',size=(30, 1),justification='right',font=("Times New Roman",20)), sg.InputText(key='-Chr-',size=(10, 1))],
	[sg.Text('Enter Position',size=(30, 1),justification='right',font=("Times New Roman",20)), sg.InputText(key='-Pos-',size=(10, 1))],
    [sg.Text('Enter Reference Base',size=(30, 1),justification='right',font=("Times New Roman",20)), sg.InputText(key='-Ref-',size=(10, 1))],
    [sg.Text('Enter Alternative Base',size=(30, 1),justification='right',font=("Times New Roman",20)), sg.InputText(key='-Alt-',size=(10, 1))],
    [sg.Submit(font=("Times New Roman",20)), sg.Cancel(font=("Times New Roman",20))],
    [sg.Text( key='-Result-', font=("Times New Roman",20))]
]


window = sg.Window("BRDriver",layout,size=(700, 300))

while True:
    event, values = window.read()
    
    _url = 'https://run.opencravat.org/submit/annotate?chrom=%s&pos=%s&ref_base=%s&alt_base=%s&&annotators=mutpanning,aloft,chasmplus,prec,phi,ghis,loftool'%('chr'+values['-Chr-'],values['-Pos-'],values['-Ref-'],values['-Alt-'])

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

    toolData.to_excel('test.xlsx')
    model = pickle.load(open('/media/rajitha/DC2CC1E62CC1BC30/academic/breast cancer study/brcaModelVersion3.pkcls','rb'))
    data = Orange.data.Table('test.xlsx')

    result = model(data)

    window['-Result-'].update(result)
    if result == 1:
        window['-Result-'].update('Your gene is a Breast Cancer Driver gene')
    else:
        window['-Result-'].update('Your gene is not a driver gene')

    
    
