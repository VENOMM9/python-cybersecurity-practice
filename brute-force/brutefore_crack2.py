import itertools
import string

# Hidden password (we are pretending we don't know this)
hidden_password = "Ab3"

def brute_force_crack():
    characters = string.ascii_letters + string.digits  # A-Z, a-z, 0-9

    max_length = 4  # We'll allow guessing up to 4 characters long

    attempts = 0  # To count how many guesses it took

    for length in range(1, max_length + 1):
        for guess_tuple in itertools.product(characters, repeat=length):
            guess = ''.join(guess_tuple)
            print(f"Trying: {guess}")
            attempts += 1

            if guess == hidden_password:
                print(f"[✓] Password found: {guess}")
                print(f"🔁 Attempts taken: {attempts}")
                return

    print("[-] Password not found")

brute_force_crack()
