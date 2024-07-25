# Writing clear prompts
name = input("What is your name? ")
print(f"\nHey {name}!")

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHey {name}")