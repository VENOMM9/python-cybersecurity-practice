print("=== Secure Hacker Login ===")

# Access criteria
minimum_age = 18
secret_word = "zero_day"

# Counter for attempts
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    print(f"\nAttempt {attempts + 1} of {max_attempts}")

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    codeword = input("Enter the hacker codeword: ")

    if age >= minimum_age and codeword == secret_word:
        print(f"\nAccess granted. Welcome, {name}. System scan initiating... 🧠💻")
        break
    else:
        print("Access denied. Intrusion detected! 🚨")
        attempts += 1

if attempts == max_attempts:
    print("\n❌ Too many failed attempts. System locked. Intrusion logged.")
