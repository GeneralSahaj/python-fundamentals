# Keyword arguments = An argument preceded by an identifier
#                     Helps with Readability 
#                     Order of arguments doesn't matter. 
#                     1. Positional 2. Default 3. KEYWORD 4. Arbitrary

def get_phone(country_code, std_code, subscriber_number):
    return f"+{country_code} ({std_code})-{subscriber_number}"

country_code = input("Enter country code: ")
std_code = input("Enter STD code: ")
subscriber_number = input("Enter subscriber number: ")

phone_num = get_phone(country_code, std_code, subscriber_number)
print(phone_num)
