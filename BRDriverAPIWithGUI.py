import PySimpleGUI as sg
import requests
import pandas as pd
import Orange
import pickle

layout = [
	[sg.Text('Enter Chromosome Number'), sg.InputText(key='-Chr-')],
	[sg.Text('Enter Position'), sg.InputText(key='-Pos-')],
    [sg.Text('Enter Reference Base'), sg.InputText(key='-Ref-')],
    [sg.Text('Enter Alternative Base'), sg.InputText(key='-Alt-')],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window("BRDriver",layout)
event, values = window.read()
window.close()

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


if model(data) == 1:
    sg.popup_ok_cancel('Your gene is a Driver gene',keep_on_top=True)
else:
    sg.popup_ok_cancel('Your gene is not a driver gene', keep_on_top=True)


