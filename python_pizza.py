print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L : ") # What size pizza do you want? S, M, or L
 # Do you want pepperoni? Y or N
 # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

bill = 0
if size == "S":
  bill = 15
  # print(f"Small Pizza: $15")
  
elif size == "M":
    bill = 20
    # print(f"Medium Pizza: $20")
  
elif size == "L":
   
    bill = 25
    # print(f"Large Pizza: $25")
add_pepperoni = input("Do you want pepperoni? Y or N: ") # Do you want pepperoni? Y or N
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
extra_cheese = input("Do you want extra cheese? Y or N : ")
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: {bill}, thank you for choosing python pizza.")

        
      

    
      
 

    


 
  
   
      

