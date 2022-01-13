student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

word_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
print(word_dataframe)
word_dict = {row.letter:row.code for (index,row) in word_dataframe.iterrows()}

#print(word_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# catching the
is_true = True
while is_true:
    name = input("Please enter the name: ").upper()
    try:
        name_list = [word_dict[letter] for letter in name]
    except KeyError:
        print("Sorry! no letters only alphabets in a name Please")
    else:
        is_true = False
        print(name_list)

# another way of using the above with function

def generate_names():
    name = input("Please enter the name: ").upper()
    try:
        name_list = [word_dict[letter] for letter in name]
    except KeyError:
        print("Sorry! no letters only alphabets in a name Please")
        generate_names()
    else:
        print(name_list)

generate_names()
#test




