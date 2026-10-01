import random
import string

def generate_password():
    print("=== RANDOM PASSWORD GENERATOR ===")
    
    try:
        length = int(input("Enter the desired length for your password: "))
        if length < 4:
            print("Password length should be at least 4 characters for basic security.")
            return
            
        print("\nSelect character options to include:")
        use_letters = input("Include letters (y/n)? ").strip().lower() == 'y'
        use_digits = input("Include digits (y/n)? ").strip().lower() == 'y'
        use_symbols = input("Include special symbols (y/n)? ").strip().lower() == 'y'
        
        character_pool = ""
        if use_letters:
            character_pool += string.ascii_letters
        if use_digits:
            character_pool += string.digits
        if use_symbols:
            character_pool += string.punctuation
            
        if not character_pool:
            print("Error: You must select at least one character type category.")
            return
            
        # Generating the random password string from the selected pool
        password = "".join(random.choice(character_pool) for _ in range(length))
        
        print("\n-------------------------------------")
        print(f"Generated Password: {password}")
        print("-------------------------------------")
        
    except ValueError:
        print("Invalid input! Please enter a numeric integer value for length.")

if __name__ == "__main__":
    generate_password()
