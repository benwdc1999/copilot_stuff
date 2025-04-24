#import the string module
import string

def larger(num1, num2):
    """num1 and num2 are two numbers. Return the larger of the numbers."""
    if num1 > num2:
        return num1
    else:
        return num2
    
#Call the larger function with the values 3 and 5
#Store the result in a variable called result
#Then print the result
result = larger(3, 5)
print("The larger number is", result)

def money_made(num_shares, purchase_share_price, current_share_price):
    """
    num_shares is the number of shares purchased.
    purchase_share_price is the price per share at which the shares were purchased.
    current_share_price is the current price per share.
    Return the amount of money made on the shares.
    """
    return (current_share_price - purchase_share_price) * num_shares    


def is_strong_password(password):
    """
    A strong password has at least one uppercase character, one number, and one special character.
    Return True if the password is strong, False otherwise.
    """
    has_upper = False
    has_digit = False
    has_special = False
    
    special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/"
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
            
    return has_upper and has_digit and has_special


def get_strong_password():
    """
    Prompt the user for a password until a strong password is entered.
    Return the strong password.
    """
    while True:
        password = input("Enter a strong password: ")
        if is_strong_password(password):
            return password
        else:
            print("Password must contain at least one uppercase letter, one digit, and one special character.") 

def num_points(word):
    """
    word is a string. Return the number of points the word is worth in Scrabble.
    The points are assigned as follows:
    A, E, I, O, U, L, N, S, T, R = 1 point
    D, G = 2 points
    B, C, M, P = 3 points
    F, H, V, W, Y = 4 points
    K = 5 points
    J, X = 8 points
    Q, Z = 10 points
    """
    points = 0
    letter_points = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1,
        'S': 1, 'T': 1, 'R': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }
    
    for char in word.upper():
        points += letter_points.get(char, 0)
        
    return points

def best_word(word_list):
    """
    word_list is a list of words. Return the word with the highest Scrabble points.
    """
    best_word = ""
    max_points = 0
    
    for word in word_list:
        points = num_points(word)
        if points > max_points:
            max_points = points
            best_word = word
            
    return best_word

def price_and_discount(price, discount):
    """
    price is the original price of an item.
    discount is the percentage discount to be applied.
    Return the final price after applying the discount.
    """
    return price - (price * (discount / 100))

def full_price_of_meal(price, tax, tip):
    """
    price is the original price of the meal.
    tax is the percentage tax to be applied.
    tip is the percentage tip to be applied.
    Return the final price after applying the tax and tip.
    """
    total_price = price + (price * (tax / 100)) + (price * (tip / 100))
    return total_price


def convert_temperature(temp, scale):
    """
    temp is the temperature to be converted.
    scale is the scale to convert to ('C' for Celsius, 'F' for Fahrenheit).
    Return the converted temperature.
    """
    if scale == 'C':
        return (temp - 32) * 5/9
    elif scale == 'F':
        return (temp * 9/5) + 32
    else:
        raise ValueError("Scale must be 'C' or 'F'")
    
    