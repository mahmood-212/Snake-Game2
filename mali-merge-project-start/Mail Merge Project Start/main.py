#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



PLACE_HOLDER = "[name]"
with open("./Input/Names/invited_names.txt", "r") as file_name:
    # x1 = file1.read()
    x1 = file_name.readlines()
    print(x1)
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_constant = letter_file.read()
    for name in x1:
        strip_text = name.strip()
        print(strip_text)
        new_letter = letter_constant.replace(PLACE_HOLDER, strip_text)
        with open(f"./Output/ReadyToSend/letter_for_{strip_text}.txt", mode="w") as final_letter:
            final_letter.write(new_letter)

