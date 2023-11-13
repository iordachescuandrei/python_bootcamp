#final goal is to create in the Output folder, letters for each name in this format:
#letter_for_{name} where {name} represents each name from Input/Names/ invitated_names.txt file

with open("./Mail Merge Project Start/Input/Names/invited_names.txt", mode='r') as names:
    names = names.readlines()

with open("./Mail Merge Project Start/Input/Letters/starting_letter.txt", mode='r') as letter:
    letter_contents = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter=letter_contents.replace("[name]", stripped_name)
        with open(f"./Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode='w') as completed:
            completed.write(new_letter)