from utilitylogic import generallogic
obj = generallogic()
changing_amount = int(input("Enter the amount returned by Vanding machine :"))
avilable_notes = [1000, 500, 100, 50, 20, 10, 5, 2, 1]

print(f"Total number of notes = { obj.vending_machine(avilable_notes,changing_amount)}")