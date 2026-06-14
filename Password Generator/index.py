import string
import random

def generate_func(pass_length, num_choice, upper_choice, symbol_choice):
    # Fix: Move pool INSIDE so it resets every time you click generate
    pool = string.ascii_lowercase 
    
    digits = string.digits
    capital_letters = string.ascii_uppercase
    special_chars = string.punctuation

    # Add to the pool based on user selection
    if num_choice.get() == 1:
        pool += digits
    
    if upper_choice.get() == 1:
        pool += capital_letters
    
    if symbol_choice.get() == 1:
        pool += special_chars

    try:
        # Convert the string input from Entry to an Integer
        length = int(pass_length)
        
        # Build the password
        password = ""
        for i in range(length):
            password += random.choice(pool)
        return password
    
    except ValueError:
        # If the user typed "abc" instead of "12"
        return "Invalid Length"
    except IndexError:
        # If the pool is somehow empty (though we have lowercase as default)
        return "Select Options"