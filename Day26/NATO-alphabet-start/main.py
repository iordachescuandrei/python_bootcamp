
import pandas
#Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic={row.letter:row.code for (index, row) in data.iterrows()}

print (phonetic)

# Create a list of the phonetic code words from a word that the user inputs.

word =input ("Enter the word: ").upper()
output=[phonetic[letter] for letter in word]

print (output)