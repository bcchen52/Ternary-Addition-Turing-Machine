import random

# Function to generate a random ternary string of a given length
def generate_random_ternary_string(length):
    return ''.join(random.choice('012') for _ in range(length))

# Function to convert a ternary string to a decimal number
def ternary_to_decimal(ternary_str):
    return int(ternary_str, 3)

# Function to convert a decimal number to a ternary string
def decimal_to_ternary(decimal_num):
    if decimal_num == 0:
        return "0"
    ternary_str = ""
    while decimal_num > 0:
        ternary_str = str(decimal_num % 3) + ternary_str
        decimal_num //= 3
    return ternary_str

# Function to generate and write random ternary numbers to test_cases.txt and their expected sum to expected_cases.txt
def generate_ternary_pairs_and_write_files(test_cases_file, expected_cases_file, num_pairs=1):
    with open(test_cases_file, 'w') as test_file, open(expected_cases_file, 'w') as expected_file:
        for _ in range(num_pairs):
            # Generate two random ternary strings of random length between 40 and 60
            length_x = random.randint(100, 120)
            length_y = random.randint(100, 120)
            X = generate_random_ternary_string(length_x)
            Y = generate_random_ternary_string(length_y)
            
            # Convert the ternary strings to decimal
            X_decimal = ternary_to_decimal(X)
            Y_decimal = ternary_to_decimal(Y)
            
            # Add the numbers in decimal
            sum_decimal = X_decimal + Y_decimal
            
            # Convert the sum back to ternary
            sum_ternary = decimal_to_ternary(sum_decimal)
            
            # Write the test case X#Y to test_cases.txt
            test_file.write(f"{X}#{Y}")
            
            # Write the expected sum Z to expected_cases.txt
            expected_file.write(f"{sum_ternary}")

def clear(filename):
    open(filename, 'w').close()

# Call the function to generate pairs and write to test_cases.txt and expected_cases.txt
clear('result.txt')
generate_ternary_pairs_and_write_files('test_cases.txt', 'expected_cases.txt')