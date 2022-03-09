import pandas as pd

data = pd.read_csv(
    "nato_phonetic_alphabet.csv")

dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user = input("Type a name.: ").upper()
result = [dict[letter] for letter in user]
print(result)
