# The extensible version of fizzbuzz.py
# Assumes an input dictionary of integer keys and string values


def extensible_fizz_buzz(n, input_dict):
    return_string = ''

# iterate over the items in the dictionary, finding the divisible of n therefor
    for k in sorted(input_dict.keys()):
        if n % k == 0:
            # Add the appropriate syllable to that string
            return_string += input_dict[k]

    # Is there a syllable yet? -> return the number as a string
    if return_string == '':
        return str(n)
    # Otherwise, return Fizz and/or Buzz
    else:
        return return_string


# Build the dictionary using console input
def build_user_dict():
    user_dict = {}  # Create an empty dictionary
    user_dict_key = int(raw_input("Enter the number to be handled (enter 0 if finished): "))

    # While the user has not entered zero, keep accepting values
    while user_dict_key:
        user_dict_val = raw_input("What syllable is to be associated with that number? ")
        user_dict[user_dict_key] = user_dict_val  # Add the key/value pair to the dictionary
        user_dict_key = int(raw_input("Enter the number to be handled (enter 0 if finished): "))
    # And now the dictionary is built
    return user_dict

if __name__ == '__main__':
    user_input = raw_input("What is the number with which we are concerned? ")
    user_dict = build_user_dict()
    print extensible_fizz_buzz(int(user_input), user_dict)
