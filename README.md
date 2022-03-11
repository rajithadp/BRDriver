# BRDriver
BRDriver is a breast cancer driver gene predictor. BRDriver built upon seven different variant prediction tools and it uses the Random Forest machine learning algorithm for giving predictions. The tools are </br>
<b>Mutpanning </br>
ALoFT </br>
CHASMplus </br>
P(rec) </br>
P(HI) </br>
GHIS </br>
LoFtool </b></br>

Here we are using opencravat API to get results easily from above mentioned tools. The API needs <b>Chromosome number, Variant position, Reference Base, Alternative Base</b> for giving results for each tool. BRDriver predict the given gene is a breast cancer driver gene or a passanger gene.

### BRDriver Interface
![alt text](https://github.com/rajithadp/BRDriver/blob/main/withoutData.png)

Based on the given values BRDriver will give predictions.
![alt text](https://github.com/rajithadp/BRDriver/blob/main/withData.png)
