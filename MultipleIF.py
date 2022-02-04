print("Welcome to the FUCK ZONE")
bill = 0

height = int(input("What is your height in CM? "))

if height >= 120:
    print("You can ride the fuck")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    photo = input("Want a photo taken? y or n. ")
    if photo == "y":
        bill += 3

    print(f"Your final bill is ${bill}")

    
else:
    print("Fuck you, no")
    
