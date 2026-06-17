import random
import string
print("=== RANDOM PASSWORD GENERATOR ===")
while True:
    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Please enter a valid number")
        continue
    
    if length < 4:
        print("Password length should be atleast 4 characters")
        continue
    break
choice = input("Do you want special characters? (yes/no): ")

if choice.lower() == "yes":
    characters = string.ascii_letters + string.digits + string.punctuation
elif choice.lower() == "no":
    characters = string.ascii_letters + string.digits
else:
    print("Please enter yes or no")
    exit()

password = "".join(random.choice(characters) for i in range(length))
print(f"Generated password: {password}")
