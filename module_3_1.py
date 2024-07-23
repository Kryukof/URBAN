def count_calls(one):
    global calls
    calls += one
    return calls


def string_info(string):
    count_calls(1)
    while True:
        return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls(1)
    string = string.lower()
    list_to_search = [s.lower() for s in list_to_search]
    if string in list_to_search:
        return True
    else:
        return False


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
