# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:

if age > 0 and age <=12:
    print("You are a Child")
elif age >=13 and age <=19:
    print("You are a Teenager")
elif age >=20 and age <=59:
    print("You are an Adult")
elif age >=60:
    print("You are a Senior")
else :
    print("Invalid age")
