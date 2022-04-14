Var1 = len(input("Enter City Name: "))
print("City name that you have entered has "+ str(Var1)+ " Characters")
Var2 = 130.75
print(Var2)
print("You have entered Floating Value of : ", Var2)
print("You have entered Floating Value of : " + str(Var2))# here Float value Var2= 130.75 gets converted to String and then gets printed


two_digit_number = input("Type a two digit number: ")
print(int(two_digit_number[0]) + int(two_digit_number[1]))

a = two_digit_number[0]
b = two_digit_number[1]

print("Sum of a + b ", int(a) + int(b))
c = a + b
print("Sum of a + b ", c) # this code will simply concatenate the value as it treat them as string

c1 = int(a) + int(b) # this code convert the string into integer and then add it
print("Value of c1 : ", c1)

a2 = 3
b2 = 9
c2 = a2+b2 # over here since values are assigned it treat them as numeric
print("Value of c2: ", c2)


# To have a full proof solution in case only single digit was entered
two_digit_number = input("Type a two digit number: ")
length = len(two_digit_number)
print(length)
a = two_digit_number[0]
if(length < 2):
 print("Only single digit entered:", a)
else:
  b = two_digit_number[1]
  print("Sum of Entered 2 digits is ", int(a) + int(b))