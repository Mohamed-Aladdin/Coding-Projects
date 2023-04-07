#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def main():
    guests = []

    with open(r"Input\Names\invited_names.txt", "r") as names:
        for name in names.readlines():
            name = name.strip()
            guests.append(name)

    with open(r"Input\Letters\starting_letter.txt", "r") as template:
        text = template.read()
    
    for guest in guests:
        new_letter = text.replace("[name]", guest)
        with open(fr"Output\ReadyToSend\{guest}_letter.txt", "w") as final_letter:
            final_letter.write(new_letter)

main()