#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end

def band_name():
  print("Greetings Rockstar")
  city = input("What city did you grow up in?\n")
  pet = input("What was the name of your childhood pet?\n")
  band = city + " " + pet
  return band

my_band = band_name()
print(my_band)