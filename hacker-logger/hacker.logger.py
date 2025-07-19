from datetime import datetime

def log_attempt(name, age, success):
    """
    Logs each login attempt to access_log.txt
    name: user's name
    age: user's age
    success: True or False
    """
    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file = "access_log.txt"

    status = "SUCCESS" if success else "FAILED"
    
    with open(log_file, "a") as file:
        file.write(f"[{now}] {status} - {name} ({age})\n")

print("=== Secure Hacker Login ===")

# Access criteria
minimum_age = 18
secret_word = "zero_day"

# Log file path
log_file = "access_log.txt"

# Attempt loop
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    print(f"\nAttempt {attempts + 1} of {max_attempts}")

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    codeword = input("Enter the hacker codeword: ")

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if age >= minimum_age and codeword == secret_word:
        print(f"\nAccess granted. Welcome, {name}. Initiating system scan... 🧠💻")
        
        # Log success
        with open(log_file, "a") as file:
            file.write(f"[{now}] SUCCESS - {name} ({age})\n")
        break
    else:
        print("Access denied. Intrusion detected! 🚨")
        
        # Log failure
        with open(log_file, "a") as file:
            file.write(f"[{now}] FAILED  - {name} ({age})\n")
        
        attempts += 1

if attempts == max_attempts:
    print("\n❌ Too many failed attempts. System locked.")


# Only offer to view logs if access was successful
if attempts < max_attempts:
    view_logs = input("\nWould you like to view the access logs? (yes/no): ").lower()
    if view_logs == "yes":
        print("\n📂 Access Log Contents:\n")
        with open(log_file, "r") as file:
            contents = file.read()
            print(contents)
    else:
        print("Okay, logs remain secured.")
