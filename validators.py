import re

def validate_email(email):
    pattern = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(pattern, email))

def validate_phone(phone):
    return phone.isdigit() and len(phone) in [11]

def get_valid_input(prompt, validator, error_message):

    while True:
        value = input(prompt)
        if validator(value):
            return value
        print(error_message)