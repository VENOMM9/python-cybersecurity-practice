import itertools
import string

def brute_force_crack(password, max_length=4):
    characters = string.ascii_lowercase + string.digits
    attempts = 0

    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            guess_word = ''.join(guess)
            attempts += 1
            print(f"Trying: {guess_word}")
            if guess_word == password:
                print(f"Password found: {guess_word} (in {attempts} attempts)")
                return guess_word

    print("Password not found.")
    return None

# Example usage
target_password = input("Enter a lowercase+digits password to crack: ")
brute_force_crack(target_password)
