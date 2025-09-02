score = int(input("Enter the score: "))
if score>=90:
  print("The grade is A")
elif score >= 80 and score <= 89:
  print("The grade is B")
elif score >= 70 and score <= 79:
  print("The grade is C")
elif score >= 60 and score <= 69:
  print("The grade is D")
else:
  print("The grade is F")
