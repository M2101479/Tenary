x=9
answer= 'even' if x % 2 == 0 else 'false'

print(answer)




grade=int(input("What grade did you get "))
if grade >=90:
  print("A")
elif grade <90 and grade>= 80:
  print("B")
else:
  print("C")




bill=int(input("What is your bill "))
discount= bill * 10.0/100 if bill >= 1000 else bill * 5.0/100
print(discount)