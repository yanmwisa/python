# Write your code below this line 👇
import math
def paint_calc(height,width,cover):
  number_can=(height*width)/5
  number_can=math.ceil(number_can)
  
  print(f"You'll need {number_can} cans of paint.")
  return  number_can
  
 

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)