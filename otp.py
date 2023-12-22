import math, random
# let's store all the digits in a single place
digits = "0123456789"
# delcare a variable to store OTP
OTP = "" 
#if we have to generate 4 digit password, we have to run below code 4 times:
for i in range(4):
  OTP += digits[math.floor(random.random()*10)] #here random generates a float number, which we multiply with 10 to get a single digit which is again converted to a whole number using math.floor
print(OTP)
