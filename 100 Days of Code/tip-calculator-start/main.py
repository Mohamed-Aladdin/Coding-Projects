#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

def bill_split():
  bill = float(input("How much's the bill? $"))
  people = int(input("How many are you guys? "))
  eachPay = round((bill / people) * 1.12, 2)
  return eachPay

bill = bill_split()
print(bill)