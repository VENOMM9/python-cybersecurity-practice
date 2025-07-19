def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            shifted = (ord(char) - base - shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

def brute_force(text):
    print("\nBrute Force Results:")
    for shift in range(1, 26):
        decrypted = decrypt(text, shift)
        print(f"Shift {shift}: {decrypted}")

# === Menu ===
while True:
    print("\n=== Caesar Cipher Tool ===")
    print("1. Encrypt Text")
    print("2. Decrypt Text")
    print("3. Brute Force Decryption")
    print("4. Exit")

    choice = input("Select an option (1-4): ")

    if choice == "1":
        msg = input("Enter the message to encrypt: ")
        shift = int(input("Enter shift value (1-25): "))
        print("Encrypted:", encrypt(msg, shift))

    elif choice == "2":
        msg = input("Enter the message to decrypt: ")
        shift = int(input("Enter shift value (1-25): "))
        print("Decrypted:", decrypt(msg, shift))

    elif choice == "3":
        msg = input("Enter encrypted message for brute force: ")
        brute_force(msg)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
