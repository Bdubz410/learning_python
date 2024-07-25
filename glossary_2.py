# Now that you know how to loop through a dictionary, clean up the code from exercise 6-3 from page 99.
# by replacing your series of print() calls with a loop that runs through the dictionary's key and values.
# When you're sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should automatically be included in the output.
glossary = {
    'string': 'series of characters',
    'integer': 'number',
    'program': 'code',
    'syntax': 'rules',
    'tuple': 'list that cannot change',
    }

glossary['dictionary'] = 'key-value pair'
glossary['block'] = 'collection of statements'
glossary['conditional test'] = 'evaluates to True or False'
glossary['if statement'] = 'conditional execution'
glossary['boolean'] = 'data type that is either True or False'

for word, meaning in glossary.items():
    print(f"{word}:\n {meaning}")