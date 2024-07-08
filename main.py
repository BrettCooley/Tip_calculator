# Introduce the Application
print("Welcome to the tip calculator!")

# Ask the user how much the bill is
bill_amount = float(input("How much is the bill?\n£"))

# Ask the user how many people they are splitting the bill with.
splitting_party = int(input("How many people are you splitting the bill with\n"))

# Ask how much they would like to tip
tip_amount = int(input("what tip percentage would you like to add? 10, 12 or 15?\n"))

# Tip as percentage
tip_as_percentage = tip_amount / 100

# Total tip for the bill
total_tip_amount = bill_amount * tip_as_percentage

# Calculate the new bill balance
bill_total = bill_amount + total_tip_amount 

# Calculate bill split between party
split_bill = bill_total / splitting_party

# The split bill with two numbers after decimal
split_bill_structured = "{:.2f}".format(split_bill)

# The bill with two numbers after decimal
bill_total_structured = "{:.2f}".format(bill_total) 
                                        
# Shows total bill with tip
print(f"Total bill amount with tip £{bill_total_structured}")

# Shows total split per person
print(f"The price per person is £{split_bill}")
