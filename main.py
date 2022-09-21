#arrived = False
#while not arrived:
# answer = input("Are we nearly there yet? ")
  #if answer == "yes":
   # arrived = True
    #print("Yay!")
#  elif answer == "no":
#    print("Fuck sake!")

import welcome_sign

for number in range(0, 101):
  if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
  elif number % 3 == 0:
    print("Fuzz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)