import itertools
import string

def brute_force_crack(target_password):
    characters = string.ascii_lowercase  # a-z
    max_length = 4  # Limit to speed things up

    attempts = 0
    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            guess_word = ''.join(guess)
            attempts += 1
            print(f"Trying: {guess_word}")
            if guess_word == target_password:
                print(f"\n✅ Password found: {guess_word} in {attempts} attempts!")
                return

    print("\n❌ Password not found (too complex or too long)")

# 🔐 Test it
secret = input("Enter a simple password (a-z only, max 4 letters): ").lower()
brute_force_crack(secret)
