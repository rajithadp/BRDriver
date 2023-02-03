# BRDriver
The BRDriver is a Breast Cancer Driver Gene predictor. This Machine Learning Model was built using the Random Forest machine learning algorithm and seven different gene prediction tools.

It based on
- Mutpanning
- ALoFT
- CHASMplus
- P(HI)
- P(rec)
- GHIS
- LoFtool

# SetUp
If you havent got following packages you need to install them.
- PySimpleGUI
- requests
- pandas
- Orange
- pickle

Clone the repository and simply run the BRDriver.py python script by

```
Python3 BRDriver.py
```

# How it Works
- BRDriver is a GUI with various input fields and a submit button.
- It waits for user input through the GUI.
- When the submit button is pressed, it sends an HTTP GET request to an API with the values entered in the input fields.
- It parses the JSON response from the API and stores certain values in a dictionary.
- It converts the dictionary to a Pandas DataFrame, saves it to an excel file and loads a machine learning model.
- The model is applied to the data and the result is displayed in the GUI.
- If the result is 1, the GUI show that the gene is a breast cancer driver gene.

# How Model was built

![ScreenShot](https://github.com/rajithadp/BRDriver/tree/main/src/images/BRDriver_model.png)
