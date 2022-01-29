print("Welcome to Fuck Town!")


bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, 15? "))
people = int(input("How many people in the party? "))
tip_as_percent = tip /100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_pp = total_bill / people
final = round(bill_pp, 2)
final = "{:.2f}".format(bill_pp) 
print(f"Each person should pay {final}")


#Ran Yu's solution just to see the round format she did
