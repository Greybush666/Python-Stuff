print("Welcome to El Maguey!")

bill = input("What was the total bill? $")

tip = input("What percentage would you like to give? 10%, 12%, 15%? ")

party = input("How many people are splitting the bill? ")

bill_fl = float(bill)

tip_fl = float(tip)

party_int = int(party)

billtotal = bill_fl / party_int

billtotal = float(billtotal)

totaltip = float(billtotal) * tip_fl

final = billtotal + totaltip

final = "{:.2f}".format(final)

message =("Each person should pay " + (round(final, 2)))

print(message)

            
#Yu Solution
#bill = float(input("What was the total bill? $"))
#tip = int(input("How much tip would you like to give? 10, 12, 15? "))
#people = int(input("How many people in the party? "))
#tip_as_percent = tip /100
#total_tip_amount = bill * tip_as_percent
#total_bill = bill + total_tip_amount
#bill_pp = total_bill / people
#final = round(bill_pp, 2)
#final = "{:.2f}".format(bill_pp) 
#print(f"Each person should pay {final}")
