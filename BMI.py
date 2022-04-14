# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_float = float(height)
height_sq = height_float ** 2
weight_float = float(weight)

bmi = weight_float/height_sq
#print(bmi)
print(int(bmi))