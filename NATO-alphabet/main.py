import pandas as pd
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


df=pd.read_csv("nato_phonetic_alphabet.csv")
# print(df)

# dict=df.to_dict()
# print(dict)

# dataFrame=pd.DataFrame(dict)
# print(dataFrame)

# for (index,row) in df.iterrows():
#     print(row.code)

newDict={row.letter:row.code for index,row in df.iterrows()}
# print(newDict["A"])

def keep_generating():

    try:
        name = input("enter a name: ").upper()
        list=[newDict[letter] if letter !=" " else "space" for letter in name]
    except KeyError:
        print("only letters in the string please. no spaces allowed")
        keep_generating()
    else:
        print(list)

keep_generating()