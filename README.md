# BRDriver
BRDriver is a breast cancer driver gene predictor. BRDriver built upon seven different variant prediction tools and it uses the Random Forest machine learning algorithm for giving predictions. The tools are </br>
<b>Mutpanning </br>
ALoFT </br>
CHASMplus </br>
P(rec) </br>
P(HI) </br>
GHIS </br>
LoFtool </b></br>

BRDRiver use [opencravat API](https://open-cravat.readthedocs.io/en/latest/API.html) to get results easily from above mentioned tools. The API needs <b>Chromosome number, Variant position, Reference Base, Alternative Base</b> for giving results for each tool. BRDriver predict the given gene is a breast cancer driver gene or a passanger gene.

### BRDriver Interface
![alt text](https://github.com/rajithadp/BRDriver/blob/main/beforeSubmit.png)

Based on the given values BRDriver will give predictions as follows.

![alt text](https://github.com/rajithadp/BRDriver/blob/main/afterSubmit.png)

To work with this script you need to pre-install the following python packages
- PySimpleGUI
- requests
- pandas
- Orange
- pickle
