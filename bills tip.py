print("welcome to the tip calculator!")

bill = float(input("what was the total bill? $"))

tip = int(input("how much  tip would you like to give? 10, 12, or 15? "))

people = int(input("how many people to split the bill? "))

tip_percent=tip/100

total_tip_amount = bill*tip_percent

total_bill = bill+total_tip_amount

bill_per_person = total_bill/people

# final_amount = f"Each person should pay :{:.2f}".format(bill_per_person)"
final_amount = f"Each person should pay :{round(bill_per_person,2)}"
print(final_amount)