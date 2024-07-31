# Start with a copy of user_profile.py. Build a profile of yourself by calling build_profile(),
# using your first and last name and three other key-value pairs that describe you.
def build_profile(first, last, **user_info):
    """Build a profile of yourself."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('anakin', 'skywalker',
                             birth_place='tatooine',
                             nickname='darth vader',
                             kin='luke skywalker')

print(user_profile)