print("= Hacker Terminal Access =")

# Ask for user info
name = input("Enter your name: ")
age = int(input("Enter your age: "))
codeword = input("Enter the hacker codeword: ")

# Set access criteria
minimum_age = 18
secret_word = "zero_day"

# Check access
if age >= minimum_age and codeword == secret_word:
    print(f"Access granted. Welcome, {name}. Initiating system scan... 🧠💻")
else:
    print("Access denied. Intrusion detected! 🚨")

