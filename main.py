with open("./Input/Letters/starting_letter.txt") as letter:
    letter_name = letter.read()

with open("./Input/Names/invited_names.txt") as names:
    names = names.readlines()
    for name in names:
        striped_name = name.strip()
        x = letter_name.replace("[name]", striped_name)
        f = open(f"./Output/ReadyToSend/letter_for_{striped_name}.txt", "w+")
        f.write(x)
        f.close()
