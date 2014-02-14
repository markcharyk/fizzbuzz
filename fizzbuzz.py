def fizz_buzz(n):
    return_string = ''

    # Is the number divisible by three? -> Add a Fizz
    if n % 3 == 0:
        return_string += 'Fizz'

    # Is the number divisible by five? -> Add a Buzz
    if n % 5 == 0:
        return_string += 'Buzz'

    # Is there a Fizz or Buzz yet? -> return the number as a string
    if return_string == '':
        return str(n)
    # Otherwise, return Fizz and/or Buzz
    else:
        return return_string

if __name__ == '__main__':
    user_input = raw_input("What is the number with which we are concerned? ")
    print fizz_buzz(int(user_input))
