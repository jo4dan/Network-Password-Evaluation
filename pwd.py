import random
import string

def generate_passwords(num_passwords=10):
    passwords = []

    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/|"

    pools = [
        lower,
        lower + upper,
        lower + upper + digits,
        lower + upper + digits + symbols
    ]

    lengths = [8, 10, 12, 14, 16]  

    for i in range(num_passwords):
        pool = random.choice(pools)  
        length = random.choice(lengths)  
        password = ''.join(random.choice(pool) for _ in range(length))
        passwords.append(password)

    return passwords


if __name__ == "__main__":
    for pwd in generate_passwords(12):
        print(pwd)
