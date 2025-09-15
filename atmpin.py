correct_pin="1234"
attempts=0
max_attempts=5

while attempts< max_attempts:
  pin=input("enter your ATM PIN:")
  attempts=attempts+1
  
  if pin ==correct_pin:
    print("PIn correct!Access granted ")
    break
  else:
    remaining = max_attempts-attempts
    if remaining>0:
      print("Wrong pin!",remaining,"attempts left")
    else:
      print("Account blocked! too many Wrong attempts")  