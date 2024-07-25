# Using variables in strings

first_name = 'ada'
last_name = 'lovelace'
full_name = f"{first_name} {last_name}"
print(full_name)

# Use f-string to compose complete messages using the info associated with a variable
first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'
print(f"Hello, {full_name.title()}!")

# Can also use f-strings to compose a message then assign the message to an entire variable
first_name = 'ada'
last_name = 'lovelace'
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)